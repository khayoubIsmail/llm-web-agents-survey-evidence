import asyncio, sys, time, platform
from pathlib import Path
from importlib.metadata import version
from .common import ROOT,config,read_json,write_json,now,verify_freeze,error_text,digest
from .models import ModelClient
from .browser import browser_session
from .offline_dom import OfflineDOM
from agents import REGISTRY


def resolved_agent(cfg, aid):
    a=cfg['agents'][aid]
    arch_id=a['architecture'];model_key=a['model_key']
    model=dict(cfg['models'][model_key])
    arch=dict(cfg['architectures'][arch_id])
    return {'agent_id':aid,'architecture_id':arch_id,'model_key':model_key,'model':model,'architecture':arch}

async def check_models(agent_ids):
    cfg=config();by_model={}
    for aid in agent_ids:
        r=resolved_agent(cfg,aid);key=r['model_key']
        if key in by_model:continue
        client=ModelClient(r['model'],cfg)
        ident=await client.identify()
        text=await client.complete([{'role':'user','content':'Return exactly this JSON object: {"ready":true}'}])
        import json
        if json.loads(text)!={'ready':True}:raise RuntimeError(f'{key}: model generation probe did not return expected JSON')
        by_model[key]=ident
        print(f'OK model {key}: {r["model"]["model"]}',flush=True)
    return {aid:by_model[resolved_agent(cfg,aid)['model_key']] for aid in agent_ids}

async def execute(entry,base_url,run_root,identity,smoke=False):
    cfg=config();aid=entry['agent'];site=entry['site'];rep=entry['rep'];resolved=resolved_agent(cfg,aid)
    folder=Path(run_root)/aid/site/f'run_{rep:02d}'
    frozen=verify_freeze()
    if (folder/'metadata.json').exists():
        old=read_json(folder/'metadata.json')
        if old.get('finished'):
            if old.get('freeze_sha256')!=frozen:raise RuntimeError('Existing run belongs to another freeze; archive runs first')
            print(f'SKIP {aid}/{site}/{rep} ({old.get("status")})');return old
        archive=folder.with_name(folder.name+'_interrupted_'+str(time.time_ns()));folder.rename(archive)
    folder.mkdir(parents=True,exist_ok=True)
    started=time.monotonic()
    model_cfg=resolved['model'];arch_cfg=resolved['architecture']
    md={**entry,'started_at':now(),'finished':False,'smoke':smoke,'freeze_sha256':frozen,
        'architecture_id':resolved['architecture_id'],'architecture':arch_cfg,'model_key':resolved['model_key'],
        'model_config':model_cfg,'model_identity':identity,'python':sys.version,'platform':platform.platform(),
        'mcp_python_version':version('mcp'),'playwright_python_version':version('playwright'),
        'sampling':{'temperature':cfg['local_temperature']} if model_cfg['provider']=='ollama' else {'thinking':'disabled','temperature':'provider default 0.6'},
        'status':'running'}
    write_json(folder/'metadata.json',md)
    client=ModelClient(model_cfg,cfg,folder/'model_calls.jsonl');env=None;agent=None
    try:
        async with asyncio.timeout(cfg['max_run_seconds']):
            klass=REGISTRY[resolved['architecture_id']]
            if arch_cfg['environment']=='playwright_mcp':
                async with browser_session(base_url,site,cfg['sites'][site],folder,cfg['max_browser_actions']) as env:
                    agent=klass(client,env,cfg,folder)
                    output=await agent.run(1 if smoke else cfg['sites'][site]['limit'])
            else:
                env=OfflineDOM(site,cfg['sites'][site])
                agent=klass(client,env,cfg,folder)
                output=await agent.run(1 if smoke else cfg['sites'][site]['limit'])
            write_json(folder/'output.json',output)
            md['status']='completed' if not agent.errors else 'partial_failure'
    except Exception as exc:
        md['status']='failed';md['error']=error_text(exc)
        if not (folder/'output.json').exists():write_json(folder/'output.json',{'records':[]})
    finally:
        actions=getattr(env,'actions',0) if env is not None else 0
        md.update({'finished_at':now(),'finished':True,'latency_seconds':round(time.monotonic()-started,3),
                   'input_tokens':client.input_tokens,'output_tokens':client.output_tokens,'total_tokens':client.input_tokens+client.output_tokens,
                   'model_calls':client.calls,'tool_actions':actions,'browser_actions':actions if arch_cfg['environment']=='playwright_mcp' else 0})
        md['output_sha256']=digest(folder/'output.json');write_json(folder/'metadata.json',md)
    print(f'{aid}/{site}/run_{rep:02d}: {md["status"]} ({md["latency_seconds"]}s)',flush=True)
    return md

async def run_all(base_url,agent_id=None,run_index=None,smoke=False,architecture=None,model_key=None):
    cfg=config();ids=list(cfg['agents'])
    if agent_id:ids=[agent_id]
    if architecture:ids=[aid for aid in ids if cfg['agents'][aid]['architecture']==architecture]
    if model_key:ids=[aid for aid in ids if cfg['agents'][aid]['model_key']==model_key]
    if not ids:raise ValueError('No agent configurations match the selected filters')
    schedule=read_json(ROOT/'execution_schedule.json')
    if run_index is not None:
        selected=[e for e in schedule if e['run_index']==run_index]
        if not selected:raise ValueError(f'Run index must be 1-{len(schedule)}')
        ids=[selected[0]['agent']]
    identities=await check_models(ids)
    if smoke:
        entries=[{'run_index':0,'agent':aid,'site':'site_01','rep':1} for aid in ids]
        root=ROOT/'smoke_runs'/now().replace(':','-')
    else:
        entries=[e for e in schedule if e['agent'] in ids and (run_index is None or e['run_index']==run_index)]
        root=ROOT/'runs'
    statuses=[]
    for e in entries:statuses.append(await execute(e,base_url,root,identities[e['agent']],smoke))
    return statuses
