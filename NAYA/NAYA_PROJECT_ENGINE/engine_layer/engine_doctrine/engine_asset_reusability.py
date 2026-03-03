def asset_reusability(asset):
    """
    Évalue si un asset peut être réutilisé ou cloné.
    """
    return {
        "reusable": asset.get("generic", False),
        "scalability": asset.get("scalability", "low")
    }
