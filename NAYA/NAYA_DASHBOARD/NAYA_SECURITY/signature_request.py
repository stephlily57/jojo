
from time import time
from uuid import uuid4

def create_signature_request(action: str, payload: dict) -> dict:
    return {
        "id": str(uuid4()),
        "action": action,
        "payload": payload,
        "timestamp": time(),
        "status": "pending"
    }
