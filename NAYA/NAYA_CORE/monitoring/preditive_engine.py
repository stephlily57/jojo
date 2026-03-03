class PredictiveEngine:

    def __init__(self, memory_narrative):
        self.memory = memory_narrative

    def forecast_risk(self, mission_context):
        history = self.memory.retrieve_similar(mission_context)
        if not history:
            return 0

        failure_rate = sum(h["failed"] for h in history) / len(history)
        return failure_rate

    def should_escalate(self, mission_context):
        risk = self.forecast_risk(mission_context)
        return risk > 0.4
