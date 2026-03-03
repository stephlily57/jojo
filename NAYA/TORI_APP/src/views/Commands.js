// src/views/Commands.js
const WS_URL = "ws://127.0.0.1:8766";

export function sendIntent(text) {
  const ws = new WebSocket(WS_URL);

  ws.onopen = () => {
    ws.send(JSON.stringify({
      intent: "USER_MESSAGE",
      text,
      timestamp: Date.now()
    }));
  };
}
