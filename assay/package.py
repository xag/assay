"""assay@ — blind trials as checkable data: does the thing survive the world?

The third substrate, beside flight-recorder and bom. flight-recorder answers *what
happened* (tapes at the nondeterminism boundary); bom answers *what must hold* (claims
as data, rules that go red); assay answers *does it survive the world* — confronting
intent-derived, implementation-blind expectations with the running system. The name is
the old gate to capitalization: ore became coin only by passing the assay office, and
nothing becomes capital without surviving a trial.

What hardened into RULES here are the method's four scars, each earned in a real run:

- **an expectation is falsifiable** — or it is a mood. A persona's "it should feel
  nice" produces no verdict; "invite the other parent within two minutes, on the phone
  she actually holds" does.
- **a scenario records what it was permitted to see** — blindness is a property of
  inputs, and an unrecorded input list is unauditable. A contaminated context does not
  announce itself; the record of sight is the only alibi (one run had to regenerate
  every report because a code-aware agent quietly simulated its personas).
- **a stand-in names the source of truth it is built from** — an uninstrumented fake is
  relocated guessing. The rig that earned this rule was built from the vendor's own
  host implementation and found three bugs reasoning never would have; a hand-rolled
  fake would have found three bugs in itself.
- **a verdict carries evidence** — a count of receipts (tapes, screenshots, recorded
  interactions), as a grounding Quantity: `grounded` when the receipts were verified,
  ungrounded while the verdict is provisoire. Falsified verdicts are kept, never
  deleted — a record that forgets what it got wrong will hold it again — and a gate
  (ledger@'s `nothing-unsound-passes-a-gate`) can refuse a release resting on
  provisoire verdicts without a single new rule.

Casting doctrine, carried by the vocabulary: a HUMAN counterparty is simulated by an
agent, explicitly and never silently; a MACHINE counterparty is rigged from the
vendor's reference implementation; a PLATFORM GUARANTEE casts nobody — auditing the
other side of a published spec is not this trial's job.

Requires ledger@ because a trial without a ledger has nowhere to keep its verdicts:
expectations that die become recorded falsifications, carried debts gate releases, and
the evidence discipline is grounding's — one epistemic verb, no re-invention.
"""

from __future__ import annotations

from bom.library import CounterExample, Package
from bom.provenance import Quantity
from bom.tree import KindDef, Node, PackageRef, Rule

VOCABULARY = [
    KindDef(
        kind="persona",
        description="Who the trial casts as the counterparty. A human counterparty is "
        "simulated by an agent — explicitly, with the simulation named, never silently. "
        "A machine counterparty is a stand-in rigged from the vendor's reference "
        "implementation. A platform guarantee (does this client honour the spec it "
        "published) casts nobody: it is not ours to audit, and a persona for it would "
        "be theatre.",
    ),
    KindDef(
        kind="scenario",
        description="One storyline a persona lives, generated BLIND: from the intent "
        "and nothing else — no code, no README, not even the app's name. Its `sight` "
        "children are the complete record of what the generation was permitted to see; "
        "blindness is a property of inputs, and the record is the only alibi. A "
        "scenario embeds its expectations as children.",
    ),
    KindDef(
        kind="sight",
        description="One thing a scenario's generation was shown, by name (the intent "
        "file, and normally nothing else). Complete by construction: anything not "
        "listed here was not seen, and a scenario whose sight list would embarrass it "
        "is not blind.",
    ),
    KindDef(
        kind="expectation",
        description="An observable outcome a persona is owed at a step of their story, "
        "with an effort/time budget where one makes sense. Falsifiable or it is a "
        "mood: every expectation carries at least one `falsifier`. Verdicts accumulate "
        "underneath it as the trials run — including the ones that failed.",
    ),
    KindDef(
        kind="falsifier",
        description="The observation that would fail the expectation above it — stated "
        "so a verdict can be `fail` and not merely 'I did not like it'. The same shape "
        "a craft law's falsifier takes, on purpose: expectations may cite laws, and "
        "both must be violable observably.",
    ),
    KindDef(
        kind="verdict",
        description="The outcome of confronting one expectation once: pass, mitigé, "
        "fail or hors-champ, with the mode that produced it (walkthrough, flight, "
        "rendered-surface reading, monitor). Carries `evidence`: a count of receipts, "
        "grounded when they were verified, ungrounded while the verdict is provisoire. "
        "Verdicts are KEPT, falsified ones above all — deleting a failed verdict is "
        "how a record comes to hold the same belief twice.",
    ),
    KindDef(
        kind="stand-in",
        description="A rigged counterparty for a machine role: the thing the system "
        "under trial talks to, built from the vendor's own implementation and wired to "
        "the real committed bytes. Its `source-of-truth` child names what it is built "
        "from; its `fidelity` param counts the behaviours verified against the real "
        "dependency, grounded once someone exercised them. An uninstrumented fake is "
        "relocated guessing, and a stand-in without a source is exactly that.",
    ),
    KindDef(
        kind="source-of-truth",
        description="What a stand-in is built from: the vendor SDK, the reference "
        "host, the recorded wire behaviour — by name and version/rev, so the claim "
        "'this fake is faithful' has an address a later reader can check.",
    ),
]

