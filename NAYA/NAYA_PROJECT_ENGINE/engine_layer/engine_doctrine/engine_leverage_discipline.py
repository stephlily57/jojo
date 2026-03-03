def leverage_discipline(action):
    """
    Refuse toute action sans effet levier clair.
    """
    return {
        "accepted": action.get("leverage", 0) >= 5
    }
