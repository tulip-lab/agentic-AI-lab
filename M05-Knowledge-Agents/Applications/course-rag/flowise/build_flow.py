#!/usr/bin/env python3
"""Create a Flowise Agentflow V2 human gate for an already checked synthetic candidate."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import run_demo as demo
HERE=Path(__file__).resolve().parent

def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def build(nodes,edges,plan,task):
    source_ids=[f['source_id'] for f in plan['facts']]
    digest=hashlib.sha256(json.dumps(plan,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    prompt=f'请教师审核合成教学资源候选：{task["topic"]}。来源：{", ".join(source_ids)}。候选 SHA-256：{digest}。请先核对目标、来源、适切性与隐私；Proceed 仅记录本地练习的审核意见，不发布课件。Reject 表示退回修改。'
    by={n['data']['name']:n for n in nodes}
    start=by['startAgentflow'];human=by['humanInputAgentflow']
    replies=[n for n in nodes if n['data']['name']=='directReplyAgentflow']
    if len(replies)!=2:raise ValueError('需要两个明确结果分支')
    start['data']['inputs']={'startInputType':'chatInput','startState':''}
    human['data']['inputs']={'humanInputDescriptionType':'fixed','humanInputDescription':prompt,'humanInputEnableFeedback':True}
    replies[0]['data']['inputs']={'directReplyMessage':'审核路径：Proceed。仍需教师在课程材料中记录采用决定；此流程没有发布或评分动作。'}
    replies[1]['data']['inputs']={'directReplyMessage':'审核路径：Reject。候选退回修改；没有发布或评分动作。'}
    return {'nodes':nodes,'edges':edges},digest

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--plan',type=Path,default=demo.HERE/'fixture-plan.json');p.add_argument('--task',type=Path,default=demo.CASE/'task.json');p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();task=load(a.task);plan=load(a.plan);selected=demo.prepare(demo.CASE,task);demo.validate_plan(plan,selected)
    template=load(HERE/'gate-template.json');graph,digest=build(template['nodes'],template['edges'],plan,task)
    if a.out.exists():raise ValueError('不覆盖现有文件')
    a.out.write_text(json.dumps({'name':'FLIP LAB-COURSE-RAG-01 local human gate','type':'AGENTFLOW','flowData':json.dumps(graph,ensure_ascii=False),'deployed':False},ensure_ascii=False,indent=2)+'\n')
    print('Flowise graph 已生成；候选 SHA-256 '+digest)
if __name__=='__main__':main()
