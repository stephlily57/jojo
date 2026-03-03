class KPIEngine:

    def evaluate_performance(self, revenue, execution_speed, reliability):

        score = (
            (revenue * 0.4) +
            (execution_speed * 0.3) +
            (reliability * 0.3)
        )

        return round(score, 2)
