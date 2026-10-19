#!/usr/bin/env python3
"""Exercise a local Flowise Agentflow V2 human gate without publishing anything."""
import argparse
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen


def predict(base_url, flow_id, payload, api_key=None):
    url=base_url.rstrip('/')+'/api/v1/prediction/'+flow_id
    headers={'Content-Type':'application/json'}
    if api_key:headers['Authorization']='Bearer '+api_key
    request=Request(url,data=json.dumps(payload,ensure_ascii=False).encode(),headers=headers,method='POST')
    with urlopen(request,timeout=35) as response:
        return json.load(response)


def states(result):
    return [(entry.get('nodeId'),entry.get('status')) for entry in result.get('agentFlowExecutedData',[])]


def pilot(base_url,flow_id,api_key=None):
    records=[]
    for choice in ('reject','proceed'):
        pause=predict(base_url,flow_id,{'question':'审核原创合成教学候选'},api_key)
        before=states(pause)
        if not any(status=='STOPPED' and node.startswith('humanInput') for node,status in before):
            raise ValueError('未在人工节点暂停；检查导入的流程版本和连线')
        resumed=predict(base_url,flow_id,{'question':'审核原创合成教学候选','chatId':pause['chatId'],
                        'humanInput':{'type':choice,'feedback':'仅用于本地演示'}},api_key)
        after=states(resumed)
        expected='directReplyAgentflow_1' if choice=='reject' else 'directReplyAgentflow_0'
        if (expected,'FINISHED') not in after:
            raise ValueError('人工决定没有进入预期分支')
        records.append({'choice':choice,'paused':True,'resumed':True,'branch':expected,
                        'response':resumed.get('text',''),'chat_id':resumed.get('chatId')})
    return {'platform':'Flowise Agentflow V2','branches':records,'publication':False,'grading':False,
            'human_adoption':'pending'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base-url',default='http://127.0.0.1:3000')
    p.add_argument('--flow-id',required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('不覆盖已有文件')
    report=pilot(a.base_url,a.flow_id,os.getenv('FLOWISE_API_KEY'))
    a.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('Flowise 暂停、Reject/Proceed 与恢复均通过。')
if __name__=='__main__':main()
