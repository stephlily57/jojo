from pathlib import Path

from .project_registry import ProjectRegistry
from .industrial_state_machine import IndustrialStateMachine, ProjectState
from .resource_allocator import ResourceAllocator
from .performance_monitor import PerformanceMonitor


class IndustrialController:
    """
    Central Industrial Brain
    ------------------------
    - Registers projects
    - Controls state transitions
    - Allocates execution order
    - Tracks performance
    - Locked after initialization (CORE level)
    """

    def __init__(self, base_path: Path):
        self.base_path = base_path

        # Core industrial components
        self.registry = ProjectRegistry(base_path)
        self.state_machine = IndustrialStateMachine()
        self.allocator = ResourceAllocator()
        self.monitor = PerformanceMonitor()

        # Runtime state
        self.project_states = {}
        self._locked = False

    # -------------------------------------------------
    # INITIALIZATION
    # -------------------------------------------------

    def initialize_projects(self):
        all_projects = self.registry.get_all_projects()

        # Activation queue first
        for project in all_projects["activation_queue"]:
            self.project_states[project["name"]] = ProjectState.DISCOVERED
            self.monitor.register_project(project["name"])

        # Standard projects
        for project in all_projects["standard_projects"]:
            self.project_states[project["name"]] = ProjectState.DISCOVERED
            self.monitor.register_project(project["name"])

        # Lock controller after initialization
        self._locked = True

        return self.project_states

    # -------------------------------------------------
    # STATE MANAGEMENT
    # -------------------------------------------------

    def validate_project(self, project_name: str):

        if not self._locked:
            raise RuntimeError("Engine not initialized properly")

        current_state = self.project_states.get(project_name)

        if not current_state:
            raise ValueError(f"Project {project_name} not registered")

        next_state = ProjectState.VALIDATED

        if self.state_machine.can_transition(current_state, next_state):
            self.project_states[project_name] = next_state
            self.monitor.update_state(project_name, next_state)
            return next_state

        raise ValueError(f"Invalid transition for {project_name}")

    def get_project_state(self, project_name: str):
        return self.project_states.get(project_name)

    # -------------------------------------------------
    # ALLOCATION
    # -------------------------------------------------

    def allocate_projects(self):
        return self.allocator.allocate(self)

    # -------------------------------------------------
    # MONITORING
    # -------------------------------------------------

    def get_project_metrics(self, project_name: str):
        return self.monitor.get_project_metrics(project_name)

    def get_all_metrics(self):
        return self.monitor.get_all_metrics()
