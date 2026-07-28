# Repository Continuity contracts

> **Continuity role:** normative invariants
> **Status:** current
> **Last verified:** 2026-07-15
> **Owns:** confirmed promises the public skill must not drift from casually
> **Update when:** an authorized decision changes an invariant or its proof

A failing implementation is not, by itself, authorization to weaken these
contracts.

## Sources of truth

| Fact | Owner | Proof or inventory |
|---|---|---|
| Skill triggering and runtime routing | `skills/manage-project-docs/SKILL.md` | official skill validator plus review |
| Detailed operation procedure | matching file in `skills/manage-project-docs/references/` | direct-link and document checks |
| Reusable output shape | `skills/manage-project-docs/assets/templates/` | placeholder and fixture review |
| Generic structural checks | `skills/manage-project-docs/scripts/check_docset.py` | `tests/test_check_docset.py` |
| Public project state | `STATUS.md` | recorded validation commands and Git state |
| Repository licensing | `LICENSE` | GitHub license detection and direct review |

## Invariants

| ID | Claim | Representation owner | Proof |
|---|---|---|---|
| `RC-001` | Resume and audit are read-only unless the user explicitly authorizes changes. | `SKILL.md`, `resume.md`, `audit.md` | instruction review |
| `RC-002` | Only a human or designated owner may accept a draft spec. | `SKILL.md`, `plan.md`, spec template | instruction and template review |
| `RC-003` | Existing repository documents are never blindly overwritten from shared templates. | `SKILL.md`, `bootstrap.md`, `promote.md` | instruction review |
| `RC-004` | Generic checks do not claim to prove project-specific semantics. | `SKILL.md`, checker help and README | unit and prose review |
| `RC-005` | Detailed workflows load through direct references instead of bloating routine skill context. | `SKILL.md`, `references/` | official validator and link check |
| `RC-006` | Public artifacts contain no private registry, audit report, local path, or personalized authorization rule. | entire repository | private-content review before publication |

## Interfaces and boundaries

- The installable interface is the complete `skills/manage-project-docs/` directory.
- `SKILL.md` routes operations; direct reference files own the detailed procedures.
- Templates are assets copied into output repositories only during authorized work.
- The generic checker may inspect Markdown but must not execute project commands.
- Project-specific semantic proof remains in the target repository.

## Data and schema

The skill stores no runtime data. It reads repository files and, during an
authorized operation, may create or edit Markdown using the bundled templates.
The checker reads UTF-8 Markdown and emits findings to standard output.

## Lifecycle and failure semantics

- Specs use `draft`, `accepted`, and `retired` states.
- Invalid or missing required structure causes the checker to exit nonzero.
- Warnings and strong-claim review items do not cause failure.
- Unknown or unprovable facts remain labeled unknown rather than reconstructed
  as exact.

## Privacy and secrets

- Do not read secret values to document their locations or sources.
- Do not copy target-repository content into public fixtures without explicit
  review and sanitization.
- Audit and resume reports may describe private repositories locally, but the
  reusable skill package must contain only generic examples.

## Required validation

```text
python3 -m unittest discover -s tests -v
python3 skills/manage-project-docs/scripts/check_docset.py .
python3 /path/to/skill-creator/scripts/quick_validate.py skills/manage-project-docs
```

## Intentionally unspecified

- Public release cadence.
- Git hosting organization and repository URL.
- Compatibility adapters for agent products other than Codex.
- Whether future versions use a machine-readable per-project manifest.
