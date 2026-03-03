class InterfaceContract:

    REQUIRED_FIELDS = ["directive_id", "origin", "payload"]

    @staticmethod
    def validate_structure(data: dict):
        for field in InterfaceContract.REQUIRED_FIELDS:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        return True