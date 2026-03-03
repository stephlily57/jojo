# REAPERS/reapers_repair.py

from datetime import datetime
from typing import Dict

from REAPERS.snapshot_manager import SnapshotManager
from REAPERS.isolation_engine import IsolationEngine
from REAPERS.threat_memory import ThreatMemory


class ReapersRepair:
    """
    Final integrated repair engine.
    Handles quarantine, restore, memory logging.
    """

    def __init__(
        self,
        snapshot_manager: SnapshotManager,
        isolation_engine: IsolationEngine,
        threat_memory: ThreatMemory
    ) -> None:

        self.snapshot_manager = snapshot_manager
        self.isolation_engine = isolation_engine
        self.threat_memory = threat_memory

        self._repair_log: Dict[str, datetime] = {}

    # ---------------------------------------------------------
    # RESTORE MODULE
    # ---------------------------------------------------------

    def restore_module(self, module_name: str, target_path: str) -> None:

        print(f"[REAPERS] Repair initiated: {module_name}")

        # Log threat
        self.threat_memory.record("integrity_breach")

        # Quarantine
        self.isolation_engine.quarantine(module_name)

        # Restore
        self.snapshot_manager.restore_snapshot(module_name, target_path)

        # Reintegration
        self.isolation_engine.reintegrate(module_name)

        # Log repair timestamp
        self._repair_log[module_name] = datetime.utcnow()

        print(f"[REAPERS] Repair completed: {module_name}")

    # ---------------------------------------------------------
    # HISTORY
    # ---------------------------------------------------------

    def repair_history(self) -> Dict[str, datetime]:
        return dict(self._repair_log)
