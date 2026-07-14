#!/usr/bin/env python3
"""Regression tests for grading, timing, priorities, and report output."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from assessment_lib import (  # noqa: E402
    AnswerRecord,
    grade,
    load_exam,
    parse_answer_payload,
    render_report,
    write_report,
)


ROOT = Path(__file__).resolve().parents[1]


class AssessmentLibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.exam = load_exam(ROOT / "quizzes" / "dominio-1-seguranca" / "quiz-01.json")

    def test_per_question_time_is_not_inflated_by_session_time(self) -> None:
        first = self.exam["questoes"][0]
        records = {first["id"]: AnswerRecord(first["resposta_correta"], 60.0)}
        report = grade(self.exam, records, {"wall_seconds": 100.0})
        summary = report["summary"]
        self.assertEqual(summary["total_seconds"], 60.0)
        self.assertEqual(summary["average_seconds"], 60.0)
        self.assertEqual(summary["timed_count"], 1)
        self.assertEqual(summary["wall_seconds"], 100.0)

    def test_perfect_on_time_attempt_has_no_false_priority(self) -> None:
        records = {
            question["id"]: AnswerRecord(question["resposta_correta"], 1.0)
            for question in self.exam["questoes"]
        }
        report = grade(self.exam, records)
        self.assertEqual(report["summary"]["correct"], len(self.exam["questoes"]))
        self.assertEqual(report["priorities"], [])

    def test_invalid_times_are_rejected(self) -> None:
        for invalid in (-1, float("nan"), float("inf")):
            with self.subTest(invalid=invalid), self.assertRaises(SystemExit):
                parse_answer_payload({"answers": {"Q1": {"answer": "A", "seconds": invalid}}})

    def test_reports_include_full_question_feedback(self) -> None:
        first = self.exam["questoes"][0]
        report = grade(self.exam, {first["id"]: AnswerRecord("A", 2.0)})
        markdown = render_report(report)
        self.assertIn(first["enunciado"], markdown)
        with tempfile.TemporaryDirectory() as directory:
            md_path = Path(directory) / "report.md"
            json_path = Path(directory) / "report.json"
            write_report(report, md_path, json_path)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["results"][0]["question"]["id"], first["id"])
            self.assertIn("explicacao_alternativas", payload["results"][0]["question"])

    def test_wrong_output_extension_is_rejected_before_write(self) -> None:
        first = self.exam["questoes"][0]
        report = grade(self.exam, {first["id"]: AnswerRecord("A", 2.0)})
        with tempfile.TemporaryDirectory() as directory:
            bad_path = Path(directory) / "report.json"
            with self.assertRaises(SystemExit):
                write_report(report, bad_path)
            self.assertFalse(bad_path.exists())


if __name__ == "__main__":
    unittest.main()
