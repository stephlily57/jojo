# engine_parallel_controller.py


class ParallelController:

    def mode(self, density_score: float) -> str:
        if density_score > 15000:
            return "CLUSTER_PARALLEL"
        if density_score > 5000:
            return "HYBRID"
        return "FOCUSED"


PARALLEL_CONTROLLER = ParallelController()
