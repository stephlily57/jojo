// src/core/sources.js

export const SOURCES = {
    // ===== INTERNE NAYA =====
    "local-system": {
        id: "local-system",
        role: "naya-system",
        url: "ws://127.0.0.1:8765",
        status: "DISCONNECTED",
        lastSeen: null,
        lastMessage: null
    },

    "local-ui": {
        id: "local-ui",
        role: "app-shell",
        url: "ws://127.0.0.1:8766",
        status: "DISCONNECTED",
        lastSeen: null,
        lastMessage: null
    },

    "cloudrun": {
        id: "cloudrun",
        role: "external-runtime",
        url: "wss://naya-cloudrun-ws-735034661802.europe-west1.run.app/ws",
        status: "DISCONNECTED",
        lastSeen: null,
        lastMessage: null
    },

    // ===== EXTERNE (OBSERVATION / COMMANDE) =====
    "event-stream": {
        id: "event-stream",
        role: "external-events",
        url: "ws://127.0.0.1:8765",
        status: "DISCONNECTED",
        lastSeen: null,
        lastMessage: null
    },

    "observation-bus": {
        id: "observation-bus",
        role: "system-state",
        url: "ws://127.0.0.1:8899",
        status: "DISCONNECTED",
        lastSeen: null,
        lastMessage: null
    },

    "command-gateway": {
        id: "command-gateway",
        role: "intent-gateway",
        url: "ws://127.0.0.1:8766",
        status: "DISCONNECTED",
        lastSeen: null,
        lastMessage: null
    }
};
