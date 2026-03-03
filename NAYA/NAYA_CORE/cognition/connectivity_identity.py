# NayaCore / connectivity_identity.py
# ------------------------------------------------------------
# Ce fichier définit l’identité relationnelle de NAYA.
# Il structure les connexions business sans jamais créer
# de dépendance ou de contrainte.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class BusinessConnection:
    """
    Connexion business identifiée par NAYA.
    """
    connection_type: str
    entity_name: str
    relationship_nature: str
    created_at: str
    context: Dict[str, str]


@dataclass(frozen=True)
class ConnectivityMap:
    """
    Carte des connexions business de NAYA.
    """
    connections: List[BusinessConnection]
    mapped_at: str

    def summary(self) -> str:
        types = ", ".join(c.connection_type for c in self.connections)
        return (
            f"Connections mapped: {len(self.connections)}\n"
            f"Connection types: {types}"
        )


class ConnectivityIdentity:
    """
    Identité relationnelle de NAYA.
    Elle relie sans jamais asservir.
    """

    def map_connections(self, inputs: List[Dict[str, str]]) -> ConnectivityMap:
        """
        Transforme des informations relationnelles en connexions structurées.
        Aucun lien n’est ignoré.
        """
        connections: List[BusinessConnection] = []

        for entry in inputs:
            connection = BusinessConnection(
                connection_type=entry.get("type", "unspecified"),
                entity_name=entry.get("entity", ""),
                relationship_nature=entry.get("nature", "neutral"),
                created_at=datetime.utcnow().isoformat(),
                context=entry,
            )
            connections.append(connection)

        return ConnectivityMap(
            connections=connections,
            mapped_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
CONNECTIVITY_IDENTITY = ConnectivityIdentity()
