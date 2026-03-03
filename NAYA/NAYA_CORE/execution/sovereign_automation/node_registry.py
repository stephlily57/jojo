# node_registry.py

import json
import uuid
from pathlib import Path
from datetime import datetime


class NodeRegistry:

    def __init__(self, file_path="node_registry.json"):
        self.file_path = Path(file_path)
        self.node_id = str(uuid.uuid4())

        if not self.file_path.exists():
            self._save({})

    def _load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def heartbeat(self):

        data = self._load()
        data[self.node_id] = datetime.utcnow().isoformat()
        self._save(data)

    def get_nodes(self):
        return self._load()
