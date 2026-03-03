
def evaluate(metrics: dict) -> list:
    alerts = []
    if metrics.get("cpu_percent", 0) > 85:
        alerts.append("CPU usage high")
    if metrics.get("memory_percent", 0) > 85:
        alerts.append("Memory usage high")
    return alerts
