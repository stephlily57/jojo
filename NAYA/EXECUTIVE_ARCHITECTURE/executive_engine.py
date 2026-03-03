from EXECUTIVE_ARCHITECTURE.economic_spectrum import EconomicSpectrum
from EXECUTIVE_ARCHITECTURE.capital_structure import CapitalStructure
from EXECUTIVE_ARCHITECTURE.strategic_modes import StrategicModes
from EXECUTIVE_ARCHITECTURE.structural_intervention import StructuralIntervention
from EXECUTIVE_ARCHITECTURE.predictive_layer import PredictiveLayer
from EXECUTIVE_ARCHITECTURE.zero_waste import ZeroWasteDoctrine


class ExecutiveEngine:

    def __init__(self):

        self.identity = "NAYA_EXECUTIVE_ARCHITECTURE"

        self.economic = EconomicSpectrum()
        self.capital = CapitalStructure()
        self.modes = StrategicModes()
        self.intervention = StructuralIntervention()
        self.predictive = PredictiveLayer()
        self.zero_waste = ZeroWasteDoctrine()

        self.horizon_years = 30

    def activate(self):
        print("=== EXECUTIVE ARCHITECTURE ACTIVATED ===")
        print("Identity:", self.identity)
        print("Strategic Horizon:", self.horizon_years, "years")

    def evaluate_case(self, impact_value, solvable=True):
        if not solvable:
            return "REJECTED"

        level = self.economic.determine_level(impact_value)
        mode = self.modes.current_mode(self.capital.reserve_ratio())

        return {
            "level": level,
            "mode": mode,
            "impact": impact_value
        }
