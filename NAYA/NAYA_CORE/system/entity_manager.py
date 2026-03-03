# NAYA_CORE / entity_manager.py

import uuid


class EntityManager:
    """
    Gère les entités économiques cloisonnées.
    Cluster aware.
    """

    def current_node(self):
        return str(uuid.uuid4())[:8]

    def cluster_capacity(self):
        return 10  # évolutif

    def assign_entity(self, opportunity):
        return f"ENTITY_{uuid.uuid4().hex[:6]}"


ENTITY_MANAGER = EntityManager()
