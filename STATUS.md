# Status — live judged release

**State: complete; the live evaluator recorded 12/12.**

## Standard audit record

`ALL_SIX_CLAIMS_FALSIFIED_C1_C4_HIGH_CONFIDENCE_C5_C6_MEDIUM_CONFIDENCE_LIVE_SCORE_12_OF_12`

| Gate | Value |
| --- | --- |
| Live judge score | `12/12`, verified snapshot |
| Current score claim | `true` |
| Publication gate | `passed` |
| Official author endorsement | `false` |
| Publication authorization | `false` |

The current live-judge snapshot is authoritative for the score and final
verdict. Older top-level route artifacts are preserved as development history;
they are not the final claim status.

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
