class AccessStrategyEngine:

    def determine_strategy(self, channel):

        if channel["has_api"]:
            return "DIRECT_API"

        return "INDIRECT_AUTOMATION"
