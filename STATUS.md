# Repository Continuity status

> **Continuity role:** operational checkpoint
> **Status:** current
> **Last verified:** 2026-10-17
> **Owns:** verified current state, active work, known gaps, and next useful action
> **Update when:** a meaningful stopping point changes any of those facts

## Verified checkpoint

The change-atlas transition in `specs/004-change-atlas.md` is implemented and
retired. Plan can now project an authorized saved material spec into a static,
responsive owner surface while the Markdown source remains the sole planning
authority. The renderer exposes source provenance, escapes all spec prose,
embeds only validated local raster images, detects drift, and refuses unsafe
overwrites.

Verification performed:

```text
python3 -m unittest discover -s tests -v
python3 skills/manage-project-docs/scripts/check_docset.py .
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/manage-project-docs
python3 skills/manage-project-docs/scripts/render_change_atlas.py specs/004-change-atlas.md --output build/change-atlas/004-change-atlas.html --check
```

Evidence of success:

```text
17 tests OK; check_docset 0 errors and 0 warnings; skill valid; atlas current
```

## Working now

- Six continuity operations, two agent routers over one shared core
- Checker fixtures: healthy, drifted, close-residue
- Static change-atlas renderer and responsive local HTML template
- Renderer fixtures: freshness, tampering, hostile prose, image containment,
  source identity, safe overwrite, and legacy specs
- Public-safe accepted and retired specs are explicitly allowlisted for Git
- Close eval fixture in the private eval workspace (D-002, D-008)

## Incomplete or broken

- Close eval is one run per condition, not a three-run benchmark
- Plan and Promote remain untested in the field
- The change atlas has not yet mediated a live owner approval
- Independent review of the HTML trust boundary remains a release gate
- Draft, rejected, and generated spec artifacts remain ignored unless deliberately promoted
- `/skills-claude` is gitignored; Claude router edits are local only

## Active work

- Accepted spec: none
- Current focus: owner inspection and first-use field proof
- Blockers: none

## Next useful action

Use the generated atlas on the next material spec approval, then record whether
its decision-shaped surface reduces reading burden without obscuring anything
the owner needed to judge.

## Re-entry notes

- Configuration required: none
- Persistent state: Git worktree only
- External dependencies: none for unit tests and checker
- Local proof artifact: `build/change-atlas/004-change-atlas.html` (ignored)
- Recovery warning: close eval runs live outside this repository
