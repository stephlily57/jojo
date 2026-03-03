# -*- coding: utf-8-sig -*-
REQUIRED_KEYS = ["naya", "modules", "projects"]

def validate_schema(payload: dict):
    for key in REQUIRED_KEYS:
        if key not in payload:
            raise ValueError(f"Missing required key: {key}")
    return True
