import hashlib
import json


class IntegrityHashManager:

    @staticmethod
    def compute_hash(data):
        serialized = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(serialized).hexdigest()
