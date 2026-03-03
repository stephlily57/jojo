# engine_refusal_protocol.py


class RefusalProtocol:

    def evaluate(self, sovereignty_risk: float) -> dict:
        if sovereignty_risk > 0.7:
            return {
                "status": "REFUSED",
                "alternative": "Restructuration autonome recommandée"
            }
        return {"status": "ACCEPTED"}


REFUSAL_PROTOCOL = RefusalProtocol()
