class CoreSignalFusion:

    def fuse(self, signals):
        score = 0
        weight_total = 0

        for signal in signals:
            weight = signal.get("weight", 1)
            score += signal.get("value", 0) * weight
            weight_total += weight

        if weight_total == 0:
            return 0

        return score / weight_total
