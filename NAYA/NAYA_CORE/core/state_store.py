import json
import os
from threading import Lock

class StateStore:

    def __init__(self, filepath="naya_state.json"):
        self.filepath = filepath
        self.lock = Lock()
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump({}, f)

    def read(self):
        with self.lock:
            with open(self.filepath, "r") as f:
                return json.load(f)

    def write(self, data):
        with self.lock:
            with open(self.filepath, "w") as f:
                json.dump(data, f, indent=2)

    def update(self, key, value):
        data = self.read()
        data[key] = value
        self.write(data)
