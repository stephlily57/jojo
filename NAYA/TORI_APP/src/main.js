
import { connectWS } from './core/ws.js';
import { views } from './views/index.js';

const nav = document.getElementById("nav");
const view = document.getElementById("view");
const status = document.getElementById("status");

Object.keys(views).forEach(k => {
  const b = document.createElement("button");
  b.textContent = k;
  b.onclick = () => view.innerHTML = views[k]();
  nav.appendChild(b);
});

connectWS(status);
view.innerHTML = views[Object.keys(views)[0]]();
