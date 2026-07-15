#!/usr/bin/env python3
"""Regression tests for the generated static study portal."""

from __future__ import annotations

import json
import re
import struct
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"


class StudySiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = (DOCS / "index.html").read_text(encoding="utf-8")
        cls.payload = json.loads((DOCS / "data" / "site-data.json").read_text(encoding="utf-8"))

    def test_expected_learning_content_is_published(self) -> None:
        self.assertEqual(len(self.payload["topics"]["domains"]), 4)
        self.assertEqual(sum(len(item["topics"]) for item in self.payload["topics"]["domains"]), 20)
        self.assertEqual(len(self.payload["labs"]), 8)
        self.assertEqual(len(self.payload["quiz"]["questoes"]), 10)
        self.assertEqual(self.payload["stats"]["questions"], 445)

    def test_project_pages_uses_only_subpath_safe_local_urls(self) -> None:
        local_urls = re.findall(r'(?:href|src)="([^"]+)"', self.html)
        broken = [url for url in local_urls if url.startswith("/") and not url.startswith("//")]
        self.assertEqual(broken, [])

    def test_generated_assets_match_their_sources(self) -> None:
        for filename in ("app.js", "styles.css", "og.png"):
            with self.subTest(filename=filename):
                self.assertEqual((SITE / filename).read_bytes(), (DOCS / "assets" / filename).read_bytes())

    def test_social_card_is_a_landscape_png(self) -> None:
        image = (DOCS / "assets" / "og.png").read_bytes()
        self.assertEqual(image[:8], b"\x89PNG\r\n\x1a\n")
        width, height = struct.unpack(">II", image[16:24])
        self.assertGreater(width, height)
        self.assertGreaterEqual(width, 1200)

    def test_accessibility_and_interactions_are_wired(self) -> None:
        for marker in (
            'lang="pt-BR"',
            'class="skip-link"',
            'data-topic-search',
            'data-lab-grid',
            'data-quiz-card',
            'data-plan-grid',
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.html)


if __name__ == "__main__":
    unittest.main()
