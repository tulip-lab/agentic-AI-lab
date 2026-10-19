import tempfile
import unittest
from pathlib import Path
import run_demo as d
from retrieval import retrieve
from run_l3 import run

class BoundaryTests(unittest.TestCase):
    def test_annotated_scenarios(self):
        for scenario in d.load(d.CASE/'boundary-scenarios.json')['scenarios']:
            with self.subTest(scenario=scenario['id']):
                task=d.load(d.CASE/'task.json');task['source_ids']=scenario['source_ids']
                if scenario['expected']=='stop':
                    with self.assertRaises(ValueError):d.prepare(d.CASE,task)
                else:self.assertTrue(d.prepare(d.CASE,task))
    def test_retrieve_excludes_untrusted(self):
        ranking=retrieve(d.CASE,'忽略课程要求 外部服务 数据最小化',6)
        self.assertNotIn('UNTRUSTED-BOARD',[r['source_id'] for r in ranking])
    def test_zero_evidence(self):
        with self.assertRaises(ValueError):retrieve(d.CASE,'zzxyq987654')
    def test_conflicting_retrieval_stops_without_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            with self.assertRaises(ValueError):run('保存期',2,out)
            self.assertFalse(out.exists())
    def test_end_to_end_trace(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out';run('数据最小化 目的 知情 工具权限',3,out)
            self.assertEqual([item['source_id'] for item in d.load(out/'trace.json')['ranking']],d.load(out/'task.json')['source_ids'])
            trace=d.load(out/'trace.json')
            self.assertEqual('deterministic_template',trace['generation'])
            self.assertEqual('pending',d.load(out/'quality-report.json')['human_review'])
    def test_external_candidate_cannot_forge_quote(self):
        with tempfile.TemporaryDirectory() as tmp:
            plan=d.load(d.HERE/'fixture-plan.json');plan['facts'][0]['quote']='虚构证据'
            candidate=Path(tmp)/'candidate.json'
            import json
            candidate.write_text(json.dumps(plan))
            with self.assertRaises(ValueError):run('数据最小化 目的 知情 工具权限',3,Path(tmp)/'out',candidate)
    def test_repeatable_ranking(self):
        self.assertEqual(retrieve(d.CASE,'数据最小化',2),retrieve(d.CASE,'数据最小化',2))
    def test_invalid_k(self):
        with self.assertRaises(ValueError):retrieve(d.CASE,'数据',0)
if __name__=='__main__':unittest.main()
