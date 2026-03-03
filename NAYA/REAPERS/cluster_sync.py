import threading
import time

class ClusterSync:

    def __init__(self):
        self.running = True

    def start(self):
        threading.Thread(target=self._sync_loop, daemon=True).start()

    def _sync_loop(self):
        while self.running:
            time.sleep(10)