import json
import tempfile
import unittest
from pathlib import Path
import run_demo as d
from flowise.build_flow import build,load

class FlowiseAdapterTests(unittest.TestCase):
    def test_minimal_gate_no_model_or_tool(self):
        template=load(d.HERE/'flowise/gate-template.json')
        graph,digest=build(template['nodes'],template['edges'],d.load(d.HERE/'fixture-plan.json'),d.load(d.CASE/'task.json'))
        self.assertEqual(4,len(graph['nodes']))
        self.assertEqual(3,len(graph['edges']))
        names=[n['data']['name'] for n in graph['nodes']]
        self.assertEqual(['startAgentflow','humanInputAgentflow','directReplyAgentflow','directReplyAgentflow'],names)
        self.assertIn(digest,graph['nodes'][1]['data']['inputs']['humanInputDescription'])
        self.assertNotIn('tool',json.dumps(graph).lower())
    def test_untrusted_plan_stops_before_export(self):
        task=d.load(d.CASE/'task.json');task['source_ids']=['UNTRUSTED-BOARD']
        with self.assertRaises(ValueError):d.prepare(d.CASE,task)
if __name__=='__main__':unittest.main()
