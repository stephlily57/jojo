# sovereignty_guardian.py

class SovereigntyGuardian:

    def validate(self, opportunity: dict) -> bool:
        sovereignty_risk = opportunity.get("sovereignty_risk", 0)
        structural_dependency = opportunity.get("structural_dependency", 0)

        if sovereignty_risk > 0.7:
            return False

        if structural_dependency > 0.7:
            return False

        return True


SOVEREIGNTY_GUARDIAN = SovereigntyGuardian()
