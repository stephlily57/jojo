class InterfaceGuard:

    def validate(self, directive):
        if "directive_id" not in directive:
            raise ValueError("Invalid directive format")
        return True