
ALLOWED_CATEGORIES = {"supervision", "intervention", "strategy", "emergency"}

def validate_intent(intent):
    if intent.category not in ALLOWED_CATEGORIES:
        return False, "Invalid category"
    return True, "OK"
