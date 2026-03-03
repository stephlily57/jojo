class InterfacePolicy:

    @staticmethod
    def enforce(directive):
        if directive.get("origin") == "unauthorized":
            raise PermissionError("Unauthorized origin")
        return True