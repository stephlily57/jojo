
import psutil
from time import time

def collect_metrics() -> dict:
    return {
        "timestamp": time(),
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    }
