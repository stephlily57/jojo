# REAPERS/integrity_guard.py

import hashlib
import os
from typing import Dict


class IntegrityGuard:
    """
    Computes and verifies SHA-256 integrity of critical modules.
    """

    def __init__(self, targets: Dict[str, str]):
        """
        targets = { "module_name": "absolute_or_relative_path" }
        """
        self.targets = targets
        self.baseline_hashes: Dict[str, str] = {}

    def compute_hash(self, filepath: str) -> str:
        sha256 = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def create_baseline(self) -> None:
        for name, path in self.targets.items():
            if os.path.exists(path):
                self.baseline_hashes[name] = self.compute_hash(path)

    def check_integrity(self) -> Dict[str, bool]:
        results = {}
        for name, path in self.targets.items():
            if not os.path.exists(path):
                results[name] = False
                continue

            current_hash = self.compute_hash(path)
            baseline_hash = self.baseline_hashes.get(name)

            results[name] = current_hash == baseline_hash

        return results
