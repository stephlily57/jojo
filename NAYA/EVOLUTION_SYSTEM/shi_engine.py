class SHIEngine:

    def compute_shi(self, kpi_score):

        if kpi_score >= 80:
            return "HIGH"

        if kpi_score >= 60:
            return "MEDIUM"

        return "LOW"
