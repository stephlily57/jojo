def value_floor(pricing):
    """
    Empêche toute destruction de valeur.
    """
    return {
        "acceptable": pricing.get("price", 0) >= pricing.get("minimum_floor", 0)
    }
