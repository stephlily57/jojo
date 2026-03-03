# threat_aware_executor.py

class ThreatAwareExecutor:

    def evaluate(self, threat_score: int):

        if threat_score > 10:
            print("[AUTOMATION] High threat detected, restricting execution")
            return False

        return True
