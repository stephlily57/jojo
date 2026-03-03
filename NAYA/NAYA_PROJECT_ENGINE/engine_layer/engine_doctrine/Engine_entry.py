"""
NAYA — PROJECT ENGINE ENTRY
==========================

Point d’entrée UNIQUE du Project Engine.

Rôle :
- Charger et agréger l’intelligence déclarative
- Ne déclencher AUCUNE action
- Ne décider de RIEN
- Exposer un état cognitif lisible par NAYA

Sources agrégées :
- engine_pain_silence
- engine_reality
"""

from datetime import datetime

# ------------------------------------------------------------
# SAFE IMPORTS — PAIN & SILENCE
# ------------------------------------------------------------

def _safe_import(fn):
    try:
        return fn()
    except Exception:
        return None


# engine_pain_silence
try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.unspoken_needs_map import get_unspoken_needs_signals
except Exception:
    get_unspoken_needs_signals = lambda: None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.institutional_silence_zones import identify_silence_zones
except Exception:
    identify_silence_zones = lambda: None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.latent_pain_registry import register_latent_pain
except Exception:
    register_latent_pain = None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.hidden_cost_extractors import extract_hidden_costs
except Exception:
    extract_hidden_costs = lambda: None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.pain_intensity_scoring import score_pain
except Exception:
    score_pain = None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.cost_pressure_index import cost_pressure_index
except Exception:
    cost_pressure_index = None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.discretion_required_markets import discretion_profile
except Exception:
    discretion_profile = lambda: None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.solution_acceptability_filter import is_solution_acceptable
except Exception:
    is_solution_acceptable = None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.perception_scope import perception_scope
except Exception:
    perception_scope = lambda: None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.impact_simulator import simulate_impact
except Exception:
    simulate_impact = None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.action_authority import authorize_action
except Exception:
    authorize_action = None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.power_asymmetry_map import map_power_asymmetry
except Exception:
    map_power_asymmetry = lambda: None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.internal_workarounds_detector import detect_internal_workarounds
except Exception:
    detect_internal_workarounds = lambda: None

try:
    from NAYA_PROJECT_ENGINE.engine_pain_silence.shame_barrier_index import compute_shame_barrier
except Exception:
    compute_shame_barrier = None


# ------------------------------------------------------------
# SAFE IMPORTS — ENGINE REALITY
# ------------------------------------------------------------

try:
    from NAYA_PROJECT_ENGINE.engine_reality.ethical_floor import ethical_floor
except Exception:
    ethical_floor = lambda: None

try:
    from NAYA_PROJECT_ENGINE.engine_reality.market_risk_tiers import market_risk_tiers
except Exception:
    market_risk_tiers = lambda: None


# ------------------------------------------------------------
# ENGINE ENTRY
# ------------------------------------------------------------

def engine_entry() -> dict:
    """
    Agrège l’intelligence déclarative du Project Engine.
    Aucune logique d’action.
    """

    state = {
        "engine": "NAYA_PROJECT_ENGINE",
        "mode": "DECLARATIVE",
        "timestamp": datetime.utcnow().isoformat(),
        "vision": {
            "unspoken_needs": _safe_import(get_unspoken_needs_signals),
            "institutional_silence": _safe_import(identify_silence_zones),
            "power_asymmetry": _safe_import(map_power_asymmetry),
            "internal_workarounds": _safe_import(detect_internal_workarounds),
            "perception_scope": _safe_import(perception_scope),
            "shame_barrier": "AVAILABLE" if compute_shame_barrier else "UNAVAILABLE",
        },
        "calculation": {
            "hidden_costs": _safe_import(extract_hidden_costs),
            "pain_scoring": "AVAILABLE" if score_pain else "UNAVAILABLE",
            "cost_pressure": "AVAILABLE" if cost_pressure_index else "UNAVAILABLE",
            "impact_simulation": "AVAILABLE" if simulate_impact else "UNAVAILABLE",
        },
        "action_authority": {
            "acceptability_filter": "AVAILABLE" if is_solution_acceptable else "UNAVAILABLE",
            "authorization": "AVAILABLE" if authorize_action else "UNAVAILABLE",
            "discretion_profile": _safe_import(discretion_profile),
        },
        "reality_context": {
            "ethical_floor": _safe_import(ethical_floor),
            "market_risk_tiers": _safe_import(market_risk_tiers),
        },
        "guarantees": {
            "no_execution": True,
            "no_decision": True,
            "vision_free": True,
            "calculation_free": True,
            "action_sovereign": True
        }
    }

    return state
