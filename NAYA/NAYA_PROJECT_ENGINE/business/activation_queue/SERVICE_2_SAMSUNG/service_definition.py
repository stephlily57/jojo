class NayaService:
    def __init__(self):
        self.name = "Arbitrage et prévention de risque stratégique"
        self.target = "Groupe industriel / tech (Samsung)"
        self.sla = "24-72h"
        self.base_price_xpf = 11000000

    def compute_price(self, loss_value: int, factor: float = 1.0) -> int:
        return max(self.base_price_xpf, int(loss_value * factor))

    def deliver(self):
        return {
            "service": self.name,
            "target": self.target,
            "sla": self.sla,
            "pricing_model": "LOSS_BASED"
        }