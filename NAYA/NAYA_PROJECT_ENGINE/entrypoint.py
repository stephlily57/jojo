from pathlib import Path

from .industrial import create_industrial_controller
from .industrial.engine_version import ENGINE_VERSION


def run_industrial_cycle():
    """
    Bootstraps the industrial engine (intelligent lock version).
    """

    base_path = Path(__file__).parent

    print(f"NAYA_PROJECT_ENGINE – Version: {ENGINE_VERSION}")

    controller = create_industrial_controller(base_path)

    print("Industrial Controller Initialized")
    print("Registered Projects:")
    print(controller.project_states)

    allocation = controller.allocate_projects()
    print("Allocation Order:")
    print(allocation)

    return controller


if __name__ == "__main__":
    run_industrial_cycle()
