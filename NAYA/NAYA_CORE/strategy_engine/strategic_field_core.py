# strategic_field_core.py

class StrategicFieldCore:

    def evaluate_field_expansion(self, opportunity: dict) -> float:
        sector_growth = opportunity.get("sector_growth", 0.5)
        infrastructure_gain = opportunity.get("infrastructure_gain", 0.3)
        credibility_gain = opportunity.get("credibility_gain", 0.3)

        return (sector_growth + infrastructure_gain + credibility_gain) / 3


STRATEGIC_FIELD_CORE = StrategicFieldCore()
