# NAYA_CORE/doctrine/core_constitution.py

import hashlib
import json

class CoreConstitution:
    """
    Constitution stratégique de NAYA.
    Définit les invariants non négociables.
    """

    IDENTITY = "NAYA_SOVEREIGN_ECONOMIC_SYSTEM"

    NON_NEGOTIABLES = {
        "sovereignty_first": True,
        "economic_density_required": True,
        "zero_waste_principle": True,
        "capital_reserve_mandatory": True,
        "separation_internal_layers": True
    }

    STRATEGIC_INVARIANTS = {
        "min_economic_impact": 50000,
        "reserve_ratio_min": 0.20,
        "level_1_range": (5000, 10000),
        "level_2_range": (25000, 50000),
        "level_3_range": (75000, 150000)
    }

    @classmethod
    def integrity_hash(cls) -> str:
        payload = {
            "identity": cls.IDENTITY,
            "non_negotiables": cls.NON_NEGOTIABLES,
            "invariants": cls.STRATEGIC_INVARIANTS
        }
        encoded = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()
