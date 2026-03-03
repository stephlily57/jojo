# predictive_load_balancer.py

class PredictiveLoadBalancer:

    def predict(self, historical_load: int):

        if historical_load > 50:
            return "high"

        return "normal"
