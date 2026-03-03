
from collections import deque
from time import time

_HISTORY = deque(maxlen=300)

def track(metrics: dict):
    _HISTORY.append(metrics)

def get_history():
    return list(_HISTORY)
