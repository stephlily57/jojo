# NAYA_CORE/execution/sovereign_automation/workflow_registry.py

WORKFLOWS = {
    "generic_api_call": {
        "steps": [
            "prepare_request",
            "execute_api_call",
            "validate_response"
        ]
    }
}
