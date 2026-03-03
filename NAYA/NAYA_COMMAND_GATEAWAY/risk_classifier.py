# risk_classifier.py

RISK_LEVELS = {
    "supervision": 1,
    "strategy": 5,
    "intervention": 7,
    "emergency": 10,
}

def classify(category: str) -> int:
    return RISK_LEVELS.get(category, 0)
