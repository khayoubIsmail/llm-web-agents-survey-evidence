"""Actual HTTP clients. No model substitution or simulated production responses."""
import os,json
import httpx
from .common import now

class ModelClient:
    def __init__(self, settings, config, log_path=None):
        self.settings=settings;self.config=config;self.log_path=log_path
        self.input_tokens=0;self.output_tokens=0;self.calls=0
        self.identification={}
    def base(self):
        if self.settings['provider']=='ollama': return os.getenv('OLLAMA_BASE_URL','http://127.0.0.1:11434').rstrip('/')
        return os.getenv('MOONSHOT_BASE_URL','https://api.moonshot.ai/v1').rstrip('/')
    def headers(self):
        if self.settings['provider']=='ollama':return {}
        key=os.getenv('MOONSHOT_API_KEY','')
        if not key or key=='YOUR_KEY_HERE':raise RuntimeError('Set MOONSHOT_API_KEY in .env')
        return {'Authorization':'Bearer '+key}
    async def identify(self):
        local=self.settings['provider']=='ollama';model=self.settings['model']
        async with httpx.AsyncClient(timeout=30,trust_env=False) as client:
            r=await client.get(self.base()+('/api/tags' if local else '/models'),headers=self.headers())
            r.raise_for_status();data=r.json()
            models=data.get('models' if local else 'data',[])
            matches=[m for m in models if (m.get('name') if local else m.get('id'))==model]
            if not matches:raise RuntimeError(f'Model {model} not available at configured provider. '+(f'Run: ollama pull {model}' if local else 'Check your API account and model ID.'))
            self.identification=matches[0]
            if local:
                r=await client.get(self.base()+'/api/version');r.raise_for_status()
                self.identification['ollama_version']=r.json().get('version')
        return self.identification
    async def complete(self,messages):
        local=self.settings['provider']=='ollama'
        body={'model':self.settings['model'],'messages':messages,'stream':False}
        if local:
            body.update({'format':'json','options':{'temperature':self.config['local_temperature'],'num_ctx':self.config['num_ctx'],'num_predict':self.config['max_tokens']}})
        else:
            # Kimi K2.6 has provider-fixed sampling: do not send temperature=0.
            body.update({'thinking':{'type':'disabled'},'max_tokens':self.config['max_tokens']})
        async with httpx.AsyncClient(timeout=self.config['request_timeout_seconds'],trust_env=False) as client:
            r=await client.post(self.base()+('/api/chat' if local else '/chat/completions'),headers=self.headers(),json=body)
            if r.is_error:raise RuntimeError(f'{self.settings["provider"]} HTTP {r.status_code}: {r.text[:400]}')
            data=r.json()
        self.calls+=1
        if local:
            content=data['message']['content'];it=data.get('prompt_eval_count',0);ot=data.get('eval_count',0)
            finish=data.get('done_reason');actual=data.get('model')
        else:
            choice=data['choices'][0];content=choice['message'].get('content') or ''
            it=data.get('usage',{}).get('prompt_tokens',0);ot=data.get('usage',{}).get('completion_tokens',0)
            finish=choice.get('finish_reason');actual=data.get('model')
        self.input_tokens+=it;self.output_tokens+=ot
        if self.log_path:
            with self.log_path.open('a',encoding='utf-8') as f:
                f.write(json.dumps({'at':now(),'request':body,'response':data},ensure_ascii=False)+'\n')
        if finish in ('length','max_tokens'):raise RuntimeError('Model output exceeded token budget')
        # Moonshot/Kimi sometimes wraps JSON in ```json...``` fences; strip them.
        if not local:
            stripped=content.strip()
            if stripped.startswith('```'):
                stripped=stripped.split('\n',1)[-1]
                if '```' in stripped:stripped=stripped.rsplit('```',1)[0]
                content=stripped.strip()
        return content
