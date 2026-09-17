import json, os, shutil
from contextlib import asynccontextmanager
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from playwright.sync_api import sync_playwright
from .common import ROOT, now


def executable():
    custom = os.getenv('BROWSER_EXECUTABLE')
    if custom:
        if not Path(custom).is_file(): raise RuntimeError('BROWSER_EXECUTABLE does not point to a file')
        return custom
    # Only obtain the path; no sync browser is run in the asynchronous agent loop.
    from playwright._impl._driver import compute_driver_executable
    import subprocess
    code = 'from playwright.sync_api import sync_playwright\nwith sync_playwright() as p: print(p.chromium.executable_path)'
    import sys
    path = subprocess.check_output([sys.executable,'-c',code],text=True).strip()
    if not Path(path).is_file(): raise RuntimeError('Browser missing. Run: python -m playwright install chromium')
    return path

class Browser:
    def __init__(self, session, site_config, log_path, max_actions):
        self.session=session;self.site_config=site_config;self.log_path=Path(log_path)
        self.actions=0;self.max_actions=max_actions
    async def call(self,name,args):
        if self.actions>=self.max_actions: raise RuntimeError('Browser action budget exhausted')
        self.actions+=1
        result=await self.session.call_tool(name,args)
        blocks=[b.text for b in result.content if getattr(b,'type',None)=='text']
        text='\n'.join(blocks)
        with self.log_path.open('a',encoding='utf-8') as f:
            f.write(json.dumps({'at':now(),'tool':name,'arguments':args,'is_error':result.is_error,'result':text},ensure_ascii=False)+'\n')
        if result.is_error: raise RuntimeError('MCP tool failed: '+text[:500])
        return text
    async def dom(self,card_index,action='read',offset=0,node_ids=None):
        args={'card_selector':self.site_config['card_selector'],'card_index':card_index,'action':action,'offset':offset,'node_ids':node_ids or []}
        code=(ROOT/'r1/dom.js').read_text(encoding='utf-8')
        text=await self.call('browser_evaluate',{'function':f'() => ({code})({json.dumps(args)})'})
        # Playwright MCP returns a Result section followed by code/snapshot sections.
        if '### Result\n' not in text: raise RuntimeError('Unexpected MCP evaluate result format')
        content=text.split('### Result\n',1)[1].split('\n### ',1)[0].strip()
        if content.startswith('```'):
            content=content.split('\n',1)[1].rsplit('```',1)[0].strip()
        return json.loads(content)

@asynccontextmanager
async def browser_session(base_url,site,site_config,run_dir,max_actions=80):
    node=shutil.which('node');cli=ROOT/'node_modules/@playwright/mcp/cli.js'
    if not node or not cli.exists(): raise RuntimeError('Node/MCP missing. Install Node.js 20+ and run npm ci.')
    run_dir=Path(run_dir);run_dir.mkdir(parents=True,exist_ok=True)
    # Local exact-path network allowlist, including redirect requests. No external images/scripts.
    init=run_dir/'browser_init.js'
    url=f'{base_url}/{site}/'
    init.write_text('module.exports = async ({ page }) => {\n'
       +'await page.context().route("**/*", route => { const u=new URL(route.request().url()); '
       +f'if(u.origin === {json.dumps(base_url)} && ["/{site}/","/{site}/index.html"].includes(u.pathname)) '
       +'return route.continue(); return route.abort(); });\n};',encoding='utf-8')
    args=[str(cli),'--headless','--isolated','--block-service-workers','--snapshot-mode','none','--image-responses','omit','--executable-path',executable(),'--init-page',str(init),'--output-dir',str(run_dir/'browser_artifacts'),'--viewport-size','1440,900']
    if hasattr(os,'geteuid') and os.geteuid()==0: args.append('--no-sandbox')
    # Do not pass the model API key to the browser subprocess.
    env={k:v for k,v in os.environ.items() if not any(s in k.upper() for s in ('API_KEY','TOKEN','SECRET','PASSWORD'))}
    params=StdioServerParameters(command=node,args=args,env=env,cwd=str(ROOT))
    with (run_dir/'mcp_stderr.log').open('w',encoding='utf-8') as err:
        async with stdio_client(params,errlog=err) as streams:
            async with ClientSession(*streams) as session:
                await session.initialize()
                available={t.name for t in (await session.list_tools()).tools}
                if not {'browser_navigate','browser_evaluate'}.issubset(available):
                    raise RuntimeError('MCP missing required browser tools')
                b=Browser(session,site_config,run_dir/'browser_tools.jsonl',max_actions)
                await b.call('browser_navigate',{'url':url})
                yield b
