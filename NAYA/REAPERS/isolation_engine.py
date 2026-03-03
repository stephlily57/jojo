# REAPERS/isolation_engine.py

import threading
from typing import Dict, Set
from datetime import datetime


class IsolationEngine:
    """
    Handles module quarantine and reintegration.

    Responsibilities:
    - Quarantine unstable or corrupted modules
    - Track isolated modules
    - Allow controlled reintegration
    - Prevent duplicate quarantine
    """

    def __init__(self) -> None:
        self._quarantined_modules: Set[str] = set()
        self._quarantine_log: Dict[str, datetime] = {}
        self._lock = threading.Lock()

    # ---------------------------------------------------------
    # QUARANTINE
    # ---------------------------------------------------------

    def quarantine(self, module_name: str) -> None:
        """
        Isolate a module from active runtime logic.
        Safe to call multiple times.
        """

        with self._lock:

            if module_name in self._quarantined_modules:
                return

            self._quarantined_modules.add(module_name)
            self._quarantine_log[module_name] = datetime.utcnow()

            print(f"[REAPERS] Module quarantined: {module_name}")

    # ---------------------------------------------------------
    # REINTEGRATION
    # ---------------------------------------------------------

    def reintegrate(self, module_name: str) -> None:
        """
        Reinstate a previously quarantined module.
        """

        with self._lock:

            if module_name not in self._quarantined_modules:
                return

            self._quarantined_modules.remove(module_name)
            self._quarantine_log.pop(module_name, None)

            print(f"[REAPERS] Module reintegrated: {module_name}")

    # ---------------------------------------------------------
    # STATUS CHECK
    # ---------------------------------------------------------

    def is_quarantined(self, module_name: str) -> bool:
        """
        Check if module is currently isolated.
        """

        with self._lock:
            return module_name in self._quarantined_modules

    def get_quarantined_modules(self) -> Dict[str, datetime]:
        """
        Return snapshot of quarantined modules.
        """

        with self._lock:
            return dict(self._quarantine_log)

    # ---------------------------------------------------------
    # EMERGENCY RESET
    # ---------------------------------------------------------

    def reset_all(self) -> None:
        """
        Clear all quarantine states.
        """

        with self._lock:
            self._quarantined_modules.clear()
            self._quarantine_log.clear()

            print("[REAPERS] All quarantine states cleared")
