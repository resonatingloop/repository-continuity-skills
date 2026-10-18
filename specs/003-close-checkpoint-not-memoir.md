# Spec: close checkpoint, not session memoir

status: retired

> **Continuity role:** retired transition
> **Owner:** repository owner
> **Created:** 2026-09-08
> **Accepted:** 2026-09-08
> **Acceptance evidence:** owner wrote "accept and merge"
> **Supersedes:** none

## Context

Close currently has no stop-writing rule. Honesty is unbounded, so slices
accrete `VERIFICATION.md`, stacked STATUS headings, README threat-model
copies, and session affidavits. That residue recreates "too much" even when
code and contracts are sound. Audience is the repository owner and future
agents, not a public contributor.

## Scope

In:

- Close writes a STATUS snapshot and a conversational report; it does not
  create close-memoir documents.
- Document model: one owner per fact; STATUS is overwrite-in-place; README
  is the owner's front door.
- Checker warnings for `VERIFICATION.md` and extra STATUS headings.
- A close eval fixture in the private eval workspace (D-002).

Out:

- Implementing `specs/002-portable-eval-harness.md`.
- Rewriting bootstrap/resume/audit.
- Publishing, remotes, or editing installed skill copies.
- Changing the dual Codex/Claude router split (D-006).

## Governing contracts and decisions

- `CONTRACTS.md` (proposed `RC-007`)
- D-002, D-004, D-006

## Change shape

| Dimension | Changed? | Source of truth | Proof |
|---|---:|---|---|
| User-visible behavior | yes | close workflow and templates | close eval + checker fixtures |
| Persisted state or schema | no | — | review |
| External or provider-visible behavior | no | — | review |
| Identifiers, secrets or privacy | no | eval fixtures stay sanitized | review |
| Lifecycle or terminal states | yes | STATUS snapshot; spec retire unchanged | checker + eval |
| Setup, operation or recovery | yes | close artifact rule | review |
| Normative contract or decision | yes | RC-007 / D-007 | explicit review |
| Cross-repository dependency | no | stdlib checker only | import review |

## Implementation by invariant

1. STATUS is a snapshot using the template sections.
2. `VERIFICATION.md` is not a model document.
3. Close report stays in the conversation.
4. One fact, one owner; README moves only when use moves.
5. Reusable operator procedures are promoted, not pasted.

## Done when

- Checker unit tests cover close-residue warnings.
- Close eval mechanical assertions exist.
- Close, document-model, STATUS/README templates, and SKILL overview agree.
- `python3 -m unittest discover -s tests -v` and `check_docset.py .` pass.

## Risks and unknowns

- Warning rather than error on residue so historical files do not fail CI.
- `TESTING.md` is not banned; some projects use it for real test docs.
