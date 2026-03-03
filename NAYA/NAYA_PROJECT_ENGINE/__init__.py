"""
NAYA PROJECT ENGINE
Core-Level Locked Industrial Engine
"""

from .industrial.execution_guard import enforce_entrypoint_execution

# Enforce execution policy
try:
    enforce_entrypoint_execution()
except RuntimeError:
    # Allow package import, but prevent direct internal execution
    pass
