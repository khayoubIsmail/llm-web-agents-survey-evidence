import asyncio,json
from r1.models import ModelClient
from r1.common import config
import httpx

def test_real_client_request_shapes(monkeypatch):
    seen=[]
    def handle(req):
        body=json.loads(req.content);seen.append((str(req.url),body))
        if '/api/chat' in str(req.url):return httpx.Response(200,json={'message':{'content':'{"ready":true}'},'prompt_eval_count':3,'eval_count':4})
        return httpx.Response(200,json={'model':'kimi-k2.6','choices':[{'message':{'content':'{"ready":true}'},'finish_reason':'stop'}],'usage':{'prompt_tokens':5,'completion_tokens':6}})
    original=httpx.AsyncClient
    monkeypatch.setattr(httpx,'AsyncClient',lambda **kw:original(transport=httpx.MockTransport(handle),**kw))
    monkeypatch.setenv('MOONSHOT_API_KEY','test-placeholder')
    async def run():
        cfg=config()
        for mk in ('gemma','qwen','kimi'):
            c=ModelClient(cfg['models'][mk],cfg);assert json.loads(await c.complete([{'role':'user','content':'test'}]))=={'ready':True}
            assert c.input_tokens>0 and c.output_tokens>0
    asyncio.run(run())
    assert seen[0][1]['model']=='gemma4:e4b'
    assert seen[1][1]['model']=='qwen3-vl:8b'
    assert seen[2][1]['model']=='kimi-k2.6' and 'temperature' not in seen[2][1]
    assert seen[2][1]['thinking']=={'type':'disabled'}
