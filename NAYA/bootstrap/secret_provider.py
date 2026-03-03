import os
from bootstrap.secure_memory import SecureMemory


class SecretProvider:

    def __init__(self):
        self.memory = SecureMemory()

    def load(self):

        # Cloud Run → variables d’environnement
        if os.getenv("K_SERVICE"):
            for key, value in os.environ.items():
                if key.startswith("NAYA_"):
                    self.memory.store(key, value)

        # VM → dossier secret
        else:
            from pathlib import Path
            secret_dir = Path("NAYA_SECRET")
            for file in secret_dir.glob("*.key"):
                self.memory.store(file.stem, file.read_text())

        return self.memory
