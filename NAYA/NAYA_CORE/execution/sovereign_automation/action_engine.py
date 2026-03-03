# action_engine.py

import requests


class ActionEngine:

    def __init__(self, secrets_base_url: str):
        self.secrets_base_url = secrets_base_url

    def prepare_request(self, context):
        return context

    def execute_api_call(self, context):

        api_key = self._get_secret(context["secret_name"])

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        response = requests.request(
            method=context["method"],
            url=context["url"],
            headers=headers,
            json=context.get("payload", {})
        )

        context["response"] = response
        return context

    def validate_response(self, context):

        response = context["response"]

        if response.status_code >= 400:
            raise Exception(f"API Error {response.status_code}")

        return context

    def _get_secret(self, secret_name):

        r = requests.get(
            f"{self.secrets_base_url}/secret/{secret_name}"
        )

        if r.status_code != 200:
            raise Exception("Secret retrieval failed")

        return r.json()["value"]
