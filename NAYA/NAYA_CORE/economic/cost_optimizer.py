class CostOptimizer:

    def __init__(self):
        self.usage_stats = {}

    def record_usage(self, provider, latency, cost):
        self.usage_stats.setdefault(provider, []).append({
            "latency": latency,
            "cost": cost
        })

    def select_optimal(self):
        scores = {}
        for provider, entries in self.usage_stats.items():
            avg_cost = sum(e["cost"] for e in entries) / len(entries)
            avg_latency = sum(e["latency"] for e in entries) / len(entries)
            scores[provider] = avg_cost + avg_latency
        return min(scores, key=scores.get) if scores else None
