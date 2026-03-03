def premium_positioning(pain):
    """
    Détermine si la douleur supporte un pricing premium.
    """
    return {
        "premium_viable": pain.get("urgency", 0) >= 7,
        "recommended_positioning": "PREMIUM" if pain.get("urgency", 0) >= 7 else "STANDARD"
    }
