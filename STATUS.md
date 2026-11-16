# Repository Continuity status

> **Continuity role:** operational checkpoint
> **Status:** current
> **Last verified:** 2026-11-06
> **Owns:** verified current state, active work, known gaps, and next useful action
> **Update when:** a meaningful stopping point changes any of those facts

## Verified checkpoint

the static change atlas remains implemented under retired spec 004. the codex
Plan router now automatically loads an available `attention-aperture` skill
for an authorized saved material spec. the companion pass checks instrument
fit, binds its authored model to source fingerprints, and preserves atlas and
Markdown authority. text-only, unavailable-tool, and unsupported-format paths
remain explicit. no renderer or checker code changed.

Verification performed:

```text
python3 -m unittest discover -s tests -v
python3 skills/manage-project-docs/scripts/check_docset.py .
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/manage-project-docs
python3 skills/manage-project-docs/scripts/render_change_atlas.py specs/004-change-atlas.md --output build/change-atlas/004-change-atlas.html --check
```

Evidence of success:

```text
17 tests OK; check_docset 0 errors and 0 warnings; skill valid; atlas current; installed routing resolves
```

## Working now

- Six continuity operations, two agent routers over one shared core
- Codex saved-spec handoff to an available visual-companion skill; separate local output and unchanged atlas
- Checker fixtures: healthy, drifted, close-residue
- Static change-atlas renderer and responsive local HTML template
- Renderer fixtures: freshness, tampering, hostile prose, image containment,
  source identity, safe overwrite, and legacy specs
- Public-safe accepted and retired specs are explicitly allowlisted for Git
- Close eval fixture in the private eval workspace (D-002, D-008)

## Incomplete or broken

- Close eval is one run per condition, not a three-run benchmark
- The new automatic companion handoff needs its first fresh-session saved-spec use
- Broader Plan and Promote field coverage remains unverified
- The current task did not reverify live owner-approval or rendered-companion behavior
- Independent review of the HTML trust boundary remains a release gate
- Draft, rejected, and generated spec artifacts remain ignored unless deliberately promoted
- `/skills-claude` is gitignored; Claude router edits are local only

## Active work

- Accepted spec: none
- Current focus: first-use proof of the saved-spec companion handoff
- Blockers: none

## Next useful action

ask the codex variant to draft the next material spec with the companion skill
available. confirm it selects a supported instrument without a second prompt,
then inspect the companion, atlas, and source revision together.

## Re-entry notes

- Configuration required: none
- Persistent state: Git worktree only
- External dependencies: none for unit tests and checker
- Local proof artifact: `build/change-atlas/004-change-atlas.html` (ignored)
- Recovery warning: close eval runs live outside this repository
