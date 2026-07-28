# Close workflow

Use this workflow during an authorized implementation task before declaring a
material slice complete. Closing reconciles the project; it does not broaden
the approved scope.

## 1. Revisit the accepted transition

Read the accepted spec and its change-shape matrix. Compare the final diff with
the declared scope. Surface undeclared dimensions rather than quietly adding
work.

## 2. Reconcile by invariant

For every changed fact, inspect the affected representations:

1. user-visible behavior;
2. application and persisted state;
3. external projection or delivery;
4. privacy and identifiers;
5. lifecycle and recovery;
6. operational documentation;
7. normative contracts and decisions;
8. generated reference.

Update code, proof, and authorized documentation together where applicable.
If implementation contradicts a normative contract, stop for a decision.

## 3. Run proof

Run focused proofs during implementation, then the repository's complete
required validation. Run the generic document checker and any project-specific
conformance, migration, lifecycle, privacy or integration tests named by the
matrix.

Search changed governing prose for strong claims such as `exact`, `always`,
`never`, `current`, `future`, and `canonical`. Verify the intended meaning, not
only the presence of matching strings.

## 4. Persist the new checkpoint

- Update operational instructions when the successful-use path changed.
- Update `STATUS.md` with verified current state and next useful action.
- Record a decision when the slice introduced, clarified or superseded a fact
  another maintainer would otherwise have to re-derive.
- Do not create a new decision for a fix that merely restores an existing
  invariant; link the fix to that invariant instead.
- Mark the accepted spec retired only after its acceptance criteria and proofs
  are satisfied.

## 5. Report honestly

List validation results, documentation changed, unresolved unknowns, deferred
dimensions, and cross-repository dependencies. Do not describe normalized or
reconstructed facts as exact.
