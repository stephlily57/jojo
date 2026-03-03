# actor_registry.py

ALLOWED_ACTORS = {
    "tori": {"role": "sovereign", "level": 10},
    "dashboard": {"role": "observer", "level": 3},
}

def validate_actor(actor: dict):
    actor_id = actor.get("id")
    return actor_id in ALLOWED_ACTORS
