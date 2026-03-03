# heartbeat_monitor.py

import threading
import time


class HeartbeatMonitor:

    def __init__(self, registry, interval=5):
        self.registry = registry
        self.interval = interval
        self._stop = False

    def start(self):

        t = threading.Thread(target=self._loop, daemon=True)
        t.start()

    def _loop(self):

        while not self._stop:
            self.registry.heartbeat()
            time.sleep(self.interval)
