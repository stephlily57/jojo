class DensityLayer:

    def compute(self, opportunity):

        value = opportunity.get("value", 0)
        effort = opportunity.get("effort", 1)
        risk = opportunity.get("risk", 1)

        score = (value / (effort * risk + 1)) / 100000

        return min(score, 1)
