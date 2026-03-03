
import json
from cryptography.fernet import Fernet

class IntentJournal:
    def __init__(self, key_path, log_path):
        with open(key_path, "rb") as f:
            self.cipher = Fernet(f.read())
        self.log_path = log_path
        self.memory = []

    def log(self, intent_dict):
        self.memory.append(intent_dict)
        encrypted = self.cipher.encrypt(json.dumps(intent_dict).encode())
        with open(self.log_path, "ab") as f:
            f.write(encrypted + b"\n")
