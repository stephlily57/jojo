import { startVoice } from './voice.js';
const box = document.getElementById("state");
const ws = new WebSocket("ws://192.168.1.42:8765");
ws.onmessage = e => box.textContent = e.data;
window.startVoice = startVoice;
