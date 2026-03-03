# engine_density_filter.py

from dataclasses import dataclass
from typing import Dict


@dataclass
class DensityResult:
    score: float
    solvable: bool
    premium: bool
    discreet: bool


class DensityFilter:

    def evaluate(self, opportunity: Dict) -> DensityResult:
        value = opportunity.get("value", 0)
        urgency = opportunity.get("urgency", 0)
        discretion = opportunity.get("discretion", 0)
        solvability = opportunity.get("solvable", False)

        score = (value * 0.5) + (urgency * 0.3) + (discretion * 0.2)

        return DensityResult(
            score=score,
            solvable=solvability,
            premium=value >= 1000,
            discreet=discretion >= 0.6
        )


DENSITY_FILTER = DensityFilter()
