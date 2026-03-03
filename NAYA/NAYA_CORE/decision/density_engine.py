class DensityEngine:

    def compute(self, opportunity):

        value = opportunity.get("value", 0)
        urgency = opportunity.get("urgency", 0)
        solvability = opportunity.get("solvability", 0)
        margin = opportunity.get("margin", 0)

        return (value * 0.4) + (urgency * 0.3) + (solvability * 0.2) + (margin * 0.1)
