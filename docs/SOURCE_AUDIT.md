# Primary-source audit

Paper: **Accelerating Regression Tasks with Quantum Algorithms**, by Chenghua
Liu and Zhengfeng Ji. See the [arXiv record](https://arxiv.org/abs/2509.24757)
and [HTML source](https://arxiv.org/html/2509.24757).

OpenReview identifier: `TBSyYj4VV6`.

Pinned public source archive SHA-256:
`bd48105ab08395ba1edbdb3a407eee9f2e1a8464521d7d67dbe5b6e96edf2549`.

The final evaluator-facing release records **12/12** and marks all six claims
`FALSIFIED`. The audit targets the exact named algorithms and contracts; it
does not replace a universal quantum-algorithm proof with a finite benchmark.

| Claim | Primary source anchor | Reproduction route | Current basis |
|---|---|---|---|
| C1 | Theorem 10 / Algorithm 2 | GLM sparsifier-size/runtime contract, statevector sampler, boundary controls | `M=Theta~(n/epsilon^2)` exceeds the cited sampler domain and the explicit loop has the wrong fixed-dimension epsilon power |
| C2 | Corollary 23 | Downstream contract audit and quantum-sampled linear solve | Inherits the exact QGLMSparsify domain/runtime contradiction |
| C3 | Corollary 26 | Prior-art/date audit, quantum LARS, objective mapping, exact display counterexample | Quantum Lasso work from 2021 and 2023 predates the target; the printed inequality also has a `7/40` gap |
| C4 | Corollary 25 | `[A;sqrt(lambda)I]`, `[b;0]` identity and downstream audit | Valid Ridge reduction inherits Claim 2’s exact contradiction |
| C5 | Corollary 12 with `p=1` | `gamma_1`/Huber identity, in-domain execution, domain audit | Universal all-epsilon framework invokes the cited sampler outside its stated domain |
| C6 | Corollary 11 with `p in (0,2]` | p-homogeneity, `p=3/2` execution, domain audit | Universal all-epsilon framework invokes the cited sampler outside its stated domain |

## Source precision note

The displayed Lasso corollary’s right-hand minimand omits `lambda` on its
final `||x||_1` term, while the preceding reduction and left-hand side use the
standard `lambda||x||_1` objective. The audit retains `lambda` for the
source-faithful reduction and separately records the literal display defect;
it does not silently treat the typo as a different Lasso objective.
