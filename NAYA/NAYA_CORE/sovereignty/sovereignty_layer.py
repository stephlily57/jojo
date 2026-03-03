class SovereigntyLayer:

    def validate(self, opportunity, context):

        if opportunity.get("equity_loss", 0) > 0:
            return False

        if context["dependency"] > 0.7:
            return False

        return True
