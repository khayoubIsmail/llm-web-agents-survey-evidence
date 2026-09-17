import json
from r1.common import ROOT
from .utils import validate_record_shape,selectors_from_catalog,save_progress,parse_json_object

class DirectDOMSnapshotAgent:
    """A1: one-shot card extraction from frozen DOM + exact selector catalog; no browser/MCP."""
    def __init__(self,client,environment,config,run_dir):
        self.client=client;self.env=environment;self.config=config;self.run_dir=run_dir;self.errors=[]
    async def extract_card(self,index):
        prompt=(ROOT/'prompts/a1_direct_dom_snapshot.txt').read_text(encoding='utf-8')
        snap=self.env.snapshot(index)
        messages=[{'role':'system','content':prompt},{'role':'user','content':json.dumps(snap,ensure_ascii=False)}]
        attempts=1+self.config.get('direct_repairs',0)
        last=None
        for attempt in range(attempts):
            raw=await self.client.complete(messages)
            try:
                record=validate_record_shape(parse_json_object(raw))
                return selectors_from_catalog(record,snap['evidence_catalog'])
            except Exception as exc:
                last=exc
                if attempt+1>=attempts:break
                messages += [{'role':'assistant','content':raw},{'role':'user','content':json.dumps({'format_error':str(exc),'instruction':'Return a corrected record only. Do not change a value unless needed to satisfy the evidence you were given.'},ensure_ascii=False)}]
        raise RuntimeError(f'A1 output invalid after bounded repair: {last}')
    async def run(self,limit):
        records=[]
        for index in range(limit):
            try:records.append(await self.extract_card(index))
            except Exception as exc:self.errors.append({'card_index':index,'error':str(exc)})
            save_progress(self,records)
        return {'records':records}
