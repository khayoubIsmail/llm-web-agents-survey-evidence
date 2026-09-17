#!/usr/bin/env python3
"""Entry point: verify, doctor, smoke, run-all, evaluate, serve, freeze."""
import argparse,asyncio,json,sys
from r1.common import ROOT,config,freeze,verify_freeze,write_json,error_text
from r1.server import serve
from r1.validation import validate_gold,validate_browser

def main():
    cfg=config()
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('command',choices=['verify','doctor','smoke','run-all','evaluate','serve','freeze'])
    p.add_argument('--agent',choices=list(cfg['agents']))
    p.add_argument('--architecture',choices=list(cfg['architectures']))
    p.add_argument('--model',choices=list(cfg['models']))
    p.add_argument('--run-index',type=int)
    p.add_argument('--browser',action='store_true',help='Verify gold locator pairs in Chromium through MCP')
    p.add_argument('--allow-partial',action='store_true',help='Allow explicitly labelled incomplete evaluation')
    args=p.parse_args()
    if args.command=='freeze':
        validate_gold();freeze();print('Experiment frozen.');return
    verify_freeze();print('Freeze verified. Gold:',json.dumps(validate_gold()))
    if args.command=='evaluate':
        from r1.evaluation import evaluate
        evaluate(args.allow_partial);print('Evaluation written to results/REPORT.md and CSV files.');return
    if args.command=='verify' and not args.browser:return
    if args.command=='serve':
        with serve(cfg['port']) as base:
            print(base,flush=True)
            try:input('Press Enter to stop.\n')
            except (EOFError,KeyboardInterrupt):pass
        return
    with serve(cfg['port']) as base:
        if args.command in ('doctor','verify'):
            result=asyncio.run(validate_browser(base,ROOT/'diagnostics'/'browser'));print('Browser:',json.dumps(result))
            if args.command=='doctor':
                from r1.runner import check_models
                ids=list(cfg['agents'])
                if args.agent:ids=[args.agent]
                if args.architecture:ids=[a for a in ids if cfg['agents'][a]['architecture']==args.architecture]
                if args.model:ids=[a for a in ids if cfg['agents'][a]['model_key']==args.model]
                identity=asyncio.run(check_models(ids));write_json(ROOT/'diagnostics/model_availability.json',identity)
                print('All selected model backends loaded and answered a real request.')
        else:
            from r1.runner import run_all
            statuses=asyncio.run(run_all(base,args.agent,args.run_index,args.command=='smoke',args.architecture,args.model))
            if any(s['status']!='completed' for s in statuses):
                raise RuntimeError('Some runs failed or were partial. Inspect metadata/card_errors/model_calls; failed formal runs remain recorded.')
            if args.command=='smoke':print('Smoke runs completed. Inspect their JSON before the formal experiment.')

if __name__=='__main__':
    try:main()
    except Exception as exc:
        print(f'ERROR: {error_text(exc)}',file=sys.stderr);sys.exit(1)
