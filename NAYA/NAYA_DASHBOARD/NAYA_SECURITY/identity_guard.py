
AUTHORIZED_SIGNERS = {"owner", "admin"}

def check_identity(signer: str) -> bool:
    return signer in AUTHORIZED_SIGNERS
