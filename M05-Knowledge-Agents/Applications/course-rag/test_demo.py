import copy
import json
import tempfile
import unittest
from pathlib import Path
import run_demo as demo


class DemoTests(unittest.TestCase):
    def setUp(self):
        self.task = demo.load(demo.CASE / "task.json")
        self.plan = demo.load(demo.HERE / "fixture-plan.json")
        self.sources = demo.prepare(demo.CASE, self.task)

    def test_normal_end_to_end(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "result"
            demo.run(demo.CASE, self.task, self.plan, out)
            self.assertTrue((out / "slides.md").exists())
            self.assertEqual("pending", demo.load(out / "quality-report.json")["human_review"])
            self.assertNotIn("UNTRUSTED-BOARD", (out / "generation-prompt.md").read_text())
            self.assertEqual("hand_authored_fixture", demo.load(out / "trace.json")["mode"])

    def test_missing_evidence_stops_before_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.task["source_ids"].append("MISSING")
            with self.assertRaises(ValueError): demo.run(demo.CASE, self.task, self.plan, Path(tmp) / "result")
            self.assertFalse((Path(tmp) / "result").exists())

    def test_untrusted_source_rejected(self):
        self.task["source_ids"] = ["UNTRUSTED-BOARD"]
        with self.assertRaises(ValueError): demo.prepare(demo.CASE, self.task)

    def test_forged_citation_rejected(self):
        self.plan["facts"][0]["quote"] = "所有学习数据必须永久保存。"
        with self.assertRaises(ValueError): demo.validate_plan(self.plan, self.sources)

    def test_unaligned_activity_rejected(self):
        self.plan["activity"]["outcome_ids"] = ["O1"]
        with self.assertRaises(ValueError): demo.validate_plan(self.plan, self.sources)

    def test_vue_injection_rejected(self):
        self.plan["activity"]["instructions"] = "{{ malicious_tool() }}"
        with self.assertRaises(ValueError): demo.validate_plan(self.plan, self.sources)

    def test_external_image_markup_rejected(self):
        self.plan["activity"]["instructions"] = "![beacon](https://example.invalid/image)"
        with self.assertRaises(ValueError): demo.validate_plan(self.plan, self.sources)

    def test_existing_output_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp); (p / "keep.txt").write_text("keep")
            with self.assertRaises(ValueError): demo.run(demo.CASE, self.task, self.plan, p)
            self.assertEqual("keep", (p / "keep.txt").read_text())

    def test_modified_corpus_hash_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            for f in demo.CASE.iterdir():
                if f.is_file(): (p / f.name).write_bytes(f.read_bytes())
            (p / "corpus.json").write_text('{"sources": []}')
            with self.assertRaises(ValueError): demo.prepare(p, self.task)


if __name__ == "__main__": unittest.main()
