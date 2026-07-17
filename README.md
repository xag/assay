# assay

A blind trial: an agent that has never seen your code — not even your app's name — reads
only your statement of *intent*, invents the people who would depend on it and the
storylines they would live, and writes down what each of them is owed as falsifiable
expectations. Those expectations are then confronted with the running system, and every
verdict carries its receipts. The point is what your own tests cannot do: your tests
check what you thought of, from inside; a blind trial checks what the intent promised,
from outside.

**The founding scar.** A localisation shipped with 486 tests passing, 303/303 strings
covered in both directions, twelve tapes replaying bit-for-bit — and it was incredibly
bad: the empty screen said *"there is nothing to add"* forty pixels above a button
marked **AJOUTER**. Every check was green. **None of them reads.** Green is not good; a
check that doesn't read proves nothing — which is why this method exists, and why it
ends in verdicts with evidence instead of a passing suite.

## The confrontation modes

| mode | what happens | what the verdict rests on |
|---|---|---|
| **walkthrough** | a simulated persona *lives their storyline* against the running app and judges what they meet against the intent | judgment, recorded — rich, charitable, and expensive |
| **flight** | a scripted stretch of lived time recorded as a tape, replayed on the real code, held to invariants and to the app's semantic model | mechanics — replay, invariants, conformance; no judgment involved |
| **rendered-surface reading** | every surface × state × locale rendered and *read* by a competent reader | the one mode that catches what the scar shipped |
| **monitor** | the same expectations held against real production tapes | lived usage instead of scripted |
| **proof** | a falsifier that compiles to the app's semantic alphabet is decided mechanically over a proven model and refined tapes | artifacts, content-addressed — milliseconds, with receipts |

The difference that matters most, in one line: a **walkthrough** is somebody using the
app and telling you what it was like; a **flight** is a proof obligation with a
storyline attached — if it stops replaying or refining, a mechanical diagnostic names
the first divergence, and nobody's opinion is involved.

Verdict vocabulary (part of the method's identity, glossed once): `pass` / `mitigé`
(mixed — part of the promise holds, part breaks) / `fail` / `hors-champ` (out of frame —
the intent never promised it, so the finding is about the intent). A verdict awaiting
its evidence is `provisoire` (provisional), and a gate refuses releases resting on one.
The `RÉSERVE` is a held-out third of the expectations, confronted exactly once at the
end, to measure overfitting to the generated personas.

## The three substrates

assay is the third of three tools that work together.
[flight-recorder](https://github.com/xag/flight-recorder) records what the outside world
told your code and replays it bit for bit — one recording is a *tape*.
[quern](https://github.com/xag/quern) keeps rules and vocabulary as data your program can
check, published as versioned packages — "the registry" below is its package registry.

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

## License

Apache-2.0 — see [LICENSE](LICENSE).

© 2026 Xavier Grehant
