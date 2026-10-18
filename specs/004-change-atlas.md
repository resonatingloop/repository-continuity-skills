# Spec: change atlas

status: retired

> **Continuity role:** retired transition
> **Owner:** repository owner
> **Created:** 2026-10-17
> **Accepted:** 2026-10-17
> **Retired:** 2026-10-17
> **Acceptance evidence:** owner wrote "i agree with your recommendation. accepted"
> **Supersedes:** none

## Context

The canonical implementation spec is useful and working: it preserves exact
scope, contracts, proof, and cold-session continuity. It is also serving as the
owner's approval interface, which makes approval require a linear reading of
material written primarily for exhaustive execution and resumption.

This transition separates those cognitive duties without creating a second
source of truth. The Markdown spec remains the execution covenant. A generated
change atlas presents the same revision as a visual, decision-shaped review
surface with direct access to the complete source.

## Owner view

- Change: an authorized saved material spec also receives a local visual review surface.
- Before: the owner reads the canonical spec linearly to understand and approve it.
- After: the owner reviews changes, non-changes, decisions, risks, and proof in an atlas, then drills into the complete canonical spec where useful.
- Authority: acceptance still applies only to the exact canonical spec revision.

## Scope

In:

- Extend Plan so an authorized saved material spec can produce a generated
  local change atlas.
- Keep Markdown as the sole planning authority.
- Add compact owner-view, owner-decision, and optional review-visual structures
  to the reusable spec shape.
- Generate deterministic static HTML with inline CSS, source provenance, and an
  expandable escaped copy of the complete spec.
- Support optional local raster images without invoking an image provider.
- Check that an atlas exactly matches its source spec and renderer version.
- Track sanitized accepted and retired specs when this public repository names
  them as authority; keep drafts and generated atlases local until deliberately
  promoted.

Out:

- An acceptance button, local server, or browser-to-repository writes.
- JavaScript, remote assets, telemetry, hosting, or publication.
- Arbitrary Markdown-to-HTML behavior.
- Automatic image generation.
- Replacing the canonical spec.
- Changing Resume, Audit, Close, or Promote.
- Imposing one Git-tracking policy on downstream repositories.

## Governing contracts and decisions

- `RC-002`: only a human or designated owner may accept a draft spec.
- `RC-003`: reusable assets never blindly overwrite repository documents.
- `RC-004`: generic checks do not prove project-specific semantics.
- `RC-005`: detailed procedures remain progressively disclosed.
- `RC-006`: public artifacts contain no private project material.
- D-002, D-004, D-006, D-007, and D-008.
- Owner decision recorded by this acceptance: public-safe accepted and retired
  specs named as public authority are tracked; drafts and generated atlases
  remain local until deliberately promoted.

## Change shape

| Dimension | Changed? | Source of truth | Proof |
|---|---:|---|---|
| User-visible behavior | yes | Plan workflow and atlas template | rendered browser inspection |
| Persisted state or schema | yes | canonical spec and disposable generated HTML | deterministic regeneration |
| External or provider-visible behavior | no | local-only renderer | network-free review |
| Identifiers, secrets or privacy | yes | renderer boundary and existing privacy contract | hostile-input and private-content tests |
| Lifecycle or terminal states | yes | current/stale atlas projection; spec states unchanged | freshness tests |
| Setup, operation or recovery | yes | development guide and renderer CLI | generate, check, regenerate, remove |
| Normative contract or decision | yes | proposed `RC-008` and `D-009` | explicit review |
| Cross-repository dependency | no | Python standard library only | import and package review |

## Implementation by invariant

1. Establish `RC-008`: a change atlas is generated and advisory. Only its
   named Markdown spec owns the transition, and acceptance applies to an exact
   spec revision.
2. Add a compact owner-facing structure to new material specs while rendering
   older specs gracefully from their existing sections.
3. Add a deterministic renderer that recognizes only the supported spec
   structure, escapes all prose, and never executes raw Markdown HTML.
4. Permit only validated local raster review images. Reject absolute paths,
   traversal, symlink escape, remote or data URLs, SVG, and unsupported content.
5. Show source path, status, full SHA-256 fingerprint, and renderer version.
   A check mode regenerates in memory and byte-compares the expected result.
6. Require an explicit output path. Replace only a recognized generated atlas
   bound to the same source; otherwise stop. Removing the generated HTML is the
   complete rollback.
7. Render semantic, responsive, keyboard-native HTML with strong contrast,
   print styling, and no motion dependency. Keep the full escaped spec
   available through a native disclosure element.
8. Reconcile Plan, the document model, templates, contracts, decisions,
   architecture, development procedure, public front door, tests, and status.

## Done when

- The atlas foregrounds the one-breath change, before and after, decisions,
  change and non-change, risks, proof, and complete source.
- Hostile prose and image references cannot become executable HTML, active
  URLs, path escape, or silent external fetches.
- Deterministic checks catch source edits, renderer/template changes, output
  tampering, and unsafe overwrite attempts.
- Existing specs remain renderable without migration.
- Desktop and narrow browser inspection confirms hierarchy, overflow behavior,
  keyboard access, and complete-spec reachability.
- Unit tests, the document checker, and the official skill validator pass.
- Public/private-content review is clean.
- An independent review examines the HTML trust boundary before release.
- `STATUS.md` records the implemented checkpoint and any owner-visible proof
  still outstanding.

## Risks and unknowns

- Repository prose entering HTML is a red trust boundary until escaping, URL,
  path, image, and overwrite behavior are proved against hostile fixtures.
- A visually polished projection can conceal omissions; deterministic source
  binding and complete-source access are mandatory, not decorative.
- Browser rendering proves presentation, not that the owner found the review
  surface cognitively sufficient. The first live approval remains field proof.

## Open questions

- None. The owner selected tracked public-safe accepted/retired specs and local
  drafts/generated atlases, and accepted this transition on 2026-10-17.

## Completion

Retired on 2026-10-17 after the owner requested implementation. The completed
slice added the deterministic static renderer, dark responsive template,
owner-facing spec fields, exact-source freshness and overwrite protection,
strict local-raster handling, hostile-input tests, and reconciled public docs.

Seventeen unit tests, the repository document checker, and the official skill
validator pass. Desktop and narrow headless-browser renders were inspected.
The next live owner approval remains field proof, and an independent HTML
trust-boundary review remains required before any public release. No release or
publication occurred in this transition.
