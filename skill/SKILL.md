---
name: assay
description: >
  Assay — blind trials of intent against the real system: test an app's usability AND its
  interface craft (and any funnel or machine counterparty) by confronting code-blind,
  intent-derived expectations with the running thing. Use when the user wants to test usability, write an
  app intent, generate blind personas/scenarios, confront storylines with flight-recorder
  tapes, or find out why an interface reads badly when every test is green.
  The pipeline: intent (job altitude) → blind scenario generation (subagent) →
  falsifiable expectations, plus craft expectations triggered by the intent →
  confrontation (walkthroughs, flights, monitors, and reading the rendered screens).
---

# The assay

*(formerly `blind-usability`, renamed at extraction — an assay is the standardized blind
trial that tells you what a thing is actually made of, and it verbs: assay the funnel,
assay the widget. Source of truth: `xag/assay/skill/SKILL.md`; the method's hard rules
are data — `assay@`, in the registry — and go red in `assay.check` rather than sitting
here being true.)*

## The cast

Every scenario declares its cast before anything runs:

- **Human counterparty** → an agent simulates the persona, explicitly and never
  silently. A simulated walkthrough can only *carry* a broken-control finding its
  author already knew; only the browser-driven mode can *detect* one.
- **Machine counterparty** → a **stand-in rigged from the vendor's reference
  implementation**, never a hand-rolled fake: an uninstrumented fake is relocated
  guessing. First rig: `rigs/mcp-app-host/` (the MCP Apps SDK's own AppBridge over the
  real committed bundle), with its jsdom traps documented alongside.
- **Platform guarantee** (does this client honour the spec it published) → cast
  nobody. Not ours to audit.

Usability is tested by people who don't know how the app works. We simulate that with a
firewall: scenarios are generated from the app's *intent* by an agent that has never seen
the code, the README, or even the app's name — then confronted with the real system.

**Two questions, not one.** *Can this persona do the job?* is what the firewall answers. *Is
this interface any good?* is a different question, and the firewall cannot answer it: a
persona shown an awkward screen infers the intent, completes the job, and returns PASS. So
craft defects survive a fully green run — as they survive tests, string coverage, and type
checks, none of which read. **Step 3b** is the second question, and it is not optional: it
was added after an app shipped a localisation with 486 tests passing and 303/303 strings
covered, whose empty screen told the user *"there is nothing to add"* directly above a button
marked **Add**.

## The intents directory

