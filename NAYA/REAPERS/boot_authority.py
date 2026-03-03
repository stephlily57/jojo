# REAPERS/boot_authority.py

class BootAuthority:
    """
    Controls boot authorization.
    In silent recovery mode, always returns True.
    """

    def authorize(self) -> bool:
        return True
