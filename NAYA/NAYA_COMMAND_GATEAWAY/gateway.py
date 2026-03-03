from .policy_guard import validate_intent
from .actor_registry import validate_actor
from .permission_matrix import is_authorized
from .risk_classifier import classify
from .signature_verifier import verify_signature
from .replay_guard import is_replay, mark
from .gateway_dispatcher import dispatch_to_core
from .reapers_bridge import reapers_threat_check
from .journal import IntentJournal


class CommandGateway:

    def __init__(self, journal: IntentJournal):
        self.journal = journal

    def handle(self, intent, signature: str):

        intent_dict = intent.__dict__

        # 1️⃣ Signature
        if not verify_signature(intent_dict, signature):
            return {"status": "rejected", "reason": "invalid_signature"}

        # 2️⃣ Replay
        if is_replay(intent.intent_id):
            return {"status": "rejected", "reason": "replay_detected"}

        # 3️⃣ Actor validation
        if not validate_actor(intent.actor):
            return {"status": "rejected", "reason": "invalid_actor"}

        role = intent.actor.get("role")

        # 4️⃣ Category validation
        valid, reason = validate_intent(intent)
        if not valid:
            return {"status": "rejected", "reason": reason}

        # 5️⃣ Permission
        if not is_authorized(role, intent.category):
            return {"status": "rejected", "reason": "not_authorized"}

        # 6️⃣ Risk classification
        risk = classify(intent.category)

        # 7️⃣ REAPERS check
        if not reapers_threat_check(risk):
            return {"status": "blocked", "reason": "reapers_blocked"}

        # 8️⃣ Journal
        self.journal.log(intent_dict)

        # 9️⃣ Mark processed
        mark(intent.intent_id)

        # 🔟 Dispatch
        dispatch_to_core(intent)

        return {"status": "accepted", "risk": risk}
