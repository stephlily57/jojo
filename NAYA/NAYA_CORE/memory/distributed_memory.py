import json
import threading

class DistributedMemory:

    def __init__(self, path="naya_memory.json"):
        self.path = path
        self.lock = threading.Lock()
        self._init_file()

    def _init_file(self):
        try:
            with open(self.path, "x") as f:
                json.dump([], f)
        except FileExistsError:
            pass

    def store(self, opportunity, decision):
        with self.lock:
            with open(self.path, "r") as f:
                data = json.load(f)

            data.append({
                "opportunity": opportunity,
                "decision": decision
            })

            with open(self.path, "w") as f:
                json.dump(data, f, indent=2)

    def load(self):
        with open(self.path, "r") as f:
            return json.load(f)
