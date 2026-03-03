class FailoverController:

    def __init__(self, registry):
        self.registry = registry

    def trigger_failover(self):
        regions = self.registry.get_regions()
        if not regions:
            return None

        # Remove current leader from consideration
        current_leader = self.registry.get_leader()
        candidates = {
            k: v for k, v in regions.items()
            if k != current_leader
        }

        if not candidates:
            return None

        sorted_candidates = sorted(
            candidates.items(),
            key=lambda x: x[1]["performance_score"],
            reverse=True
        )

        new_leader = sorted_candidates[0][0]
        self.registry.set_leader(new_leader)
        return new_leader
