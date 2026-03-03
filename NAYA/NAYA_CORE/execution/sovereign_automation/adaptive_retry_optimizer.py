# adaptive_retry_optimizer.py

class AdaptiveRetryOptimizer:

    def optimize(self, failure_count: int):

        if failure_count > 5:
            return 5  # max attempts augmenté

        return 3