`C:\Users\trans\Projects\intents\` holds one intent file per app, plus its derived
artifacts (`<slug>.scenarios.md`, `<slug>.expectations.md`, …).

**Hard rules for everything in this directory:**
- No reference to the source app: not its name, repo, stack, or medium. Filenames are
  job-derived slugs (`un-ete-sans-perdre-la-main.md`), never app names.
- The dependency points one way: the app repo may carry a pointer to its intent file
  (one line in README or ledger); the intent knows nothing of the app.

## Step 1 — Write the intent

From the code and docs of the app, write what purpose it serves — then strip the how.

- **Job-to-be-done altitude only.** What must become true, for whom. Never a feature
  inventory, never interface vocabulary (no "click", "notification", "page", "compte" —
  nothing that reveals the medium, not even that it is digital).
- **Every persona the app serves gets its job stated** (e.g. the parent's job and the
  child's job are distinct promises).
- **Don't confuse the trigger with the intent.** The first user or originating project is
  a trigger; the intent describes who the app is *for*, generally.
- Include the cadence/shape of engagement if it's a promise (e.g. "one short challenge a
  day"), and end with what success looks like.
- Short and human: ~5 paragraphs, written like you'd explain it to a friend.
- Language: the users' language.

Journal the intent's creation in the app's ledger/quern with a pointer to the file.

## Step 2 — Blind scenario generation (subagent)

Spawn a subagent whose prompt contains ONLY: the firewall rules, the generation
instructions, the full intent text inline, and the output path. It must be told:

- Its only input is the intent below. **Do not read any file, do not explore the
  filesystem, do not search the web, do not try to guess what app exists behind this.**
  The working directory name is to be ignored — it is not information.
- Make **no assumption about the medium** (paper, human service, app, …). Personas
  express what they would naturally expect, try, and feel — in life terms.
- Generate 6–8 personas with **prescribed diversity axes** (LLM personas trend median —
  force the spread): family/user shape and who's the buyer; ages/attitudes across the
  intent's range; tech comfort and device access; disrupted contexts (travel, no
  connectivity, shared devices); error behaviors (skipping, rushing, someone else doing
  the work, the counterpart responding late); timing edge cases; one non-actor (signs
  up, never starts — what would re-engage them?); and the questions people ask before
  trusting anything (where their work/data goes and who sees it, what it costs, what
  happens after) — an axis blind generation was observed to omit entirely on its own.
- Each persona gets a **storyline**: how the need arises → how they discover such a thing
  → first contact → life over the weeks → the precise moments where it could break.
  Realistic, detailed, narrative — names, places, times, everyday objects. Embed
  expectations inline, marked `ATTENTE:` — each one an observable outcome plus an
  effort/time budget where sensible.
- Write the output to `intents\<slug>.scenarios.md`, starting with a note that it was
  generated blind from the intent, and return a one-paragraph summary.

## Step 3 — Expectations

Back in a code-aware session: distill the storylines into a ledger of falsifiable
expectations (`<slug>.expectations.md`, still app-neutral).

Expectations arise **at each step of a personal story** — need, discovery, first
contact, daily life, disruptions, endings. Anchor every entry to its persona and story
step. Two passes:

1. Lift the explicit `ATTENTE:` lines.
2. Re-read each storyline *including its "where it can break" notes* and harvest the
   implicit expectations — concrete abilities ("invite the other parent through the
   channels the family already uses"), qualities ("doesn't smell like school"), absences
   ("never a guilt pile"). The form catalogue below is a **sieve for noticing, never a
   mold**: keep each expectation in the storyline's own words.

Ledger entry fields: id · statement (observable outcome + budget) · personas and story
step · kind · confrontation mode · source (explicit/harvested) · status.

- **Predict the taxonomy of kinds before distilling**, then record how the material
  revises it — kinds are discovered, not imposed, and the revisions are findings (in one
  run, "partition" — multi-child, multi-adult, shared device — emerged as a major kind
  the prediction had missed entirely).
- **Merge duplicates across personas**, keeping the hardest budget and case.
- **Flag hors-champ candidates now**: expectations demanding what the intent never
  promised. They are questions for the intent, not tests of the app.
- **Freeze a held-out subset** (~1/3, balanced across kinds and modes, marked RÉSERVE)
  before any confrontation; confront it exactly once, after iterating on the working
  set — it measures overfitting to the generated personas. Outcome/monitor entries are
  exempt (they only bind to real usage).
- **Audit systematic absences**: a whole family of concerns with zero instances (trust,
  money, data) is a finding about the generation prompt — fold it back into step 2's
  axes.
- **Extract the confrontation matrix**: while distilling, collect every persona's
  devices and contexts (the Android in the break room, the iPhone at the campsite, the
  cracked shared tablet, the desktop nobody has). Each expectation records the matrix
  cells its PASS is defined over. This matrix — not the tester's convenience — is where
  step 4's empirical work must land.

### Form catalogue (a sieve, not a mold)

- capability: a means to [action]; …without [precondition]; a way to know / be told
  [state/event]; a way back from [wrong turn]; [A] can [act] for [B]
- quality: a [adjective] interface; doesn't feel like [category]; makes me [role], not
  [role]
- bounds: [action] within [time/effort budget]; [response] within [bound]
- absence: never [unwanted thing]; no [burden] required
- continuity: survives [disruption]; adapts as [change]; starting late or over costs
  nothing
- partition: each [party] their own [thing]; only [party] sees [thing]; [tracking] is
  never a weapon
- trust & cost: I can trust that [assurance]; costs at most [price], known upfront;
  works with what we already have

## Step 3b — Craft expectations (triggered, not checklisted)

**The gap this closes.** Everything above asks *can this persona do the job?* Nothing above
asks *is this interface any good?* — and those are different questions. An LLM persona is
charitable: shown an awkward screen it infers the intent, completes the job, and returns
PASS. So craft defects survive a fully green usability run. They also survive tests
(which assert on values, not prose), string-coverage checks, and type checks. **Nothing in
the standard apparatus reads.**

So the ledger carries a second family of expectations. They are not harvested from the
storylines — they are **craft laws that the storylines switch on**. That is what makes them
free: the author writes an intent and gets the relevant ones without asking.

### Triggers → laws

Read the intent and the scenarios for properties. Each property switches on its laws. Record
in each expectation *which trigger fired it* — a law with no trigger is a checklist item, and
checklists are ignored.

| property of the intent / scenarios | laws it triggers |
|---|---|
| the app speaks the users' own language (any localisation at all) | COMPOSED-PROSE · GLOSSARY-FIRST · NO-CALQUE · UNTRANSLATABLE-TONE |
| any surface has a zero state (a new user; a day with nothing due) | EMPTY-STATE-NEVER-CONTRADICTS |
| a rare action shares a surface with frequent ones (create vs. switch; delete vs. edit) | ONE-SURFACE-ONE-JOB · RARE-ACTION-FOLDS-AWAY |
| the app coins domain concepts of its own (a "wall", a "ledger", a "charter", a "turn") | NO-SYSTEM-VOCABULARY |
| any count, duration, date, currency or name is interpolated into a sentence | COMPOSED-PROSE · PLURALS-AND-AGREEMENT |
| the intent promises near-zero upkeep | PRIMARY-ACTION-IS-ONE-TAP |
| personas span ages/reading levels (a child and a parent) | READING-LEVEL |
| an action is contested, destructive or irreversible | A-WAY-BACK · SAYS-WHAT-HAPPENS |

### The laws

**The laws are a quern package — `craft@0.1.0`, in `xag/craft-laws`, pinned by rev.** They are not
a checklist and they do not live here.

`./references/craft-laws.md` is a **rendered view** of that data, stamped with the commit it came
from. Read it. Do not edit it: edit the package and re-render, because editing a view is how a
view becomes a second source of truth.

Twelve laws. Nine cite a source — NN/g, GOV.UK Design System, Mozilla L10n, Unicode CLDR,
W3C/IBM, Lionbridge — **with the quote**, because a citation without the words is one nobody can
check. Three cite nobody, say so, and are **red** in `craft.check` until somebody sources them or
deletes them.

Each law carries four things, and the rules enforce all four:

| | |
|---|---|
| **falsifier** | the observation that constitutes a violation — so a verdict is `fail`, not *I don't like it* |
| **trigger** | the property of the app's *intent* that switches it on. **This is what makes the laws free**: write what the app is for, and the relevant laws arrive. A law with no trigger is a checklist item, and checklists are ignored |
| **citation** | who actually said this. Uncited ⇒ the law is a hypothesis, carried visibly, and the publication gate will not pass it |
| **sighting** | a real defect it caught. A law that has never caught anything is a law nobody should trust |

**Why it is a package and not this file.** These laws were first written *inline here*, from
memory, by the agent that had just been burnt by the defects they describe — and that file
contained a sentence saying three of its laws were unsourced. The sentence was true. It could not
fire. Which is the failure the ledger exists to prevent, reproduced inside the artifact teaching
it; and worse, inventing laws and making them binding is the same act as inventing a translation
glossary and handing it to a translator, which is the very thing GLOSSARY-FIRST forbids. **The
laws broke themselves in the act of being written down.** So they became data.

To add a law: add it to `xag/craft-laws`, with a source or an explicit `UNCITED` marking. Never
here.

### Confrontation mode: rendered-surface reading

**New mode, and the one the other three cannot cover.** Not a walkthrough (a persona is too
charitable), not a flight (a tape records values, not prose), not a content audit (that judges
level and tone, not composition).

Boot the real app against the real backend. Walk **every surface × every state × every
locale** and dump the text as a person would read it. Then a competent reader reads it.

- **The state axis is where the bugs are, and it is the one that gets skipped.** Seed the
  system and you render the populated screens and never see the zero state — which is the
  first screen a new user meets and the one the app speaks most in. Enumerate: empty, one,
  many, overflowing, error, mid-disruption.
- It has **no assertions and passes nothing**. Its only job is to put composed prose in front
  of someone who can judge it. Do not turn it into a test; a test that could judge this prose
  would already be the judgement.
- A reference instrument: `chores/tools/read_screens.mjs` (jsdom + the real server; prints
  every tab and sheet in both languages).

**The instrument's own blind spots, each of which hid a real defect on its first run.** Check
yours for all three before you trust a clean reading:

1. **`textContent` is not what a person reads.** Placeholders, input values and aria-labels are
   prose — *"Le gîte"*, *"Arroser les plantes"* — and none of them are in `textContent`. Walk
   the tree and render each control as what it *shows*. (Found: a button labelled with a noun,
   `Absence`, where an action belonged.)
2. **Silence is a lie.** The first version reached a sheet by guessing a CSS selector, missed,
   and printed `(vide)` — so the wordiest surface in the app went unread while the instrument
   reported success. It must *throw* when a surface renders nothing.
3. **Seeded state hides the zero state.** See above. Run it against an empty system too.

Reach every surface by **clicking the control a person clicks**. A harness that needs the app
to export a hook is reading a surface the user does not have.

### Does it do work? (the run that produced it)

`chores`, 2026-07-13. A French localisation shipped to production with **486 tests passing,
303/303 string keys covered in both directions, `node --check` clean, cp1252 verified, and
twelve flight-recorder tapes replaying bit-for-bit.** The owner opened the app and called the
French "incredibly bad". Every defect below was invisible to every existing check *and* would
have passed a persona walkthrough — the persona understands the screen and does the job.

| what the screen said | law that catches it | why nothing else could |
|---|---|---|
| `Il n'y a rien à ajouter.` — 40px above a button marked **AJOUTER** | EMPTY-STATE-NEVER-CONTRADICTS | Correct as a sentence. Absurd only *in place*. No string table contains position. |
| `Encore encore 3 min pour contester.` | COMPOSED-PROSE | Two strings, each correct alone; the defect exists only in the sentence they compose. |
| Household tab **40% English** (`about their share`, `Minutes a week`) | COMPOSED-PROSE | The prose came from a *data file* and from server computation — in no string catalogue anyone could review. |
| `Ses propres habitants` (a *team* has no inhabitants) | NO-CALQUE | Survived a glossary swap because the sentences around the changed word were never re-read. |
| `Les murs`, `l'arbitre`, `le registre` | NO-SYSTEM-VOCABULARY · NO-CALQUE | Vivid English metaphors; jargon in French. |
| `maisonnée`, counting chores in `tours` | GLOSSARY-FIRST | The glossary was invented by the translator's commissioner and made binding. A native speaker settled it in one question. |
| A sheet doing rename + language + create-a-team, with the create form expanded by default | ONE-SURFACE-ONE-JOB · RARE-ACTION-FOLDS-AWAY | Opened to switch teams; met a signup form. |

