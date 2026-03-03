# compensation_engine.py

class CompensationEngine:

    def compensate(self, workflow_name: str, context: dict):

        print(f"[AUTOMATION] Compensation triggered for {workflow_name}")

        # Exemple simple : rollback flag
        context["compensated"] = True

        return context
