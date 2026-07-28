# Document model

Use the smallest document set that gives each kind of truth one clear owner.
Locations may vary when a repository already has established conventions;
record the actual map in its README instead of forcing renames.

## Core documents

| Document | Owns | Update trigger |
|---|---|---|
| `README.md` | Front door, maturity, shortest successful use, documentation map | Primary installation or use path changes |
| `AGENTS.md` | Agent authorization, required reading, scope rules, validation and close protocol | Collaboration policy changes |
| `STATUS.md` | Last verified checkpoint, working and broken paths, active work, next useful action | A meaningful stopping point is reached |

These three documents form the minimum continuity surface for a maintained
project. Small scripts and disposable experiments may use a header comment
instead.

## Add documents when their truth exists

| Document | Add when | Owns |
|---|---|---|
| `PROJECT_BRIEF.md` | Direction or non-goals matter | Durable purpose, intended users, scope and non-goals |
| `CONTRACTS.md` | Interfaces, storage, privacy or compatibility promises must not drift casually | Normative invariants and their proofs |
| `docs/DEVELOPMENT.md` | Setup, configuration or recovery is non-trivial | Exact build, run, test, data and troubleshooting procedures |
| `docs/ARCHITECTURE.md` | Multiple components or boundaries need explanation | Implemented system shape and data flow |
| `DECISIONS.md` | Consequential choices should not be re-derived | Accepted rationale, consequences and supersession history |
| `specs/*.md` | A substantial slice needs approval and acceptance criteria | Proposed or accepted transition, never durable current truth |
| `docs/INTEGRATIONS.md` | Use crosses repository, service or client boundaries | End-to-end setup and conformance expectations |
| Generated reference | Facts can be derived deterministically | CLI, API, schema or configuration inventory |

Do not create both `PLAN.md` and an active spec when they would own the same
transition. Prefer one explicit lifecycle: `draft -> accepted -> retired`.

## Assign authority explicitly

Label governing documents and include an authority map in the README:

- **operational/current:** how the project works now;
- **normative:** behavior implementation must preserve;
- **historical:** what was intended or decided at an earlier time;
- **planning:** proposed or accepted future transition;
- **advisory:** useful guidance that does not override a contract;
- **generated:** derived from an executable source of truth.

When documents disagree, do not apply a universal filename-based precedence.
Determine which document owns the disputed fact, whether a later decision
explicitly superseded it, and what the executable evidence shows. Report an
unresolved authority conflict rather than silently choosing convenient prose.

## Distinguish representations of one fact

A material change may affect several representations:

```text
user-visible behavior
    -> application state
    -> persisted state
    -> external or provider projection
    -> delivery or export
    -> operational and normative documentation
```

Keep configured intent, effective behavior, external wire facts, reported
results, and reconstructed legacy facts separate. Tests passing at one layer
do not prove that all representations agree.

## Attach proof at the right layer

Use generic checks for structured claims such as files, links, statuses,
commands, generated inventories, and referenced paths. Use project-owned tests
for semantic claims such as:

- provider-visible request fields;
- privacy and secret-exclusion guarantees;
- lifecycle terminal states;
- storage migrations and schema invariants;
- cross-repository behavior;
- recovery and retry semantics.

Avoid brittle tests over whole paragraphs. Test structured facts and review
the surrounding prose for meaning.
