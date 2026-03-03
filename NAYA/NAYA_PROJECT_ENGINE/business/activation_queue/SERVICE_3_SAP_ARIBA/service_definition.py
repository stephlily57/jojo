class NayaService:
    def __init__(self):
        self.name = "Audit intelligent invisible – procurement luxe"
        self.target = "Plateforme B2B luxe / parfum (SAP Ariba)"
        self.sla = "24-72h"
        self.base_price_xpf = 5500000

    def compute_price(self, loss_value: int, factor: float = 1.0) -> int:
        return max(self.base_price_xpf, int(loss_value * factor))

    def deliver(self):
        return {
            "service": self.name,
            "target": self.target,
            "sla": self.sla,
            "pricing_model": "LOSS_BASED"
        }