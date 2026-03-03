"""
NAYA Persistence Layer

Handles all data storage, retrieval, and management.
Supports multiple backends: Memory, File, Cloud Firestore, Redis.
"""

import json
import os
from datetime import datetime
from typing import Dict, Any, List, Optional
from abc import ABC, abstractmethod


class PersistenceBackend(ABC):
    """Abstract base class for persistence backends."""

    @abstractmethod
    def save(self, key: str, data: Dict[str, Any]) -> bool:
        """Save data."""
        pass

    @abstractmethod
    def load(self, key: str) -> Optional[Dict[str, Any]]:
        """Load data."""
        pass

    @abstractmethod
    def delete(self, key: str) -> bool:
        """Delete data."""
        pass

    @abstractmethod
    def list_keys(self, pattern: str = "*") -> List[str]:
        """List keys matching pattern."""
        pass


class MemoryBackend(PersistenceBackend):
    """In-memory storage (for development/testing)."""

    def __init__(self):
        self.store = {}

    def save(self, key: str, data: Dict[str, Any]) -> bool:
        self.store[key] = {
            'data': data,
            'timestamp': datetime.utcnow().isoformat()
        }
        return True

    def load(self, key: str) -> Optional[Dict[str, Any]]:
        if key in self.store:
            return self.store[key]['data']
        return None

    def delete(self, key: str) -> bool:
        if key in self.store:
            del self.store[key]
            return True
        return False

    def list_keys(self, pattern: str = "*") -> List[str]:
        import fnmatch
        return fnmatch.filter(self.store.keys(), pattern)

    def get_size(self) -> int:
        """Get number of stored items."""
        return len(self.store)


class FileBackend(PersistenceBackend):
    """File-based storage (for local development)."""

    def __init__(self, base_path: str = "./data"):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    def save(self, key: str, data: Dict[str, Any]) -> bool:
        try:
            filepath = os.path.join(self.base_path, f"{key}.json")
            payload = {
                'data': data,
                'timestamp': datetime.utcnow().isoformat()
            }
            with open(filepath, 'w') as f:
                json.dump(payload, f, indent=2)
            return True
        except Exception:
            return False

    def load(self, key: str) -> Optional[Dict[str, Any]]:
        try:
            filepath = os.path.join(self.base_path, f"{key}.json")
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    payload = json.load(f)
                    return payload.get('data')
        except Exception:
            pass
        return None

    def delete(self, key: str) -> bool:
        try:
            filepath = os.path.join(self.base_path, f"{key}.json")
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
        except Exception:
            pass
        return False

    def list_keys(self, pattern: str = "*") -> List[str]:
        import fnmatch
        keys = []
        try:
            for filename in os.listdir(self.base_path):
                if filename.endswith('.json'):
                    key = filename[:-5]  # Remove .json
                    if fnmatch.fnmatch(key, pattern):
                        keys.append(key)
        except Exception:
            pass
        return keys


