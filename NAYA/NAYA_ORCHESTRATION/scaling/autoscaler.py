class AutoScaler:
    def scale(self, density: float):
        if density > 0.8:
            return "scale_up"
        return "stable"