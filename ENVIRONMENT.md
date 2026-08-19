# Environment and reproduction contract

## Fixed command

```bash
uv sync --frozen
uv run python repro/src/verify.py
uv run python repro/src/publication_gate.py
```

Python `3.12` and NumPy `2.3.2` are locked with `uv`. The statevector routes
are CPU simulations of the cited sampling circuit and quantum-LARS search;
they do not model QRAM construction, fault-tolerant hardware, or GPU
execution.

## Evidence tiers

- `repro/src/` contains current audits and independent checkers.
- `.trackio/logbook/pages/claim-*` contains the final evaluator-facing pages.
- `.trackio/logbook/evidence/claim_*` contains per-claim routes, controls, and
  runtime records.
- `.trackio/logbook/evidence/release/` contains the authoritative live score
  and final release report.
- `outputs/` retains earlier development and blocked-route records.

The final live score comes from the recorded evaluator snapshot, not from a
local rerun. Re-running the locked checks validates the repository contracts
but does not create a new judge result.
