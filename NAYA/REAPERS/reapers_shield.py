from typing import Optional


class ReapersShield:
    """
    Bouclier REAPERS.
    Isole, confine et protège sans bloquer Naya.
    Actions réversibles et silencieuses.
    """

    def __init__(self, reporter):
        self.reporter = reporter

        self.reporter.emit(
            module="shield",
            action="init",
            target="reapers",
            status="ok",
            message="Reapers shield initialized"
        )

    def isolate(self, target: str, reason: Optional[str] = None) -> None:
        """
        Isole un élément suspect sans interrompre Naya.
        """
        self.reporter.emit(
            module="shield",
            action="isolate",
            target=target,
            status="mitigated",
            severity="warning",
            message=reason or "Target isolated"
        )

    def confine(self, target: str, scope: str = "internal") -> None:
        """
        Confinement discret d’un élément.
        """
        self.reporter.emit(
            module="shield",
            action="confine",
            target=target,
            status="mitigated",
            scope=scope,
            severity="warning",
            message="Target confined"
        )

    def release(self, target: str) -> None:
        """
        Libère un élément précédemment isolé.
        """
        self.reporter.emit(
            module="shield",
            action="release",
            target=target,
            status="ok",
            message="Target released"
        )
