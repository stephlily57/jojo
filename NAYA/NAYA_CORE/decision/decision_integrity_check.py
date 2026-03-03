class DecisionIntegrityCheck:

    def validate(self, decision_result: dict):

        if "density" not in decision_result:
            raise Exception("Decision missing density.")

        if decision_result.get("cluster_scale") not in [True, False]:
            decision_result["cluster_scale"] = False

        return decision_result

DECISION_INTEGRITY_CHECK = DecisionIntegrityCheck()
