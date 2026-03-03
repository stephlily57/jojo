
from NAYA_INTERFACE.bus.state_stream import state_stream
from NAYA_DASHBOARD.NAYA_MONITORING.metrics_collector import collect_metrics
from NAYA_DASHBOARD.NAYA_MONITORING.performance_tracker import track
from NAYA_DASHBOARD.NAYA_MONITORING.alerts_engine import evaluate

def _tick():
    metrics = collect_metrics()
    track(metrics)
    alerts = evaluate(metrics)
    state_stream.update_state("monitoring", {
        "metrics": metrics,
        "alerts": alerts
    })

# simple timer hook (called externally)
def monitoring_tick():
    _tick()
