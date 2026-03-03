# persistence_store.py

import json
from pathlib import Path


class PersistenceStore:

    def __init__(self, file_path="automation_state.json"):
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            self._save({})

    def _load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def update_job(self, job_id, status):
        data = self._load()
        data[job_id] = status
        self._save(data)
