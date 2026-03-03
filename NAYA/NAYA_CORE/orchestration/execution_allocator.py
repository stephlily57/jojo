class ExecutionAllocator:

    def allocate(self, opportunity, density_score):

        if density_score > 75:
            return "priority_execution"

        if density_score > 50:
            return "parallel_queue"

        return "incubation"
