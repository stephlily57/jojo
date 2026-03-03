
import { state } from '../core/ws.js';
export default function() {
  return `<h3>System</h3><pre>` + JSON.stringify(state,null,2) + `</pre>`;
}
