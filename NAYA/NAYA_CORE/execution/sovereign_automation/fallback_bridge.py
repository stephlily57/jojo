# fallback_bridge.py

import requests


class FallbackBridge:

    def __init__(self, n8n_url: str):
        self.n8n_url = n8n_url

    def trigger(self, workflow_name: str, payload: dict):

        requests.post(
            f"{self.n8n_url}/webhook/{workflow_name}",
            json=payload
        )
