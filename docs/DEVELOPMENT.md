# Repository Continuity development

> **Continuity role:** operational procedure
> **Status:** current
> **Last verified:** 2026-07-15
> **Owns:** exact local validation and publication-preparation procedures
> **Update when:** commands, dependencies, or package layout change

## Prerequisites

- Python 3.10 or newer for the checker and tests.
- A local Codex installation containing the system `skill-creator` utilities
  for official skill validation.

The skill and its checker have no third-party runtime dependencies.

## Run unit tests

```text
python3 -m unittest discover -s tests -v
```

## Run repository documentation checks

```text
python3 skills/manage-project-docs/scripts/check_docset.py .
```

Review strong claims without changing the exit status:

```text
python3 skills/manage-project-docs/scripts/check_docset.py . --review-claims
```

## Validate the skill package

Run the installed `skill-creator` validator against the complete skill
directory. A common local form is:

```text
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/manage-project-docs
```

Do not commit a machine-specific absolute path into executable configuration.

## Prepare for public review

1. Run all three validation layers above.
2. Inspect `git diff --check` and `git status`.
3. Search for home-directory paths, usernames, private project names, secrets,
   and raw audit material.
4. Confirm `STATUS.md` and the active spec reflect the result.
5. Confirm GitHub detects the root `LICENSE` as MIT.
6. Forward-test the skill against sanitized or disposable repositories.

## Recovery

The checker is read-only. If a test fixture is damaged, restore only the
fixture from version control; do not point repair code at a live repository.
