# REAPERS/crash_predictor.py

import time
import threading
from collections import defaultdict


class CrashPredictor:
    """
    Detects abnormal exception frequency or freeze patterns.
    """

    def __init__(self, threshold: int = 5, window_seconds: int = 30):
        self.threshold = threshold
        self.window = window_seconds
        self.exceptions = defaultdict(list)
        self.lock = threading.Lock()

    def register_exception(self, module_name: str):
        with self.lock:
            now = time.time()
            self.exceptions[module_name].append(now)

            # Clean old timestamps
            self.exceptions[module_name] = [
                t for t in self.exceptions[module_name]
                if now - t <= self.window
            ]

    def is_unstable(self, module_name: str) -> bool:
        with self.lock:
            return len(self.exceptions[module_name]) >= self.threshold
