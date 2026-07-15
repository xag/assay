"""Run the ledger's rules and report. `uv run python -m assay.check`

Exit code is 1 while any rule is red, so this is wireable into CI as a gate.
"""

from __future__ import annotations

import sys

from quern import run_rules

from .tree import build


def main() -> int:
    results = run_rules(build())
    red = [r for r in results if not r.ok]
    for r in sorted(results, key=lambda r: (r.ok, r.rule, r.node)):
        mark = "ok  " if r.ok else "RED "
        at = f" @ {r.node}" if r.node else ""
        detail = f" - {r.detail}" if r.detail else ""
        print(f"{mark}{r.rule}{at}{detail}")
    print()
    if not red:
        print(f"{len(results)} rule(s), all green.")
        return 0
    print(f"{len(red)} of {len(results)} rule(s) RED.")
    print("Discharge a red node by doing the work it names - never by editing the ledger.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
