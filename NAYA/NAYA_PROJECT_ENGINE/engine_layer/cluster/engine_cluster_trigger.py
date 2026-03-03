# engine_cluster_trigger.py


class ClusterTrigger:

    def evaluate(self, density_score: float) -> bool:
        return density_score > 8000  # seuil premium élevé


CLUSTER_TRIGGER = ClusterTrigger()
