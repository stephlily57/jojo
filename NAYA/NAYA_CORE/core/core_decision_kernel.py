class CoreDecisionKernel:

    def __init__(self, decision_core, economic_engine, sovereignty_filter):
        self.decision_core = decision_core
        self.economic_engine = economic_engine
        self.sovereignty_filter = sovereignty_filter

    def evaluate(self, opportunity):
        if not self.sovereignty_filter.validate(opportunity):
            return {"status": "rejected", "reason": "sovereignty_violation"}

        economic_score = self.economic_engine.score(opportunity)
        decision = self.decision_core.process(opportunity, economic_score)

        return decision
