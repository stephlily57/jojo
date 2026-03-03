from NAYA_CORE.state_store import StateStore
from NAYA_CORE.strategic_context import StrategicContext
from NAYA_CORE.sovereignty_layer import SovereigntyLayer
from NAYA_CORE.restructuring_layer import RestructuringLayer
from NAYA_CORE.density_layer import DensityLayer
from NAYA_CORE.strategic_memory import StrategicMemory
from NAYA_CORE.adaptive_feedback import AdaptiveFeedback
from NAYA_CORE.degradation_control import DegradationControl

class NayaCore:

    def __init__(self):

        self.state_store = StateStore()
        self.context_layer = StrategicContext(self.state_store)
        self.sovereignty = SovereigntyLayer()
        self.restructure = RestructuringLayer()
        self.density = DensityLayer()
        self.memory = StrategicMemory(self.state_store)
        self.adaptive = AdaptiveFeedback()
        self.degradation = DegradationControl()

    def process(self, opportunity):

        context = self.context_layer.snapshot()

        level = self.degradation.evaluate(context)
        if level > 0:
            return {"status": "DEGRADED", "level": level}

        if not self.sovereignty.validate(opportunity, context):
            alt = self.restructure.generate_alternative(opportunity)
            return {"status": "REJECTED", "alternative": alt}

        density_score = self.density.compute(opportunity)

        if density_score > 0.7:
            self.memory.store(opportunity)
            self.adaptive.learn(opportunity, {"impact": opportunity.get("value", 0)})
            return {"status": "EXECUTE"}

        return {"status": "INCUBATE"}
