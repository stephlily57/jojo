
import hashlib
import json
from time import time

def validate_signature(request: dict, signer: str) -> dict:
    content = json.dumps(request, sort_keys=True).encode()
    signature = hashlib.sha256(content).hexdigest()

    return {
        "request_id": request["id"],
        "signed_by": signer,
        "signature": signature,
        "timestamp": time()
    }
