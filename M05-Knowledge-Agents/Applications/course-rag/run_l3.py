#!/usr/bin/env python3
"""Retrieve -> candidate -> checked resources, with an explicit extractive baseline."""
import argparse
import json
from pathlib import Path
import run_demo as demo
from retrieval import retrieve


def baseline(selected):
    return {
        'outcomes':[{'id':'O1','text':'识别数据使用方案中的风险，并引用课程资料解释理由。'},
                    {'id':'O2','text':'提出有证据支持的修改建议，并说明需要教师判断的事项。'}],
        'facts':[{'source_id':sid,'quote':s['text']} for sid,s in selected.items()],
        'activity':{'outcome_ids':['O1','O2'],'instructions':'审核一份合成学习数据方案，用资料编号支持风险判断与修改建议；对资料不能确定的事项提出核查问题。'},
        'reflection':['检索命中是否意味着资料适用于当前课程？','哪些判断需要更多证据或教师确认？']}


def run(query, top_k, output, candidate=None):
    ranking = retrieve(demo.CASE, query, top_k)
    task = demo.load(demo.CASE/'task.json')
    task['source_ids']=[r['source_id'] for r in ranking]
    selected = demo.prepare(demo.CASE, task)
    plan = demo.load(candidate) if candidate else baseline(selected)
    result = demo.run(demo.CASE, task, plan, output,
                      'retrieval_external_candidate' if candidate else 'lexical_extractive_baseline')
    (Path(output)/'task.json').write_text(json.dumps(task,ensure_ascii=False,indent=2)+'\n')
    trace = demo.load(Path(output)/'trace.json')
    trace.update({'retriever':'CJK-bigram-word-cosine-v1','query':query,'top_k':top_k,
                  'ranking':ranking,'generation':'external_candidate' if candidate else 'deterministic_template',
                  'limitations':['词面检索不保证语义相关性','只识别显式标注的来源冲突','教学设计需人工审核']})
    (Path(output)/'trace.json').write_text(json.dumps(trace,ensure_ascii=False,indent=2)+'\n')
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--query',required=True);p.add_argument('--top-k',type=int,default=3)
    p.add_argument('--candidate',type=Path);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    try:run(a.query,a.top_k,a.out,a.candidate)
    except (ValueError,KeyError,TypeError,OSError) as e:p.exit(2,f'停止：{e}\n')
    print('检索和资源检查完成；教师审核待完成。')
if __name__=='__main__':main()
