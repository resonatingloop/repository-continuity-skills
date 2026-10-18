# Repository Continuity architecture

> **Continuity role:** implemented system model
> **Status:** current
> **Last verified:** 2026-10-17
> **Owns:** package components, boundaries, workflow routing, and proof layers
> **Update when:** structural implementation changes

## System context

```text
user request
    -> Codex skill metadata triggers manage-project-docs
    -> SKILL.md selects one operation and preserves authorization
    -> one workflow reference supplies detailed procedure
    -> optional template assets create authorized project documents
    -> Plan may project one saved spec through the local change-atlas renderer
    -> owner reviews the atlas and explicitly accepts or rejects the canonical spec
    -> generic checker validates structured facts
    -> target repository tests prove project-specific semantics
```

The public repository packages the generic layer. A user's local control plane
may maintain a project registry, private reports, custom policies, and
additional checks without entering the public package.

## Components

| Component | Path | Responsibility | Public seam |
|---|---|---|---|
| Skill router | `skills/manage-project-docs/SKILL.md` | trigger coverage, authorization, operation selection | Codex skill contract |
| Workflow references | `skills/manage-project-docs/references/` | detailed bootstrap, resume, plan, close, audit and promotion procedures | direct links from `SKILL.md` |
| Template assets | `skills/manage-project-docs/assets/templates/` | generic document scaffolds copied into target repositories | Markdown files |
| Change-atlas renderer | `skills/manage-project-docs/scripts/render_change_atlas.py` | safe deterministic owner-facing projection of one canonical spec | static local HTML and exact-output check |
| Structural checker | `skills/manage-project-docs/scripts/check_docset.py` | repository-independent documentation findings | command-line exit and text output |
| Validation fixtures | `tests/fixtures/` | sanitized healthy and drifted document sets | unit tests |

## Workflow state

```text
unbootstrapped
    -> documented checkpoint
    -> draft spec
    -> generated atlas (advisory, current or stale)
    -> owner-accepted spec
    -> authorized implementation
    -> reconciled checkpoint
    -> retired spec
```

`resume` and `audit` observe state without transitioning it. `promote` changes
the reusable protocol only after a local lesson is classified and generalized.

## Proof layers

1. Official skill validation proves package shape and metadata syntax.
2. Unit tests prove generic checker behavior against sanitized fixtures.
3. Renderer tests prove escaping, local-image containment, deterministic
   freshness checks and overwrite refusal.
4. Browser inspection proves the generated atlas is legible at desktop and
   narrow widths; it does not prove owner approval or source semantics.
5. The checker proves cheap structured facts in a target repository.
6. Target-repository tests prove semantics such as wire behavior, state
   transitions, privacy, migrations, and composed integrations.
7. Human review resolves intent, authority, and strong prose claims that cannot
   be reduced safely to string checks.

## Important boundaries

- Runtime skill context stays concise; detailed workflows load on demand.
- Template assets do not become authority until filled and adopted locally.
- Generated atlases are disposable views. Their visible source fingerprint and
  byte-comparison check bind them to the canonical spec without promoting them
  to project truth.
- The renderer interprets no raw Markdown HTML, performs no network access and
  embeds only validated local raster review images.
- Shared updates never automatically overwrite filled downstream documents.
- Generic clean checks never imply semantic documentation correctness.

## Known structural pressure

- A future machine-readable project manifest may improve repeatable check
  selection, but its ownership and duplication costs have not been proven.
- Cross-agent adapters may need product-specific packaging while keeping these
  workflow references canonical.
