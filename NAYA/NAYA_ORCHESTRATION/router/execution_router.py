"""
NAYA Execution Router

Routes tasks to the most appropriate executor based on:
- Environment (CloudRun/VM/Local)
- Task type (RESEARCH/VALIDATE/PROTOTYPE/DEPLOY/MONITOR)
- Resource requirements
- Availability and cost
"""

import os
from typing import Dict, Any, Tuple


class ExecutionRouter:
    """
    Intelligent routing system for task execution.

    Selects optimal executor for each task based on:
    - Current environment
    - Task requirements
    - Cost optimization
    - Performance requirements
    """

    def __init__(self):
        self.environment = self._detect_environment()
        self.executors_available = self._detect_executors()

    def _detect_environment(self) -> str:
        """Detect current environment."""
        if os.environ.get("K_SERVICE"):
            return "CLOUDRUN"
        elif os.environ.get("VM_HOST"):
            return "VM"
        else:
            return "LOCAL"

    def _detect_executors(self) -> Dict[str, bool]:
        """Detect which executors are available."""
        return {
            'LOCAL': True,  # Always available
            'CLOUDRUN': bool(os.environ.get("GCP_PROJECT_ID")),
            'VM': bool(os.environ.get("VM_HOST"))
        }

    def route_task(self, task: Dict[str, Any]) -> str:
        """
        Route a task to the best executor.

        Args:
            task: Task with type, params, executor preference

        Returns:
            Executor name: 'LOCAL', 'CLOUDRUN', or 'VM'
        """
        # Check if executor preference is specified
        preferred = task.get('executor')
        if preferred and self.executors_available.get(preferred):
            return preferred

        # Route based on task type
        task_type = task.get('type')
        return self._route_by_type(task_type)

    def _route_by_type(self, task_type: str) -> str:
        """Route based on task type and available executors."""

        routing_rules = {
            'RESEARCH': self._route_research,
            'VALIDATE': self._route_validate,
            'PROTOTYPE': self._route_prototype,
            'DEPLOY': self._route_deploy,
            'MONITOR': self._route_monitor
        }

        router_func = routing_rules.get(task_type, self._route_generic)
        return router_func()

    def _route_research(self) -> str:
        """Route research tasks - prefer LOCAL for fast iteration."""
        return 'LOCAL'

    def _route_validate(self) -> str:
        """Route validation tasks - prefer LOCAL for dev."""
        return 'LOCAL'

    def _route_prototype(self) -> str:
        """Route prototype building - prefer CLOUDRUN for isolation."""
        if self.executors_available['CLOUDRUN']:
            return 'CLOUDRUN'
        elif self.executors_available['VM']:
            return 'VM'
        return 'LOCAL'

    def _route_deploy(self) -> str:
        """Route deployment - prefer CLOUDRUN for production."""
        if self.executors_available['CLOUDRUN']:
            return 'CLOUDRUN'
        elif self.executors_available['VM']:
            return 'VM'
        return 'LOCAL'

    def _route_monitor(self) -> str:
        """Route monitoring - prefer CLOUDRUN for continuous running."""
        if self.executors_available['CLOUDRUN']:
            return 'CLOUDRUN'
        elif self.executors_available['VM']:
            return 'VM'
        return 'LOCAL'

    def _route_generic(self) -> str:
        """Route generic tasks - use current environment."""
        if self.executors_available.get(self.environment):
            return self.environment
        return 'LOCAL'

    def get_routing_info(self) -> Dict[str, Any]:
        """Get current routing configuration."""
        return {
            'environment': self.environment,
            'executors_available': self.executors_available,
            'routing_rules': {
                'RESEARCH': 'LOCAL (fast iteration)',
                'VALIDATE': 'LOCAL (fast iteration)',
                'PROTOTYPE': 'CLOUDRUN > VM > LOCAL',
                'DEPLOY': 'CLOUDRUN > VM > LOCAL',
                'MONITOR': 'CLOUDRUN > VM > LOCAL'
            }
        }


__all__ = ['ExecutionRouter']
