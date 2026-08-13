# Branch audit

`main` is the canonical publication surface. Every former `orx/*` branch has
one clean replacement below; branch names describe the work without depending
on the OpenResearch implementation detail.

| Former branch | Clean branch | What it contains |
|---|---|---|
| `orx/c1-evaluator-visible-falsification-artifact` | `audit/c1-evaluator-falsification-artifact` | First evaluator-visible Claim 1 contract/falsification artifact. |
| `orx/c1-exact-qglmsparsify-contract-audit` | `audit/c1-qglmsparsify-contract` | Exact QGLMSparsify sampler-domain and runtime-power audit. |
| `orx/c2-c4-c5-c6-four-route-audit` | `audit/c2-c4-c5-c6-four-route` | Early four-route review of Claims 2, 4, 5, and 6; retained as historical development evidence. |
| `orx/c3-literal-lasso-corollary-counterexample` | `audit/c3-lasso-counterexample` | Exact Lasso display counterexample and firstness investigation. |
| `orx/c6-discriminating-negative-control` | `audit/c6-negative-control` | Corrected discriminating control for the downstream claim audit. |
| `orx/corrected-claim-scope-and-fixed-order-logbook` | `integration/corrected-claim-scope` | Fixed claim order, scope language, and evaluator logbook integration. |
| `orx/direct-per-claim-verifier-source-links` | `audit/verifier-source-links` | Per-claim verifier and independent-checker links exposed to evaluators. |
| `orx/evaluator-visible-complete-candidate` | `release/evaluator-visible-complete` | Complete evaluator-visible candidate with claim pages and controls. |
| `orx/evaluator-visible-statevector-evidence` | `release/statevector-evidence` | Statevector source, raw evidence, controls, and release package. |
| `orx/exact-downstream-corollary-adjudication` | `audit/downstream-corollary-adjudication` | Exact downstream contracts for Claims 2, 4, 5, and 6. |
| `orx/final-hf-provenance-and-live-verdict-release` | `release/final-hf-provenance` | Final Hugging Face provenance and live-verdict record. |
| `orx/final-six-claim-release-candidate` | `release/final-six-claim` | Six-claim release candidate after the core adjudication. |
| `orx/final-trackio-dependency-disclosure` | `release/trackio-dependency-disclosure` | Trackio dependency and disclosure metadata for publication. |
| `orx/final-validated-statevector-release` | `release/final-statevector` | Validated statevector release surface. |
| `orx/github-main-publication-merge` | `integration/github-publication` | Merge of the reproduction package onto GitHub publication `main`. |
| `orx/hf-validate-supplemental-scale-evidence` | `audit/supplemental-scale` | Supplemental scale evidence at larger sample counts. |
| `orx/integrate-repaired-appendix-without-changing-fix` | `integration/repaired-claims-appendix` | Repaired-claims appendix kept outside the canonical six-claim order. |
| `orx/judged-baseline-with-locked-uv-environment` | `audit/judged-baseline` | Historical locked baseline that received the earlier 0/12 result. |
| `orx/leaderboard-compliant-publication-candidate` | `release/leaderboard-candidate` | Leaderboard-compliant publication candidate. |
| `orx/official-icml-template-and-hardware-accounting` | `release/icml-template-hardware` | ICML logbook structure and explicit CPU/hardware accounting. |
| `orx/preserve-space-metadata-in-final-release` | `release/space-metadata` | Hugging Face Space metadata preservation during final release. |
| `orx/protected-history-complete-release-candidate` | `release/protected-history` | Complete candidate with protected publication history. |
| `orx/remove-nonexistent-workspace-bucket-reference` | `audit/remove-workspace-reference` | Removal audit for a nonexistent workspace/Bucket reference. |
| `orx/statevector-quantum-pipeline-and-prior-lars` | `experiment/statevector-quantum-lars` | Statevector MultiSample circuit and prior quantum-LARS execution. |

## Claim-to-branch routing

| Evidence area | Primary branches |
|---|---|
| Claim 1 | `audit/c1-qglmsparsify-contract`, `audit/c1-evaluator-falsification-artifact`, `experiment/statevector-quantum-lars` |
| Claims 2, 4, 5, 6 | `audit/downstream-corollary-adjudication`, `audit/c2-c4-c5-c6-four-route`, `audit/c6-negative-control`, `audit/supplemental-scale` |
| Claim 3 | `audit/c3-lasso-counterexample`, `experiment/statevector-quantum-lars` |
| Publication evidence | `release/statevector-evidence`, `release/final-six-claim`, `release/final-hf-provenance`, `release/final-statevector` |
| Logbook and repository assembly | `integration/corrected-claim-scope`, `integration/github-publication`, `integration/repaired-claims-appendix` |

The branch history is development evidence, not a second verdict system. The
final claim statuses and score are those recorded on `main` in the canonical
logbook and live-verdict snapshot.