RULES = [
    Rule(
        name="an-expectation-is-falsifiable",
        kind="expectation",
        description="An expectation nothing could fail produces no verdict, and a "
        "verdict is the only thing a trial is for. Without this, a trial is a "
        "compliment with a methodology section.",
        expr="len(nodes('falsifier', self)) >= 1",
    ),
    Rule(
        name="a-scenario-records-its-blindness",
        kind="scenario",
        description="Blind is a claim about inputs, and claims about inputs need a "
        "record: a scenario with no sight list cannot show it was not contaminated, "
        "and a contaminated context does not announce itself — the run that taught "
        "this had to regenerate every report.",
        expr="len(nodes('sight', self)) >= 1",
    ),
    Rule(
        name="a-stand-in-names-its-source-of-truth",
        kind="stand-in",
        description="An uninstrumented fake is relocated guessing: a bug in it is "
        "indistinguishable from a bug in the thing under trial. Building from the "
        "vendor's own implementation is what let one rig find three real bugs in one "
        "night instead of three bugs in itself.",
        expr="len(nodes('source-of-truth', self)) >= 1",
    ),
    Rule(
        name="a-verdict-carries-evidence",
        kind="verdict",
        description="A verdict with no receipts is an opinion filed under a stronger "
        "word. The count may be provisoire (ungrounded) while verification is owed — "
        "that is honest and a gate can see it — but a verdict with nothing behind it "
        "at all goes red here.",
        expr="evidence >= 1",
    ),
]


# --- examples: one sound miniature trial, exercising every rule ---------------------
# Generic by decree: assay knows nothing of its consumers, so the trial below is of an
# unnamed thing that keeps appointments — any resemblance to a real app is the point.

def _receipts(count: float, verified: bool, source: str) -> Quantity:
    return Quantity(value=count, unit="receipt", grounded=verified,
                    provenance="verified" if verified else "provisoire", source=source)


EXAMPLES = [
    Node(
        id="the-latecomer",
        kind="persona",
        name="Signs up in a rush, disappears for three weeks, comes back guilty",
        payload={"cast": "simulated by a fresh agent, declared as such",
                 "axes": "disrupted context; error behaviour: returns late"},
        children=[
            Node(
                id="the-return",
                kind="scenario",
                name="Coming back after three silent weeks must cost nothing",
                children=[
                    Node(id="saw-the-intent", kind="sight",
                         name="the intent file, inline, and nothing else",
                         payload={"note": "no code, no README, no app name; the working "
                                          "directory name was declared non-information"}),
                    Node(
                        id="no-guilt-pile",
                        kind="expectation",
                        name="Returning shows what to do next — never a pile of what was missed",
                        payload={"budget": "understood within one screen, no scrolling"},
                        children=[
                            Node(id="pile-observed", kind="falsifier",
                                 name="Any enumeration of missed items on the return surface",
                                 payload={"claim": "one list, count or streak-shame on "
                                                   "first contact after absence fails this"}),
                            Node(id="return-verdict", kind="verdict",
                                 name="pass — rendered return surface shows next step only",
                                 payload={"outcome": "pass",
                                          "mode": "rendered-surface reading"},
                                 params={"evidence": _receipts(
                                     2, True, "two rendered zero-state dumps, read")}),
                        ],
                    ),
                ],
            ),
        ],
    ),
    Node(
        id="the-calendar-peer",
        kind="stand-in",
        name="The calendar service the system syncs against, rigged not guessed",
        params={"fidelity": Quantity(
            value=3, unit="behaviour", grounded=True, provenance="exercised",
            source="three sync behaviours replayed against the vendor SDK's own client")},
        children=[
            Node(id="vendor-sdk-client", kind="source-of-truth",
                 name="the vendor's published client library, at the pinned version",
                 payload={"address": "the reference implementation the wire behaviour "
                                     "was verified against, by name and version"}),
        ],
    ),
]


COUNTER_EXAMPLES = [
    CounterExample(
        rule="an-expectation-is-falsifiable",
        because="a mood wearing an expectation's kind",
        node=Node(id="feels-nice", kind="expectation",
                  name="It should feel pleasant to come back"),
    ),
    CounterExample(
        rule="a-scenario-records-its-blindness",
        because="a scenario that cannot show what it was generated from",
        node=Node(id="trust-me-it-was-blind", kind="scenario",
                  name="A storyline with no record of what its author saw"),
    ),
    CounterExample(
        rule="a-stand-in-names-its-source-of-truth",
        because="an uninstrumented fake — relocated guessing",
        node=Node(id="hand-rolled-stub", kind="stand-in",
                  name="A calendar stub written from memory of the docs",
                  params={"fidelity": Quantity(
                      value=0, unit="behaviour", grounded=False,
                      provenance="asserted", source="nobody checked it against anything")}),
    ),
    CounterExample(
        rule="a-verdict-carries-evidence",
        because="an opinion filed under a stronger word",
        node=Node(id="looked-fine-to-me", kind="verdict",
                  name="pass, probably",
                  payload={"outcome": "pass", "mode": "vibes"}),
    ),
]


ASSAY_PACKAGE = Package(
    name="assay",
    version="0.1.0",
    description="Blind trials as checkable data: intent-derived, implementation-blind "
                "expectations confronted with the running system. Personas cast the "
                "counterparty (simulated humans, rigged machines, nobody for platform "
                "guarantees); scenarios record what they were permitted to see; "
                "expectations carry their falsifiers; verdicts carry their receipts "
                "and are kept, falsified ones above all. The gate that refuses a "
                "release resting on provisoire verdicts is ledger@'s — a trial "
                "without a ledger has nowhere to keep what it learned.",
    publisher="xag/assay",
    requires=[PackageRef(name="ledger", version="0.1.0")],  # exact, by doctrine
    vocabulary=VOCABULARY,
    rules=RULES,
    examples=EXAMPLES,
    counter_examples=COUNTER_EXAMPLES,
)


def build() -> Package:
    return ASSAY_PACKAGE
