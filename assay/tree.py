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
    ]
    return quern
