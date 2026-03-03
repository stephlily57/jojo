# engine_execution_allocator.py

from typing import List, Dict


class ExecutionAllocator:

    def allocate(self, opportunities: List[Dict]) -> Dict:
        active = []
        incubation = []

        for opp in opportunities:
            if len(active) < 3:
                active.append(opp)
            else:
                incubation.append(opp)

        return {
            "active": active,
            "incubation": incubation
        }


EXECUTION_ALLOCATOR = ExecutionAllocator()
