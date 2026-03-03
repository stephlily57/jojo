class SignatureValidator:

    @staticmethod
    def verify(signature: str):
        if not signature or len(signature) < 10:
            raise ValueError("Invalid signature")
        return True