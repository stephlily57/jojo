# idempotency_guard.py

import hashlib
import json
from pathlib import Path


class IdempotencyGuard:

    def __init__(self, store_file="idempotency_store.json"):
        self.store_file = Path(store_file)
        if not self.store_file.exists():
            self._save({})

    def _load(self):
        with open(self.store_file, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.store_file, "w") as f:
            json.dump(data, f, indent=2)

    def generate_key(self, payload: dict) -> str:
        raw = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(raw.encode()).hexdigest()

    def is_processed(self, key: str) -> bool:
        data = self._load()
        return key in data

    def mark_processed(self, key: str):
        data = self._load()
        data[key] = True
        self._save(data)
