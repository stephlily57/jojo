# REAPERS/anti_clone_guard.py

import os
import uuid
import hashlib
from pathlib import Path


class AntiCloneGuard:
    """
    Prevents system execution if environment signature changes.
    Binds REAPERS to machine fingerprint.
    """

    def __init__(self, storage_file: str = "REAPERS/.machine_signature"):
        self.storage_file = storage_file

    # ---------------------------------------------------------
    # MACHINE FINGERPRINT
    # ---------------------------------------------------------

    def _generate_fingerprint(self) -> str:
        system_data = f"{uuid.getnode()}-{os.name}-{os.getenv('COMPUTERNAME', '')}"
        return hashlib.sha256(system_data.encode()).hexdigest()

    # ---------------------------------------------------------
    # FIRST BOOT BINDING
    # ---------------------------------------------------------

    def bind_if_needed(self) -> None:
        fingerprint = self._generate_fingerprint()

        if not Path(self.storage_file).exists():
            with open(self.storage_file, "w") as f:
                f.write(fingerprint)
            return

    # ---------------------------------------------------------
    # VALIDATION
    # ---------------------------------------------------------

    def validate_environment(self) -> bool:
        fingerprint = self._generate_fingerprint()

        if not Path(self.storage_file).exists():
            return False

        with open(self.storage_file, "r") as f:
            stored = f.read().strip()

        return stored == fingerprint
