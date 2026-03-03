# NAYA_CORE/mission_fusion_engine.py

class MissionFusionEngine:

    def __init__(self, memory_hierarchy):
        self.memory = memory_hierarchy

    def retrieve_strategic_layer(self):
        return self.memory.memory.read_stream("memory_strategic", count=200)

    def retrieve_doctrine_layer(self):
        return self.memory.memory.read_stream("memory_doctrine", count=200)
