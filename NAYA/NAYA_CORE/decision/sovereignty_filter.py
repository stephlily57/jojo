# NAYA_CORE/decision/sovereignty_filter.py

from typing import Dict


class SovereigntyFilter:

    def check(self, opportunity: Dict) -> bool:
        """
        Vérifie si l'opportunité menace la souveraineté.
        """

        dependency_level = float(opportunity.get("dependency_risk", 0))
        control_loss = float(opportunity.get("control_risk", 0))

        if dependency_level > 0.7:
            return False

        if control_loss > 0.7:
            return False

        return True


SOVEREIGNTY_FILTER = SovereigntyFilter()
