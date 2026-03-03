# REAPERS/runtime_watchdog.py

import os
import sys


class RuntimeWatchdog:
    """
    Basic anti-debug & runtime environment validation.
    """

    def debugger_detected(self) -> bool:
        return sys.gettrace() is not None

    def suspicious_environment(self) -> bool:
        suspicious_vars = ["PYCHARM_HOSTED", "VSCODE_PID"]
        return any(var in os.environ for var in suspicious_vars)
