"""assay's own design ledger. The trial substrate takes the medicine it prescribes:
its rig carries a debt, the debt gates the rig's trustworthiness, and the gate is red
until the work is done — never until the file is edited."""

from __future__ import annotations

import os
from pathlib import Path

import quern.grounding  # noqa: F401 -- the natives; the packages arrive by pin
from quern import Quern, Node, Quantity
from quern.library import consume

_ROOT = Path(__file__).resolve().parents[1]


def build() -> Quern:
    lib, refs = consume(_ROOT, os.environ.get("QUERN_REGISTRY",
                                              _ROOT.parent / "quern-registry"))
    quern = Quern(packages=[next(r for r in refs if r.name == "ledger")])
    quern = lib.effective(quern)

    quern.root.children = [
        Node(
            id="extracted-at-third-use",
            kind="decision",
            name="blind-usability generalizes into assay at its third use, not before",
            payload={
                "rationale":
                    "defi-vacances designed the practice, chores repeated its shape and "
                    "added the craft dimension, home forced the generalization by casting "
                    "a MACHINE as the counterparty — the case that proved the method was "
                    "never about usability. Three uses is where a pattern has earned an "
                    "abstraction; earlier is speculation, later is copy-paste drift "
                    "(invest re-authored the ledger's kinds, home rolled its own — the "
                    "fleet has paid for late extraction before).",
                "note": "Proposed and argued in xag/claude-plugins#1; unblocked by "
                        "xag/quern#19 (the channel assay@ travels on).",
            },
            children=[
                Node(id="alt-stay-a-skill", kind="alternative",
                     name="Keep it a claude-plugins skill and never a package",
                     payload={"why": "A skill is advice to a mind, read at task time — "
                                     "rung 2 of the hardening ladder. The method's "
                                     "hard-won lessons (falsifiability, blindness, "
                                     "stand-in fidelity, receipts) are claims that can "
                                     "go RED, and prose cannot fire. The skill stays, "
                                     "but as the procedure half only."}),
                Node(id="alt-fourth-substrate-in-quern", kind="alternative",
                     name="Author assay@ inside quern's source like ledger@ once was",
                     payload={"why": "Rejected by discharge: the exact siting quern's own "
                                     "ledger.py confessed to and #19 dissolved. New "
                                     "packages start in authoring repos now."}),
            ],
        ),
        Node(
            id="named-assay",
            kind="decision",
            name="The name is assay: the standardized blind trial that gates capitalization",
            payload={
                "rationale":
                    "Ore became coin only by passing the assay office — nothing becomes "
                    "capital without surviving a trial, which is this substrate's whole "
                    "claim. It verbs cleanly (assay the funnel, assay the widget, the "
                    "chores assay). 'blind-usability' is wrong for funnels and machine "
                    "hosts, and extraction is the one moment renaming is allowed.",
            },
            children=[
                Node(id="alt-crucible", kind="alternative", name="crucible",
                     payload={"why": "Evokes destruction-testing, not measurement; an "
                                     "assay tells you what the thing is made of."}),
                Node(id="alt-bench", kind="alternative", name="bench",
                     payload={"why": "Collides with benchmark and with the furniture "
                                     "domain the fleet already has."}),
                Node(id="alt-keep-blind-usability", kind="alternative",
                     name="keep blind-usability",
                     payload={"why": "Names one use case of three; a machine host has "
                                     "no usability and a funnel has no screens."}),
            ],
        ),
        Node(
            id="proof-scopes-by-kind",
            kind="decision",
            name="A verdict decided by proof is its own kind (proof-verdict): rule "
                 "scoping rides the grammar's kind axis, never payload introspection",
            payload={
                "rationale":
                    "a-proof-names-its-model must bind proof-decided verdicts and no "
                    "others, and the rule grammar cannot read payload.mode — by design: "
                    "payload is testimony, prose-shaped and free; params are the "
                    "checkable ledger. The kind axis is the grammar's own scoping "
                    "mechanism and every rule in this package already uses it, so a "
                    "proof-decided verdict becomes a kind. It is honestly a different "
                    "animal: different premise (a pinned model), different receipt (a "
                    "content-addressed artifact), one obligation no executed verdict "
                    "has (name your model). The cost is that a reader collecting all "
                    "verdicts under an expectation asks for two kinds — accepted, and "
                    "cheap next to either alternative.",
            },
            children=[
                Node(id="alt-mode-as-a-param", kind="alternative",
                     name="Make mode a param so exprs can read it",
                     payload={"why": "Params are Quantities — grounding apparatus, "
                                     "provenance, units. A mode is a categorical, and "
                                     "encoding one as a number to make it readable "
                                     "would spend the epistemic machinery on a "
                                     "dispatch problem."}),
                Node(id="alt-payload-reading-native", kind="alternative",
                     name="A small native that reads payload.mode",
                     payload={"why": "Dissolves the boundary the vocabulary rests on: "
                                     "the day rules read payload, every prose field "
                                     "becomes load-bearing and testimony can no longer "
                                     "be edited for clarity without re-verifying the "
                                     "world. Machinery for a question the kind system "
                                     "already answers."}),
            ],
        ),
        Node(
            id="proof-is-a-mode-of-the-method",
            kind="decision",
            name="Proof enters the skill as the first routing stop and a design-time "
                 "confrontation — inside the method, never a practice beside it",
            payload={
                "rationale":
                    "Step 4 now examines every falsifier for an expr before any mode is "
                    "chosen, and a model-carrying app gets its storylines compiled "
                    "against the model before the realization exists. Kept inside the "
                    "method, proof inherits its disciplines for free: verdicts kept "
                    "(falsified ones above all), the held-out set, blindness as a property of "
                    "inputs (the orchestrator owns the compilation), and the critic — "
                    "whose brief grows the one question only the method can ask: is the "
                    "model's abstraction of this promise the promise the persona was "
                    "owed? The routing principle is stated where routing happens: proof "
                    "displaces execution, never judgment.",
            },
            children=[
                Node(id="alt-proof-as-separate-practice", kind="alternative",
                     name="Keep proof outside the method as a separate practice",
                     payload={"why": "Two verdict streams over one expectation with no "
                                     "shared ledger: proof-mode PASSes would never meet "
                                     "the critic, the model would never meet the "
                                     "personas, and un-mechanized falsifiers would be "
                                     "nobody's debt. The founding scar is exactly a "
                                     "green channel nobody reads running beside the "
                                     "channel that reads — a separate proof practice "
                                     "would build a second one."}),
            ],
        ),
        Node(
            id="rigs-catch-what-reasoning-cannot",
            kind="hypothesis",
            name="Casting machine counterparties from reference implementations catches "
                 "bugs reasoning cannot",
            payload={"held_because":
                     "Already evidenced once: the MCP-App host rig (built from the SDK's "
                     "own AppBridge, not a hand-rolled fake) found three bugs in one "
                     "night that review had not — jsdom's window.parent === window, "
                     "String.replace $-substitution corrupting a 400 kB bundle, missing "
                     "ResizeObserver. One night is evidence, not proof."},
            children=[
                Node(id="rigs-stop-paying", kind="falsification",
                     name="Rig runs stop finding what review missed",
                     payload={"claim": "If the next three machine-counterparty "
                                       "confrontations surface no defect that reasoning "
                                       "or review had not already found, the rig cost "
                                       "is overhead and this belief is dead.",
                              "cadence": "per machine-counterparty confrontation"}),
            ],
        ),
        Node(
            id="the-rig-has-not-run-since-the-port",
            kind="debt",
            name="mcp-app-host was verified in xag/home, then generalized — and the "
                 "generalized copy had never run. Discharged the same day: the node "
                 "stays, because the debt is part of the record, not something to "
                 "delete once paid",
            params={"behaviours": Quantity(
                value=3, unit="behaviour", grounded=True, provenance="exercised",
                source="2026-07-14: the ported rig drove the real committed bundle "
                       "from its origin repo (rev 2a9713e's widget) with a payload "
                       "built by that app's own evidence code — 7 tree_set write-backs, "
                       "model context published, no error. Receipts committed beside "
                       "the rig: example-payload.json, result.json")},
            children=[
                Node(id="run-it-from-here", kind="discharge",
                     name="Drive a real committed bundle through the rig from this repo "
                          "and read the answer",
                     payload={"who": "anyone with a bundle and ten minutes",
                              "how": "npm install in rigs/mcp-app-host, then "
                                     "node host-harness.mjs <bundle.html> < payload.json",
                              "done": "2026-07-14"}),
            ],
        ),
        Node(
            id="a-rig-is-trusted",
            kind="gate",
            name="No rig is offered as a stand-in while its own port is unverified",
            links={"admits": ["the-rig-has-not-run-since-the-port"]},
        ),

        Node(
            id="the-cases-name-their-apps",
            kind="decision",
            name="The worked cases keep their apps' names; the rig receipts go synthetic "
                 "— the per-case exposure decisions of the public flip (#4)",
            payload={
                "rationale":
                    "Taken case by case, as the flip required. defi-vacances, chores, "
                    "home, korean-gpt-coach: all the author's own apps, and naming your "
                    "own apps in your own method repo is the same call craft-laws "
                    "journaled for its sightings — the cases are the evidence, and an "
                    "anonymous case is an anecdote. Each case's text was re-read: what "
                    "each exposes is the method's own story (a defect, a mode it forced, "
                    "a generalization it demanded), no member name, no screenshot, no "
                    "verbatim private string beyond UI copy already public in "
                    "craft-laws' sightings. KEPT, all four.\n\n"
                    "The rig receipts failed the same reading and were replaced: "
                    "example-payload.json carried a real home's compiled floorplan — "
                    "room dimensions, photo-evidence references, a published "
                    "gross-internal figure traceable to a listing. A receipt is "
                    "evidence of the RIG, not of anyone's flat, so the payload is now a "
                    "wholly invented four-room twin compiled through the home app's own "
                    "layout_payload and re-driven through the harness against the real "
                    "committed bundle (4 tree_set write-backs, model context published, "
                    "no error). The rig's provenance story is intact — the port "
                    "verification and the three bugs stand as history in xag/home — and "
                    "the committed evidence now exposes nothing.",
                "consequence":
                    "The bar for every future case and receipt: the defect is the "
                    "content, the person never; a committed artifact must be synthetic "
                    "or it does not enter. History note: the pre-flip history still "
                    "contains the earlier real-floorplan receipts; the flip decision "
                    "must weigh that (fresh-root or history rewrite) — recorded here so "
                    "whoever takes the go/no-go sees it.",
            },
            children=[
                Node(id="alt-genericize-the-cases", kind="alternative",
                     name="Strip the app names from docs/CASES.md",
                     payload={"why":
                              "Destroys the evidentiary value that is the entire point "
                              "of a worked case, and protects nothing: the apps' own "
                              "stories are the estate's public narrative already."}),
                Node(id="alt-keep-the-real-receipts", kind="alternative",
                     name="Keep the real-floorplan receipts; they are only rectangles",
                     payload={"why":
                              "They are somebody's home, with photo references and a "
                              "listing-traceable area figure, committed forever in a "
                              "public repo to prove a point synthetic data proves "
                              "equally well. The cheapest genericization in the whole "
                              "flip, and the clearest."}),
            ],
        ),

        Node(
            id="the-vocabulary-speaks-english",
            kind="decision",
            name="The working vocabulary is English from 0.3.0: a generic library must "
                 "not make an adopter learn French to read a verdict",
            payload={
                "rationale":
                    "The method's terms were born in defi-vacances — a French app, "
                    "trialed in French — and travelled into the generic package as its "
                    "voice: mitigé, hors-champ, provisoire, RÉSERVE, ATTENTE:, "
                    "trouvailles. The charter (assay-office#4) named this a pre-pull "
                    "debt: cheap while the audience is zero, expensive after the first "
                    "outside pin. Paid in 0.3.0, before any external adopter: mixed, "
                    "out-of-scope, provisional, the held-out set, EXPECT:, findings "
                    "(with unverified and 'not confronted' in the skill). 0.2.0 stays "
                    "immutable; 0.3.0 changes no kind, rule or example — only the "
                    "words — and the consumers repinned the same day. The French that "
                    "STAYS is content under trial, not method vocabulary: the "
                    "localisation case's defects are French strings, and the worked "
                    "case that Englished a French joke would be destroying its own "
                    "evidence.",
                "consequence":
                    "provenance='provisoire' becomes provenance='provisional' — a "
                    "machine-read value, so chores' verdicts migrate with the repin, "
                    "not just its prose. CASES.md keeps one clause of origin: the "
                    "vocabulary was born in French, with the practice, and Englished "
                    "here.",
            },
            children=[
                Node(id="alt-french-as-identity", kind="alternative",
                     name="Keep the French as the method's identity, glossed once",
                     payload={"why":
                              "The README's own old line — and a toll, not a voice: "
                              "identity that taxes every stranger at their first "
                              "verdict table selects for readers who already know us, "
                              "the opposite of what a generic library is for. The "
                              "estate's rule is coined vocabulary only after it has "
                              "been seen working; these words never earned that."}),
                Node(id="alt-gloss-harder", kind="alternative",
                     name="Keep the terms, gloss at every first use",
                     payload={"why":
                              "Tried — phase 4's readiness pass added the glosses — "
                              "and the toll survived it: every table, receipt and "
                              "report still reads foreign first, and a gloss is a "
                              "patch on a word that needed replacing."}),
            ],
        ),

        Node(
            id="the-flip-fresh-roots",
            kind="decision",
            name="The public history begins at the flip: fresh root, because the old "
                 "history holds a real home's floorplan receipts",
            payload={
                "rationale":
                    "the-cases-name-their-apps replaced the rig receipts with a "
                    "synthetic twin and recorded that pre-flip history still held the "
                    "real ones — room dimensions, photo references, a listing-traceable "
                    "area figure. A targeted history rewrite would have to prove it "
                    "caught every blob the floorplan ever touched, and a missed one is "
                    "somebody's home in a public repo; a fresh root removes the whole "
                    "class in one commit. quern kept its scrubbed history because its "
                    "history could be proven clean and carries provenance; this repo's "
                    "private history proves nothing a stranger needs, and the journal "
                    "carries what mattered.",
                "consequence":
                    "Pre-flip provenance (the rig's port verification, the three bugs) "
                    "lives on in the private repos that produced it and in this "
                    "journal's own account; public archaeology starts today.",
            },
            children=[
                Node(id="alt-rewrite-history", kind="alternative",
                     name="Filter the floorplan blobs out of history and keep the rest",
                     payload={"why":
                              "The burden of proving the rewrite complete lands on "
                              "exactly the artifact class (committed evidence) the flip "
                              "exists to protect; the value preserved is history no "
                              "public reader needs."}),
                Node(id="alt-flip-as-is", kind="alternative",
                     name="Flip with history intact",
                     payload={"why":
                              "Publishes a real home's floorplan. The one outcome the "
                              "stop-and-surface conditions exist to prevent."}),
            ],
        ),
    ]
    return quern
