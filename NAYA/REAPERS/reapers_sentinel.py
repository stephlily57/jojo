from typing import Optional


class ReapersSentinel:
    """
    Sentinel REAPERS.
    Observation continue, détection et qualification.
    N'agit jamais directement.
    """

    def __init__(self, reporter):
        self.reporter = reporter

        self.reporter.emit(
            module="sentinel",
            action="init",
            target="reapers",
            status="ok",
            message="Reapers sentinel initialized"
        )

    def observe(self, target: str, signal: Optional[str] = None) -> None:
        """
        Observe un élément (module, process, service, flux).
        """
        self.reporter.emit(
            module="sentinel",
            action="observe",
            target=target,
            status="ok",
            message=signal or "Observation completed"
        )

    def anomaly(self, target: str, description: str) -> None:
        """
        Signale une anomalie détectée.
        """
        self.reporter.emit(
            module="sentinel",
            action="anomaly_detected",
            target=target,
            status="mitigated",
            severity="warning",
            message=description
        )

    def critical(self, target: str, description: str) -> None:
        """
        Signale une menace critique.
        """
        self.reporter.emit(
            module="sentinel",
            action="critical_threat",
            target=target,
            status="detected",
            severity="critical",
            scope="client_service",
            message=description
        )
