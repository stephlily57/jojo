class HybridWriteController:

    def classify_write(self, write_type):
        if write_type == "GLOBAL":
            return "LEADER_ONLY"
        elif write_type == "REGIONAL":
            return "REGION_ALLOWED"
        elif write_type == "ANALYTICAL":
            return "FREE_WRITE"
        else:
            raise ValueError("Unknown write type.")
