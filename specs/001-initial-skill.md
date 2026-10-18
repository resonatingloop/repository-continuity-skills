# Spec: initial public continuity skill

status: retired

> **Continuity role:** retired transition
> **Owner:** repository owner
> **Created:** 2026-07-15
> **Acceptance evidence:** the owner explicitly authorized building the public skill in the originating session
> **Supersedes:** none

## Context

A private multi-project documentation system established useful static
documents but exposed three additional needs: prevent idea discussions from
becoming implementation, resume dormant projects without remembered context,
and reconcile substantive documentation with code when one fact has several
representations. This slice creates a portable public Codex skill around that
continuity protocol without publishing private control-plane material.

## Scope

In:

- Initialize a public-ready Git repository and Codex skill package.
- Route bootstrap, resume, plan, close, audit, and promote operations.
- Provide generic reusable document templates.
- Provide a dependency-free structural documentation checker.
- Test the checker against sanitized healthy and drifted fixtures.
- Dogfood the continuity document set in this repository.

Out:

- Creating a GitHub remote or publishing the repository.
- Selecting a public license.
- Installing the skill globally.
- Editing any private project or control-plane document.
- Supporting non-Codex agent packaging.
- Adding third-party dependencies.

## Governing contracts and decisions

- `CONTRACTS.md`
- `DECISIONS.md` entries D-001 through D-004

## Change shape

| Dimension | Changed? | Source of truth | Proof |
|---|---:|---|---|
| User-visible behavior | yes | skill router and workflows | package review and forward test |
| Persisted state or schema | no | no runtime persistence | architecture review |
| External or provider-visible behavior | no | no external integration | architecture review |
| Identifiers, secrets or privacy | yes | public/private boundary | publication review |
| Lifecycle or terminal states | yes | spec and workflow model | instruction and fixture review |
| Setup, operation or recovery | yes | README and development guide | commands executed locally |
| Normative contract or decision | yes | contracts and decisions | explicit review |
| Cross-repository dependency | no | portable skill package | no private imports or paths |

## Implementation by invariant

1. Establish a concise skill router that preserves authorization and loads one
   detailed workflow at a time.
2. Establish distinct document owners for durable intent, current state,
   normative invariants, historical rationale, and proposed transitions.
3. Establish a generic checker whose clean result cannot be mistaken for
   semantic conformance.
4. Establish a public boundary through generic assets and sanitized fixtures.
5. Validate package shape, checker behavior, documentation structure, and
   private-content exclusion.

## Done when

- The official skill validator passes.
- Healthy fixtures pass and known drifted fixtures fail for the intended reasons.
- The repository's structural document check passes.
- No unresolved template placeholders exist outside template assets.
- Public review finds no private paths, projects, reports, or personalized rules.
- `STATUS.md` records the verified checkpoint.

## Risks and unknowns

- Trigger language may be too broad or too narrow until forward-tested.
- The initial document bundle may need lighter profiles after real bootstrap use.
- Strong-claim review may produce too much noise on large repositories.

## Open questions

- Public license selection remains intentionally outside this slice.

## Completion

Retired on 2026-07-15 after:

- four checker unit tests passed;
- the repository documentation check reported zero errors and warnings;
- the official skill validator passed;
- the checker compiled successfully;
- private-content review found no originating project names, reports, or
  personal filesystem paths.

Forward-testing, licensing, remote creation, and publication remain explicitly
outside this completed slice.