Seven defects, one instrument, ten minutes. **Every one of them shipped green.**

Then the laws were pointed at surfaces nobody had rendered yet — the member sheet, the chore
sheet — and immediately found two more that had nothing to do with translation:

| what the screen said | law |
|---|---|
| a section headed **Absence**, and the button under it also labelled **Absence** (`Away` / `Away` in English — the defect predates the localisation) | SAYS-WHAT-HAPPENS: a control says what happens; a noun is not an action |
| `Tout l'équilibre se compte en minutes` | NO-SYSTEM-VOCABULARY: *l'équilibre* is the app's word for its own machinery |

That is the test of whether a method works: not that it explains the defects you already
found, but that it finds the ones you had not.

## Step 4 — Confrontation

Expectations split by whether the persona ever reaches the system's boundary. Key
unification: a *test scenario* and a *production monitor* are the same artifact — an
invariant over a tape — differing only in whether the tape is scripted or lived.

- **Discovery/comprehension expectations → persona walkthrough.** A fresh agent plays
  the persona, given only what the real user would see (rendered pages/screens/docs, in
  the real order), and narrates what it would do next at each step. Getting stuck or
  guessing wrong is a finding no tape can catch — a user who never reaches the boundary
  produces no flight at all. If the walkthrough drives the real app, the session records
  like any other: the tape corroborates the narration (time-to-first-action, wrong
  turns), though it cannot detect confusion.
  Mechanics that worked: transcribe each screen faithfully (labels, buttons, exact
  copy); fetch the *actual content* the persona would meet (the real challenge of the
  day for their level, the real prefilled prompt); and supply **world-facts** — behaviors
  observable only through use (what persists per device, what a button silently fails to
  do on which hardware, what nothing ever tells the user) — so a single-prompt agent
  doesn't need interactivity to live several weeks. Ask for: step-by-step narration with
  honest timing, one verdict per assigned expectation with evidence, and a ranked
  "trouvailles" list. Run the personas in parallel; convergence between independent
  personas — and between personas and flights — is the strongest signal in the method.
  **A transcribed surface is a fake, and the fake corollary applies**: verify every
  world-fact against the real running app before feeding it to personas — click the
  button, on the real platforms, and record what actually happens (one run shipped
  "nothing happens" when the truth was a generic error loop). A simulated walkthrough
  can only *carry* a broken-control finding its author already knew; only the
  browser-driven mode (real clicks, session recorded to tape) can *detect* one. Any
  expectation whose verdict claims a control "works" needs the empirical mode, not the
  simulated one.
  **World-facts need receipts**: every fact handed to a persona is backed by an
  observation (a tape, a recorded interaction, a screenshot) or explicitly labeled
  `non-vérifié` — and a verdict resting on an unverified fact is `provisoire`, listed
  as verification debt in the report.
  **A PASS must name whose job it proves, in which cell.** Empirical results outside
  the confrontation matrix (the framework's default browser, the developer's desktop)
  are engineering information, never a PASS. One run verified "the button works" on
  desktop Chrome — a device zero personas hold — while the mechanism stayed unverified
  on every phone in the storylines and fragile-by-design on iOS: the streetlight
  effect, mechanism-altitude drift. Before recording PASS, write the sentence "this
  proves [persona]'s [job] in [device × context]"; if the sentence can't be written,
  it isn't a PASS. Cells needing hardware the harness lacks (a real iPhone) become
  named user-in-the-loop steps, not silent gaps.
