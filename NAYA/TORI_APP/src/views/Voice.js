// src/views/Voice.js
import wsStore from "../core/ws.js";

export default function VoiceView() {
  wsStore.subscribe(state => {
    const evt = state.lastEvent;
    if (!evt || evt.source !== "command-gateway") return;

    const data = JSON.parse(evt.payload);
    if (data.voice === true && data.text) {
      speechSynthesis.speak(new SpeechSynthesisUtterance(data.text));
    }
  });
}
