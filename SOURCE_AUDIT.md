# Source audit

The detailed primary-source record is [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md).

## Pinned paper and release records

| Source | Identifier/hash | Role |
| --- | --- | --- |
| Paper | [arXiv:2509.24757](https://arxiv.org/abs/2509.24757) | Exact claim wording and theorem source |
| OpenReview | [TBSyYj4VV6](https://openreview.net/forum?id=TBSyYj4VV6) | Submission record |
| Retained source archive | `bd48105ab08395ba1edbdb3a407eee9f2e1a8464521d7d67dbe5b6e96edf2549` | Source hash recorded by the audit |
| Live judge snapshot | `.trackio/logbook/evidence/release/live_judge_verdict.json` | Final `12/12`, all six falsified |
| Live snapshot SHA | `8ca97b16e85f7220d5298dc4607f7623df2b5241` | Evaluator revision and score record |

## Version boundary

The older top-level `outputs/verdict.json` is a pre-live route record: it
contains one exact C1 falsification, a scoped C3 display counterexample, and
blocked C2/C4/C5/C6 routes. Later statevector and scale evidence resolved the
remaining headline claims. The `.trackio/logbook/evidence/release/` snapshot
and final release report are therefore the authoritative final evidence.

The audit targets the named algorithms and exact contracts. It does not claim
that every possible quantum regression algorithm fails, and it uses CPU and
statevector simulation only—no quantum hardware or GPU.
