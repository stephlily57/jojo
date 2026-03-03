class NayaService:
    def __init__(self):
        self.name = "Arbitrage décisionnel B2B critique"
        self.target = "Plateforme B2B mondiale (Alibaba)"
        self.sla = "24-48h"
        self.base_price_xpf = 16500000

    def compute_price(self, loss_value: int, factor: float = 1.0) -> int:
        return max(self.base_price_xpf, int(loss_value * factor))

    def deliver(self):
        return {
            "service": self.name,
            "target": self.target,
            "sla": self.sla,
            "pricing_model": "LOSS_BASED"
        }