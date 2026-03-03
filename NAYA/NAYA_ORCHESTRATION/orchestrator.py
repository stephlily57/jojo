"""
NAYA Project Execution - Orchestrator

Orchestrates project execution across Cloud Run, VMs, and local environments.
Handles task distribution, monitoring, and result aggregation.
"""

import json
import uuid
from datetime import datetime
from typing import Dict, Any, List
from enum import Enum


class ProjectStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class ExecutionPlan:
    """Represents a complete project execution plan."""

    def __init__(self, project_id: str, tasks: List[Dict[str, Any]]):
        self.id = project_id
        self.tasks = tasks
        self.created_at = datetime.utcnow().isoformat()
        self.status = ProjectStatus.PENDING
        self.results = {}
        self.execution_log = []

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status.value,
            'tasks': self.tasks,
            'created_at': self.created_at,
            'results': self.results,
            'execution_log': self.execution_log
        }


class ProjectOrchestrator:
    """
    Main orchestration engine for NAYA projects.

    Responsibilities:
    - Break down business models into executable tasks
    - Distribute tasks to appropriate executors (CloudRun/VM/Local)
    - Track execution progress
    - Aggregate results
    - Handle failures and retries
    """

    def __init__(self):
        self.plans: Dict[str, ExecutionPlan] = {}
        self.active_tasks = {}
        self.execution_history = []

    def create_execution_plan(self, business_model: Dict[str, Any]) -> ExecutionPlan:
        """
        Decompose a business model into executable tasks.

        From structured model:
        {
            'problem': '...',
            'target_market': '...',
            'value_proposition': ...,
            'capitalizable': True
        }

        Create tasks like:
        - RESEARCH: Market analysis
        - VALIDATE: Solution validation
        - PROTOTYPE: MVP building
        - DEPLOY: Launch execution
        - MONITOR: KPI tracking
        """
        project_id = str(uuid.uuid4())[:8]

        # Decompose business model into tasks
        tasks = self._decompose_model(business_model)

        plan = ExecutionPlan(project_id, tasks)
        self.plans[project_id] = plan

        return plan

    def _decompose_model(self, model: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Break down business model into concrete tasks."""
        tasks = []

        # Task 1: Market Research
        tasks.append({
            'id': 'task_research',
            'type': 'RESEARCH',
            'title': f"Research market: {model.get('target_market')}",
            'description': f"Analyze market dynamics for {model.get('problem')}",
            'executor': 'LOCAL',  # Can run locally first
            'priority': 'HIGH',
            'timeout': 300,
            'params': {
                'market': model.get('target_market'),
                'problem': model.get('problem')
            }
        })

        # Task 2: Solution Validation
        tasks.append({
            'id': 'task_validate',
            'type': 'VALIDATE',
            'title': f"Validate solution for {model.get('problem')}",
            'description': f"Test value proposition: {model.get('value_proposition')}",
            'executor': 'LOCAL',
            'priority': 'HIGH',
            'timeout': 300,
            'depends_on': ['task_research'],
            'params': {
                'value_prop': model.get('value_proposition'),
                'capital': model.get('capitalizable')
            }
        })

        # Task 3: Prototype Development
        tasks.append({
            'id': 'task_prototype',
            'type': 'PROTOTYPE',
            'title': 'Build MVP prototype',
            'description': 'Create minimum viable product',
            'executor': 'CLOUDRUN',
            'priority': 'MEDIUM',
            'timeout': 600,
            'depends_on': ['task_validate'],
            'params': {
                'market': model.get('target_market')
            }
        })

        # Task 4: Deployment
        tasks.append({
            'id': 'task_deploy',
            'type': 'DEPLOY',
            'title': 'Deploy to production',
            'description': 'Launch solution to market',
            'executor': 'CLOUDRUN',
            'priority': 'HIGH',
            'timeout': 900,
            'depends_on': ['task_prototype'],
            'params': {
                'market': model.get('target_market')
            }
        })

        # Task 5: Monitoring & KPI
        tasks.append({
            'id': 'task_monitor',
            'type': 'MONITOR',
            'title': 'Monitor KPIs and performance',
            'description': 'Track metrics: revenue, speed, reliability',
            'executor': 'CLOUDRUN',
            'priority': 'HIGH',
            'timeout': 0,  # Continuous
            'depends_on': ['task_deploy'],
            'params': {
                'kpi_interval': 60
            }
        })

        return tasks

    def execute_plan(self, plan_id: str, executor_map: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a plan using the provided executor map.

        executor_map = {
            'LOCAL': LocalExecutor(),
            'CLOUDRUN': CloudRunExecutor(),
            'VM': VMExecutor()
        }
        """
        if plan_id not in self.plans:
            raise ValueError(f"Plan {plan_id} not found")

        plan = self.plans[plan_id]
        plan.status = ProjectStatus.RUNNING

        executed = set()
        failed = set()

        for task in plan.tasks:
            # Check dependencies
            deps = task.get('depends_on', [])
            if not all(dep in executed for dep in deps):
                plan.execution_log.append({
                    'task': task['id'],
                    'status': 'SKIPPED',
                    'reason': 'Dependency not met',
                    'timestamp': datetime.utcnow().isoformat()
                })
                continue

            # Execute task
            executor_type = task.get('executor', 'LOCAL')
            executor = executor_map.get(executor_type)

            if not executor:
                plan.execution_log.append({
                    'task': task['id'],
                    'status': 'FAILED',
                    'reason': f'Executor {executor_type} not available',
                    'timestamp': datetime.utcnow().isoformat()
                })
                failed.add(task['id'])
                continue

            try:
                result = executor.execute(task)
                plan.results[task['id']] = result
                executed.add(task['id'])

                plan.execution_log.append({
                    'task': task['id'],
                    'status': 'COMPLETED',
                    'result': result,
                    'timestamp': datetime.utcnow().isoformat()
                })
            except Exception as e:
                plan.execution_log.append({
                    'task': task['id'],
                    'status': 'FAILED',
                    'error': str(e),
                    'timestamp': datetime.utcnow().isoformat()
                })
                failed.add(task['id'])

        # Update plan status
        if failed:
            plan.status = ProjectStatus.FAILED
        else:
            plan.status = ProjectStatus.COMPLETED

        self.execution_history.append(plan.to_dict())

        return {
            'plan_id': plan_id,
            'status': plan.status.value,
            'executed_tasks': len(executed),
            'failed_tasks': len(failed),
            'results': plan.results,
            'log': plan.execution_log[-10:]  # Last 10 events
        }

    def get_plan_status(self, plan_id: str) -> Dict[str, Any]:
        """Get current status of an execution plan."""
        if plan_id not in self.plans:
            raise ValueError(f"Plan {plan_id} not found")

        plan = self.plans[plan_id]
        return {
            'id': plan_id,
            'status': plan.status.value,
            'tasks_total': len(plan.tasks),
            'tasks_completed': len([t for t in plan.tasks if t['id'] in plan.results]),
            'results': plan.results,
            'last_events': plan.execution_log[-5:]
        }


__all__ = ['ProjectOrchestrator', 'ExecutionPlan', 'ProjectStatus']
