from NAYA_ORCHESTRATION.router.scoring_matrix import ScoringMatrix

class EnvironmentRouter:
    def __init__(self, environments: dict):
        self.environments = environments

    def select(self, economic_weight: float):
        best_env = None
        best_score = -1
        for name, metrics in self.environments.items():
            score = ScoringMatrix.compute(metrics, economic_weight)
            if score > best_score:
                best_score = score
                best_env = name
        return best_env