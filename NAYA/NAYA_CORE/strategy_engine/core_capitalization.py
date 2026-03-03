# NayaCore / core_capitalization.py
# ------------------------------------------------------------
# Ce fichier empêche toute logique one-shot.
# Toute exécution devient un actif capitalisable.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class CapitalAsset:
    """
    Actif capitalisable issu d’une action ou d’une exécution.
    """
    asset_id: str
    origin: str
    description: str
    created_at: str
    metadata: Dict[str, str]
    reusable: bool = True
    clonable: bool = True
    redirectable: bool = True


@dataclass(frozen=True)
class CapitalRegistry:
    """
    Registre d’actifs capitalisés.
    """
    assets: List[CapitalAsset]
    registered_at: str

    def summary(self) -> str:
        return (
            f"Capitalized assets: {len(self.assets)}\n"
            f"Registered at: {self.registered_at}"
        )


class CapitalizationEngine:
    """
    Moteur de capitalisation.
    Il transforme toute sortie en actif exploitable.
    """

    def capitalize(self, execution_packages: List[Dict[str, str]]) -> CapitalRegistry:
        """
        Capitalise des résultats d’exécution en actifs durables.
        """
        assets: List[CapitalAsset] = []

        for idx, package in enumerate(execution_packages):
            asset = CapitalAsset(
                asset_id=f"ASSET-{idx}-{int(datetime.utcnow().timestamp())}",
                origin=package.get("origin", "unknown"),
                description=package.get("description", ""),
                created_at=datetime.utcnow().isoformat(),
                metadata=package,
            )
            assets.append(asset)

        return CapitalRegistry(
            assets=assets,
            registered_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
CAPITALIZATION_ENGINE = CapitalizationEngine()
