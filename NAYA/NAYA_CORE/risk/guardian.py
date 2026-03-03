class Guardian:

    def evaluate(self, opportunity):
        return opportunity.get("risk", 0.3)

    def allow(self, opportunity, risk_level):
        return risk_level < 0.85

    def restructure(self, opportunity):
        return {
            "status": "restructured",
            "alternative": "risk mitigated proposal"
        }
