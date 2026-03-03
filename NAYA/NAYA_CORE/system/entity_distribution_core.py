# entity_distribution_core.py

import uuid


class EntityDistributionCore:

    def assign(self, opportunity: dict):
        return f"ENTITY_{uuid.uuid4().hex[:8]}"


ENTITY_DISTRIBUTION_CORE = EntityDistributionCore()
