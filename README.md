# Repository Continuity

> **Continuity role:** operational front door
> **Status:** experimental
> **Last verified:** 2026-07-15
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
`skills-claude/`), generic document templates, six workflow references, and a
dependency-free structural documentation checker. The variants differ only in
their `SKILL.md` router; workflow references, templates, and scripts are owned
by the Codex package and shared into the Claude variant by relative symlink. The project is an early working version intended for
local pilots before a stable public release.

See [STATUS.md](STATUS.md) for the verified checkpoint and next work.

## Lifecycle

```text
repository state
    -> bootstrap or resume
    -> draft and accept a transition
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
| [specs/001-initial-skill.md](specs/001-initial-skill.md) | planning/history | accepted | initial public skill slice |

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
- The checker validates local file links but not Markdown anchor fragments.
- Installation and publication automation are intentionally deferred until the
  first local pilots establish the stable package shape.
