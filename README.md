# assay

Blind trials of intent against the real system — the third substrate, beside
flight-recorder and quern.

| substrate | question it answers | holds |
|---|---|---|
| **flight-recorder** | *what happened?* | evidence — tapes at the nondeterminism boundary |
| **quern** | *what must hold?* | claims as checkable data — rules, hypotheses, debts, gates |
| **assay** | *does it survive the world?* | confrontation — blind trials of intent against the running thing |

An assay was the standardized blind trial at the gate to capitalization: ore became coin
only by passing the assay office. Nothing becomes capital without surviving a trial.

## What lives here

- **`assay/package.py` → `assay@`** — the method's hard-won lessons as RULES that go
  red, not prose: an expectation is falsifiable (or it is a mood); a scenario records
  what it was permitted to see (blindness is a property of inputs); a stand-in names
  the reference implementation it is built from (an uninstrumented fake is relocated
  guessing); a verdict carries its receipts, and falsified verdicts are kept. Published
  to the registry, pinned by digest. Requires `ledger@`: a trial without a ledger has
  nowhere to keep what it learned, and a release gate refuses provisoire verdicts with
  no new machinery at all.
- **`skill/SKILL.md`** — the procedure: intent (job altitude) → blind scenario
  generation → falsifiable expectations + triggered craft laws → **cast** → confront
  (walkthroughs, flights, rendered-surface reading, monitors) → verdicts to the app's
  ledger. Source of truth; a thin shim in claude-plugins invokes it.
- **`rigs/`** — the casting library for machine counterparties. First rig:
  `mcp-app-host` (the MCP Apps SDK's own `AppBridge` over the real committed bundle),
  its jsdom traps documented, its port verified with committed receipts.
- **`docs/CASES.md`** — the worked cases (defi-vacances, chores, home, and the coach
  funnel as intended second consumer). The examples are what keep the abstraction
  honest.
- **`assay/tree.py`** — this repo's own ledger (`python -m assay.check`): the
  extraction and naming decisions with their rejected alternatives, the standing
  hypothesis (*rigs catch what reasoning cannot* — evidenced, killable), and the rig
  debt, discharged by running the work and kept as a record.

Flight boundary, said out loud: assay itself is pure data plus rigs. The rigs drive
real implementations deterministically; recording lives with the app under trial
(walkthrough sessions and flights record like any other), and the only IO in this repo
is `Library.publish` — quern's code under quern's tests.
