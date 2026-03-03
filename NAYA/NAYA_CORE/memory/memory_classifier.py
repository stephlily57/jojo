# NAYA_CORE/memory_classifier.py

class MemoryClassifier:

    def classify(self, decision_context):

        impact = decision_context.get("impact_score", 0)
        risk = decision_context.get("risk_score", 0)
        long_term = decision_context.get("long_term", False)

        if long_term or impact > 8:
            return "DOCTRINE"

        if impact > 4 or risk > 5:
            return "STRATEGIC"

        return "OPERATIONAL"
