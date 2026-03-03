# NAYA_CORE/decision/cluster_scale_controller.py

class ClusterScaleController:

    def compute_scale(self, density_score: float) -> int:
        """
        Détermine le nombre de workers nécessaires.
        """

        if density_score > 200000:
            return 10

        if density_score > 100000:
            return 5

        if density_score > 20000:
            return 3

        return 1


CLUSTER_SCALE_CONTROLLER = ClusterScaleController()
