# Accelerating Regression Tasks with Quantum Algorithms

Independent reproduction audit for [arXiv:2509.24757](https://arxiv.org/abs/2509.24757),
“Accelerating Regression Tasks with Quantum Algorithms,” by Chenghua Liu and
Zhengfeng Ji.

## Audit record

Overall status:
`ALL_SIX_CLAIMS_FALSIFIED_C1_C4_HIGH_CONFIDENCE_C5_C6_MEDIUM_CONFIDENCE_LIVE_SCORE_12_OF_12`.

The standardized claim ledger is [`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md), the
source/version record is [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md), and the final
GitHub branch/identity check is [`verify_final.py`](verify_final.py).
`current_score_claim=true` because the live evaluator snapshot is retained and
verified; `official_author_endorsement=false` and
`publication_allowed=false` remain explicit boundaries.

## Result at a glance

The evaluator-facing release received **12/12** at revision
`8ca97b16e85f7220d5298dc4607f7623df2b5241`. The live judge marked all six
original claims **FALSIFIED** and rated reproduction quality **high**. Claims
1–4 have high scientific confidence; Claims 5–6 have medium confidence
because their exact contradiction is a sampler-domain failure rather than a
separate end-to-end lower bound.

This is an audit of the paper’s named algorithms and exact stated contracts.
It does not claim that every possible quantum regression algorithm fails, and
it uses CPU/statevector simulations only—no quantum hardware or GPU.

The reader-facing evidence is organized in the [illustrated report](reports/quantum-regression/report.md),
the [canonical conclusion](.trackio/logbook/pages/conclusion/page.md), the
[final release report](.trackio/logbook/evidence/release/final_release_report.md),
and the [live-verdict snapshot](.trackio/logbook/evidence/release/live_judge_verdict.json).

## Paper and scope

The paper proposes a quantum GLM-sparsification framework for linear,
multiple, Lasso, Ridge, Huber, `ell_p`, and `gamma_p` regression. Its central
runtime is approximately
`r*sqrt(m*n)/epsilon + poly(n, 1/epsilon)`, with a sparsifier of size roughly
`n/epsilon^2`.

The audit checks the exact theorem/corollary contracts, including their
quantifiers, sampler preconditions, explicit loops, reductions, and claimed
prior art. The pinned source archive is recorded in
[`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md).

## Claim-to-evidence ledger

| Claim | Paper statement audited | How the result is produced | Canonical status |
|---|---|---|---|
| C1 — GLM sparsification | Theorem 10 / Algorithm 2 | [`claim1_runtime_audit.py`](repro/src/claim1_runtime_audit.py) checks `M=Theta~(n/epsilon^2)`, the cited `M<=m` sampler contract, and the explicit `M`-sample loop; the independent checker and statevector boundary controls are linked from the [Claim 1 page](.trackio/logbook/pages/claim-1/page.md). | FALSIFIED — HIGH |
| C2 — Linear regression | Corollary 23 | [`downstream_contract_audit.py`](repro/src/downstream_contract_audit.py) follows the exact QGLMSparsify-to-solve chain and checks the inherited domain and epsilon-power contradiction; the [Claim 2 page](.trackio/logbook/pages/claim-2/page.md) records the sampled solve and controls. | FALSIFIED — HIGH |
| C3 — Lasso regression | Corollary 26 and the firstness claim | [`claim3_lasso_counterexample.py`](repro/src/claim3_lasso_counterexample.py) checks prior quantum Lasso work, the objective mapping, and the exact printed-inequality gap; the [Claim 3 page](.trackio/logbook/pages/claim-3/page.md) records the quantum-LARS and negative-control evidence. | FALSIFIED — HIGH |
| C4 — Ridge regression | Corollary 25 | The downstream audit verifies `[A; sqrt(lambda)I]`, `[b;0]` and transfers the C2 contradiction; see the [Claim 4 page](.trackio/logbook/pages/claim-4/page.md). | FALSIFIED — HIGH |
| C5 — Huber regression | Corollary 12 with `p=1` | The downstream audit verifies the `gamma_1`/Huber specialization, in-domain execution, and the all-epsilon sampler-domain contradiction; see the [Claim 5 page](.trackio/logbook/pages/claim-5/page.md). | FALSIFIED — MEDIUM |
| C6 — `ell_p` regression | Corollary 11 for `p in (0,2]` | The downstream audit checks p-homogeneity, an in-domain `p=3/2` execution, and the universal all-epsilon domain failure; see the [Claim 6 page](.trackio/logbook/pages/claim-6/page.md). | FALSIFIED — MEDIUM |

The independent checkers are [`claim1_independent_checker.py`](repro/src/claim1_independent_checker.py),
[`downstream_contract_checker.py`](repro/src/downstream_contract_checker.py),
[`claim3_independent_checker.py`](repro/src/claim3_independent_checker.py),
and [`quantum_statevector_checker.py`](repro/src/quantum_statevector_checker.py).
The statevector audit reconstructs the cited sampling circuit and a prior
quantum-LARS search; it tests the computational stages, not QRAM construction
or fault-tolerant hardware.

## Reproduce the published checks

The locked environment is Python 3.12 with NumPy 2.3.2:

```bash
uv sync --frozen
uv run python repro/src/verify.py
uv run python repro/src/publication_gate.py
```

The commands regenerate/check the local evidence contract. The final live
judge result is preserved in the release snapshot linked above; rerunning
locally does not create a new evaluator score.

## Branch organization

`main` is the canonical reader-facing release. The former `orx/*` branches
are preserved as clean names grouped by purpose: `audit/*` contains claim and
contract investigations, `experiment/*` contains executable quantum or scale
runs, `integration/*` contains publication/logbook assembly, and `release/*`
contains evaluator-facing release candidates and provenance checkpoints.

The complete old-to-new mapping and the purpose of every branch are in
[`branch-audit.md`](branch-audit.md). No branch name beginning with `orx/` is
part of the cleaned collection.

## Important historical records

The repository preserves the development trail. In particular,
`outputs/verdict.json`, `outputs/remaining_claim_routes.json`,
`outputs/remaining_claim_checker.json`, and the `.trackio` pages named
`current-claim-*` record the pre-final four-route review, where several claims
were honestly marked `BLOCKED`. They are not the current live verdict. Use
the `claim-*`, `executive-summary`, `conclusion`, and
`evidence/release/final_release_report.md` pages for the final adjudication.

## Citation

```bibtex
@misc{liu2025accelerating,
  title         = {Accelerating Regression Tasks with Quantum Algorithms},
  author        = {Chenghua Liu and Zhengfeng Ji},
  year          = {2025},
  eprint        = {2509.24757},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph},
  doi           = {10.48550/arXiv.2509.24757}
}
```

For the prior-art portion of Claim 3, see [Quantum Algorithms for the
Pathwise Lasso](https://arxiv.org/abs/2312.14141) and [Quantum Algorithms and
Lower Bounds for Linear Regression with Norm Constraints](https://arxiv.org/abs/2110.13086).

## Thank you

Thank you to Chenghua Liu and Zhengfeng Ji for making the paper and its source
available for independent examination. The work provided a useful, concrete
case study for testing quantum regression claims against explicit algorithmic
contracts, reductions, controls, and reproducible evidence. This repository
is an independent audit and does not imply endorsement by the authors.

## Attribution and license

Repository maintenance and audit commits are attributed to
**MachineLearning-Nerd**. The paper, source archive, and cited prior work
remain the property of their respective authors and publishers; consult the
upstream paper for its license and reuse terms.
