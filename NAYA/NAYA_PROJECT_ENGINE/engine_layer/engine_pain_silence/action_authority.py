"""
Autorité souveraine de transformation en action.
"""

def authorize_action(acceptable: bool) -> dict:
    return {
        "authorized": acceptable,
        "authority": "ACTION_SOVEREIGN"
    }