- **Executable expectations → flights.** Script the storyline as event sequences at the
  app's instrumented nondeterminism boundary (clock, storage, push, …) — fast-forward a
  whole summer of clock ticks in a minute — and write invariants over the resulting tape
  for the promised outcomes (feedback delivered, latency bounds, no-debt after
  interruptions of every scale, correct routing/partition). Fakes injected at the
  boundary must be verified once against the real dependency's wire behaviour — an
  uninstrumented fake is relocated guessing.
- **Standing expectations** ("never lose work", "never a guilt pile") → invariants that
  must hold on *every* tape, scripted or lived — not one scenario.
- **Outcome expectations** (retention, "no disputes", felt readiness) → **monitors**:
  the same invariant language bound to production tapes; not confrontable pre-launch —
  tag them as such rather than pretend a walkthrough can verify them.
- **Boundary-invisible expectations** (e.g. someone else did the work — the recorded
  events are identical) compile to nothing: record them as design questions, not tests.
- **Content-fit expectations** (level, tone, playfulness) → content audit alongside the
  walkthroughs.
- **Craft expectations** (step 3b) → **rendered-surface reading**. Never a walkthrough: the
  persona is charitable and will do the job through an awkward screen, returning PASS over a
  defect. Never a flight: a tape records values, and prose is not a value. Render every
  surface × state × locale, dump the text, and have a competent reader read it. A craft
  expectation whose verdict rests on a persona's PASS is `provisoire` and belongs in the
  verification debt.

