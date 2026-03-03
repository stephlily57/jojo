# signature_verifier.py

import hashlib

SECRET = "CHANGE_THIS"

def verify_signature(intent_dict: dict, signature: str):

    raw = str(sorted(intent_dict.items())) + SECRET
    expected = hashlib.sha256(raw.encode()).hexdigest()

    return expected == signature
