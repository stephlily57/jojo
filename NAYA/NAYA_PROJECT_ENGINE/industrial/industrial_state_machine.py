from enum import Enum


class ProjectState(Enum):
    DISCOVERED = "discovered"
    VALIDATED = "validated"
    ALLOCATED = "allocated"
    EXECUTING = "executing"
    MONITORING = "monitoring"
    COMPLETED = "completed"
    FAILED = "failed"


class IndustrialStateMachine:
    """
    Controls legal state transitions
    Prevents chaotic execution flows
    """

    allowed_transitions = {
        ProjectState.DISCOVERED: [ProjectState.VALIDATED],
        ProjectState.VALIDATED: [ProjectState.ALLOCATED],
        ProjectState.ALLOCATED: [ProjectState.EXECUTING],
        ProjectState.EXECUTING: [ProjectState.MONITORING, ProjectState.FAILED],
        ProjectState.MONITORING: [ProjectState.COMPLETED, ProjectState.FAILED],
        ProjectState.FAILED: [],
        ProjectState.COMPLETED: [],
    }

    def can_transition(self, current_state: ProjectState, next_state: ProjectState) -> bool:
        return next_state in self.allowed_transitions.get(current_state, [])

    def next_state(self, current_state: ProjectState, next_state: ProjectState):
        if self.can_transition(current_state, next_state):
            return next_state
        raise ValueError(
            f"Invalid transition from {current_state} to {next_state}"
        )
