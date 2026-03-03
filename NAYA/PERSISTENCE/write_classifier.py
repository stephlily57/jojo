"""
Write Classification & Optimization

Determines how each write operation should be handled based on content and context.
Optimizes for consistency, performance, and cost.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, List, Tuple, Optional
from datetime import datetime


class WriteStrategy(Enum):
    """Strategy for handling a write."""
    IMMEDIATE_SYNC = "immediate_sync"        # Sync to all regions
    ASYNC_REPLICATE = "async_replicate"      # Fire-and-forget replication
    LOCAL_ONLY = "local_only"                # Keep data local
    CACHE_FIRST = "cache_first"              # Write to cache first, persist async
    BATCH_OPTIMIZE = "batch_optimize"        # Batch multiple writes


class DataClassification(Enum):
    """Data sensitivity/importance classification."""
    GOVERNANCE = "governance"                # Critical governance rules
    FINANCIAL = "financial"                  # Financial/contractual data
    OPERATIONAL = "operational"              # Daily operational data
    AUDIT = "audit"                          # Audit logs
    TRANSIENT = "transient"                  # Ephemeral data


@dataclass
class WriteProfile:
    """Profile of a write operation for decision making."""

    write_id: str
    operation_type: str
    data_classification: DataClassification
    estimated_size: int
    priority: int  # 1-10, 10 is highest
    timestamp: str
    related_projects: List[str]

    def get_criticality_score(self) -> float:
        """Calculate how critical this write is (0-100)."""

        base_score = {
            DataClassification.GOVERNANCE: 100,
            DataClassification.FINANCIAL: 90,
            DataClassification.OPERATIONAL: 60,
            DataClassification.AUDIT: 40,
            DataClassification.TRANSIENT: 10
        }[self.data_classification]

        priority_boost = self.priority * 2

        return min(100, base_score + priority_boost)


class WriteClassifier:
    """
    Classifies writes and selects optimal handling strategy.

    Considers:
    - Data type and criticality
    - System load
    - Network conditions
    - Cost vs consistency tradeoffs
    """

    def __init__(self):
        self.write_history = []
        self.recent_failures = 0
        self.system_load = 0.5  # 0-1, where 1 is saturated

    def classify_write(
        self,
        operation_type: str,
        data: Dict[str, Any],
        priority: int = 5
    ) -> Tuple[DataClassification, WriteStrategy]:
        """Classify a write and determine strategy."""

        # Determine data classification
        classification = self._classify_data(data)

        # Determine strategy based on classification and system state
        strategy = self._select_strategy(classification, priority)

        return classification, strategy

    def _classify_data(self, data: Dict[str, Any]) -> DataClassification:
        """Classify data based on content."""

        data_str = str(data).lower()

        # Governance keywords
        if any(k in data_str for k in ['contract', 'governance', 'rule', 'constraint', 'evolution']):
            return DataClassification.GOVERNANCE

        # Financial keywords
        if any(k in data_str for k in ['price', 'cost', 'revenue', 'financial', 'budget']):
            return DataClassification.FINANCIAL

        # Operational keywords
        if any(k in data_str for k in ['project', 'plan', 'execution', 'state', 'status']):
            return DataClassification.OPERATIONAL

        # Audit keywords
        if any(k in data_str for k in ['audit', 'log', 'event', 'access', 'security']):
            return DataClassification.AUDIT

        # Default to transient
        return DataClassification.TRANSIENT

    def _select_strategy(
        self,
        classification: DataClassification,
        priority: int
    ) -> WriteStrategy:
        """Select handling strategy."""

        # High priority, critical data → immediate sync
        if priority >= 8 and classification in [
            DataClassification.GOVERNANCE,
            DataClassification.FINANCIAL
        ]:
            return WriteStrategy.IMMEDIATE_SYNC

        # Normal critical data → async replicate
        if classification in [DataClassification.GOVERNANCE, DataClassification.FINANCIAL]:
            return WriteStrategy.ASYNC_REPLICATE

        # Operational under light load → async
        if self.system_load < 0.7 and classification == DataClassification.OPERATIONAL:
            return WriteStrategy.ASYNC_REPLICATE

        # Operational under heavy load → cache first
        if self.system_load >= 0.7 and classification == DataClassification.OPERATIONAL:
            return WriteStrategy.CACHE_FIRST

        # Audit/transient → local only
        if classification in [DataClassification.AUDIT, DataClassification.TRANSIENT]:
            return WriteStrategy.LOCAL_ONLY

        # Default
        return WriteStrategy.ASYNC_REPLICATE

    def record_write(
        self,
        write_id: str,
        classification: DataClassification,
        strategy: WriteStrategy,
        success: bool,
        duration_ms: float
    ):
        """Record a write for learning."""

        self.write_history.append({
            'write_id': write_id,
            'classification': classification.value,
            'strategy': strategy.value,
            'success': success,
            'duration_ms': duration_ms,
            'timestamp': datetime.utcnow().isoformat()
        })

        if not success:
            self.recent_failures += 1
        else:
            self.recent_failures = max(0, self.recent_failures - 1)

    def update_system_load(self, load: float):
        """Update current system load (0-1)."""
        self.system_load = max(0, min(1, load))

    def get_classification_stats(self) -> Dict[str, Any]:
        """Get statistics about writes."""

        total = len(self.write_history)
        if total == 0:
            return {'writes': 0}

        success = sum(1 for w in self.write_history if w['success'])

        by_classification = {}
        for w in self.write_history:
            cls = w['classification']
            if cls not in by_classification:
                by_classification[cls] = 0
            by_classification[cls] += 1

        by_strategy = {}
        for w in self.write_history:
            strat = w['strategy']
            if strat not in by_strategy:
                by_strategy[strat] = 0
            by_strategy[strat] += 1

        return {
            'total_writes': total,
            'success_count': success,
            'success_rate': success / total if total > 0 else 0,
            'recent_failures': self.recent_failures,
            'by_classification': by_classification,
            'by_strategy': by_strategy,
            'avg_duration_ms': sum(w['duration_ms'] for w in self.write_history) / total
        }


class WriteBatcher:
    """
    Batches writes for efficiency.
    Collects writes and flushes when beneficial.
    """

    def __init__(self, batch_size: int = 10, batch_timeout_ms: int = 5000):
        self.batch_size = batch_size
        self.batch_timeout_ms = batch_timeout_ms
        self.pending_writes = []
        self.last_flush = datetime.utcnow()

    def add_write(self, write_profile: WriteProfile) -> bool:
        """Add write to batch. Returns True if batch ready to flush."""

        self.pending_writes.append(write_profile)

        # Check if batch is full
        if len(self.pending_writes) >= self.batch_size:
            return True

        # Check if batch is old
        age_ms = (datetime.utcnow() - self.last_flush).total_seconds() * 1000
        if age_ms >= self.batch_timeout_ms and len(self.pending_writes) > 0:
            return True

        return False

    def get_pending_batch(self) -> List[WriteProfile]:
        """Get and clear pending writes."""
        batch = self.pending_writes
        self.pending_writes = []
        self.last_flush = datetime.utcnow()
        return batch

    def get_batch_stats(self) -> Dict[str, Any]:
        """Get current batch statistics."""
        return {
            'pending_writes': len(self.pending_writes),
            'batch_size': self.batch_size,
            'age_ms': (datetime.utcnow() - self.last_flush).total_seconds() * 1000
        }


__all__ = [
    'WriteClassifier',
    'WriteBatcher',
    'WriteProfile',
    'WriteStrategy',
    'DataClassification'
]
