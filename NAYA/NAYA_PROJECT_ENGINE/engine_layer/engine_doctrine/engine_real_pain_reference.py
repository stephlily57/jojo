def validate_real_pain(pain):
    """
    Vérifie si la douleur est réelle, coûteuse, évitée par les grandes structures.
    """
    score = 0
    if pain.get("is_costly"):
        score += 1
    if pain.get("is_hidden"):
        score += 1
    if pain.get("decision_maker_involved"):
        score += 1

    return {
        "score": score,
        "is_real_pain": score >= 2
    }