**Verdicts:** each expectation gets `pass` / `mitigé` / `fail` / `hors-champ`.
`mitigé` names which half of the promise holds and which breaks — walkthroughs produce
it constantly and flattening it to pass/fail loses the finding. `fail` → fix the app.
`hors-champ` → a finding about the intent: extend it, journal why, regenerate scenarios
from the extended part only.

**Where results live:** verdicts and the confrontation report go in the *app's* ledger
(they describe the realization); the intents directory stays verdict-free. Report shape
that worked: verdict table per mode with one-line evidence → transverse findings ranked
by convergence → **new expectations the confrontation itself revealed** (append to the
expectations ledger, source: `confrontation`) → synthesis with ranked chantiers.
Undeclared nondeterminism doors discovered during confrontation (e.g. a clock decision
living client-side, outside the recorded boundary) are method findings — journal them
with the boundary.

**After the fixes:** re-confront the working set, *then* unfreeze the RÉSERVE for its
single confrontation (the overfitting measure), then close the loop on real traces.

## Orchestration (multi-agent runs)

The firewall is a property of *contexts*, so the orchestrator — not a worker — owns all
spawning. A code-aware confrontation agent that cannot spawn personas will quietly
*simulate* them, and a simulated persona from a contaminated context is not blind (run
2 did exactly this; the reports had to be regenerated). Division of labor that works:
the code-aware agent prepares self-contained walkthrough *packs* (verified surfaces +
world-facts with receipts + output path); the orchestrator spawns one fresh blind agent
per pack; a step-5 critic reviews; the code-aware agent integrates. Two integration
rules, both violated once: **verdict tables must carry the persona's verdict verbatim**
(requalifying needs a stated receipt — integrators soften FAILs into MITIGÉs when left
alone), and **everything not confronted is listed by name** in a "non confronté"
section — an absent verdict otherwise reads as covered.

## Step 5 — Critic of the confrontation

Before the report is final, spawn one adversarial agent given the *intent, the
scenarios, and the report* — but not the code. Its brief: hunt altitude drift. For
every PASS, it asks "what does this mean in the persona's life — whose job, on whose
device?"; for every verified mechanism, "is this where the users are, or where the
light was?"; for every world-fact, "where's the receipt?". Its findings reopen
verdicts. This role existed in one run only because the human asked "what does it
even mean to enable notifications on desktop?" — the question that exposed a PASS
proving nothing and a product trap (per-device permission ≠ the device in the
pocket). The method must ask it itself.

## Closing the loop

When the app has real users, their real traces (tapes, logs) are ground truth: score the
blind generation by how many observed behaviors it anticipated. That tests the method,
not just the app.
