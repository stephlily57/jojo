# permission_matrix.py

PERMISSIONS = {
    "sovereign": {"supervision", "intervention", "strategy", "emergency"},
    "observer": {"supervision"},
}

def is_authorized(role: str, category: str):
    return category in PERMISSIONS.get(role, set())
