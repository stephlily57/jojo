class DirectiveSplitter:
    @staticmethod
    def split(payload: dict, threshold: int = 1000):
        if len(str(payload)) > threshold:
            return [payload]
        return [payload]