"""assay@ publishes with its proofs, and the vocabulary's discipline actually binds."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

import bom.grounding  # noqa: F401 -- ledger@'s proofs re-run at sync and call these
from bom import Bom, Library, run_rules
from bom.library import consume, package_digest, sync

from assay.package import ASSAY_PACKAGE

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def library(tmp_path):
    lib = Library(tmp_path)
    cache, refs = consume(ROOT, os.environ.get("BOM_REGISTRY",
                                               ROOT.parent / "bom-registry"))
    sync(cache, lib, [r for r in refs if r.name in ("ledger", "grounding")])
    return lib


def test_assay_publishes_with_its_proofs(library):
    log = library.publish(ASSAY_PACKAGE, {})
    assert any("4 rule(s) exercised" in line for line in log)
    assert any("refuted by their counter-example" in line for line in log)


def test_the_authored_package_is_the_published_artifact():
    _, refs = consume(ROOT, os.environ.get("BOM_REGISTRY",
                                           ROOT.parent / "bom-registry"))
    pinned = next(r for r in refs if r.name == "assay")
    assert package_digest(ASSAY_PACKAGE) == pinned.sha256


def test_a_provisoire_verdict_is_visible_to_a_gate(library):
    """The receipts discipline composes with ledger@'s gate without a single new rule:
    a verdict whose evidence is ungrounded (provisoire) cannot pass a release gate that
    admits it — exactly as a debt cannot."""
    from bom import Node, Quantity
    library.publish(ASSAY_PACKAGE, {})
    tree = Bom(packages=[{"name": "assay", "version": "0.1.0"}])
    tree = library.effective(tree)
    tree.root.children = [
        Node(id="v", kind="verdict", name="pass, pending receipt verification",
             params={"evidence": Quantity(value=1, unit="receipt", grounded=False,
                                          provenance="provisoire")}),
        Node(id="release", kind="gate", name="ship it",
             links={"admits": ["v"]}),
    ]
    results = {r.rule: r.ok for r in run_rules(tree)}
    assert results["a-verdict-carries-evidence"] is True   # it HAS a receipt...
    assert results["nothing-unsound-passes-a-gate"] is False  # ...but nobody verified it
