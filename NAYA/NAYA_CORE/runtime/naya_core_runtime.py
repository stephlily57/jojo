from NAYA_CORE.decision.decision_core import DecisionCore
from NAYA_CORE.memory.distributed_memory import DistributedMemory
from NAYA_CORE.evolution.adaptive_feedback import AdaptiveFeedback
from NAYA_CORE.orchestration.opportunity_pipeline import OpportunityPipeline
from NAYA_CORE.risk.guardian import Guardian

class NayaCoreRuntime:

    def __init__(self):
        self.memory = DistributedMemory()
        self.decision = DecisionCore(self.memory)
        self.feedback = AdaptiveFeedback(self.memory)
        self.pipeline = OpportunityPipeline(self.decision)
        self.guardian = Guardian()

    def process_opportunity(self, opportunity):

        risk_level = self.guardian.evaluate(opportunity)

        if not self.guardian.allow(opportunity, risk_level):
            return self.guardian.restructure(opportunity)

        enriched = self.pipeline.analyze(opportunity)
        decision = self.decision.evaluate(enriched)

        self.memory.store(enriched, decision)
        self.feedback.learn(enriched, decision)

        return decision
