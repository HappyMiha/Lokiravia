"""The backlog records what was produced, and cannot claim acceptance without it.

Lokiravia loads its manifest through the repository validator rather than a
library of its own, so these checks cover that script. The rules match the ones
Lokvetia Core applies, deliberately: one manifest format, one gate.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_backlog as validator  # noqa: E402

ENTRY = {"kind": "test", "reference": "tests/test_example.py", "recorded_by": "Reviewer"}
MANIFEST = "examples/agentfactory-cloud-backlog.json"


def item(stable_id: str = "AF-CLD-001", **overrides) -> dict:
    document = {
        "stable_id": stable_id,
        "kind": "task",
        "title": f"Title {stable_id}",
        "description": f"Description {stable_id}",
        "acceptance_criteria": ["An operator can verify the result."],
    }
    document.update(overrides)
    return document


class RepositoryValidatorTests(unittest.TestCase):
    """The script and the loader refuse the same manifests."""

    def test_the_script_accepts_a_recorded_entry(self):
        self.assertEqual(validator.validate_evidence("AF-001", item(evidence=[ENTRY])), 1)

    def test_the_script_refuses_acceptance_without_evidence(self):
        with self.assertRaises(validator.ValidationError) as refusal:
            validator.validate_evidence("AF-001", item(labels=["status:accepted"]))
        self.assertIn("record what was produced", str(refusal.exception))

    def test_the_script_refuses_an_invented_kind_and_an_unknown_field(self):
        for entry in ({**ENTRY, "kind": "vibes"}, {**ENTRY, "verdict": "passed"}):
            with self.subTest(entry=entry):
                with self.assertRaises(validator.ValidationError):
                    validator.validate_evidence("AF-001", item(evidence=[entry]))

    def test_the_script_reports_the_number_of_recorded_entries(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "examples").mkdir()
            (root / "docs").mkdir()
            readable = Path(__file__).resolve().parents[1] / "docs/backlog.md"
            (root / "docs/backlog.md").write_text(readable.read_text(encoding="utf-8-sig"),
                                                  encoding="utf-8")
            source = Path(__file__).resolve().parents[1] / MANIFEST
            document = json.loads(source.read_text(encoding="utf-8-sig"))
            for entry in document["items"]:
                if entry["stable_id"] == "AF-CLD-010":
                    entry["evidence"] = [ENTRY]
            (root / MANIFEST).write_text(
                json.dumps(document, ensure_ascii=False), encoding="utf-8"
            )
            baseline = sum(
                len(entry.get("evidence", []))
                for entry in json.loads(source.read_text(encoding="utf-8-sig"))["items"]
            )
            results = validator.validate_repository(root)
            self.assertEqual(results[0][2], baseline + 1)

    def test_the_shipped_backlogs_still_validate(self):
        root = Path(__file__).resolve().parents[1]
        for name, count, recorded in validator.validate_repository(root):
            self.assertGreater(count, 0, name)
            self.assertGreaterEqual(recorded, 0, name)


class RecordedEvidenceTests(unittest.TestCase):
    """The shipped manifest records only artifacts that are actually here."""

    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]
        self.items = json.loads(
            (self.root / MANIFEST).read_text(encoding="utf-8-sig")
        )["items"]

    def test_every_recorded_reference_exists_in_this_repository(self):
        missing = [
            entry["reference"]
            for item in self.items
            for entry in item.get("evidence", [])
            if not (self.root / entry["reference"]).exists()
        ]
        self.assertEqual(missing, [])

    def test_recording_evidence_does_not_declare_acceptance(self):
        for item in self.items:
            if item.get("evidence"):
                labels = {str(value).lower() for value in item.get("labels", [])}
                self.assertFalse(labels & validator.ACCEPTED_STATUS_LABELS, item["stable_id"])


if __name__ == "__main__":
    unittest.main()

class EvidenceBoundaryTests(unittest.TestCase):
    def test_malformed_evidence_is_rejected_before_acceptance(self):
        invalid = [None, [ENTRY, ENTRY], [ENTRY] * 21,
                   [{**ENTRY, "reference": None}], [{**ENTRY, "recorded_by": False}],
                   [{**ENTRY, "note": {}}], [{**ENTRY, "reference": "x" * 301}],
                   [{**ENTRY, "note": "x" * 501}]]
        for evidence in invalid:
            with self.subTest(evidence=evidence):
                with self.assertRaises(validator.ValidationError):
                    validator.validate_evidence("AF-001", {"evidence": evidence})
