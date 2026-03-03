# metrics_collector.py

import time


class MetricsCollector:

    def __init__(self):
        self.metrics = {
            "executions": 0,
            "failures": 0,
            "avg_latency": 0.0
        }

    def record_execution(self, latency: float):
        self.metrics["executions"] += 1
        self.metrics["avg_latency"] = (
            (self.metrics["avg_latency"] + latency) / 2
        )

    def record_failure(self):
        self.metrics["failures"] += 1

    def get_metrics(self):
        return self.metrics
