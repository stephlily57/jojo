# -*- coding: utf-8-sig -*-
class RuntimeState:
    def __init__(self):
        self.active = False
        self.websocket_ready = False
        self.started_at = None

STATE = RuntimeState()
