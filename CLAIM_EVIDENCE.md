# Claim-to-evidence ledger

The final evaluator-facing release marks all six original claims falsified.
Claims 1–4 have high scientific confidence; Claims 5–6 have medium confidence
because their exact contradiction is a cited sampler-domain failure rather
than a separate end-to-end lower-bound proof.

| Claim | Verdict | How the claim is produced | Primary evidence |
| --- | --- | --- | --- |
| C1. GLM sparsification | `FALSIFIED_HIGH_CONFIDENCE` | Parse Theorem 10 / Algorithm 2, check `M=Θ̃(n/ε²)`, the cited `M≤m` sampler contract, the explicit `M`-sample loop, an independent checker, and statevector boundary controls. The sampler domain and fixed-dimension ε power contradict the printed runtime. | [`repro/src/claim1_runtime_audit.py`](repro/src/claim1_runtime_audit.py), [`repro/src/claim1_independent_checker.py`](repro/src/claim1_independent_checker.py), [Claim 1 page](.trackio/logbook/pages/claim-1/page.md) |
| C2. Linear regression | `FALSIFIED_HIGH_CONFIDENCE` | Follow Corollary 23's exact QGLMSparsify-to-solve chain, preserve its sampler domain and ε power, run the quantum-sampled solve, and require all four independent routes and negative controls to pass. The downstream contract inherits C1's contradiction. | [`repro/src/downstream_contract_audit.py`](repro/src/downstream_contract_audit.py), [`repro/src/downstream_contract_checker.py`](repro/src/downstream_contract_checker.py), [Claim 2 page](.trackio/logbook/pages/claim-2/page.md) |
| C3. Lasso regression and firstness | `FALSIFIED_HIGH_CONFIDENCE` | Check primary quantum Lasso prior art from 2021/2023, run the statevector quantum-LARS route, verify the objective mapping, and test the printed inequality with exact arithmetic. The prior-art claim predates the target and the display has a `7/40` gap. | [`repro/src/claim3_lasso_counterexample.py`](repro/src/claim3_lasso_counterexample.py), [`repro/src/claim3_independent_checker.py`](repro/src/claim3_independent_checker.py), [Claim 3 page](.trackio/logbook/pages/claim-3/page.md) |
| C4. Ridge regression | `FALSIFIED_HIGH_CONFIDENCE` | Verify the valid augmentation `[A;√λI]`, `[b;0]`, then transfer the exact C2 runtime/domain contradiction through the downstream audit and sampled solve. | [`repro/src/downstream_contract_audit.py`](repro/src/downstream_contract_audit.py), [Claim 4 page](.trackio/logbook/pages/claim-4/page.md) |
| C5. Huber regression | `FALSIFIED_MEDIUM_CONFIDENCE` | Verify the `γ₁`/Huber specialization and an in-domain execution, then check the universal all-ε contract. The proposed framework invokes the cited sampler outside its stated domain. | [`repro/src/downstream_contract_audit.py`](repro/src/downstream_contract_audit.py), [`repro/src/quantum_statevector_checker.py`](repro/src/quantum_statevector_checker.py), [Claim 5 page](.trackio/logbook/pages/claim-5/page.md) |
| C6. `ℓ_p` regression | `FALSIFIED_MEDIUM_CONFIDENCE` | Check p-homogeneity for `p∈(0,2]`, execute a valid `p=3/2` route in-domain, and test the universal all-ε sampler contract. The cited primitive is invoked outside its domain. | [`repro/src/downstream_contract_audit.py`](repro/src/downstream_contract_audit.py), [`repro/src/quantum_statevector_checker.py`](repro/src/quantum_statevector_checker.py), [Claim 6 page](.trackio/logbook/pages/claim-6/page.md) |

## Authoritative score record

The current score is recorded in
[`live_judge_verdict.json`](.trackio/logbook/evidence/release/live_judge_verdict.json):
`12/12`, all six claims `falsified`, quality `high`, snapshot SHA
`8ca97b16e85f7220d5298dc4607f7623df2b5241`, judged on 2026-07-31.

The top-level [`outputs/verdict.json`](outputs/verdict.json) and
`outputs/remaining_claim_*.json` files are retained pre-live development
records. They contain earlier blocked routes and must not override the final
`.trackio` release snapshot.

## Branch-to-evidence map

`main` is the canonical reader-facing release. The 24 supporting branches are
clean `audit/`, `experiment/`, `integration/`, and `release/` names. Their
former `orx/*` names, role, and exact evidence scope are recorded in
[`branch-audit.md`](branch-audit.md). The key routes are:

- [`audit/c1-qglmsparsify-contract`](https://github.com/MachineLearning-Nerd/icml26-quantum-regression/tree/audit/c1-qglmsparsify-contract) — C1 exact sampler/runtime contract.
- [`audit/c3-lasso-counterexample`](https://github.com/MachineLearning-Nerd/icml26-quantum-regression/tree/audit/c3-lasso-counterexample) — C3 prior-art and display counterexample.
- [`audit/downstream-corollary-adjudication`](https://github.com/MachineLearning-Nerd/icml26-quantum-regression/tree/audit/downstream-corollary-adjudication) — C2/C4/C5/C6 dependency routes.
- [`experiment/statevector-quantum-lars`](https://github.com/MachineLearning-Nerd/icml26-quantum-regression/tree/experiment/statevector-quantum-lars) — statevector sampler and quantum-LARS evidence.
- [`release/final-hf-provenance`](https://github.com/MachineLearning-Nerd/icml26-quantum-regression/tree/release/final-hf-provenance) — final live-score provenance.
