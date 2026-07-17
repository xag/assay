/* The other half of the picture: an MCP App HOST, so the widget can be run rather than
 * assumed.
 *
 * The temptation was to say "the in-client run needs a human with a phone". That is the
 * wrong instinct. The client is not a person — it is a DOM, an iframe, a postMessage
 * bridge and a JSON-RPC peer, and every one of those is more faithfully reproducible than
 * a human. Punting it to a human is not caution, it is deciding not to look.
 *
 * The host here is NOT hand-rolled — a hand-rolled fake is just relocated guessing, and a
 * bug in it would be indistinguishable from a bug in the widget. It is `AppBridge`, the
 * host implementation the MCP Apps SDK itself ships, wired over a postMessage channel to
 * the real committed bundle (webapp/mcp-app.html — the exact bytes the server serves).
 *
 * So this harness answers the question that actually matters, and it is not "does wasm
 * work in a browser" (there is no wasm here, and platform guarantees are not ours to
 * audit). It is: given a tool result carrying a compiled survey, does the shipped widget
 * SOLVE it, WRITE the polygons back through tools/call, and TELL the model what it found?
 *
 *   node host-harness.mjs < payload.json   ->  {toolCalls: [...], modelContext: [...]}
 */

import { readFileSync } from "node:fs";
import { resolve } from "node:path";

import { JSDOM } from "jsdom";
import { AppBridge } from "@modelcontextprotocol/ext-apps/app-bridge";

// The SDK narrates every frame with console.debug/log, straight onto stdout — where our
// one and only JSON answer goes. Silence the narration, keep the errors.
console.debug = () => {};
console.log = () => {};

// The bundle under trial is an argument, not a constant: this rig is generic over any
// MCP-App widget. `node host-harness.mjs <bundle.html> < payload.json`
const BUNDLE = resolve(process.cwd(), process.argv[2] ?? "");
if (!process.argv[2]) {
  process.stderr.write("usage: node host-harness.mjs <bundle.html> < payload.json\n");
  process.exit(2);
}

const chunks = [];
for await (const c of process.stdin) chunks.push(c);
const structuredContent = JSON.parse(Buffer.concat(chunks).toString("utf8"));

// --- the shipped page, in a DOM -------------------------------------------------------
const html = readFileSync(BUNDLE, "utf8");
// The bundle is a module script only because of its top-level `await app.connect(...)`;
// esbuild already inlined every import, so there is nothing left to resolve. jsdom does
// not execute module scripts, so run the SAME bytes as a classic script inside an async
// IIFE. The code is unchanged — only its wrapper is.
const code = html.match(/<script type="module">([\s\S]*?)<\/script>/)[1];
// A replacer FUNCTION, not a string: `String.replace` reads `$&`, `$'` and `` $` `` as
// substitution patterns, and 400 kB of minified JS is full of `$`. A string replacement
// here silently corrupts the bundle into a SyntaxError. (build.mjs already knows this.)
// The leading newline matters too: the bundle can end in a `//` comment, which would
// otherwise swallow the closing paren.
const page = html.replace(/<script type="module">[\s\S]*?<\/script>/, () =>
  `<script>(async () => {
${code}
})().catch((e) => { window.__boom = String(e); });</script>`);

// --- the host side of the bridge ------------------------------------------------------
//
// The widget builds `new PostMessageTransport()`, which captures `window.parent` AT
// CONSTRUCTION and posts to it. Two things follow, and both bit:
//
//  - In jsdom a top-level window IS its own `parent`, so without this the widget posts to
//    itself, answers its own ui/initialize with "Method not found", and hangs. The parent
//    must therefore exist BEFORE the page's script runs — hence `beforeParse`, not an
//    assignment afterwards.
//  - The script runs during JSDOM construction, before we can connect the bridge, so the
//    widget's first messages would be dropped on the floor. Buffer them.
let win;
const inbox = [];
const hostTransport = {
  onmessage: null, onclose: null, onerror: null,
  async start() {},
  async send(msg) {
    win.dispatchEvent(new win.MessageEvent("message", { data: msg }));
  },
  async close() {},
};
const deliver = (msg) => {
  if (hostTransport.onmessage) hostTransport.onmessage(msg);
  else inbox.push(msg);
};

const dom = new JSDOM(page, {
  runScripts: "dangerously",
  pretendToBeVisual: true,
  beforeParse(window) {
    win = window;
    Object.defineProperty(window, "parent", {
      configurable: true,
      value: { postMessage: (msg) => deliver(msg) },
    });
    // jsdom has no ResizeObserver, and the SDK's autoResize builds one on connect. Absent
    // it, the widget dies immediately after the handshake — which is a fact about jsdom,
    // not about the widget, so shim it rather than "fix" the widget around it.
    window.ResizeObserver = class {
      observe() {} unobserve() {} disconnect() {}
    };
  },
});

const toolCalls = [];
const modelContext = [];

const bridge = new AppBridge(
  null,                                        // no upstream MCP client; we ARE the server
  { name: "harness", version: "1.0.0" },
  { tools: { listChanged: true } },
  { hostContext: { displayMode: "inline", theme: "light" } },
);

// The two things the widget is supposed to do with what it computed.
bridge.oncalltool = async (params) => {
  toolCalls.push(params);
  return { content: [{ type: "text", text: "ok" }] };   // as the server would answer
};
bridge.onupdatemodelcontext = async (params) => {
  modelContext.push(params);
  return {};
};

await bridge.connect(hostTransport);
for (const msg of inbox.splice(0)) hostTransport.onmessage?.(msg);   // whatever we missed

// Wait for the widget's ui/initialize handshake to land before pushing it a tool result —
// otherwise the notification races the connect and the widget never sees it.
const started = Date.now();
while (bridge.getAppVersion() === undefined) {
  if (Date.now() - started > 10_000) throw new Error("the widget never completed ui/initialize");
  await new Promise((r) => setTimeout(r, 10));
}

bridge.sendToolInput({});
bridge.sendToolResult({ structuredContent });

// The widget solves synchronously, but writes back over async JSON-RPC. Settle when the
// model context has arrived (the widget's last act) or we run out of patience.
const deadline = Date.now() + 120_000;
while (modelContext.length === 0 && Date.now() < deadline) {
  if (win.__boom) break;
  await new Promise((r) => setTimeout(r, 25));
}

process.stdout.write(JSON.stringify({
  error: win.__boom ?? null,
  toolCalls,
  modelContext,
  text: win.document.getElementById("root")?.textContent ?? "",
}));
process.exit(0);
