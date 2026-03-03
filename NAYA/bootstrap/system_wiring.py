# bootstrap/system_wiring.py

def wire_system(registry):

    core = registry.get("core")
    reapers = registry.get("reapers")
    orchestration = registry.get("orchestration")
    interface = registry.get("interface")
    gateway = registry.get("gateway")

    # Attache Reapers au Core
    reapers.attach()

    # Active Core
    core.activate()

    # Lance Orchestration
    orchestration.start()

    # Bind Interface
    interface.bind()

    print("[BOOT] System wiring complete")
