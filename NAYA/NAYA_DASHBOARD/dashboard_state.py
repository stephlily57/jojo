"""
NAYA DASHBOARD — STATE

Ce module gère l’état interne du Dashboard.
Il ne contient aucune logique métier.
"""

from typing import Optional
from datetime import datetime


class DashboardState:
    """
    État global du Dashboard.
    """

    def __init__(self) -> None:
        self.started: bool = False
        self.started_at: Optional[str] = None

    def mark_started(self) -> None:
        """
        Marque le dashboard comme démarré.
        """
        self.started = True
        self.started_at = datetime.utcnow().isoformat()

    def is_started(self) -> bool:
        """
        Indique si le dashboard est démarré.
        """
        return self.started

    def snapshot(self) -> dict:
        """
        Retourne un état lisible du dashboard.
        """
        return {
            "started": self.started,
            "started_at": self.started_at,
        }
