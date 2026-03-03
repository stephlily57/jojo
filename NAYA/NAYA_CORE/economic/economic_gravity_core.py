# NAYA_CORE / economic_gravity_core.py

class EconomicGravityCore:
    """
    Centre décisionnel basé sur densité économique augmentée.
    Non prioritaire, non bridé.
    """

    def evaluate(self, opportunity: dict) -> float:

        impact = opportunity.get("impact", 0.5)
        urgency = opportunity.get("urgency", 0.5)
        margin = opportunity.get("margin", 0.5)
        discretion = opportunity.get("discretion", 0.5)

        leverage = opportunity.get("strategic_leverage", 0.3)
        sovereignty_risk = opportunity.get("sovereignty_risk", 0.0)
        energy_cost = opportunity.get("energy_cost", 0.3)

        economic_core = impact * urgency * margin * discretion
        strategic_component = leverage
        risk_component = sovereignty_risk + energy_cost

        density = (economic_core + strategic_component) - risk_component

        return max(0.0, min(1.0, density))


ECONOMIC_GRAVITY_CORE = EconomicGravityCore()
