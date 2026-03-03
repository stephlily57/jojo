# NayaCore / core_activation.py
# ------------------------------------------------------------
# Gère l’activation consciente de NAYA.
# Ne lance aucune action business.
# ------------------------------------------------------------

from dataclasses import dataclass
from datetime import datetime

from internal_sovereignty_core import INTERNAL_SOVEREIGNTY


@dataclass(frozen=True)
class ActivationState:
    """
    État d’activation de NAYA.
    """
    status: str
    activated_at: str
    identity_checksum: str
    sovereignty_checksum: str

    def summary(self) -> str:
        return (
            f"Status: {self.status}\n"
            f"Activated at: {self.activated_at}\n"
            f"Identity checksum: {self.identity_checksum}\n"
            f"Sovereignty checksum: {self.sovereignty_checksum}"
        )


def _simple_checksum(text: str) -> str:
    """
    Empreinte simple, stable, non cryptographique.
    """
    return str(abs(hash(text)))


def activate_naya(identity_text: str) -> ActivationState:
    """
    Active NAYA à partir de son identité textuelle.
    """
    sovereignty_text = INTERNAL_SOVEREIGNTY.sovereignty_statement()

    return ActivationState(
        status="READY",
        activated_at=datetime.utcnow().isoformat(),
        identity_checksum=_simple_checksum(identity_text),
        sovereignty_checksum=_simple_checksum(sovereignty_text),
    )
