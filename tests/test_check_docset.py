from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "manage-project-docs" / "scripts" / "check_docset.py"
FIXTURES = ROOT / "tests" / "fixtures"


def run_checker(fixture: str, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            str(FIXTURES / fixture),
            "--max-status-age",
            "99999",
            *arguments,
        ],
        check=False,
        capture_output=True,
        text=True,
    )


class CheckDocsetTests(unittest.TestCase):
    def test_healthy_fixture_passes(self) -> None:
        result = run_checker("healthy")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("0 error(s)", result.stdout)

    def test_drifted_fixture_reports_structural_failures(self) -> None:
        result = run_checker("drifted")

        self.assertEqual(result.returncode, 1)
        self.assertIn("unresolved template placeholder", result.stdout)
        self.assertIn("unresolved verification marker", result.stdout)
        self.assertIn("local Markdown target does not exist", result.stdout)
        self.assertIn("invalid spec status", result.stdout)

    def test_strong_claim_review_does_not_add_failure(self) -> None:
        result = run_checker("drifted", "--review-claims")

        self.assertEqual(result.returncode, 1)
        self.assertIn("[REVIEW]", result.stdout)
        self.assertIn("verify strong claim", result.stdout)

    def test_extra_required_document_is_enforced(self) -> None:
        result = run_checker("healthy", "--require", "CONTRACTS.md")

        self.assertEqual(result.returncode, 1)
        self.assertIn("CONTRACTS.md", result.stdout)
        self.assertIn("required document is missing", result.stdout)

    def test_close_residue_is_warned_not_failed(self) -> None:
        result = run_checker("close-residue")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("VERIFICATION.md is not a model document", result.stdout)
        self.assertIn("STATUS.md owns the checkpoint", result.stdout)
        self.assertIn("unexpected STATUS heading", result.stdout)
        self.assertIn("Depth pass — 2026-09-08", result.stdout)
        self.assertIn("extra Verified checkpoint section", result.stdout)
        self.assertIn("session transcript", result.stdout)
        self.assertNotIn("[ERROR]", result.stdout)

    def test_healthy_fixture_has_no_close_residue_warnings(self) -> None:
        result = run_checker("healthy")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("VERIFICATION.md is not a model document", result.stdout)
        self.assertNotIn("unexpected STATUS heading", result.stdout)
        self.assertNotIn("extra Verified checkpoint section", result.stdout)


if __name__ == "__main__":
    unittest.main()
