class CapitalStructure:

    def __init__(self):
        self.operational_reserve = 0.0
        self.strategic_reserve = 0.0
        self.equity_pool = 0.0

    def update_reserves(self, operational, strategic, equity):
        self.operational_reserve = operational
        self.strategic_reserve = strategic
        self.equity_pool = equity

    def reserve_ratio(self):
        total = self.operational_reserve + self.strategic_reserve
        if total == 0:
            return 0
        return self.operational_reserve / total
