# Plan workflow

Use this read-only workflow to turn a substantial idea or requested change into
a reviewable spec. Planning does not authorize implementation.

## 1. Ground the transition

Read durable intent, current status, relevant contracts, the implemented seams
likely to change, and existing tests. Do not re-derive the entire project.

Name the current state and the proposed new state. Identify any conflict that
requires a contract decision before the spec can be accepted.

## 2. Declare the change shape

Include this matrix in every material spec:

| Dimension | Changed? | Source of truth | Proof |
|---|---:|---|---|
| User-visible behavior | yes/no | | |
| Persisted state or schema | yes/no | | |
| External or provider-visible behavior | yes/no | | |
| Identifiers, secrets or privacy | yes/no | | |
| Lifecycle or terminal states | yes/no | | |
| Setup, operation or recovery | yes/no | | |
| Normative contract or decision | yes/no | | |
| Cross-repository dependency | yes/no | | |

Require a conscious `no`; do not leave dimensions blank. The proof may be a
test, generated comparison, manual observation, or explicit review.

## 3. Draft the spec

Define:

- context and reason for the change now;
- scope in and scope out;
- governing contracts and decisions;
- files or components likely to change;
- ordered implementation by invariant, not merely by file;
- observable acceptance criteria;
- validation commands;
- risks, unknowns and blocking questions.

Keep the status `draft`. Open questions that affect acceptance criteria block
approval.

## 4. Request the transition

Present the draft and name any decisions needed. The user or designated owner
may mark it `accepted` or `rejected`. Do not interpret enthusiasm, discussion,
or a request for options as acceptance.
