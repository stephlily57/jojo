class ScoringMatrix:
    @staticmethod
    def compute(metrics: dict, economic_weight: float):
        cost = metrics.get("cost", 1)
        density = metrics.get("density", 1)
        performance = metrics.get("performance", 1)
        return ((1/cost)*0.5 + density*0.3 + performance*0.2) * economic_weight