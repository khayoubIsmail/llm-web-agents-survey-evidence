import asyncio,json
from r1.common import ROOT,config,read_json
from r1.offline_dom import OfflineDOM
from agents.direct_dom import DirectDOMSnapshotAgent
from agents.ground_verify import SchemaStateGroundVerifyAgent

class A1FixtureClient:
    def __init__(self,record):self.record=record;self.calls=0
    async def complete(self,messages):self.calls+=1;return json.dumps(self.record)

class A2FixtureClient:
    def __init__(self,record):self.record=record;self.calls=0;self.ids={}
    async def complete(self,messages):
        self.calls+=1
        payload=json.loads(messages[-1]['content'])
        if 'nodes' in payload:
            nodes=payload['nodes']
            def pick(field):
                ev=self.record['evidence'][field]
                quote=ev['text_quote']
                attr=ev['attribute']
                for n in nodes:
                    actual=n['attributes'].get(attr,'') if attr else n['text']
                    if actual==quote or (field=='product_name' and quote in (n['text'] or '')):
                        return n['node_id']
                raise AssertionError(f'could not find {field}')
            self.ids={'product_name':pick('product_name'),'price':pick('price'),'rating':pick('rating') if self.record['rating'] is not None else None}
            return json.dumps({'product_name':self.record['product_name'],'price':self.record['price'],'rating':self.record['rating'],'node_ids':self.ids})
        grounded=payload['grounded_nodes'];by_id={n['node_id']:n for n in grounded};out={k:v for k,v in self.record.items() if k!='evidence'};out['evidence']={}
        for field,node_id in self.ids.items():
            if node_id is None:continue
            n=by_id[node_id];orig=self.record['evidence'][field];attr=orig['attribute']
            out['evidence'][field]={'css':n['css'],'xpath':n['xpath'],'text_quote':n['attributes'][attr] if attr else n['text_quote'],'attribute':attr}
        return json.dumps(out)

def test_a1_and_a2_are_distinct_offline_architectures(tmp_path):
    cfg=config();site='site_01';gold=read_json(ROOT/'gold/site_01.json')['records'][0]
    async def run():
        env1=OfflineDOM(site,cfg['sites'][site]);c1=A1FixtureClient(gold);a1=DirectDOMSnapshotAgent(c1,env1,cfg,tmp_path/'a1')
        o1=await a1.run(1);assert not a1.errors and o1['records'][0]['price']==gold['price'] and c1.calls==1
        env2=OfflineDOM(site,cfg['sites'][site]);c2=A2FixtureClient(gold);a2=SchemaStateGroundVerifyAgent(c2,env2,cfg,tmp_path/'a2')
        o2=await a2.run(1);assert not a2.errors and o2['records'][0]['price']==gold['price'] and c2.calls==2
        assert env1.actions==1
        assert env2.actions>=2
    asyncio.run(run())

def test_gold_selector_pairs_exist_in_offline_catalog():
    cfg=config()
    for site,sc in cfg['sites'].items():
        env=OfflineDOM(site,sc);gold=read_json(ROOT/'gold'/f'{site}.json')['records']
        for i,record in enumerate(gold):
            pairs={(n['css'],n['xpath']) for n in env.snapshot(i)['evidence_catalog']}
            for ev in record['evidence'].values():assert (ev['css'],ev['xpath']) in pairs
