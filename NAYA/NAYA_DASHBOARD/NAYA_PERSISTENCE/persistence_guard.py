
from threading import Lock

_lock = Lock()

def atomic(func):
    def wrapper(*args, **kwargs):
        with _lock:
            return func(*args, **kwargs)
    return wrapper
