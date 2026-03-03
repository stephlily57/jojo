import hashlib
import os

class CoreIntegrityLock:

    def __init__(self, base_path):
        self.base_path = base_path

    def compute_checksum(self):
        hash_obj = hashlib.sha256()
        for root, dirs, files in os.walk(self.base_path):
            for file in sorted(files):
                if file.endswith(".py"):
                    with open(os.path.join(root, file), "rb") as f:
                        hash_obj.update(f.read())
        return hash_obj.hexdigest()

    def verify(self, stored_hash):
        current = self.compute_checksum()
        return current == stored_hash
