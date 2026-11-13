# Repository Continuity contracts

> **Continuity role:** normative invariants
> **Status:** current
> **Last verified:** 2026-11-12
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
| Generated change-atlas behavior | `skills/manage-project-docs/scripts/render_change_atlas.py` and `CHANGE_ATLAS.template.html` | renderer unit tests and browser inspection |
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
| `RC-007` | Close overwrites `STATUS.md` as a snapshot and reports the session to the owner; it does not create close-memoir documents or restated contracts. | `references/close.md`, `references/document-model.md`, checker warnings | `tests/test_check_docset.py`, close eval |
| `RC-008` | A change atlas is a deterministic advisory projection of one canonical Markdown spec revision. It cannot accept, modify or replace that spec. | `references/plan.md`, renderer, atlas template | renderer tests, exact-output check and instruction review |
| `RC-009` | Before a material terminal claim, Close seals actual rather than anticipated consequence and returns `closed`, `partial`, or `divergent`; only `closed` may retire the accepted spec. | `SKILL.md`, `references/close.md`, `references/transition-seal.md` | instruction review and private close eval |
| `RC-010` | Adversarial review is risk-triggered rather than universal: deterministic consequence signals choose the route, reviewers remain independent and read-only, and findings retain epistemic status until reconciled. | `SKILL.md`, `references/risk-gates.md`, `references/plan.md`, `references/close.md` | instruction review; sanitized private-eval evidence recorded in D-011 |

## Interfaces and boundaries

- The installable interface is the complete `skills/manage-project-docs/` directory.
- `SKILL.md` routes operations; direct reference files own the detailed procedures.
- Templates are assets copied into output repositories only during authorized work.
- The generic checker may inspect Markdown but must not execute project commands.
- The change-atlas renderer reads one explicitly named spec and optional local
  raster review images, then writes one explicitly named local HTML output.
- Generated atlases contain no JavaScript, remote assets, server, telemetry or
  browser-to-repository write path.
- Project-specific semantic proof remains in the target repository.
- Actual-change receipts are transient seam inputs. The continuity close owns
  promotion into repository truth; an implementation workflow cannot seal its
  own receipt merely by producing it.
- Risk-gate receipts identify the reviewed source or diff revision. They are
  evidence for Close, not authority to edit files or promote raw findings into
  contracts, decisions, status, or continuity memory.

## Data and schema

The skill stores no runtime data. It reads repository files and, during an
authorized operation, may create or edit Markdown using the bundled templates.
The checker reads UTF-8 Markdown and emits findings to standard output. The
change-atlas renderer produces disposable static HTML; its source fingerprint
and exact-output check expose drift without making the HTML authoritative.

## Lifecycle and failure semantics

- Specs use `draft`, `accepted`, and `retired` states.
- `closed`, `partial`, and `divergent` are close-attempt outcomes, not additional
  spec lifecycle states.
- Ordinary verification is the default. Semantic preflight and a fresh diff
  adversary are summoned only when the shared risk-gate protocol's consequence
  signals apply.
- An atlas is current only when check mode byte-compares it successfully with a
  fresh render from the named spec, template and review images.
- Invalid or missing required structure causes the checker to exit nonzero.
- Warnings and strong-claim review items do not cause failure.
- Unknown or unprovable facts remain labeled unknown rather than reconstructed
  as exact.

## Privacy and secrets

- Do not read secret values to document their locations or sources.
- Do not copy target-repository content into public fixtures without explicit
  review and sanitization.
- Escape all spec-derived HTML text. Accept review images only from validated
  local PNG, JPEG or WebP files beneath the spec directory; reject path escape,
  symbolic links, SVG, remote sources and caller-supplied data URLs.
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
