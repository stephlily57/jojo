class DegradationControl:

    def evaluate(self, context):

        if context["exposure"] > 0.8:
            return 2
        if context["cluster_load"] > 0.9:
            return 1

        return 0
