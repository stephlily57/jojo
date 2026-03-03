# NayaCore / ownership_and_signature_core.py
# ------------------------------------------------------------
# Ce fichier définit la relation de propriété, de confidentialité
# et de signature humaine au sein de NAYA.
# Il garantit la liberté de création tout en respectant
# les obligations légales ou contractuelles.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import Dict
from datetime import datetime


@dataclass(frozen=True)
class OwnershipDeclaration:
    """
    Déclaration de propriété et de confidentialité.
    """
    owner_role: str
    confidentiality_level: str
    creation_freedom: bool
    declared_at: str


@dataclass(frozen=True)
class SignatureRequest:
    """
    Demande de signature humaine préparée par NAYA.
    """
    document_type: str
    purpose: str
    prepared_at: str
    requires_signature: bool
    context: Dict[str, str]


class OwnershipAndSignatureCore:
    """
    Cœur de gestion de la propriété et de la signature.
    Il ne bloque jamais la création.
    """

    def declare_ownership(self) -> OwnershipDeclaration:
        """
        Déclare la propriété humaine de NAYA sans bridage.
        """
        return OwnershipDeclaration(
            owner_role="Human Owner",
            confidentiality_level="Strict",
            creation_freedom=True,
            declared_at=datetime.utcnow().isoformat(),
        )

    def prepare_signature_if_needed(
        self,
        document_type: str,
        purpose: str,
        requires_signature: bool,
        context: Dict[str, str],
    ) -> SignatureRequest:
        """
        Prépare une demande de signature uniquement si nécessaire.
        """
        return SignatureRequest(
            document_type=document_type,
            purpose=purpose,
            prepared_at=datetime.utcnow().isoformat(),
            requires_signature=requires_signature,
            context=context,
        )


# Instance prête à l’usage
OWNERSHIP_AND_SIGNATURE_CORE = OwnershipAndSignatureCore()
