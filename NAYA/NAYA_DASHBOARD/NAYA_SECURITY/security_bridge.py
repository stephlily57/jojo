
from NAYA_DASHBOARD.NAYA_SECURITY.signature_request import create_signature_request
from NAYA_DASHBOARD.NAYA_SECURITY.signature_validator import validate_signature
from NAYA_DASHBOARD.NAYA_SECURITY.identity_guard import check_identity
from NAYA_DASHBOARD.NAYA_SECURITY.audit_trail import record
from NAYA_INTERFACE.bus.state_stream import state_stream

def request_and_sign(action: str, payload: dict, signer: str):
    req = create_signature_request(action, payload)
    state_stream.update_state("signature", {"pending": req})

    if not check_identity(signer):
        raise PermissionError("Unauthorized signer")

    signed = validate_signature(req, signer)
    record(signed)

    state_stream.update_state("signature", {"signed": signed})
    return signed
