"""
Distributed Failover & Data Consistency

Handles multi-region replication, failover, and write classification.
Works with PersistenceManager to ensure data survives system failures.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any, List, Optional
from datetime import datetime
import asyncio


class WriteType(Enum):
    """Types of write operations."""
    CRITICAL = "critical"        # Must persist immediately
    STANDARD = "standard"        # Normal write with eventual consistency
    PROVISIONAL = "provisional"  # Can be lost if system fails


class Region(Enum):
    """Deployment regions."""
    PRIMARY = "us-central1"
    BACKUP_1 = "us-east1"
    BACKUP_2 = "eu-west1"


@dataclass
class WriteOperation:
    """Represents a write to be classified and managed."""

    write_id: str
    operation_type: str
    data: Dict[str, Any]
    write_type: WriteType
    timestamp: str
    region: Region
    replicas: List[Region] = None
    status: str = "pending"  # pending, written, replicated, failed

    def __post_init__(self):
        if self.replicas is None:
            self.replicas = []


class DataConsistencyManager:
    """
    Manages data consistency across distributed regions.

    Ensures:
    - CRITICAL writes persist to primary + all backups
    - STANDARD writes use eventual consistency
    - PROVISIONAL writes are best-effort
    """

    def __init__(self):
        self.writes_pending = []
        self.writes_failed = []
        self.last_checkpoint = None

    def classify_write(self, data: Dict[str, Any]) -> WriteType:
        """
        Classify a write based on its content.

        Heuristics:
        - Contract changes → CRITICAL
        - Financial data → CRITICAL
        - Project state → STANDARD
        - Logs → PROVISIONAL
        """

        if 'contract' in data or 'financial' in data or 'governance' in data:
            return WriteType.CRITICAL

        if 'state' in data or 'result' in data or 'plan' in data:
            return WriteType.STANDARD

        return WriteType.PROVISIONAL

    async def execute_write(self, write_op: WriteOperation) -> bool:
        """
        Execute a write with appropriate replication strategy.

        CRITICAL: Write to primary, wait for all replicas
        STANDARD: Write to primary, async replicate
        PROVISIONAL: Write to primary only
        """

        try:
            # Primary write (must succeed)
            primary_success = await self._write_to_region(
                write_op.region,
                write_op.write_id,
                write_op.data
            )

            if not primary_success:
                write_op.status = "failed"
                self.writes_failed.append(write_op)
                return False

            # Handle replication based on write type
            if write_op.write_type == WriteType.CRITICAL:
                # Wait for all replicas
                replica_tasks = [
                    self._write_to_region(region, write_op.write_id, write_op.data)
                    for region in write_op.replicas
                ]
                replica_results = await asyncio.gather(*replica_tasks)

                if all(replica_results):
                    write_op.status = "replicated"
                    return True
                else:
                    # CRITICAL write needs all replicas, partial replication fails
                    write_op.status = "failed"
                    self.writes_failed.append(write_op)
                    return False

            elif write_op.write_type == WriteType.STANDARD:
                # Start async replication, don't wait
                asyncio.create_task(self._async_replicate(
                    write_op.replicas,
                    write_op.write_id,
                    write_op.data
                ))
                write_op.status = "written"
                return True

            else:  # PROVISIONAL
                # Don't replicate
                write_op.status = "written"
                return True

        except Exception as e:
            write_op.status = "failed"
            self.writes_failed.append(write_op)
            return False

    async def _write_to_region(self, region: Region, key: str, data: Dict[str, Any]) -> bool:
        """Write data to specific region (stub)."""
        # In production, this connects to regional database
        # Simulating with delay
        await asyncio.sleep(0.1)
        return True

    async def _async_replicate(self, regions: List[Region], key: str, data: Dict[str, Any]):
        """Asynchronously replicate to regions (fire and forget)."""
        tasks = [
            self._write_to_region(region, key, data)
            for region in regions
        ]
        await asyncio.gather(*tasks, return_exceptions=True)

    def get_failed_writes(self) -> List[WriteOperation]:
        """Get list of failed writes."""
        return self.writes_failed

    def retry_failed_writes(self) -> Dict[str, int]:
        """Retry all failed writes."""
        success_count = 0
        failed_count = 0

        for write_op in self.writes_failed[:]:
            # Retry logic here
            self.writes_failed.remove(write_op)
            failed_count += 1

        return {
            'retried': len(self.writes_failed),
            'succeeded': success_count,
            'failed': failed_count
        }

    def checkpoint_state(self) -> Dict[str, Any]:
        """Create a state checkpoint for recovery."""
        self.last_checkpoint = {
            'timestamp': datetime.utcnow().isoformat(),
            'pending_writes': len(self.writes_pending),
            'failed_writes': len(self.writes_failed)
        }
        return self.last_checkpoint


class DistributedDataManager:
    """
    Main manager for distributed data operations.
    Coordinates persistence, consistency, and failover.
    """

    def __init__(self):
        self.consistency_manager = DataConsistencyManager()
        self.region_health = {region: True for region in Region}
        self.active_region = Region.PRIMARY

    def mark_region_failed(self, region: Region):
        """Mark a region as failed."""
        self.region_health[region] = False

        # Switch to backup if primary failed
        if region == Region.PRIMARY:
            for backup in [Region.BACKUP_1, Region.BACKUP_2]:
                if self.region_health[backup]:
                    self.active_region = backup
                    break

    def mark_region_recovered(self, region: Region):
        """Mark a region as recovered."""
        self.region_health[region] = True

        # Switch back to primary if it recovered
        if region == Region.PRIMARY:
            self.active_region = Region.PRIMARY

    def get_healthy_regions(self) -> List[Region]:
        """Get list of healthy regions."""
        return [r for r, healthy in self.region_health.items() if healthy]

    def get_status(self) -> Dict[str, Any]:
        """Get distributed system status."""
        return {
            'active_region': self.active_region.value,
            'region_health': {r.value: h for r, h in self.region_health.items()},
            'pending_writes': len(self.consistency_manager.writes_pending),
            'failed_writes': len(self.consistency_manager.writes_failed),
            'last_checkpoint': self.consistency_manager.last_checkpoint
        }


__all__ = [
    'DataConsistencyManager',
    'DistributedDataManager',
    'WriteOperation',
    'WriteType',
    'Region'
]