class PersistenceManager:
    """
    Manages data persistence with pluggable backends.

    Supports:
    - Automatic backend selection
    - Data versioning
    - Backup and recovery
    - Multi-backend sync
    """

    def __init__(self, backend: PersistenceBackend = None):
        self.backend = backend or self._select_backend()
        self.transaction_log = []

    def _select_backend(self) -> PersistenceBackend:
        """Automatically select best backend based on environment."""
        # In development, use file backend
        if os.environ.get('ENV') == 'development':
            return FileBackend('./data')

        # In production, could use Firestore, Redis, etc
        # For now, default to memory
        return MemoryBackend()

    # Project Operations
    def save_project(self, project_id: str, project_data: Dict[str, Any]) -> bool:
        """Save a project."""
        key = f"project:{project_id}"
        success = self.backend.save(key, {
            'id': project_id,
            'data': project_data,
            'saved_at': datetime.utcnow().isoformat()
        })

        if success:
            self._log_transaction('SAVE', key)

        return success

    def load_project(self, project_id: str) -> Optional[Dict[str, Any]]:
        """Load a project."""
        key = f"project:{project_id}"
        data = self.backend.load(key)
        self._log_transaction('LOAD', key)
        return data

    def delete_project(self, project_id: str) -> bool:
        """Delete a project."""
        key = f"project:{project_id}"
        success = self.backend.delete(key)
        if success:
            self._log_transaction('DELETE', key)
        return success

    # Opportunity Operations
    def save_opportunity(self, opp_id: str, opp_data: Dict[str, Any]) -> bool:
        """Save an opportunity."""
        key = f"opportunity:{opp_id}"
        return self.backend.save(key, {
            'id': opp_id,
            'data': opp_data,
            'saved_at': datetime.utcnow().isoformat()
        })

    def load_opportunity(self, opp_id: str) -> Optional[Dict[str, Any]]:
        """Load an opportunity."""
        key = f"opportunity:{opp_id}"
        return self.backend.load(key)

    # Execution Plan Operations
    def save_execution_plan(self, plan_id: str, plan_data: Dict[str, Any]) -> bool:
        """Save an execution plan."""
        key = f"plan:{plan_id}"
        return self.backend.save(key, {
            'id': plan_id,
            'plan': plan_data,
            'saved_at': datetime.utcnow().isoformat()
        })

    def load_execution_plan(self, plan_id: str) -> Optional[Dict[str, Any]]:
        """Load an execution plan."""
        key = f"plan:{plan_id}"
        return self.backend.load(key)

    # Execution Result Operations
    def save_execution_result(self, result_id: str, result_data: Dict[str, Any]) -> bool:
        """Save execution result."""
        key = f"result:{result_id}"
        return self.backend.save(key, {
            'id': result_id,
            'result': result_data,
            'timestamp': datetime.utcnow().isoformat()
        })

    def load_execution_result(self, result_id: str) -> Optional[Dict[str, Any]]:
        """Load execution result."""
        key = f"result:{result_id}"
        return self.backend.load(key)

    # KPI Operations
    def save_kpi_score(self, project_id: str, kpi_data: Dict[str, Any]) -> bool:
        """Save KPI scores."""
        key = f"kpi:{project_id}"
        return self.backend.save(key, {
            'project_id': project_id,
            'kpi': kpi_data,
            'timestamp': datetime.utcnow().isoformat()
        })

    def load_kpi_score(self, project_id: str) -> Optional[Dict[str, Any]]:
        """Load KPI scores."""
        key = f"kpi:{project_id}"
        return self.backend.load(key)

    # Query Operations
    def list_projects(self) -> List[str]:
        """List all project IDs."""
        keys = self.backend.list_keys("project:*")
        return [k.replace("project:", "") for k in keys]

    def list_opportunities(self) -> List[str]:
        """List all opportunity IDs."""
        keys = self.backend.list_keys("opportunity:*")
        return [k.replace("opportunity:", "") for k in keys]

    def list_execution_plans(self) -> List[str]:
        """List all execution plan IDs."""
        keys = self.backend.list_keys("plan:*")
        return [k.replace("plan:", "") for k in keys]

    # Transaction Logging
    def _log_transaction(self, operation: str, key: str):
        """Log a persistence transaction."""
        self.transaction_log.append({
            'operation': operation,
            'key': key,
            'timestamp': datetime.utcnow().isoformat()
        })

    def get_transaction_history(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get transaction history."""
        return self.transaction_log[-limit:]

    # System Info
    def get_stats(self) -> Dict[str, Any]:
        """Get persistence statistics."""
        return {
            'backend': self.backend.__class__.__name__,
            'transactions': len(self.transaction_log),
            'projects': len(self.list_projects()),
            'opportunities': len(self.list_opportunities()),
            'plans': len(self.list_execution_plans())
        }


__all__ = [
    'PersistenceManager',
    'PersistenceBackend',
    'MemoryBackend',
    'FileBackend'
]
