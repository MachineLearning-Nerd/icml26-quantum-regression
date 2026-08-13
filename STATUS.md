# Status — live judged release

**State: complete; the live evaluator recorded 12/12.**

- Paper: [arXiv:2509.24757](https://arxiv.org/abs/2509.24757)
- Authors: Chenghua Liu and Zhengfeng Ji
- Live verdict revision: `8ca97b16e85f7220d5298dc4607f7623df2b5241`
- Quality: `high`
- Claims 1–6: `FALSIFIED`
- Confidence: high for Claims 1–4; medium for Claims 5–6
- Canonical snapshot: `.trackio/logbook/evidence/release/live_judge_verdict.json`

Claims 1–4 have exact sampler-domain/runtime or prior-art contradictions.
Claims 5–6 have exact all-epsilon sampler-domain contradictions, with
additional in-domain specialization checks. The result applies to the named
paper contracts, not every conceivable quantum regression algorithm.

The earlier 0/12 and 4/12 records remain available as historical development
evidence. The older `current-claim-*` pages and top-level `outputs/*` route
artifacts should not be read as the current live verdict; see the root
[README](README.md) and [branch audit](branch-audit.md).
