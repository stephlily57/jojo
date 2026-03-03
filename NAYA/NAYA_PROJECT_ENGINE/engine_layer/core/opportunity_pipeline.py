class OpportunityPipeline:

    def scan(self):

        return [
            {
                "name": "Premium Audit",
                "value": 50000,
                "effort": 2,
                "risk": 0.3,
                "equity_loss": 0,
                "dependency": 0.2
            },
            {
                "name": "Weak SaaS",
                "value": 500,
                "effort": 1,
                "risk": 0.5,
                "equity_loss": 0,
                "dependency": 0.1
            }
        ]
