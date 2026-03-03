def hybrid_decision(data):
    """
    Arbitrage logique + intuition stratégique.
    """
    return {
        "logic": data.get("logic_score", 0),
        "intuition": data.get("intuition_score", 0),
        "decision": "GO" if data.get("logic_score", 0) + data.get("intuition_score", 0) >= 10 else "WAIT"
    }
