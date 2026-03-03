def score_cash_speed(project):
    """
    Évalue la capacité d’un projet à générer du cash rapidement.
    """
    return {
        "time_to_cash": project.get("time_to_cash", "unknown"),
        "cash_priority": project.get("cash_priority", 0),
        "verdict": "FAST" if project.get("cash_priority", 0) >= 7 else "SLOW"
    }
