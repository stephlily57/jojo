from pathlib import Path
from .industrial import create_industrial_controller


class VentureEngine:

    def __init__(self):
        base_path = Path(__file__).parent
        self.controller = create_industrial_controller(base_path)
        self.initialized = True

    def activate(self):
        print("=== VENTURE ENGINE INITIALIZED (SILENT MODE) ===")

    def run(self):
        return self.controller.allocate_projects()
