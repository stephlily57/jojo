import time
from typing import Dict

from REAPERS.integrity_guard import IntegrityGuard
from REAPERS.snapshot_manager import SnapshotManager
from REAPERS.boot_authority import BootAuthority
from REAPERS.reapers_repair import ReapersRepair
from REAPERS.crash_predictor import CrashPredictor
from REAPERS.runtime_watchdog import RuntimeWatchdog
from REAPERS.isolation_engine import IsolationEngine


class ReapersKernel:

    def __init__(self):

        self.targets: Dict[str, str] = {
            "decision_core": "NAYA_CORE/decision/decision_core.py",
            "execution_trigger": "NAYA_CORE/decision/execution_trigger.py",
            "capital_manager": "NAYA_CORE/economic/capital_reserve_manager.py",
            "project_bridge": "NAYA_CORE/decision/project_engine_bridge.py",
        }

        self.snapshot_manager = SnapshotManager()
        self.integrity_guard = IntegrityGuard(self.targets)
        self.boot_authority = BootAuthority()
        self.repair_engine = ReapersRepair()
        self.crash_predictor = CrashPredictor()
        self.runtime_watchdog = RuntimeWatchdog()
        self.isolation_engine = IsolationEngine()

    def start(self):

        self.snapshot_manager.ensure_snapshots(self.targets)
        self.integrity_guard.create_baseline()

        if not self.boot_authority.authorize():
            raise SystemExit("Boot blocked by REAPERS")

        self.monitor_loop()

    def monitor_loop(self):

        while True:

            # 🔐 Runtime Protection
            if self.runtime_watchdog.debugger_detected():
                print("[REAPERS] Debugger detected")

            if self.runtime_watchdog.suspicious_environment():
                print("[REAPERS] Suspicious environment detected")

            # 🔎 Integrity Check
            integrity_results = self.integrity_guard.check_integrity()

            for module_name, is_valid in integrity_results.items():

                if not is_valid:
                    print(f"[REAPERS] Integrity breach: {module_name}")

                    self.isolation_engine.quarantine(module_name)

                    self.snapshot_manager.restore_snapshot(
                        module_name,
                        self.targets[module_name]
                    )

                    self.integrity_guard.create_baseline()

                    print(f"[REAPERS] Restored: {module_name}")

            time.sleep(5)
