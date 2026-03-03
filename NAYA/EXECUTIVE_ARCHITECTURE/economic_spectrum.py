class EconomicSpectrum:

    def __init__(self):
        self.levels = {
            "LEVEL_1": {"min": 5000, "max": 10000},
            "LEVEL_2": {"min": 25000, "max": 50000},
            "LEVEL_3": {"min": 75000, "max": 150000}
        }

    def determine_level(self, impact_value):

        if self.levels["LEVEL_1"]["min"] <= impact_value <= self.levels["LEVEL_1"]["max"]:
            return "LEVEL_1"

        if self.levels["LEVEL_2"]["min"] <= impact_value <= self.levels["LEVEL_2"]["max"]:
            return "LEVEL_2"

        if self.levels["LEVEL_3"]["min"] <= impact_value <= self.levels["LEVEL_3"]["max"]:
            return "LEVEL_3"

        if impact_value > 150000:
            return "STRATEGIC_CUSTOM"

        return "BELOW_THRESHOLD"
