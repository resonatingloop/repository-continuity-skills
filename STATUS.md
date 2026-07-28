# Repository Continuity status

> **Continuity role:** operational checkpoint
> **Status:** current
> **Last verified:** 2026-07-24
> **Owns:** verified current state, active work, known gaps, and next useful action
> **Update when:** a meaningful stopping point changes any of those facts

## Verified checkpoint

The `manage-project-docs` skill now ships in two agent-shaped variants: the
original Codex package under `skills/` and a Claude Code router under
`skills-claude/` that shares the workflow references, templates, and checker
through relative symlinks (see D-006). The repository otherwise contains the
six progressively loaded workflow references, ten reusable document templates,
a dependency-free structural checker, and sanitized healthy and drifted
checker fixtures.

Verification performed:

```text
python3 -m unittest discover -s tests -v
python3 skills/manage-project-docs/scripts/check_docset.py .
python3 skills-claude/manage-project-docs/scripts/check_docset.py .
python3 <skill-creator>/scripts/quick_validate.py skills-claude/manage-project-docs
```

Evidence of success:

- Four checker unit tests passed.
- The repository check reported zero errors and zero warnings through both
  the Codex path and the symlinked Claude path.
- The official skill validator reported `Skill is valid!` for the Claude
  variant.

## Working now

- Skill routing covers bootstrap, resume, plan, close, audit, and promotion.
- Detailed procedures are progressively disclosed through direct references.
- Generic document templates are separated from runtime instructions.
- The checker uses only the Python standard library.

## Incomplete or broken

- Forward-testing has covered the Bootstrap, Resume, and Audit workflows via
  subagent evals against three synthetic repositories (three feedback
  iterations, all assertions passing); Plan, Close, and Promote remain
  untested in the field.
- No GitHub remote has been created.
- Optional whole-repository strong-claim review is noisy; changed-file scoping
  is a likely later refinement.

## Active work

- Accepted spec: none; `specs/001-initial-skill.md` is retired and
  `specs/002-portable-eval-harness.md` is a draft awaiting an owner decision
- Current focus: none
- Blockers: none

## Next useful action

Decide on `specs/002-portable-eval-harness.md` (accept, revise, or reject).
Independently of that decision, the repository is ready for license-confirmed
publication to a public remote. Owner-feedback refinements from the eval
iterations are already reconciled into `references/resume.md`,
`references/bootstrap.md`, and the README template; the eval workspace lives
outside this repository per D-002.

## Re-entry notes

- Configuration required: none
- Persistent state: Git worktree only
- External dependencies: none for local validation
- Recovery warning: review the final diff and remote target before publishing
