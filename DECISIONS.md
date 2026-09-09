# Repository Continuity decisions

> **Continuity role:** historical rationale and supersession
> **Status:** append-only
> **Last verified:** 2026-09-08
> **Owns:** consequential choices another maintainer should not have to re-derive
> **Update when:** a decision introduces, clarifies, or supersedes a durable fact

Current procedures live in operational documentation. These entries preserve
rationale rather than duplicating instructions.

## D-001 — Separate the public project name from the skill name

- Date: 2026-07-15
- Status: accepted
- Supersedes: none
- Related spec: `specs/001-initial-skill.md`

Context:

The public project describes a broader continuity model, while an installable
skill benefits from a short action-oriented trigger name.

Decision:

Name the repository `repository-continuity` and the skill
`manage-project-docs`. The names are intentionally not required to match.

Consequences:

- The repository has a distinctive public identity.
- Installation documentation must name the skill subdirectory explicitly.

## D-002 — Keep the public protocol separate from private control planes

- Date: 2026-07-15
- Status: accepted
- Supersedes: none
- Related spec: `specs/001-initial-skill.md`

Context:

The originating workflow includes personal project catalogs, reports, paths,
and collaboration preferences that are valuable locally but not portable.

Decision:

Publish only generic workflows, templates, checks, and sanitized fixtures.
Keep private registries, audit reports, local policies, and filled project
documents outside this repository.

Consequences:

- Public examples require deliberate sanitization.
- Local control planes may remain more opinionated than the public skill.

## D-003 — Model continuity as explicit state transitions

- Date: 2026-07-15
- Status: accepted
- Supersedes: none
- Related spec: `specs/001-initial-skill.md`

Context:

Static documentation alone did not prevent unauthorized implementation,
re-entry failure, or semantic drift across multiple representations of a fact.

Decision:

Treat documents as durable state, approved workflows as state transitions,
tests and checks as invariant proofs, and the human owner as authority for
consequential transitions.

Consequences:

- The skill is organized by operations rather than document-generation tasks.
- Completion requires reconciliation, not merely the presence of prose.

## D-004 — Keep the generic checker deliberately shallow

- Date: 2026-07-15
- Status: accepted
- Supersedes: none
- Related spec: `specs/001-initial-skill.md`

Context:

Links, paths, statuses, and placeholders can be checked generically. Provider
payloads, privacy, schemas, and lifecycle semantics depend on each project.

Decision:

Limit the bundled checker to structured repository-independent facts. Require
target repositories to own semantic proof.

Consequences:

- The checker can remain dependency-free and portable.
- A clean generic check is not evidence that documentation fully matches code.

## D-005 — Publish under the MIT License

- Date: 2026-07-15
- Status: accepted
- Supersedes: none
- Related spec: none; licensing was explicitly outside the initial skill slice

Context:

The project is intended for broad reuse and adaptation as a public skill and
workflow toolkit. The repository owner normally uses the MIT License for public
projects.

Decision:

License the complete repository under MIT with the copyright line
`Copyright (c) 2026 resonatingloop`.

Consequences:

- Others may use, modify, distribute, sublicense, and sell copies under MIT's
  notice-preservation condition.
- The project carries MIT's standard warranty and liability disclaimer.

## D-006 — Ship per-agent skill routers over one shared workflow core

- Date: 2026-07-23
- Status: accepted
- Supersedes: none
- Related spec: none; direct bounded change requested by the owner

Context:

The skill was authored for Codex and then ported to Claude Code. The two
harnesses differ in triggering (description-driven, undertriggering-prone),
native machinery (plan mode, subagents, CLAUDE.md, hooks), and invocation
syntax, but the six workflows are deliberately tool-neutral.

Decision:

Keep one workflow core (`references/`, `assets/`, `scripts/`) owned by the
Codex package, and give each agent its own `SKILL.md` router: `skills/` for
Codex, `skills-claude/` for Claude Code. The Claude variant reaches the shared
core through relative symlinks and is installed with `cp -rL`.

Consequences:

- Workflow improvements land once and serve both agents.
- Agent-specific guidance concentrates in the routers, keeping the shared
  references portable.
- Installation for Claude Code must dereference symlinks, and tooling that
  mishandles symlinked directories will see the Claude variant as incomplete.

## D-007 — Close files a checkpoint, not the session

- Date: 2026-09-08
- Status: accepted
- Supersedes: none
- Related spec: `specs/003-close-checkpoint-not-memoir.md`

Context:

Close had no stop-writing rule. Agents kept contracts and proofs sound, then
filed session affidavits into STATUS or extra memoir files. The owner still
could not re-enter without reading a defense of the last turn. Documentation
is for the owner and future agents, not a public contributor by default.

Decision:

STATUS is overwritten as a snapshot (commands + one result). The close report
stays in the conversation. README moves only when use moves. One fact, one
owner. The checker warns on `VERIFICATION.md`, extra STATUS headings, and
STATUS transcripts (more than two fenced blocks).

Consequences:

- Close evals grade snapshot shape, not merely "STATUS was touched."
- Historical `VERIFICATION.md` files warn rather than fail.
- `TESTING.md` is not banned; it is not a close output.

## D-008 — Eval harness stays in the private workspace

- Date: 2026-09-08
- Status: accepted
- Supersedes: none
- Related spec: `specs/002-portable-eval-harness.md` (rejected)

Context:

A draft proposed extracting the private eval loop into this public repository
so both agent variants could grade the same fixtures. The mechanical loop
already exists in the private eval workspace. D-002 keeps that control plane
out of the public package.

Decision:

Reject spec 002. Do not ship an eval harness, eval fixtures, or run trees in
this repository. Forward-tests of the skill remain in the private workspace.

Consequences:

- This package continues to own the skill, templates, and shallow checker.
- Re-proposing a public harness needs a new spec, not revival of 002.
