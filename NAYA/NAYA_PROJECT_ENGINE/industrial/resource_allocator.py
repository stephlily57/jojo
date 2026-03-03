from .industrial_state_machine import ProjectState


class ResourceAllocator:
    """
    Basic industrial allocation logic
    Priority:
    1. Activation queue projects
    2. Standard projects
    """

    def allocate(self, controller):
        allocation_order = []

        # Activation projects first
        for name, state in controller.project_states.items():
            if state == ProjectState.DISCOVERED:
                allocation_order.append(name)

        return allocation_order
