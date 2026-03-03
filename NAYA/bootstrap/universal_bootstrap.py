from bootstrap.environment_detector import EnvironmentDetector
from bootstrap.runtime_attestation import RuntimeAttestation
from bootstrap.secret_provider import SecretProvider
from bootstrap.contract_loader import ContractLoader


def activate():

    # 1️⃣ Detect environment
    env = EnvironmentDetector.detect()

    # 2️⃣ Attestation
    fingerprint = RuntimeAttestation.fingerprint()

    # 3️⃣ Prepare environment
    if env == "cloudrun":
        from bootstrap.cloudrun_initializer import CloudRunInitializer
        CloudRunInitializer.prepare()

    elif env == "vm":
        from bootstrap.vm_initializer import VMInitializer
        VMInitializer.prepare()

    # 4️⃣ Load Contract
    contract = ContractLoader("NAYA_FOUNDATION/contract.json")
    contract_data = contract.load_and_lock()

    # 5️⃣ Load Secrets
    secrets = SecretProvider().load()

    # 6️⃣ Initialize Core + Modules
    from NAYA_CORE.core.engine_master import EngineMaster
    from REAPERS.reapers_core import ReapersCore
    from NAYA_ORCHESTRATION.orchestration_controller import OrchestrationController
    from NAYA_INTERFACE.interface_entry import NayaInterface

    core = EngineMaster(contract_data)
    reapers = ReapersCore()
    orchestration = OrchestrationController(core)
    interface = NayaInterface(core)

    reapers.attach()
    core.activate()
    orchestration.start()
    interface.bind()

    print("NAYA INFRASTRUCTURE ACTIVE")
    print(f"Environment: {env}")
    print(f"Fingerprint: {fingerprint}")

    return True


if __name__ == "__main__":
    activate()
