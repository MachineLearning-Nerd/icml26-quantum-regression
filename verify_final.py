#!/usr/bin/env python3
"""Verify the public documentation, branch namespace, and live score record."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPOSITORY = "MachineLearning-Nerd/icml26-quantum-regression"
CANONICAL = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"
OVERALL_STATUS = (
    "ALL_SIX_CLAIMS_FALSIFIED_C1_C4_HIGH_CONFIDENCE_"
    "C5_C6_MEDIUM_CONFIDENCE_LIVE_SCORE_12_OF_12"
)
EXPECTED_BRANCHES = {
    "main",
    "audit/c1-evaluator-falsification-artifact",
    "audit/c1-qglmsparsify-contract",
    "audit/c2-c4-c5-c6-four-route",
    "audit/c3-lasso-counterexample",
    "audit/c6-negative-control",
    "audit/downstream-corollary-adjudication",
    "audit/judged-baseline",
    "audit/remove-workspace-reference",
    "audit/supplemental-scale",
    "audit/verifier-source-links",
    "experiment/statevector-quantum-lars",
    "integration/corrected-claim-scope",
    "integration/github-publication",
    "integration/repaired-claims-appendix",
    "release/evaluator-visible-complete",
    "release/final-hf-provenance",
    "release/final-six-claim",
    "release/final-statevector",
    "release/icml-template-hardware",
    "release/leaderboard-candidate",
    "release/protected-history",
    "release/space-metadata",
    "release/statevector-evidence",
    "release/trackio-dependency-disclosure",
}
REQUIRED_FILES = {
    "README.md",
    "STATUS.md",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "docs/SOURCE_AUDIT.md",
    "ENVIRONMENT.md",
    "REPORT.md",
    "branch-audit.md",
    "repro/src/verify.py",
    "repro/src/publication_gate.py",
    "outputs/verdict.json",
    "outputs/publication_gate.json",
    ".trackio/logbook/evidence/release/live_judge_verdict.json",
    ".trackio/logbook/evidence/release/final_release_report.md",
    ".trackio/logbook/pages/claim-1/page.md",
    ".trackio/logbook/pages/claim-2/page.md",
    ".trackio/logbook/pages/claim-3/page.md",
    ".trackio/logbook/pages/claim-4/page.md",
    ".trackio/logbook/pages/claim-5/page.md",
    ".trackio/logbook/pages/claim-6/page.md",
    "claims.json",
    "reproduction_verdicts.json",
    "AUTONOMOUS_STATE.json",
    "CITATION.cff",
    "AUTHOR_THANK_YOU.md",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
}


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def main() -> None:
    missing = sorted(path for path in REQUIRED_FILES if not (ROOT / path).exists())
    assert not missing, f"missing required files: {missing}"
    assert not git("status", "--porcelain"), "working tree is not clean"
    assert not git("for-each-ref", "--format=%(refname)", "refs/original"), "refs/original remains"

    remote = git("remote", "get-url", "origin").removesuffix(".git")
    assert remote.endswith(REPOSITORY), remote
    branch_lines = git("ls-remote", "--heads", "origin").splitlines()
    remote_branches = {
        line.split("\t", 1)[1].removeprefix("refs/heads/")
        for line in branch_lines
        if "\t" in line
    }
    assert remote_branches == EXPECTED_BRANCHES, remote_branches
    assert git("symbolic-ref", "--short", "refs/remotes/origin/HEAD") == "origin/main"

    identities = set(git("log", "--all", "--format=%an <%ae> | %cn <%ce>").splitlines())
    assert identities == {f"{CANONICAL} | {CANONICAL}"}, identities
    assert "Co-authored-by:" not in git("log", "--all", "--format=%B")

    claims = json.loads((ROOT / "claims.json").read_text())
    assert claims["overall_status"] == OVERALL_STATUS
    assert [claim["id"] for claim in claims["claims"]] == ["C1", "C2", "C3", "C4", "C5", "C6"]
    assert {claim["status"] for claim in claims["claims"]} == {
        "FALSIFIED_HIGH_CONFIDENCE",
        "FALSIFIED_MEDIUM_CONFIDENCE",
    }

    live = json.loads((ROOT / ".trackio/logbook/evidence/release/live_judge_verdict.json").read_text())
    assert live["total_score"] == "12/12"
    assert live["quality"] == "high"
    assert live["sha"] == "8ca97b16e85f7220d5298dc4607f7623df2b5241"
    assert {claim["verdict"] for claim in live["claims"]} == {"falsified"}

    state = json.loads((ROOT / "AUTONOMOUS_STATE.json").read_text())
    assert state["overall_status"] == OVERALL_STATUS
    assert state["current_score_claim"] is True
    assert state["publication_allowed"] is False

    print(
        "FINAL_AUDIT=VERIFIED "
        f"branches={len(remote_branches)} commits={git('rev-list', '--all', '--count')} "
        "claims=C1:C6_falsified,C1:C4_high_confidence,C5:C6_medium_confidence "
        "historical_score=12/12 current_score_claim=true publication_allowed=false"
    )


if __name__ == "__main__":
    main()
