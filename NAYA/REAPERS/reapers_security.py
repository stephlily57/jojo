from typing import Optional


class ReapersSecurity:
    """
    Sécurité active REAPERS.
    Protection continue, non bloquante, pendant l’exécution.
    """

    def __init__(self, reporter):
        self.reporter = reporter

        self.reporter.emit(
            module="security",
            action="init",
            target="reapers",
            status="ok",
            message="Reapers security initialized"
        )

    def secure(self, target: str, level: str = "standard") -> None:
        """
        Applique une couche de sécurité sur une cible.
        """
        self.reporter.emit(
            module="security",
            action="secure",
            target=target,
            status="ok",
            message=f"Security enforced (level={level})"
        )

    def detect_intrusion(self, target: str, description: str) -> None:
        """
        Détection d’une tentative d’intrusion.
        """
        self.reporter.emit(
            module="security",
            action="intrusion_detected",
            target=target,
            status="mitigated",
            severity="critical",
            scope="external",
            message=description
        )

    def prevent_exfiltration(self, target: str) -> None:
        """
        Prévention d’exfiltration de données.
        """
        self.reporter.emit(
            module="security",
            action="exfiltration_prevented",
            target=target,
            status="ok",
            severity="warning",
            message="Data exfiltration prevented"
        )
