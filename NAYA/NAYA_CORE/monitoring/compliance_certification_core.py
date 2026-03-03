# NayaCore / compliance_certification_core.py
# ------------------------------------------------------------
# Ce fichier gère l’identification et la préparation
# des certifications nécessaires selon les projets,
# les déclarations et les zones géographiques.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class CertificationRequirement:
    """
    Certification requise pour un projet donné.
    """
    project_type: str
    market_zone: str
    certification_name: str
    mandatory: bool
    identified_at: str
    context: Dict[str, str]


@dataclass(frozen=True)
class CertificationPlan:
    """
    Plan de certifications à demander.
    """
    requirements: List[CertificationRequirement]
    planned_at: str

    def summary(self) -> str:
        names = ", ".join(r.certification_name for r in self.requirements)
        return (
            f"Certifications identified: {len(self.requirements)}\n"
            f"Certifications: {names}"
        )


class ComplianceCertificationCore:
    """
    Cœur de conformité et certifications de NAYA.
    Il identifie et prépare sans jamais bloquer.
    """

    def identify(self, inputs: List[Dict[str, str]]) -> CertificationPlan:
        """
        Identifie les certifications nécessaires à partir
        des informations projet et marché.
        """
        requirements: List[CertificationRequirement] = []

        for entry in inputs:
            requirement = CertificationRequirement(
                project_type=entry.get("project_type", "generic"),
                market_zone=entry.get("market_zone", "global"),
                certification_name=entry.get(
                    "certification",
                    "unspecified_certification"
                ),
                mandatory=bool(entry.get("mandatory", True)),
                identified_at=datetime.utcnow().isoformat(),
                context=entry,
            )
            requirements.append(requirement)

        return CertificationPlan(
            requirements=requirements,
            planned_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
COMPLIANCE_CERTIFICATION_CORE = ComplianceCertificationCore()
