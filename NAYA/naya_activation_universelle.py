# =========================================================
# NAYA — ACTIVATION UNIVERSELLE FINALE PRODUCTION
# Monitoring + Heartbeat + Auto-Fallback
# =========================================================

import importlib
import os
import json
import hashlib
import threading
import time
import requests
from datetime import datetime
from pathlib import Path
from flask import Flask, jsonify


# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "naya_activation.log"
STATE_FILE = LOG_DIR / "naya_state.json"
SEAL_FILE = LOG_DIR / "naya_state.seal"

HEARTBEAT_PORT = 8787
CHECK_INTERVAL = 30


# ---------------------------------------------------------
# OUTILS
# ---------------------------------------------------------

def now():
    return datetime.utcnow().isoformat() + "Z"


def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now()}] {msg}\n")


def seal_state(data):
    payload = json.dumps(data, sort_keys=True).encode()
    digest = hashlib.sha256(payload).hexdigest()
    SEAL_FILE.write_text(digest)
    log("Etat scellé (SHA256)")


def detect_support():
    if os.environ.get("K_SERVICE"):
        return "cloud_run"
    if Path("/etc/systemd/system/naya.service").exists():
        return "vm"
    return "offline"


def load(module_path):
    log(f"Chargement : {module_path}")
    return importlib.import_module(module_path)


# ---------------------------------------------------------
# HEARTBEAT DISTRIBUE
# ---------------------------------------------------------

app = Flask(__name__)
CORE_REFERENCE = None


def attach_core(core):
    global CORE_REFERENCE
    CORE_REFERENCE = core


@app.route("/heartbeat")
def heartbeat():
    return jsonify({
        "status": "alive",
        "mode": CORE_REFERENCE.get_mode() if CORE_REFERENCE else "unknown",
        "timestamp": now()
    })


def start_heartbeat():
    app.run(host="0.0.0.0", port=HEARTBEAT_PORT)


# ---------------------------------------------------------
# MONITORING + AUTO FALLBACK
# ---------------------------------------------------------

class MonitoringEngine:

    def __init__(self, core):
        self.core = core

    def run(self):
        while True:
            self.check_internal()
            self.check_external()
            time.sleep(CHECK_INTERVAL)

    def check_internal(self):
        if not self.core.is_alive():
            log("ALERTE : Core non actif")

        if not self.core.reapers.is_ready():
            log("ALERTE : Reapers non prêt")

    def check_external(self):
        # Exemple : vérifier cloud
        cloud_url = os.environ.get("NAYA_CLOUD_URL")
        if cloud_url:
            try:
                r = requests.get(f"{cloud_url}/heartbeat", timeout=5)
                if r.status_code != 200:
                    self.activate_safe_mode()
            except:
                self.activate_safe_mode()

    def activate_safe_mode(self):
        log("Fallback SAFE MODE activé")
        self.core.force_safe_mode()


# ---------------------------------------------------------
# ACTIVATION PRINCIPALE
# ---------------------------------------------------------

def activate_naya():

    support = detect_support()
    log(f"Activation démarrée sur : {support}")

    # ===============================
    # PHASE 0 — OBSERVATION
    # ===============================
    load("NAYA_OBSERVATION.observer")
    load("NAYA_EVENT_STREAM.stream")
    load("NAYA_COMMAND_GATEWAY.gateway")
    load("NAYA_DASHBOARD.dashboard")

    # ===============================
    # PHASE 1 — ACTIVATION COMPLETE
    # ===============================

    contract = load("NAYA_CONTRACTS.contract_reader")
    contract.lock()
    log("Contrat verrouillé")

    secrets = load("NAYA_SECRETS.secret_manager")
    secrets.load_secure()
    log("Secrets sécurisés en mémoire")

    load("NAYA_INTERFACE.interface")

    core = load("NAYACOR.core_engine")
    reapers = load("NAYACOR.reapers_engine")
    automation = load("NAYA_AUTOMATION.n10")
    project_engine = load("NAYA_PROJECT_ENGINE.engine")
    orchestration = load("NAYA_ORCHESTRATION.router")

    load("NAYACOR.intention_loop")
    load("NAYACOR.memory_narrative")
    load("NAYACOR.self_diagnostic")
    load("NAYACOR.guardian")

    log("Tous les modules système activés")

    # ===============================
    # PHASE 2 — DECOUVERTE
    # ===============================

    first_execute = project_engine.load_first_execute()
    projects = project_engine.load_projects()

    # ===============================
    # PHASE 3 — LIAISON
    # ===============================

    core.attach_project_engine(project_engine)
    core.attach_reapers(reapers)
    core.attach_orchestration(orchestration)
    core.attach_automation(automation)

    core.register_first_execute(first_execute)
    core.register_projects(projects)

    log("Liaisons complètes établies")

    # ===============================
    # PHASE 4 — CONSCIENCE
    # ===============================

    log("Naya consciente de sa mission (Contrat + Doctrine)")
    log("Reapers reconnu avec sa fonction propre")

    # ===============================
    # PHASE 5 — ACTIVATION EXECUTIVE
    # ===============================

    state = {
        "identity": "NAYA",
        "support": support,
        "sovereign": True,
        "executive": True,
        "autonomous": True,
        "independent_from_pc": True,
        "timestamp": now()
    }

    STATE_FILE.write_text(json.dumps(state, indent=2))
    seal_state(state)

    log("NAYA activée — souveraine — exécutive — autonome")

    # Monitoring + Heartbeat
    attach_core(core)

    threading.Thread(target=start_heartbeat, daemon=True).start()
    threading.Thread(target=MonitoringEngine(core).run, daemon=True).start()

    # Lancement boucle souveraine
    core.start()


# ---------------------------------------------------------
# ENTRYPOINT
# ---------------------------------------------------------

if __name__ == "__main__":
    activate_naya()
