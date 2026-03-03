class BusinessModelEngine:

    def analyze_opportunity(self, opportunity):
        """
        Structure une opportunité business exploitable.
        """

        structured_model = {
            "problem": opportunity.get("problem"),
            "target_market": opportunity.get("market"),
            "value_proposition": opportunity.get("value"),
            "capitalizable": True,
            "reusable": True
        }

        return structured_model
