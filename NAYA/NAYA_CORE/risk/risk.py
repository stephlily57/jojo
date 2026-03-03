class Risk:

    def compute(self, opportunity):

        volatility = opportunity.get("volatility", 0.3)
        dependency = opportunity.get("dependency", 0.2)

        return (volatility * 0.6) + (dependency * 0.4)
