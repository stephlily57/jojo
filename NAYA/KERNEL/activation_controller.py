from BUSINESS_ENGINES.strategic_pricing_engine.pricing_engine import StrategicPricingEngine
from BUSINESS_ENGINES.supplier_intelligence_engine.supplier_engine import SupplierIntelligenceEngine
from BUSINESS_ENGINES.business_model_engine.model_builder import BusinessModelEngine
from BUSINESS_ENGINES.discretion_protocol.discretion_controller import DiscretionProtocol


class ActivationController:

    def __init__(self) -> None:
        # Business Engines
        self.pricing_engine = StrategicPricingEngine()
        self.supplier_engine = SupplierIntelligenceEngine()
        self.business_model_engine = BusinessModelEngine()
        self.discretion_protocol = DiscretionProtocol()

    def activate(self) -> dict:
        print("=== NAYA EXECUTIVE BOOTSTRAP START ===")

        # Leader Election (mock stable)
        leader = "REGION_B"

        # Business Engines Initialization
        price = self.pricing_engine.calculate_price(
            impact_value=50000,
            client_capacity=20000
        )

        supplier_score = self.supplier_engine.evaluate_supplier(
            quality_score=90,
            cost=40,
            reliability_score=85
        )

        kpi_score = (price or 0) * 0.405

        print(f"Leader: {leader}")
        print(f"Price: {price}")
        print(f"Supplier Score: {supplier_score}")
        print(f"KPI Score: {kpi_score}")
        print("=== NAYA SYSTEM READY ===")

        return {
            "leader": leader,
            "price": price,
            "supplier_score": supplier_score,
            "kpi_score": kpi_score
        }
