class StructuralIntervention:

    def __init__(self):
        self.imbalance_types = [
            "DECISION_MISALIGNMENT",
            "EXPANSION_MISARCHITECTURE",
            "MULTI_SITE_FRICTION",
            "GROWTH_SATURATION"
        ]

    def detect(self, imbalance_type):

        if imbalance_type in self.imbalance_types:
            return True

        return False
