"""
PERSISTENCE Layer

Manages data storage, consistency, and recovery.

Key Components:
- PersistenceManager: Main data storage interface
- DistributedDataManager: Multi-region consistency
- SnapshotManager: Point-in-time snapshots
- WriteClassifier: Intelligent write optimization
"""

from .persistence_manager import (
    PersistenceManager,
    PersistenceBackend,
    MemoryBackend,
    FileBackend
)

from .distributed_data_manager import (
    DistributedDataManager,
    DataConsistencyManager,
    WriteOperation,
    WriteType,
    Region
)

from .snapshot_manager import (
    SnapshotManager,
    RecoveryManager,
    Snapshot
)

from .write_classifier import (
    WriteClassifier,
    WriteBatcher,
    WriteProfile,
    WriteStrategy,
    DataClassification
)

__all__ = [
    # Core persistence
    'PersistenceManager',
    'PersistenceBackend',
    'MemoryBackend',
    'FileBackend',

    # Distributed operations
    'DistributedDataManager',
    'DataConsistencyManager',
    'WriteOperation',
    'WriteType',
    'Region',

    # Snapshots and recovery
    'SnapshotManager',
    'RecoveryManager',
    'Snapshot',

    # Write optimization
    'WriteClassifier',
    'WriteBatcher',
    'WriteProfile',
    'WriteStrategy',
    'DataClassification'
]
