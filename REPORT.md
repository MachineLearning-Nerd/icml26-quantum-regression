# Audit report

This repository is an independent reproduction audit of **Accelerating
Regression Tasks with Quantum Algorithms**.

The final evaluator-facing release records `12/12`, all six original claims
falsified, and high reproduction quality. Claims 1–4 have high scientific
confidence because their exact sampler/runtime or prior-art contradictions are
independently checked. Claims 5–6 have medium confidence because their
falsifications rely on the proposed algorithm invoking a cited sampler outside
its stated domain rather than on separate end-to-end lower bounds.

The live score and final verdict are in
[`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md) and the `.trackio` release snapshot.
The historical blocked-route artifacts remain useful development evidence but
are not the final status. Branch roles and claim routing are documented in
[`branch-audit.md`](branch-audit.md).

This audit applies to the named contracts, not to every conceivable quantum
regression algorithm. It is not an author endorsement or a quantum-hardware
demonstration.
