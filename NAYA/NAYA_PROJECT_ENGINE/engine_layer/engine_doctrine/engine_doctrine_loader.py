import os
from typing import Dict, List, Any

# ============================================================
# ENGINE DOCTRINE LOADER — DECLARATIVE ONLY
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

ENGINE_DIR = BASE_DIR
PROJECTS_DIR = os.path.join(BASE_DIR, "projects")


def safe_listdir(path: str) -> List[str]:
    try:
        return [
            f for f in os.listdir(path)
            if not f.startswith("__") and not f.startswith(".")
        ]
    except Exception:
        return []


def scan_engines() -> Dict[str, Any]:
    engines = {}

    for item in safe_listdir(ENGINE_DIR):
        full_path = os.path.join(ENGINE_DIR, item)

        if os.path.isdir(full_path) and item.startswith("engine_"):
            engines[item] = {
                "type": "ENGINE",
                "declared": True,
                "files": safe_listdir(full_path)
            }

    return engines


def scan_projects() -> Dict[str, Any]:
    projects = {}

    for project in safe_listdir(PROJECTS_DIR):
        project_path = os.path.join(PROJECTS_DIR, project)

        if os.path.isdir(project_path):
            projects[project] = {
                "type": "PROJECT",
                "ready": True,
                "structure": safe_listdir(project_path)
            }

    return projects


def build_doctrine() -> Dict[str, Any]:
    doctrine = {
        "doctrine": {
            "cash_orientation": "REAL",
            "pain_required": True,
            "execution_speed": ["24H", "48H", "72H"],
            "budget_policy": "ZERO_REQUIRED",
            "mode": "PREMIUM_ONLY",
            "value_floor": 1000,
            "value_ceiling": 15000000,
            "pipeline_policy": "CONTINUOUS",
            "ambition": "UNBOUNDED"
        },
        "engines": scan_engines(),
        "projects": scan_projects(),
        "status": "DECLARED"
    }

    return doctrine


# ============================================================
# PUBLIC ENTRY (CALLED BY ORCHESTRATION / CORE)
# ============================================================

def declare_project_engine() -> Dict[str, Any]:
    """
    This function DOES NOT execute anything.
    It only DECLARES how Naya must create.
    """
    return build_doctrine()


# ============================================================
# SAFE STANDALONE CHECK (OPTIONAL)
# ============================================================

if __name__ == "__main__":
    import json
    print(json.dumps(declare_project_engine(), indent=2))
