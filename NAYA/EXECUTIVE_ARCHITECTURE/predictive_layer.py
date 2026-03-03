class PredictiveLayer:

    def __init__(self):
        self.volatility_index = 0.0

    def update_volatility(self, value):
        self.volatility_index = value

    def risk_level(self):

        if self.volatility_index > 0.7:
            return "HIGH"

        if self.volatility_index > 0.4:
            return "MEDIUM"

        return "LOW"
