from EXECUTIVE_ARCHITECTURE.executive_engine import ExecutiveEngine
from NAYA_PROJECT_ENGINE.venture_engine import VentureEngine


class DomainInitializer:

    def initialize(self):
        domains = {}

        # Core system domains (silent registration)
        domains["business_engines"] = "BUSINESS_ENGINES_REGISTERED"
        domains["channel_intelligence"] = "CHANNEL_INTELLIGENCE_REGISTERED"
        domains["data_governance"] = "DATA_GOVERNANCE_REGISTERED"
        domains["distributed_layer"] = "DISTRIBUTED_LAYER_REGISTERED"
        domains["global_sync"] = "GLOBAL_SYNC_REGISTERED"
        domains["protocols"] = "PROTOCOLS_REGISTERED"
        domains["constitution"] = "CONSTITUTION_REGISTERED"
        domains["persistence"] = "PERSISTENCE_REGISTERED"

        # Executive Architecture
        executive = ExecutiveEngine()
        executive.activate()
        domains["executive_architecture"] = executive

        # Venture Engine (silent)
        venture = VentureEngine()
        venture.activate()
        domains["project_engine"] = venture

        return domains
