# Repository Continuity

> **Continuity role:** operational front door
> **Status:** experimental
> **Last verified:** 2026-11-06
> **Owns:** the public purpose, installation path, lifecycle overview, and documentation map
> **Update when:** skill installation, supported workflows, maturity, or document authority changes

## The substrate

`state → ui → event → new state → ui`

> that is basically the whole goblin in its polite blazer.

Repository Continuity is an agent skill and document toolkit — packaged for
both Codex and Claude Code — for preserving a software project's usable state
across sessions, collaborators, and periods of dormancy. It treats documentation as durable state, approved workflows as
state transitions, and executable checks as invariant proofs.

It is not a README generator. It helps an agent bootstrap, resume, plan, close,
audit, and improve a repository documentation lifecycle without confusing
historical intent, current behavior, normative contracts, and proposed work.

## Current state

The repository contains an installable `manage-project-docs` skill in two
agent-shaped variants (Codex under `skills/`, Claude Code under
`skills-claude/`), generic document templates, six workflow references, a
dependency-free structural documentation checker, and a deterministic static
change-atlas renderer. The variants differ only in
their `SKILL.md` router; workflow references, templates, and scripts are owned
by the Codex package and shared into the Claude variant by relative symlink. The project is an early working version intended for
local pilots before a stable public release.

See [STATUS.md](STATUS.md) for the verified checkpoint and next work.

## Lifecycle

```text
repository state
    -> bootstrap or resume
    -> draft a canonical transition
    -> render its advisory change atlas
    -> explicitly accept or reject the canonical spec
    -> implement by invariant
    -> reconcile and close
    -> new repository state
    -> periodic audit and promoted lessons
```

The human or designated project owner approves consequential transitions. The
skill preserves that authority; discussion and read-only diagnosis do not
silently become implementation.

## Install the skill locally

For Codex, copy the complete skill directory into a Codex skills directory:

```text
skills/manage-project-docs/ -> ~/.codex/skills/manage-project-docs/
```

For Claude Code, copy the Claude variant with symlinks dereferenced:

```text
cp -rL skills-claude/manage-project-docs ~/.claude/skills/manage-project-docs
```

Keep `SKILL.md`, `references/`, `assets/`, and `scripts/` together (plus
`agents/` for Codex). The skill directories intentionally have no separate
README; this repository front door is for humans, while the skill packages
contain only agent runtime material.

Example prompts (Codex uses `$manage-project-docs`, Claude Code
`/manage-project-docs` or plain natural language):

```text
Use manage-project-docs to resume this repository without changing files.
Use manage-project-docs to draft a continuity spec for this feature.
Use manage-project-docs to audit the documentation against the live code.
```

## Render a change atlas

For an authorized saved material spec, generate a local owner-facing review
surface while keeping the Markdown source canonical:

```text
python3 skills/manage-project-docs/scripts/render_change_atlas.py specs/example.md --output build/change-atlas/example.html
python3 skills/manage-project-docs/scripts/render_change_atlas.py specs/example.md --output build/change-atlas/example.html --check
```

The static page exposes its source path and fingerprint, performs no network
access, and retains the complete escaped spec beneath the visual review layer.
It cannot accept or modify the spec.

## spec companions in codex

when `attention-aperture` is already available, the Codex Plan router
automatically reads it while creating or materially revising an authorized
saved spec. it adds a source-linked anatomy/trace or dense-plan review when
one of the installed skill's instruments fits. no second invocation is needed.
text-only requests skip visual output; absent tooling or unsupported material
falls back to the ordinary atlas with a short explanation.

the companion is a separate local bundle with declared coverage and source
fingerprints. it does not replace the atlas, accept the spec, or add a runtime
dependency to this package. see the [companion handoff](skills/manage-project-docs/references/spec-companion.md)
for selection, freshness, and authority rules.

## Run the structural checker

```text
python3 skills/manage-project-docs/scripts/check_docset.py .
python3 skills/manage-project-docs/scripts/check_docset.py . --review-claims
```

The checker validates repository-independent structure. It does not claim to
prove project semantics such as provider payloads, privacy boundaries, schema
compatibility, or lifecycle behavior; those proofs remain project-owned.

## Test

```text
python3 -m unittest discover -s tests -v
```

## Documentation authority

| Document | Role | Status | Owns |
|---|---|---|---|
| `README.md` | operational | current | public front door and lifecycle overview |
| [STATUS.md](STATUS.md) | operational | current | verified checkpoint and next action |
| [AGENTS.md](AGENTS.md) | behavioral | current | authorization and contribution protocol |
| [PROJECT_BRIEF.md](PROJECT_BRIEF.md) | durable intent | current | purpose, scope, goals and non-goals |
| [CONTRACTS.md](CONTRACTS.md) | normative | current | portable skill invariants and proof boundaries |
| [DECISIONS.md](DECISIONS.md) | historical | append-only | accepted rationale and supersession |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | descriptive/current | current | implemented package and workflow shape |
| [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | operational | current | local validation and release preparation |
| [specs/001-initial-skill.md](specs/001-initial-skill.md) | planning/history | retired | initial public skill slice |
| [specs/003-close-checkpoint-not-memoir.md](specs/003-close-checkpoint-not-memoir.md) | planning/history | retired | compact close behavior |
| [specs/004-change-atlas.md](specs/004-change-atlas.md) | planning/history | retired | canonical-spec and visual-approval split |

## Public boundary

This repository contains generic workflows, templates, checks, and sanitized
fixtures. A user's private project registry, audit reports, local paths,
personal authorization language, and project-specific contracts belong in a
separate local control plane.

## License

Repository Continuity is available under the [MIT License](LICENSE).
Copyright (c) 2026 resonatingloop.

## Known limitations

- The skill has not yet been forward-tested against multiple fresh repositories.
- The change atlas has not yet been field-tested on the next live owner approval.
- Review visuals accept local PNG, JPEG and WebP files; arbitrary Markdown HTML,
  remote assets and SVG are deliberately unsupported.
- The checker validates local file links but not Markdown anchor fragments.
- Installation and publication automation are intentionally deferred until the
  first local pilots establish the stable package shape.
