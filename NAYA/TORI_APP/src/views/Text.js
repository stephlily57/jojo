// src/views/Text.js
import wsStore from "../core/ws.js";

export default function TextView(container) {
  wsStore.subscribe(state => {
    const evt = state.lastEvent;
    if (!evt || evt.source !== "command-gateway") return;

    const data = JSON.parse(evt.payload);
    if (data.text) {
      container.innerHTML += `<p>${data.text}</p>`;
    }
  });
}
