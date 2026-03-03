class StrategicDomainRouter:

    def __init__(self, registry):
        self.registry = registry
        self.executive_threshold = 25000  # seuil stratégique minimum

    def route(self, impact_value, solvable=True):

        executive = self.registry.get("executive_architecture")
        venture = self.registry.get("project_engine")

        if impact_value >= self.executive_threshold and solvable:
            print(">>> ROUTED TO EXECUTIVE ARCHITECTURE")
            return executive.evaluate_case(impact_value, solvable)

        print(">>> ROUTED TO VENTURE ENGINE")
        return venture.run()
