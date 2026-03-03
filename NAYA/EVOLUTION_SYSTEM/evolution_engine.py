class EvolutionEngine:

    def __init__(self, proposal_generator):
        self.proposal_generator = proposal_generator

    def propose_evolution(self, context, shi_level):

        if shi_level == "HIGH":
            return []

        return self.proposal_generator.generate_alternatives(context)
