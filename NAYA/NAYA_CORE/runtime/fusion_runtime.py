# NAYA_CORE/fusion_runtime.py

from pattern_detector import PatternDetector
from mission_fusion_engine import MissionFusionEngine
from doctrine_adjuster import DoctrineAdjuster

class FusionRuntime:

    def __init__(self, memory_hierarchy, doctrine_engine):
        self.fusion_engine = MissionFusionEngine(memory_hierarchy)
        self.pattern_detector = PatternDetector()
        self.doctrine_adjuster = DoctrineAdjuster()
        self.doctrine_engine = doctrine_engine

    def run_fusion_cycle(self):

        strategic_memory = self.fusion_engine.retrieve_strategic_layer()

        patterns = self.pattern_detector.detect_patterns(strategic_memory)

        self.doctrine_adjuster.adjust(self.doctrine_engine, patterns)
