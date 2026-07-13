"""assay's own design ledger. The trial substrate takes the medicine it prescribes:
its rig carries a debt, the debt gates the rig's trustworthiness, and the gate is red
until the work is done — never until the file is edited."""

from __future__ import annotations

import os
from pathlib import Path

import bom.grounding  # noqa: F401 -- the natives; the packages arrive by pin
from bom import Bom, Node, Quantity
from bom.library import consume

_ROOT = Path(__file__).resolve().parents[1]


def build() -> Bom:
    lib, refs = consume(_ROOT, os.environ.get("BOM_REGISTRY",
                                              _ROOT.parent / "bom-registry"))
    bom = Bom(packages=[next(r for r in refs if r.name == "ledger")])
    bom = lib.effective(bom)

    bom.root.children = [
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
                        "xag/bom#19 (the channel assay@ travels on).",
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
                Node(id="alt-fourth-substrate-in-bom", kind="alternative",
                     name="Author assay@ inside bom's source like ledger@ once was",
                     payload={"why": "Rejected by discharge: the exact siting bom's own "
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
    return bom
