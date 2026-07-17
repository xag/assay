# mcp-app-host — the first rig

A stand-in for an MCP-App **host**: the DOM, iframe, postMessage bridge and JSON-RPC
peer a widget actually talks to. Built from `AppBridge` — the host implementation the
MCP Apps SDK itself ships — wired over a postMessage channel to the real committed
bundle. **Not hand-rolled**: an uninstrumented fake is relocated guessing, and a bug in
it would be indistinguishable from a bug in the widget.

    npm install
    node host-harness.mjs <path/to/mcp-app.html> < payload.json
    # -> {error, toolCalls, modelContext, text}

`payload.json` is the `structuredContent` of the tool result the host would push at the
widget. The answer records what the widget did with it: the tools it called back, the
model context it published, the text it rendered, and any exception.

## The jsdom traps (each hid a real bug on first contact)

1. **`window.parent === window`.** A top-level jsdom window is its own parent, so a
   widget that captures `window.parent` at construction posts to *itself*, answers its
   own `ui/initialize` with "Method not found", and hangs. The parent must exist
   **before the page's script runs** — hence `beforeParse`, never an assignment after.
2. **`String.replace` `$`-substitution.** Rewrapping the module script with a string
   replacement silently corrupts a 400 kB minified bundle: `$&`, `` $` `` and `$'` are
   substitution patterns, and minified JS is full of `$`. Use a **replacer function**.
   (The leading newline in the wrapper matters too — the bundle can end in a `//`
   comment that would swallow the closing paren.)
3. **No `ResizeObserver`.** The SDK's autoResize builds one on connect; absent it, the
   widget dies immediately *after* a successful handshake. A fact about jsdom, not the
   widget — shim it, don't "fix" the widget around it.

Also: the SDK narrates every frame via `console.debug`/`console.log` onto stdout, where
the one JSON answer goes — silence the narration, keep the errors. And the widget's
first messages race the bridge connect: buffer them.

## Provenance

Proven in `xag/home@2a9713e` against the committed home widget, where it found three of
the bugs above in one night. The generalized copy (bundle path as an argument) was then
driven from this repo against that same real committed bundle, and the run is the
discharge of the `the-rig-has-not-run-since-the-port` debt in `assay/tree.py`: the node
stays, grounded. The committed receipts (`example-payload.json`, `result.json`) are a
**synthetic** twin — an invented four-room flat compiled through the home app's own
`layout_payload`, driven through this harness against the real bundle: 4 `tree_set`
write-backs, model context published, no error. Synthetic on purpose: a receipt is
evidence of the *rig*, and it must not carry anyone's actual floorplan to do that job.
