"""assay@ publishes with its proofs, and the vocabulary's discipline actually binds."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

import quern.grounding  # noqa: F401 -- ledger@'s proofs re-run at sync and call these
from quern import Quern, Library, run_rules
from quern.library import consume, package_digest, sync

from assay.package import ASSAY_PACKAGE

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def library(tmp_path):
    lib = Library(tmp_path)
    cache, refs = consume(ROOT, os.environ.get("QUERN_REGISTRY",
                                               ROOT.parent / "quern-registry"))
    sync(cache, lib, [r for r in refs if r.name in ("ledger", "grounding")])
    return lib


def test_assay_publishes_with_its_proofs(library):
    log = library.publish(ASSAY_PACKAGE, {})
    assert any("6 rule(s) exercised" in line for line in log)
    assert any("refuted by their counter-example" in line for line in log)


def test_the_authored_package_is_the_published_artifact():
    _, refs = consume(ROOT, os.environ.get("QUERN_REGISTRY",
                                           ROOT.parent / "quern-registry"))
    pinned = next(r for r in refs if r.name == "assay")
    assert package_digest(ASSAY_PACKAGE) == pinned.sha256


def test_a_provisional_verdict_is_visible_to_a_gate(library):
    """The receipts discipline composes with ledger@'s gate without a single new rule:
    a verdict whose evidence is ungrounded (provisional) cannot pass a release gate that
    admits it — exactly as a debt cannot."""
    from quern import Node, Quantity
    library.publish(ASSAY_PACKAGE, {})
    tree = Quern(packages=[{"name": "assay", "version": ASSAY_PACKAGE.version}])
    tree = library.effective(tree)
    tree.root.children = [
        Node(id="v", kind="verdict", name="pass, pending receipt verification",
             params={"evidence": Quantity(value=1, unit="receipt", grounded=False,
                                          provenance="provisional")}),
        Node(id="release", kind="gate", name="ship it",
             links={"admits": ["v"]}),
    ]
    results = {r.rule: r.ok for r in run_rules(tree)}
    assert results["a-verdict-carries-evidence"] is True   # it HAS a receipt...
    assert results["nothing-unsound-passes-a-gate"] is False  # ...but nobody verified it


def test_an_owed_proof_artifact_is_refused_at_the_gate(library):
    """The proof mode inherits the provisional discipline unchanged: a proof-verdict
    whose artifact is owed carries ungrounded evidence, and the same gate refuses the
    release it would have vouched for. The proof rules themselves stay green — naming
    your model and carrying evidence are satisfied; it is the SOUNDNESS the gate wants."""
    from quern import Node, Quantity
    library.publish(ASSAY_PACKAGE, {})
    tree = Quern(packages=[{"name": "assay", "version": ASSAY_PACKAGE.version}])
    tree = library.effective(tree)
    tree.root.children = [
        Node(id="pv", kind="proof-verdict", name="pass, artifact owed",
             params={"evidence": Quantity(value=1, unit="artifact", grounded=False,
                                          provenance="provisional")},
             children=[Node(id="m", kind="model-ref", name="the model, pinned",
                            payload={"name": "some-model", "version": "0.1.0",
                                     "sha256": "pinned", "artifact": "owed"})]),
        Node(id="release", kind="gate", name="ship it",
             links={"admits": ["pv"]}),
    ]
    results = {r.rule: r.ok for r in run_rules(tree)}
    assert results["a-proof-names-its-model"] is True
    assert results["a-proof-verdict-carries-evidence"] is True
    assert results["nothing-unsound-passes-a-gate"] is False


def test_the_graduated_expr_is_grammar_it_can_fire_in():
    """The flagship falsifier's expr must compile and evaluate in the rule grammar it
    claims — an expr that cannot fire is prose wearing mechanization's clothes. Fired
    exactly the way a confrontation will fire it: as a rule bound to `scenario`,
    evaluated over an imported-scenario-shaped subtree. Both directions: the pile
    shown before the next action fires it; the next action leading does not."""
    from quern import Node, Quern, Rule, run_rules

    persona = ASSAY_PACKAGE.examples[0]
    falsifier = persona.children[0].children[1].children[0]
    assert falsifier.kind == "falsifier"

    def fires(children) -> bool:
        q = Quern(packages=[])
        q.rules = [Rule(name="the-falsifier", kind="scenario",
                        description="pile-observed, firing as it will in anger",
                        expr=falsifier.payload["expr"])]
        q.root.children = [Node(id="s", kind="scenario", name="a return",
                                children=children)]
        (result,) = run_rules(q)
        assert result.detail is None or result.detail == "", result.detail
        return result.ok

    assert fires([
        Node(id="r", kind="return-after-absence"),
        Node(id="pile", kind="missed-pile-shown"),
        Node(id="next", kind="next-action-shown"),
    ]) is True, "the pile precedes the next action: the falsifier must fire"
    assert fires([
        Node(id="r", kind="return-after-absence"),
        Node(id="next", kind="next-action-shown"),
    ]) is False, "the next action leads: the falsifier must stay quiet"
