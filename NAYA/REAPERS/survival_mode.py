# REAPERS/survival_mode.py

import threading
from datetime import datetime


class SurvivalMode:
    """
    Activates system stabilization under critical instability.
    Does NOT shutdown system.
    Reduces risk exposure and freezes sensitive operations.
    """

    def __init__(self) -> None:
        self._active = False
        self._activated_at = None
        self._lock = threading.Lock()

    # ---------------------------------------------------------
    # ACTIVATE
    # ---------------------------------------------------------

    def activate(self, reason: str = "UNKNOWN") -> None:
        with self._lock:

            if self._active:
                return

            self._active = True
            self._activated_at = datetime.utcnow()

            print(f"[REAPERS] SURVIVAL MODE ACTIVATED | Reason: {reason}")

    # ---------------------------------------------------------
    # DEACTIVATE
    # ---------------------------------------------------------

    def deactivate(self) -> None:
        with self._lock:

            if not self._active:
                return

            self._active = False
            print("[REAPERS] SURVIVAL MODE DEACTIVATED")

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------

    def is_active(self) -> bool:
        with self._lock:
            return self._active

    def activated_at(self):
        return self._activated_at

    # ---------------------------------------------------------
    # BEHAVIOR CONTROL
    # ---------------------------------------------------------

    def restrict_execution(self) -> bool:
        """
        If True, sensitive operations should slow down
        or enter safe execution mode.
        """
        return self.is_active()
