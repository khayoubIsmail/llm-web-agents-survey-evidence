import json
from lxml import html
from jsonschema import Draft202012Validator
from .common import ROOT,config,read_json
from .evaluation import locate,quote_norm
from .offline_dom import select_cards

def validate_gold():
    cfg=config();schema=read_json(ROOT/'schema/output.schema.json');counts=[]
    for site,sc in cfg['sites'].items():
        data=read_json(ROOT/'gold'/f'{site}.json');records=data['records']
        Draft202012Validator(schema).validate({'records':records})
        if len(records)!=sc['limit']:raise RuntimeError('Gold size differs from task scope')
        doc=html.fromstring((ROOT/'snapshots'/site/'index.html').read_text(encoding='utf-8'));cards=select_cards(doc,sc['card_selector'])
        count=0
        for i,r in enumerate(records):
            for field,e in r['evidence'].items():
                n=locate(doc,e)
                if n is None or not (n is cards[i] or cards[i] in n.iterancestors()):raise RuntimeError(f'{site}/{i}/{field}: locator mismatch')
                actual=n.get(e['attribute'],'') if e['attribute'] else n.text_content()
                if quote_norm(actual)!=quote_norm(e['text_quote']):raise RuntimeError(f'{site}/{i}/{field}: quote mismatch')
                count+=1
        counts.append({'site':site,'records':len(records),'locator_pairs':count})
    return counts

async def validate_browser(base_url,destination):
    from .browser import browser_session
    cfg=config();results=[]
    for site,sc in cfg['sites'].items():
        async with browser_session(base_url,site,sc,destination/site,10) as b:
            records=read_json(ROOT/'gold'/f'{site}.json')['records']
            # Only validation sees gold locators; experimental agents never receive them.
            entries=[{'card_index':i,'field':f,**e} for i,r in enumerate(records) for f,e in r['evidence'].items()]
            fn='''() => { const entries=ENTRIES; const norm=s=>(s||'').replace(/\\s+/g,' ').trim();
            return entries.map(e=>{let c=document.querySelectorAll(e.css);let x=document.evaluate(e.xpath,document,null,XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,null);
            let n=c[0];let same=c.length===1 && x.snapshotLength===1 && n===x.snapshotItem(0);
            let text=n?(e.attribute?n.getAttribute(e.attribute):n.textContent):'';
            return {field:e.field,card_index:e.card_index,ok:same && norm(text)===norm(e.text_quote)};});}'''.replace('ENTRIES',json.dumps(entries))
            text=await b.call('browser_evaluate',{'function':fn})
            payload=text.split('### Result\n',1)[1].split('\n### ',1)[0].strip()
            vals=json.loads(payload)
            if not all(v['ok'] for v in vals):raise RuntimeError(f'Browser gold validation failed on {site}: {[v for v in vals if not v["ok"]]}')
            results.append({'site':site,'browser_verified_pairs':len(vals)})
    return results
