# Repository Continuity status

> **Continuity role:** operational checkpoint
> **Status:** current
> **Last verified:** 2026-11-12
> **Owns:** verified current state, active work, known gaps, and next useful action
> **Update when:** a meaningful stopping point changes any of those facts

## Verified checkpoint

Repository Continuity now pairs two distinct implementation boundaries. The
risk gate controls passage: ordinary verification remains the default, while
deterministic consequence signals may summon a read-only semantic preflight or
fresh diff adversary. The transition seal controls promotion: Close consumes
the reconciled receipts, reclassifies realized change shape, and returns
`closed`, `partial`, or `divergent`. Only `closed` may retire an accepted spec.

A bounded private five-model evaluation completed 120 semantic observations.
Under its provisional labels, including one preserved routing dispute, no model
matched every route; adversarial consequential-finding gains varied from
material improvement to regression. The evidence supports selective,
deterministically triggered opposition; it does not support universal review or
model self-routing.

The Codex router and local Claude router both route triggered review through the
shared risk-gate reference and terminal claims through Close and the transition
seal. No new skill, runtime dependency, receipt ledger, or close memoir was
added.

Verification performed:

```text
python3 -m unittest discover -s tests -v
python3 skills/manage-project-docs/scripts/check_docset.py .
python3 <skill-creator>/scripts/quick_validate.py skills/manage-project-docs
python3 <skill-creator>/scripts/quick_validate.py skills-claude/manage-project-docs
```

Evidence of success:

```text
17 tests OK; check_docset 0 errors and 0 warnings; Codex package and local Claude adapter valid
```

## Working now

- Six continuity operations over one shared workflow core
- Deterministic, risk-triggered semantic preflight and diff adversary protocol
- Independent read-only reviewers; one implementing writer
- Reconciled finding statuses without automatic memory promotion
- Transition seal with `closed`, `partial`, and `divergent` close outcomes
- Optional consumption or reconstruction of an actual-change receipt
- Risk-gate receipt freshness and reconciled epistemic dispositions at close
- Codex saved-spec handoff to an available visual-companion skill
- Static deterministic change-atlas renderer and structural document checker
- Checker fixtures for healthy, drifted, and close-residue states

## Incomplete or broken

- The transition seal and receipt seam need a fresh-session end-to-end eval.
- The risk-gate result is one bounded private evaluation, not multi-repository
  field proof.
- Close eval remains one run per condition rather than a three-run benchmark.
- The new semantic terminal-claim routing has not yet been exercised through a
  real `partial` or `divergent` close.
- The saved-spec companion handoff still needs its first fresh-session use.
- Independent review of the HTML trust boundary remains a release gate.
- Draft, rejected, and generated spec artifacts remain ignored unless
  deliberately promoted.
- `/skills-claude` is gitignored; Claude router edits are local only.

## Active work

- Accepted spec: none
- Current focus: forward validation of the risk-gate and transition-seal seam
- Blockers: none

## Next useful action

Run sanitized transition-seal slices whose realized outcomes should be
`closed`, `partial`, and `divergent`, then exercise the risk gate on a repository
shape unrelated to the originating cases. Include fresh and stale review
receipts and a boundary the opening plan did not predict.

## Re-entry notes

- Configuration required: none
- Persistent state: this repository checkpoint plus a separate local Codebase
  Care source checkout
- External dependency: none; the producer-consumer seam is optional
- Local Claude router: changed but ignored by Git
- Recovery warning: no push, installation, deployment, or publication is part
  of this slice
