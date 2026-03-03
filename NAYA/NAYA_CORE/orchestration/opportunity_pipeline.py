class OpportunityPipeline:

    def __init__(self, decision_engine):
        self.decision_engine = decision_engine

    def analyze(self, opportunity):

        opportunity["analyzed"] = True
        opportunity["refined_value"] = opportunity.get("value", 0) * 1.1

        return opportunity
