# Repository Continuity agent guide

This file governs AI coding agents working in this repository. Read it before
acting.

## Required reading

1. `README.md` for the public front door and authority map.
2. `STATUS.md` for the verified checkpoint.
3. `CONTRACTS.md` before changing skill behavior or checker semantics.
4. The active accepted spec in `specs/`, when one exists.
5. `PROJECT_BRIEF.md` for generative or scope-changing work.

If documents disagree, identify which one owns the disputed fact. Do not infer
authority from filenames alone. Surface unresolved conflicts before editing.

## Authorization

- Discussion, brainstorming, critique, planning, resume, and audit requests are
  read-only unless the user explicitly requests changes.
- A direct bounded change request authorizes that change.
- Substantial, ambiguous, or cross-cutting implementation requires an accepted
  spec or equivalent explicit approval from the repository owner.
- Agents may draft specs. Only the repository owner may accept them.
- Never weaken a normative contract solely to match current implementation.

## Repository boundaries

- `skills/manage-project-docs/SKILL.md` owns runtime routing and essential
  instructions for the Codex variant.
- `skills-claude/manage-project-docs/SKILL.md` owns the Claude Code variant's
  routing; its `references/`, `assets/`, and `scripts/` are relative symlinks
  into the Codex package, which remains the single owner of shared material.
  Agent-specific behavior belongs in the variant routers, never in the shared
  references.
- `skills/manage-project-docs/references/` owns detailed workflow procedures.
- `skills/manage-project-docs/assets/templates/` contains generic output assets;
  it must not contain private project details.
- `skills/manage-project-docs/scripts/` contains deterministic generic checks,
  never project-specific semantic claims.
- The installable skill directory must remain free of auxiliary README,
  changelog, installation, or project-history files.
- Dependencies require explicit approval. Prefer the Python standard library.

## Common commands

```text
python3 -m unittest discover -s tests -v
python3 skills/manage-project-docs/scripts/check_docset.py .
python3 /path/to/skill-creator/scripts/quick_validate.py skills/manage-project-docs
```

The last command's prefix depends on the local Codex installation.

## Working protocol

Before changing files:

1. Read the governing documents for the task.
2. Inspect version-control status.
3. State the authorized slice and likely proof.

During implementation:

1. Keep `SKILL.md` concise and route detailed material to direct references.
2. Keep workflows tool-neutral where possible.
3. Test scripts by executing them against sanitized fixtures.
4. Do not add personal paths, project names, reports, or private examples.

Before completion:

1. Revisit the accepted spec's change-shape matrix when applicable.
2. Reconcile skill instructions, references, assets, scripts, tests, and public docs.
3. Update `STATUS.md` at a meaningful checkpoint.
4. Record consequential decisions without manufacturing rationale.
5. Run the unit tests, document checker, and official skill validator.
6. Report unresolved unknowns and the next authorized transition.

## Stop and ask

- Public licensing must be selected or changed.
- A change would publish user-specific or private material.
- Skill behavior would perform writes during resume or audit by default.
- A new runtime dependency appears necessary.
- The requested change exceeds the authorized slice.
