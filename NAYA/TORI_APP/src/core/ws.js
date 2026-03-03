// src/core/ws.js
import observer from "./observer.js";

class WSStore {
  constructor() {
    this.state = observer.getState();
    this.subscribers = new Set();

    observer.subscribe(state => {
      this.state = state;
      this.subscribers.forEach(fn => fn(this.state));
    });
  }

  subscribe(fn) {
    this.subscribers.add(fn);
    fn(this.state);
  }

  getState() {
    return this.state;
  }
}

export const wsStore = new WSStore();
export default wsStore;
