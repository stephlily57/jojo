class CoreSelfHealing:

    def __init__(self, integrity_lock):
        self.integrity_lock = integrity_lock

    def auto_repair(self, stored_hash):
        if not self.integrity_lock.verify(stored_hash):
            return "Integrity breach detected"
        return "System stable"
