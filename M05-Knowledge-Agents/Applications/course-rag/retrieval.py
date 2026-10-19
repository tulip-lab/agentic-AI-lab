"""Small auditable lexical retriever. No embeddings or semantic guarantees."""
import re
from collections import Counter
from math import sqrt
from run_demo import load, prepare


def tokens(text):
    english = re.findall(r'[a-z0-9]+', text.lower())
    chinese = re.findall(r'[\u4e00-\u9fff]+', text)
    return Counter(english + [part[i:i+2] for part in chinese for i in range(len(part)-1)])


def retrieve(case_dir, query, top_k=3):
    if not isinstance(query, str) or not query.strip() or not 1 <= top_k <= 6:
        raise ValueError('需要非空查询与 1–6 的 top_k')
    sources = load(case_dir / 'corpus.json')['sources']
    # Verify the complete case before ranking any source, including hash integrity.
    all_ids = [s['id'] for s in sources if s['trust'] == 'approved_teaching']
    for sid in all_ids:
        prepare(case_dir, {'topic':'检索核查','audience':'学习者','activity':'核查来源','source_ids':[sid]})
    q = tokens(query)
    ranked = []
    for source in sources:
        if source['trust'] != 'approved_teaching':
            continue
        t = tokens(source['title'] + source['text'])
        denominator = sqrt(sum(x*x for x in q.values()) * sum(x*x for x in t.values()))
        score = sum(n*t[k] for k,n in q.items()) / denominator if denominator else 0
        if score > 0: ranked.append({'source_id':source['id'], 'score':round(score,6)})
    ranked.sort(key=lambda item:(-item['score'], item['source_id']))
    if not ranked: raise ValueError('检索没有证据命中；请补充查询或资料')
    return ranked[:top_k]
