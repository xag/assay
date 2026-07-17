# Contributing

A new worked case requires receipts — tapes, rendered dumps, committed rig outputs —
because a case without evidence is an anecdote, and the cases are what keep the
abstraction honest. A new kind or rule in `assay/package.py` requires examples that
exercise it and counter-examples that refute it, or the publish gate refuses it. A new
rig names its source of truth (the vendor's own implementation) or it is exactly the
relocated guessing the rules exist to catch. `uv run pytest` runs the tests;
`uv run python -m assay.check` runs this repo's own ledger.
