"""
NAYA DASHBOARD — SYSTEM REPORTS

Générateur de rapports globaux du système Naya.
Lecture uniquement.
"""

from NAYA_DASHBOARD.views.naya_view import NayaView
from NAYA_DASHBOARD.views.orchestration_view import OrchestrationView
from NAYA_DASHBOARD.views.reapers_view import ReapersView
from NAYA_DASHBOARD.views.project_engine_view import ProjectEngineView


class SystemReports:
    """
    Rapport global du système.
    """

    def __init__(
        self,
        naya_view: NayaView,
        orchestration_view: OrchestrationView,
        reapers_view: ReapersView,
        project_engine_view: ProjectEngineView,
    ) -> None:
        self.naya_view = naya_view
        self.orchestration_view = orchestration_view
        self.reapers_view = reapers_view
        self.project_engine_view = project_engine_view

    def generate(self) -> dict:
        """
        Génère un rapport global lisible.
        """
        return {
            "naya": self.naya_view.render(),
            "orchestration": self.orchestration_view.render(),
            "reapers": self.reapers_view.render(),
            "projects": self.project_engine_view.render(),
        }
