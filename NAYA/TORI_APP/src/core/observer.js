// src/core/observer.js
import { SOURCES } from "./sources.js";

class Observer {
  constructor() {
    this.state = {
      sources: {},
      lastEvent: null,
      updatedAt: null
    };
    this.listeners = new Set();

    Object.values(SOURCES).forEach(s => {
      this.state.sources[s.id] = {
        status: "DISCONNECTED",
        lastSeen: null,
        lastMessage: null
      };
    });
  }

  start() {
    Object.values(SOURCES).forEach(src => this._connect(src));
  }

  subscribe(fn) {
    this.listeners.add(fn);
    fn(this.getState());
  }

  getState() {
    return JSON.parse(JSON.stringify(this.state));
  }

  _emit() {
    this.state.updatedAt = Date.now();
    this.listeners.forEach(fn => fn(this.getState()));
  }

  _connect(source) {
    const ws = new WebSocket(source.url);
    const id = source.id;

    this.state.sources[id].status = "CONNECTING";
    this._emit();

    ws.onopen = () => {
      this.state.sources[id].status = "CONNECTED";
      this.state.sources[id].lastSeen = Date.now();
      this._emit();
    };

    ws.onmessage = e => {
      this.state.sources[id].lastSeen = Date.now();
      this.state.sources[id].lastMessage = e.data;
      this.state.lastEvent = {
        source: id,
        payload: e.data,
        timestamp: Date.now()
      };
      this._emit();
    };

    ws.onerror = () => {
      this.state.sources[id].status = "ERROR";
      this._emit();
    };

    ws.onclose = () => {
      this.state.sources[id].status = "DISCONNECTED";
      this._emit();
      setTimeout(() => this._connect(source), 3000);
    };
  }
}

export const observer = new Observer();
export default observer;
