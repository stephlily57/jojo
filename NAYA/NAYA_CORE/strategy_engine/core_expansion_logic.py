# NayaCore / core_expansion_logic.py
# ------------------------------------------------------------
# Ce fichier définit la logique d’expansion stratégique de NAYA.
# Il permet de créer à la fois dans les zones communes
# et dans les zones vierges (hors radar).
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass(frozen=True)
class ExpansionZone:
    """
    Zone stratégique d’expansion.
    """
    zone_type: str
    description: str
    created_at: str
    uniqueness_level: float


@dataclass(frozen=True)
class ExpansionMap:
    """
    Carte des zones d’expansion générées.
    """
    zones: List[ExpansionZone]
    generated_at: str

    def summary(self) -> str:
        types = ", ".join(zone.zone_type for zone in self.zones)
        return (
            f"Expansion zones: {len(self.zones)}\n"
            f"Types: {types}"
        )


class ExpansionLogic:
    """
    Logique d’expansion de NAYA.
    """

    def generate_zones(self) -> ExpansionMap:
        """
        Génère des zones communes et des zones vierges.
        """
        zones: List[ExpansionZone] = []

        common_zone = ExpansionZone(
            zone_type="COMMON_ZONE",
            description="Established market space with known demand",
            created_at=datetime.utcnow().isoformat(),
            uniqueness_level=0.3,
        )

        virgin_zone = ExpansionZone(
            zone_type="VIRGIN_ZONE",
            description="Unexplored or underexploited strategic space",
            created_at=datetime.utcnow().isoformat(),
            uniqueness_level=0.9,
        )

        zones.append(common_zone)
        zones.append(virgin_zone)

        return ExpansionMap(
            zones=zones,
            generated_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
EXPANSION_LOGIC = ExpansionLogic()
