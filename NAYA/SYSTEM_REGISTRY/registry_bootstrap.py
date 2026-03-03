from pathlib import Path
import hashlib
import json
import sys


class SystemRegistry:

    def __init__(self):
        self.root = Path(".").resolve()
        self.domains = {}
        self.integrity_hash = None
        self.locked = False

    # =========================
    # DOMAIN REGISTRATION
    # =========================
    def register(self, name, instance):
        if self.locked:
            raise RuntimeError("Cannot register new domain in locked production mode.")
        self.domains[name] = instance

    # =========================
    # STRUCTURE VALIDATION
    # =========================
    def validate_structure(self):
        required_folders = [
            "NAYA_CORE",
            "KERNEL",
            "SYSTEM_REGISTRY"
        ]

        for folder in required_folders:
            if not (self.root / folder).exists():
                raise RuntimeError(f"Missing critical folder: {folder}")

    # =========================
    # INTEGRITY HASH
    # =========================
    def compute_integrity(self):
        hash_obj = hashlib.sha256()

        for file in sorted(self.root.rglob("*.py")):
            if "__pycache__" in str(file):
                continue
            try:
                content = file.read_bytes()
                hash_obj.update(content)
            except Exception:
                continue

        self.integrity_hash = hash_obj.hexdigest()
        return self.integrity_hash

    # =========================
    # ACTIVATION
    # =========================
    def activate(self):
        self.validate_structure()
        integrity = self.compute_integrity()

        print("=== SYSTEM REGISTRY ACTIVATED ===")
        print(f"Integrity Hash: {integrity}")

    # =========================
    # LOCK
    # =========================
    def lock_production(self):
        self.locked = True
        print("=== PRODUCTION LOCK ENABLED ===")

    # =========================
    # INITIALIZATION ENTRY
    # =========================
    def initialize(self, core_instance):
        self.register("naya_core", core_instance)
        self.activate()
        self.lock_production()
        return self
