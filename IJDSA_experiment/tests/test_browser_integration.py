"""Actual MCP+Chromium integration for A3 with a scripted model fixture."""
import asyncio,json,os
import pytest
from agents.playwright_mcp import PlaywrightMCPReActAgent
from r1.common import ROOT,read_json,config
from r1.server import serve

pytestmark=pytest.mark.skipif(os.getenv('R1_BROWSER_TESTS')!='1',reason='Set R1_BROWSER_TESTS=1 after installing Chromium and npm dependencies')

class ScriptedModel:
    def __init__(self,record):self.record=record;self.count=0
    async def complete(self,messages):
        self.count+=1
        if self.count==1:
            nodes=json.loads(messages[-1]['content'])['observation']['nodes']
            name=next(n for n in nodes if n['attributes'].get('data-test')=='product-title')
            price=next(n for n in nodes if n['text'].replace(' ','')=='36,99€')
            rating=next(n for n in nodes if 'von 5' in n['attributes'].get('aria-label',''))
            return json.dumps({'action':'inspect','node_ids':[name['node_id'],price['node_id'],rating['node_id']]})
        observations=json.loads(messages[-1]['content'])['tool_result'];record={k:v for k,v in self.record.items() if k!='evidence'};record['evidence']={}
        for field,n in zip(['product_name','price','rating'],observations):
            attr='aria-label' if field=='rating' else None
            record['evidence'][field]={'css':n['css'],'xpath':n['xpath'],'text_quote':n['attributes'][attr] if attr else n['text_quote'],'attribute':attr}
        return json.dumps({'action':'final','record':record})

def test_a3_uses_real_mcp(tmp_path):
    from r1.browser import browser_session
    cfg=config();record=read_json(ROOT/'gold/site_01.json')['records'][0]
    async def run(base):
        async with browser_session(base,'site_01',cfg['sites']['site_01'],tmp_path,10) as browser:
            client=ScriptedModel(record);agent=PlaywrightMCPReActAgent(client,browser,cfg,tmp_path)
            output=await agent.run(1)
            assert not agent.errors and output['records'][0]['price']==record['price']
            assert browser.actions==3 and client.count==2
    with serve(0) as base:asyncio.run(run(base))
    calls=[json.loads(s) for s in (tmp_path/'browser_tools.jsonl').read_text().splitlines()]
    assert [c['tool'] for c in calls]==['browser_navigate','browser_evaluate','browser_evaluate']
