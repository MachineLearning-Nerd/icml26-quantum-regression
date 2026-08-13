# Results

The current evaluator-facing release scored **12/12** at revision
`8ca97b16e85f7220d5298dc4607f7623df2b5241`. Every original claim was marked
`FALSIFIED`.

| Claim | Current result | Evidence route |
|---|---|---|
| C1 — GLM sparsification | FALSIFIED — HIGH | QGLMSparsify contract, explicit epsilon-power loop, statevector boundary and negative control |
| C2 — Linear regression | FALSIFIED — HIGH | Inherited QGLMSparsify contract plus quantum-sampled linear solve |
| C3 — Lasso | FALSIFIED — HIGH | 2021/2023 primary prior art, quantum LARS, and exact printed-display gap |
| C4 — Ridge | FALSIFIED — HIGH | Exact `[A; sqrt(lambda)I]` reduction plus inherited C2 contract |
| C5 — Huber | FALSIFIED — MEDIUM | `gamma_1` specialization, in-domain run, and all-epsilon sampler-domain failure |
| C6 — `ell_p` | FALSIFIED — MEDIUM | `p=3/2` specialization, in-domain run, and all-epsilon sampler-domain failure |

Start with the [canonical conclusion](.trackio/logbook/pages/conclusion/page.md)
or the [final release report](.trackio/logbook/evidence/release/final_release_report.md)
for raw evidence links, independent checkers, controls, compute records, and
limitations.

## Historical records

The repository preserves the earlier arithmetic-only 0/12 baseline and the
intermediate four-route review. Those records are useful for understanding the
development path but are not the final status. In particular,
`outputs/verdict.json`, `outputs/remaining_claim_routes.json`,
`outputs/remaining_claim_checker.json`, and the `.trackio` pages named
`current-claim-*` retain their pre-live-judge statuses.
