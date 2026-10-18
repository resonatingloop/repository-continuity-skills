from __future__ import annotations

import base64
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = (
    ROOT / "skills" / "manage-project-docs" / "scripts" / "render_change_atlas.py"
)
PIXEL_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
)


def run_renderer(
    spec: Path, output: Path, *arguments: str
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RENDERER),
            str(spec),
            "--output",
            str(output),
            *arguments,
        ],
        check=False,
        capture_output=True,
        text=True,
    )


def spec_text(
    *,
    title: str = "signal bridge",
    change: str = "put the owner-facing delta above the execution substrate.",
    owner_view: bool = True,
    review_visuals: str = "- none",
) -> str:
    owner_section = ""
    if owner_view:
        owner_section = f"""
## Owner view

- Change: {change}
- Before: approval requires a linear read of the complete spec.
- After: the atlas foregrounds decisions and keeps the full source one disclosure away.
- Authority: the canonical Markdown spec

## Owner decisions

### generated artifact retention

- Recommendation: keep the atlas local and disposable.
- Alternative: track every generated page.
- Consequence: tracking creates a second reconciliation surface.
"""
    return f"""# Spec: {title}

status: draft

> **Continuity role:** proposed transition
> **Owner:** fixture owner
> **Created:** 2026-10-17
> **Supersedes:** none

## Context

This fictional fixture exercises the atlas renderer without private material.
{owner_section}
## Scope

In:

- Generate one deterministic local page.
- Preserve the complete source.

Out:

- Network access.
- Browser writes.

## Change shape

| Dimension | Changed? | Source of truth | Proof |
|---|---:|---|---|
| User-visible behavior | yes | fixture | render inspection |
| External behavior | no | fixture | source review |

## Review visuals

{review_visuals}

## Implementation by invariant

1. Escape every source value before it reaches HTML.

## Done when

- The generated page contains the source fingerprint.
- Check mode catches drift.

## Risks and unknowns

- Hostile prose could become active markup without escaping.

## Open questions

- None.
"""


