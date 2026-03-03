class SupplierIntelligenceEngine:

    def evaluate_supplier(self, quality_score, cost, reliability_score):
        """
        Évalue un fournisseur sur 100.
        """

        score = (
            (quality_score * 0.4) +
            ((100 - cost) * 0.3) +
            (reliability_score * 0.3)
        )

        return round(score, 2)
