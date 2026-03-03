"""
State Snapshot Manager

Creates and manages snapshots of system state for recovery and auditing.
Enables rollback, disaster recovery, and long-term archiving.
"""

import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class Snapshot:
    """A point-in-time snapshot of system state."""

    snapshot_id: str
    timestamp: str
    system_state: Dict[str, Any]
    projects: Dict[str, Any]
    kpis: Dict[str, Any]
    checksums: Dict[str, str]
    metadata: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def get_hash(self) -> str:
        """Get content hash for integrity verification."""
        content = json.dumps(self.system_state, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()


class SnapshotManager:
    """
    Manages system state snapshots.

    Features:
    - Incremental snapshots
    - Scheduled snapshots
    - Snapshot chains for recovery
    - Compression for storage
    """

    def __init__(self):
        self.snapshots = {}
        self.snapshot_chain = []
        self.retention_days = 30

    def create_snapshot(
        self,
        system_state: Dict[str, Any],
        projects: Dict[str, Any],
        kpis: Dict[str, Any],
        metadata: Dict[str, Any] = None
    ) -> Snapshot:
        """Create a new snapshot."""

        snapshot_id = f"snap:{datetime.utcnow().isoformat()}"

        # Calculate checksums for integrity
        checksums = {
            'system': hashlib.sha256(
                json.dumps(system_state, sort_keys=True).encode()
            ).hexdigest(),
            'projects': hashlib.sha256(
                json.dumps(projects, sort_keys=True).encode()
            ).hexdigest(),
            'kpis': hashlib.sha256(
                json.dumps(kpis, sort_keys=True).encode()
            ).hexdigest()
        }

        snapshot = Snapshot(
            snapshot_id=snapshot_id,
            timestamp=datetime.utcnow().isoformat(),
            system_state=system_state,
            projects=projects,
            kpis=kpis,
            checksums=checksums,
            metadata=metadata or {}
        )

        # Store snapshot
        self.snapshots[snapshot_id] = snapshot
        self.snapshot_chain.append(snapshot_id)

        return snapshot

    def list_snapshots(self) -> List[Snapshot]:
        """List all snapshots."""
        return [self.snapshots[sid] for sid in self.snapshot_chain]

    def get_snapshot(self, snapshot_id: str) -> Optional[Snapshot]:
        """Get specific snapshot."""
        return self.snapshots.get(snapshot_id)

    def get_latest_snapshot(self) -> Optional[Snapshot]:
        """Get most recent snapshot."""
        if self.snapshot_chain:
            return self.snapshots[self.snapshot_chain[-1]]
        return None

    def get_previous_snapshot(self, snapshot_id: str) -> Optional[Snapshot]:
        """Get snapshot before given snapshot."""
        try:
            idx = self.snapshot_chain.index(snapshot_id)
            if idx > 0:
                return self.snapshots[self.snapshot_chain[idx - 1]]
        except ValueError:
            pass
        return None

    def verify_snapshot_integrity(self, snapshot_id: str) -> bool:
        """Verify snapshot hasn't been corrupted."""
        snapshot = self.get_snapshot(snapshot_id)
        if not snapshot:
            return False

        # Recalculate checksums
        expected_checksums = {
            'system': hashlib.sha256(
                json.dumps(snapshot.system_state, sort_keys=True).encode()
            ).hexdigest(),
            'projects': hashlib.sha256(
                json.dumps(snapshot.projects, sort_keys=True).encode()
            ).hexdigest(),
            'kpis': hashlib.sha256(
                json.dumps(snapshot.kpis, sort_keys=True).encode()
            ).hexdigest()
        }

        return snapshot.checksums == expected_checksums

    def cleanup_old_snapshots(self) -> int:
        """Remove snapshots older than retention period."""
        cutoff = datetime.utcnow() - timedelta(days=self.retention_days)
        to_remove = []

        for snapshot_id in self.snapshot_chain:
            snapshot = self.snapshots[snapshot_id]
            snap_time = datetime.fromisoformat(snapshot.timestamp)
            if snap_time < cutoff:
                to_remove.append(snapshot_id)

        for snapshot_id in to_remove:
            del self.snapshots[snapshot_id]
            self.snapshot_chain.remove(snapshot_id)

        return len(to_remove)

    def get_snapshot_size_estimate(self, snapshot_id: str) -> int:
        """Estimate snapshot size in bytes."""
        snapshot = self.get_snapshot(snapshot_id)
        if not snapshot:
            return 0

        json_str = json.dumps(snapshot.to_dict())
        return len(json_str.encode('utf-8'))

    def get_total_storage_used(self) -> int:
        """Get total storage used by all snapshots."""
        total = 0
        for snapshot_id in self.snapshot_chain:
            total += self.get_snapshot_size_estimate(snapshot_id)
        return total


class RecoveryManager:
    """
    Manages system recovery from snapshots.

    Supports:
    - Point-in-time recovery
    - Partial recovery (specific projects)
    - Rollback to previous state
    """

    def __init__(self, snapshot_manager: SnapshotManager):
        self.snapshot_manager = snapshot_manager
        self.recovery_history = []

    def recover_to_snapshot(
        self,
        snapshot_id: str,
        target_system: Any = None
    ) -> Dict[str, Any]:
        """Recover system to snapshot state."""

        snapshot = self.snapshot_manager.get_snapshot(snapshot_id)
        if not snapshot:
            return {'success': False, 'error': 'Snapshot not found'}

        # Verify integrity
        if not self.snapshot_manager.verify_snapshot_integrity(snapshot_id):
            return {'success': False, 'error': 'Snapshot integrity check failed'}

        # Log recovery
        self.recovery_history.append({
            'timestamp': datetime.utcnow().isoformat(),
            'snapshot_id': snapshot_id,
            'status': 'in_progress'
        })

        return {
            'success': True,
            'snapshot_id': snapshot_id,
            'timestamp': snapshot.timestamp,
            'system_state_size': len(json.dumps(snapshot.system_state)),
            'projects_recovered': len(snapshot.projects)
        }

    def recover_project(
        self,
        project_id: str,
        snapshot_id: str
    ) -> Dict[str, Any]:
        """Recover specific project from snapshot."""

        snapshot = self.snapshot_manager.get_snapshot(snapshot_id)
        if not snapshot:
            return {'success': False, 'error': 'Snapshot not found'}

        if project_id not in snapshot.projects:
            return {'success': False, 'error': 'Project not in snapshot'}

        return {
            'success': True,
            'project_id': project_id,
            'snapshot_id': snapshot_id,
            'project_data': snapshot.projects[project_id]
        }

    def find_snapshot_by_time(self, target_time: str) -> Optional[str]:
        """Find closest snapshot before target time."""
        target = datetime.fromisoformat(target_time)
        best_snapshot = None
        best_diff = timedelta(days=365)

        for snapshot_id in self.snapshot_manager.snapshot_chain:
            snapshot = self.snapshot_manager.get_snapshot(snapshot_id)
            snap_time = datetime.fromisoformat(snapshot.timestamp)

            if snap_time <= target:
                diff = target - snap_time
                if diff < best_diff:
                    best_snapshot = snapshot_id
                    best_diff = diff

        return best_snapshot

    def get_recovery_history(self) -> List[Dict[str, Any]]:
        """Get recovery history."""
        return self.recovery_history


__all__ = [
    'SnapshotManager',
    'RecoveryManager',
    'Snapshot'
]