class RenderChangeAtlasTests(unittest.TestCase):
    def test_render_and_check_round_trip_with_embedded_raster(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            image = root / "bridge.png"
            image.write_bytes(PIXEL_PNG)
            spec = root / "spec.md"
            spec.write_text(
                spec_text(review_visuals="![fictional bridge state](bridge.png)"),
                encoding="utf-8",
            )
            output = root / "atlas.html"

            rendered = run_renderer(spec, output)
            checked = run_renderer(spec, output, "--check")

            self.assertEqual(rendered.returncode, 0, rendered.stdout + rendered.stderr)
            self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
            html = output.read_text(encoding="utf-8")
            self.assertIn("repository-continuity-change-atlas/1", html)
            self.assertIn('Content-Security-Policy', html)
            self.assertIn("data:image/png;base64,", html)
            self.assertIn("generated artifact retention", html)
            self.assertIn("complete canonical source", html)
            self.assertRegex(html, r'<meta name="atlas-source-sha256" content="[0-9a-f]{64}">')
            self.assertRegex(html, r'<meta name="atlas-source-id" content="[0-9a-f]{64}">')
            self.assertNotIn("[[SOURCE_SHA256]]", html)
            self.assertNotIn("https://", html)
            self.assertNotIn("http://", html)

    def test_check_detects_source_change(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            spec = root / "spec.md"
            spec.write_text(spec_text(), encoding="utf-8")
            output = root / "atlas.html"
            self.assertEqual(run_renderer(spec, output).returncode, 0)

            spec.write_text(spec_text(change="a revised owner-facing delta."), encoding="utf-8")
            checked = run_renderer(spec, output, "--check")

            self.assertEqual(checked.returncode, 2)
            self.assertIn("stale", checked.stderr)

    def test_check_detects_output_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            spec = root / "spec.md"
            spec.write_text(spec_text(), encoding="utf-8")
            output = root / "atlas.html"
            self.assertEqual(run_renderer(spec, output).returncode, 0)
            output.write_text(output.read_text(encoding="utf-8") + "\n<!-- altered -->\n", encoding="utf-8")

            checked = run_renderer(spec, output, "--check")

            self.assertEqual(checked.returncode, 2)
            self.assertIn("modified", checked.stderr)

    def test_legacy_spec_without_owner_view_still_renders(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            spec = root / "legacy.md"
            spec.write_text(spec_text(owner_view=False), encoding="utf-8")
            output = root / "atlas.html"

            result = run_renderer(spec, output)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            html = output.read_text(encoding="utf-8")
            self.assertIn("legacy source", html)
            self.assertIn("fictional fixture exercises", html)

    def test_hostile_prose_and_alt_text_are_escaped(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "bridge.png").write_bytes(PIXEL_PNG)
            spec = root / "spec.md"
            spec.write_text(
                spec_text(
                    title='</title><script>alert("title")</script>',
                    change='<img src=x onerror=alert("change")> [[SOURCE_SHA256]]',
                    review_visuals='!["><script>alert("alt")</script>](bridge.png)',
                ),
                encoding="utf-8",
            )
            output = root / "atlas.html"

            result = run_renderer(spec, output)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            html = output.read_text(encoding="utf-8")
            self.assertNotIn("<script>", html)
            self.assertNotIn("<img src=x", html)
            self.assertIn("&lt;script&gt;", html)
            self.assertIn("&lt;img src=x onerror=alert", html)
            self.assertIn("[[SOURCE_SHA256]]", html)

    def test_unsafe_image_references_are_rejected(self) -> None:
        references = (
            "![remote](https://example.invalid/review.png)",
            "![data](data:image/png;base64,aaaa)",
            "![absolute](/tmp/review.png)",
            "![traversal](../review.png)",
            "![encoded](review%2e%2e.png)",
            "![svg](review.svg)",
        )
        for reference in references:
            with self.subTest(reference=reference), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                (root / "review.svg").write_text("<svg/>", encoding="utf-8")
                spec = root / "spec.md"
                spec.write_text(spec_text(review_visuals=reference), encoding="utf-8")

                result = run_renderer(spec, root / "atlas.html")

                self.assertEqual(result.returncode, 2)
                self.assertIn("error:", result.stderr)

    @unittest.skipUnless(hasattr(os, "symlink"), "symbolic links are unavailable")
    def test_symlinked_review_image_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            outside = root / "outside.png"
            outside.write_bytes(PIXEL_PNG)
            assets = root / "assets"
            assets.mkdir()
            (assets / "bridge.png").symlink_to(outside)
            spec = root / "spec.md"
            spec.write_text(
                spec_text(review_visuals="![bridge](assets/bridge.png)"), encoding="utf-8"
            )

            result = run_renderer(spec, root / "atlas.html")

            self.assertEqual(result.returncode, 2)
            self.assertIn("symbolic link", result.stderr)

    def test_invalid_image_content_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "bridge.png").write_text("not a png", encoding="utf-8")
            spec = root / "spec.md"
            spec.write_text(
                spec_text(review_visuals="![bridge](bridge.png)"), encoding="utf-8"
            )

            result = run_renderer(spec, root / "atlas.html")

            self.assertEqual(result.returncode, 2)
            self.assertIn("validated PNG", result.stderr)

    def test_plain_file_is_never_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            spec = root / "spec.md"
            spec.write_text(spec_text(), encoding="utf-8")
            output = root / "atlas.html"
            output.write_text("owner material", encoding="utf-8")

            result = run_renderer(spec, output)

            self.assertEqual(result.returncode, 2)
            self.assertEqual(output.read_text(encoding="utf-8"), "owner material")
            self.assertIn("refusing to overwrite", result.stderr)

    def test_generated_atlas_can_only_be_replaced_by_its_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "first.md"
            second = root / "second.md"
            first.write_text(spec_text(title="first bridge"), encoding="utf-8")
            second.write_text(spec_text(title="second bridge"), encoding="utf-8")
            output = root / "atlas.html"
            self.assertEqual(run_renderer(first, output).returncode, 0)
            original = output.read_bytes()

            wrong_source = run_renderer(second, output)

            self.assertEqual(wrong_source.returncode, 2)
            self.assertEqual(output.read_bytes(), original)
            self.assertIn("bound to", wrong_source.stderr)

            first.write_text(spec_text(title="first bridge revised"), encoding="utf-8")
            refreshed = run_renderer(first, output)
            self.assertEqual(refreshed.returncode, 0, refreshed.stdout + refreshed.stderr)
            self.assertIn("first bridge revised", output.read_text(encoding="utf-8"))

    def test_same_filename_outside_a_repository_is_not_the_same_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first_dir = root / "first"
            second_dir = root / "second"
            first_dir.mkdir()
            second_dir.mkdir()
            first = first_dir / "spec.md"
            second = second_dir / "spec.md"
            first.write_text(spec_text(title="first source"), encoding="utf-8")
            second.write_text(spec_text(title="second source"), encoding="utf-8")
            output = root / "atlas.html"
            self.assertEqual(run_renderer(first, output).returncode, 0)
            original = output.read_bytes()

            wrong_source = run_renderer(second, output)

            self.assertEqual(wrong_source.returncode, 2)
            self.assertEqual(output.read_bytes(), original)
            self.assertIn("refusing to overwrite", wrong_source.stderr)


if __name__ == "__main__":
    unittest.main()
