# Repository Continuity status

> **Continuity role:** operational checkpoint
> **Status:** current
> **Last verified:** 2026-09-08
> **Owns:** verified current state, active work, known gaps, and next useful action
> **Update when:** a meaningful stopping point changes any of those facts

## Verified checkpoint

`specs/003-close-checkpoint-not-memoir.md` is accepted and retired. Close
files a STATUS snapshot and a conversational report.

Verification performed:

```text
python3 -m unittest discover -s tests -v
python3 skills/manage-project-docs/scripts/check_docset.py .
```

Evidence of success:

```text
6 tests OK; check_docset 0 errors
```

## Working now

- Six continuity operations, two agent routers over one shared core
- Checker fixtures: healthy, drifted, close-residue
- Close eval fixture in the private eval workspace (D-002)

## Incomplete or broken

- `specs/002-portable-eval-harness.md` is still draft
- Close eval is one run per condition, not a three-run benchmark
- Plan and Promote remain untested in the field
- `/specs` and `/skills-claude` are gitignored; Claude router edits are local only

## Active work

- Accepted spec: none
- Current focus: none
- Blockers: none

## Next useful action

Decide on `specs/002-portable-eval-harness.md` (accept, revise, or reject).

## Re-entry notes

- Configuration required: none
- Persistent state: Git worktree only
- External dependencies: none for unit tests and checker
- Recovery warning: close eval runs live outside this repository
