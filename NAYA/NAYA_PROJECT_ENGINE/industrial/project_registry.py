from pathlib import Path
import json


class ProjectRegistry:
    """
    Industrial Project Registry
    ---------------------------
    - Scans business layer
    - Loads project manifests
    - Exposes structured project metadata
    - Ignores technical folders (__pycache__, hidden dirs)
    """

    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.business_path = base_path / "business"
        self.projects_path = self.business_path / "projects"
        self.activation_path = self.business_path / "activation_queue"

    # -------------------------------------------------
    # INTERNAL UTILITIES
    # -------------------------------------------------

    def _load_manifest(self, project_path: Path):
        manifest_file = project_path / "project_manifest.json"

        if not manifest_file.exists():
            return None

        try:
            with open(manifest_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None

    def _is_valid_project_dir(self, path: Path):
        return (
            path.is_dir()
            and not path.name.startswith("__")
            and not path.name.startswith(".")
        )

    # -------------------------------------------------
    # STANDARD PROJECTS
    # -------------------------------------------------

    def list_projects(self):
        projects = []

        if not self.projects_path.exists():
            return projects

        for project_dir in self.projects_path.iterdir():
            if self._is_valid_project_dir(project_dir):
                manifest = self._load_manifest(project_dir)
                projects.append({
                    "name": project_dir.name,
                    "type": "standard",
                    "manifest": manifest
                })

        return projects

    # -------------------------------------------------
    # ACTIVATION QUEUE
    # -------------------------------------------------

    def list_activation_queue(self):
        activation_projects = []

        if not self.activation_path.exists():
            return activation_projects

        for project_dir in self.activation_path.iterdir():
            if self._is_valid_project_dir(project_dir):
                activation_projects.append({
                    "name": project_dir.name,
                    "type": "activation"
                })

        return activation_projects

    # -------------------------------------------------
    # GLOBAL ACCESS
    # -------------------------------------------------

    def get_all_projects(self):
        return {
            "activation_queue": self.list_activation_queue(),
            "standard_projects": self.list_projects()
        }
