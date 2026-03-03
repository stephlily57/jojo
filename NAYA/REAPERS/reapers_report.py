from datetime import datetime
from typing import Dict, Any, List


class ReapersReport:
    """
    Collecteur d’événements REAPERS.
    Sert de base au dashboard et à la reddition de comptes.
    """

    def __init__(self):
        self._events: List[Dict[str, Any]] = []
        self._started_at = datetime.utcnow().isoformat()

        self.emit(
            module="report",
            action="init",
            target="reapers",
            status="ok",
            message="Reapers reporting initialized"
        )

    def emit(
        self,
        module: str,
        action: str,
        target: str,
        status: str,
        severity: str = "info",
        scope: str = "internal",
        message: str = ""
    ) -> None:
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "module": module,
            "action": action,
            "target": target,
            "status": status,
            "severity": severity,
            "scope": scope,
            "message": message,
        }
        self._events.append(event)

    def snapshot(self) -> List[Dict[str, Any]]:
        """
        Retourne tous les événements collectés.
        """
        return list(self._events)

    def latest(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Retourne les derniers événements (par défaut 10).
        """
        return self._events[-limit:]

    def status(self) -> Dict[str, Any]:
        """
        État synthétique de REAPERS pour le dashboard.
        """
        return {
            "started_at": self._started_at,
            "events_count": len(self._events),
            "last_event": self._events[-1] if self._events else None,
        }
