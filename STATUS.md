# Repository Continuity status

> **Continuity role:** operational checkpoint
> **Status:** current
> **Last verified:** 2026-09-08
> **Owns:** verified current state, active work, known gaps, and next useful action
> **Update when:** a meaningful stopping point changes any of those facts

## Verified checkpoint

`specs/002-portable-eval-harness.md` is rejected (D-008). Eval loops stay in
the private workspace. Spec status `rejected` is a valid terminal state.

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
- Close eval fixture in the private eval workspace (D-002, D-008)

## Incomplete or broken

- Close eval is one run per condition, not a three-run benchmark
- Plan and Promote remain untested in the field
- `/specs` and `/skills-claude` are gitignored; Claude router edits are local only

## Active work

- Accepted spec: none
- Current focus: none
- Blockers: none

## Next useful action

None. Forward-tests of Plan or Promote, if wanted, belong in the private
eval workspace.

## Re-entry notes

- Configuration required: none
- Persistent state: Git worktree only
- External dependencies: none for unit tests and checker
- Recovery warning: close eval runs live outside this repository
