"""
Filtre d’acceptabilité des solutions.
AUTORITÉ D’ACTION.
"""

def is_solution_acceptable(discretion: bool, exposure_risk: bool) -> bool:
    if discretion and not exposure_risk:
        return True
    return False
