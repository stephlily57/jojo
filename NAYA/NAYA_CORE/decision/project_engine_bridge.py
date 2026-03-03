from NAYA_PROJECT_ENGINE.entrypoint import run_industrial_cycle


class ProjectEngineBridge:

    def launch_project(self, decision_payload: dict):

        controller = run_industrial_cycle()

        return {
            "project": decision_payload.get("project_id"),
            "mode": decision_payload.get("mode"),
            "classification": decision_payload.get("classification"),
            "density": decision_payload.get("density"),
            "engine_version": getattr(controller, "version", "unknown")
        }
