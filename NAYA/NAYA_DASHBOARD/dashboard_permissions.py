"""
NAYA DASHBOARD — PERMISSIONS

Ce module définit les règles de souveraineté fondatrice.
Aucune règle ici ne doit permettre de bloquer Naya ou Reapers.
"""


class DashboardPermissions:
    """
    Règles de permissions du Dashboard.
    """

    def __init__(self) -> None:
        # Principes fondamentaux (non modifiables dynamiquement)
        self.allow_observation: bool = True
        self.allow_exchange: bool = True
        self.allow_project_addition: bool = True

        # Interdictions absolues
        self.allow_force_stop: bool = False
        self.allow_reapers_disable: bool = False
        self.allow_core_override: bool = False

    def can_observe(self) -> bool:
        """
        Le Dashboard peut-il observer l’état du système ?
        """
        return self.allow_observation

    def can_exchange(self) -> bool:
        """
        Le Dashboard peut-il échanger avec Naya (texte / voix) ?
        """
        return self.allow_exchange

    def can_add_project(self) -> bool:
        """
        Le Dashboard peut-il proposer l’ajout d’un projet ?
        """
        return self.allow_project_addition

    def can_force_stop(self) -> bool:
        """
        Le Dashboard peut-il forcer l’arrêt d’un processus ?
        (Toujours faux par principe)
        """
        return self.allow_force_stop

    def can_disable_reapers(self) -> bool:
        """
        Le Dashboard peut-il désactiver Reapers ?
        (Toujours faux par principe)
        """
        return self.allow_reapers_disable

    def can_override_core(self) -> bool:
        """
        Le Dashboard peut-il surcharger Naya Core ?
        (Toujours faux par principe)
        """
        return self.allow_core_override

    def snapshot(self) -> dict:
        """
        Retourne une vue lisible des permissions.
        """
        return {
            "observe": self.allow_observation,
            "exchange": self.allow_exchange,
            "add_project": self.allow_project_addition,
            "force_stop": self.allow_force_stop,
            "disable_reapers": self.allow_reapers_disable,
            "override_core": self.allow_core_override,
        }
