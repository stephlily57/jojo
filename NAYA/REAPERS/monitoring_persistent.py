import threading
import time

class PersistentMonitor:

    def __init__(self):
        self.running = True

    def start(self):
        threading.Thread(target=self._loop, daemon=True).start()

    def _loop(self):
        while self.running:
            time.sleep(5)