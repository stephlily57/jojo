# NAYA_CORE/doctrine/economic_thresholds.py

from .core_constitution import CoreConstitution

class EconomicThresholds:

    @staticmethod
    def classify(value: float) -> str:

        inv = CoreConstitution.STRATEGIC_INVARIANTS

        if value < inv["level_1_range"][0]:
            return "REJECT"

        if inv["level_1_range"][0] <= value <= inv["level_1_range"][1]:
            return "LEVEL_1"

        if inv["level_2_range"][0] <= value <= inv["level_2_range"][1]:
            return "LEVEL_2"

        if inv["level_3_range"][0] <= value <= inv["level_3_range"][1]:
            return "LEVEL_3"

        return "STRATEGIC_EXPANSION"
