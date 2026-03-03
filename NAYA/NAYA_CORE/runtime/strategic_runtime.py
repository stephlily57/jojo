from reaper_segmenter import ReaperSegmenter
from llm_orchestrator import LLMOrchestrator
from cost_optimizer import CostOptimizer
from predictive_engine import PredictiveEngine

class StrategicRuntime:

    def __init__(self, providers, doctrine, memory):
        self.reaper_segmenter = ReaperSegmenter()
        self.llm_orchestrator = LLMOrchestrator(providers, doctrine)
        self.cost_optimizer = CostOptimizer()
        self.predictive_engine = PredictiveEngine(memory)

    def process_mission(self, mission_id, context):

        # Prédiction risque
        if self.predictive_engine.should_escalate(context):
            context["allow_scaling"] = True

        # Multi-LLM si nécessaire
        if context.get("complex", False):
            decision = self.llm_orchestrator.run_parallel(context["prompt"])
        else:
            decision = None

        return decision
