# NayaCore / supplier_relations_core.py
# ------------------------------------------------------------
# Ce fichier définit la gestion des relations fournisseurs de NAYA.
# Il structure la sélection, l’engagement et la continuité,
# sans jamais créer de dépendance.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class SupplierProfile:
    """
    Profil d’un fournisseur potentiel ou actif.
    """
    supplier_name: str
    supplier_type: str
    quality_level: float
    reliability_level: float
    created_at: str
    context: Dict[str, str]


@dataclass(frozen=True)
class SupplierRelation:
    """
    Relation structurée avec un fournisseur.
    """
    supplier: SupplierProfile
    engagement_type: str
    continuity_level: str
    exit_capability: bool
    established_at: str


@dataclass(frozen=True)
class SupplierRegistry:
    """
    Registre des relations fournisseurs.
    """
    relations: List[SupplierRelation]
    registered_at: str

    def summary(self) -> str:
        names = ", ".join(r.supplier.supplier_name for r in self.relations)
        return (
            f"Suppliers registered: {len(self.relations)}\n"
            f"Suppliers: {names}"
        )


class SupplierRelationsCore:
    """
    Cœur des relations fournisseurs de NAYA.
    Il sélectionne et maintient sans dépendre.
    """

    def manage(self, inputs: List[Dict[str, str]]) -> SupplierRegistry:
        """
        Transforme des informations fournisseurs en relations structurées.
        Aucun fournisseur n’est ignoré.
        """
        relations: List[SupplierRelation] = []

        for entry in inputs:
            supplier = SupplierProfile(
                supplier_name=entry.get("name", "unknown"),
                supplier_type=entry.get("type", "unspecified"),
                quality_level=float(entry.get("quality", 0.5)),
                reliability_level=float(entry.get("reliability", 0.5)),
                created_at=datetime.utcnow().isoformat(),
                context=entry,
            )

            relation = SupplierRelation(
                supplier=supplier,
                engagement_type=entry.get("engagement", "flexible"),
                continuity_level=entry.get("continuity", "controlled"),
                exit_capability=True,
                established_at=datetime.utcnow().isoformat(),
            )

            relations.append(relation)

        return SupplierRegistry(
            relations=relations,
            registered_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
SUPPLIER_RELATIONS_CORE = SupplierRelationsCore()
