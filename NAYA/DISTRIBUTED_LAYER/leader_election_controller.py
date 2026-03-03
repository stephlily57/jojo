class LeaderElectionController:

    def __init__(self, registry):
        self.registry = registry

    def evaluate_leader(self):
        regions = self.registry.get_regions()

        if not regions:
            return None

        sorted_regions = sorted(
            regions.items(),
            key=lambda x: x[1]["performance_score"],
            reverse=True
        )

        leader = sorted_regions[0][0]
        self.registry.set_leader(leader)
        return leader
