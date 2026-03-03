class AntiExfiltrationGuard:

    def validate(self, payload):
        if payload is None:
            return False
        if isinstance(payload, str) and "SECRET" in payload:
            return False
        return True