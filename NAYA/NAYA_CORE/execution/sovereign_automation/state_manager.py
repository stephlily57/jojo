# state_manager.py

class StateManager:

    def __init__(self):
        self._state = {}

    def set(self, key, value):
        self._state[key] = value

    def get(self, key):
        return self._state.get(key)

    def reset(self):
        self._state.clear()
