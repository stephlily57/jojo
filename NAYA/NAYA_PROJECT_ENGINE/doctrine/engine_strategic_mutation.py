# engine_strategic_mutation.py


class StrategicMutation:

    def mutate(self, performance_score: float) -> str:
        if performance_score < 0.5:
            return "ADAPT_STRATEGY"
        return "STABLE"


STRATEGIC_MUTATION = StrategicMutation()
