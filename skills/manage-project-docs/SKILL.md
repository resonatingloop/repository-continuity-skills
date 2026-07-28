---
name: manage-project-docs
description: Maintain repository documentation as a continuity protocol tied to code, tests, contracts, and operational truth. Use when Codex needs to bootstrap or retrofit project docs, resume work in a dormant or unfamiliar repository, draft an implementation spec, reconcile documentation before closing a material change, audit documentation against a live codebase, or promote a recurring failure into a reusable workflow or check.
---

# Manage Project Docs

Treat documentation as durable project state, workflows as state transitions,
and executable checks as invariant proofs. Optimize for a future maintainer or
agent returning without conversational memory.

## Preserve authorization

- Read and obey the repository's existing agent instructions first.
- Treat discussion, exploration, critique, resume, and audit requests as
  read-only unless the user explicitly requests changes.
- Treat a direct bounded change request as implementation authorization for
  that change.
- Require an explicitly accepted spec before starting a new project or a
  substantial, ambiguous, or cross-cutting feature.
- Never promote a draft spec to accepted on the user's behalf.
- Never change a normative contract merely to make implementation and prose
  agree. Surface the conflict and request a decision.

## Select one operation

| User need | Operation | Read |
|---|---|---|
| Start or retrofit a documentation system | Bootstrap | [references/bootstrap.md](references/bootstrap.md) |
| Return after lost context or prove the happy path | Resume | [references/resume.md](references/resume.md) |
| Shape a material implementation slice | Plan | [references/plan.md](references/plan.md) |
| Reconcile a completed implementation slice | Close | [references/close.md](references/close.md) |
| Compare documentation claims with live evidence | Audit | [references/audit.md](references/audit.md) |
| Turn a recurring failure into a reusable guardrail | Promote | [references/promote.md](references/promote.md) |

Read [references/document-model.md](references/document-model.md) when choosing
documents, assigning authority, resolving apparent contradictions, or deciding
which bundled templates to use. Do not load every workflow reference by
default.

## Run the common preflight

1. Locate the repository root and read its instruction files.
2. Inspect version-control status without changing it.
3. Inventory documentation by content and apparent purpose; do not infer a
   document's authority from its filename.
4. Identify the requested operation and whether it authorizes writes.
5. Separate confirmed facts from proposals and unresolved questions.
6. State the intended reads or changes before broad exploration.

## Use the bundled resources

- Copy from `assets/templates/` only during an authorized bootstrap or
  documentation change. Resolve every template marker; never overwrite an
  existing document blindly.
- Run `scripts/check_docset.py REPO` to check the universal core: required
  front-door documents, unresolved placeholders, local Markdown links, spec
  statuses, and status freshness. Use `--help` for optional requirements and
  strong-claim review.
- Keep project-specific semantic proofs in the project itself. A generic
  checker cannot prove wire behavior, privacy guarantees, state transitions,
  schemas, or cross-repository conformance.

## Maintain the continuity boundary

Keep these categories distinct:

- durable intent;
- current operational truth;
- normative invariants;
- historical decisions;
- proposed or accepted work;
- generated reference material.

When one fact appears in multiple categories or system layers, identify every
representation affected by a change and reconcile them together. Prefer an
honest `unknown`, `historical`, or `proposed` label over invented precision.

## Finish visibly

Report:

- the operation performed;
- documents or claims inspected or changed;
- executable checks run and their results;
- unresolved contradictions, unknowns, or stale claims;
- the next authorized transition, if one exists.

Do not call the repository continuous merely because documents exist. Confirm
that a cold reader can find the current state, reach one successful use, and
identify what may happen next.
