"""
NAYA Project Engine – Industrial Layer
---------------------------------------
This module exposes the industrial orchestration components.
"""

from pathlib import Path

from .project_registry import ProjectRegistry
from .industrial_state_machine import (
    IndustrialStateMachine,
    ProjectState,
)
from .resource_allocator import ResourceAllocator
from .performance_monitor import PerformanceMonitor
from .industrial_controller import IndustrialController


def create_industrial_controller(base_path: Path) -> IndustrialController:
    """
    Factory method to create a fully initialized IndustrialController.
    """
    controller = IndustrialController(base_path)
    controller.initialize_projects()
    return controller


__all__ = [
    "ProjectRegistry",
    "IndustrialStateMachine",
    "ProjectState",
    "ResourceAllocator",
    "PerformanceMonitor",
    "IndustrialController",
    "create_industrial_controller",
]
