import json
from r1.common import ROOT
from .utils import validate_record_shape,selectors_from_catalog,save_progress,parse_json_object

class SchemaStateGroundVerifyAgent:
    """A2: fixed two-stage architecture: value/node planning -> exact node grounding -> verified final JSON."""
    def __init__(self,client,environment,config,run_dir):
        self.client=client;self.env=environment;self.config=config;self.run_dir=run_dir;self.errors=[]
    async def extract_card(self,index):
        p1=(ROOT/'prompts/a2_ground_plan.txt').read_text(encoding='utf-8')
        chunks=[];offset=0
        while True:
            obs=await self.env.dom(index,'read',offset=offset)
            chunks.extend(obs['nodes'])
            if obs['next_offset'] is None:break
            offset=obs['next_offset']
        messages=[{'role':'system','content':p1},{'role':'user','content':json.dumps({'card_index':index,'nodes':chunks},ensure_ascii=False)}]
        raw=await self.client.complete(messages);draft=parse_json_object(raw)
        if set(draft)!={'product_name','price','rating','node_ids'}:raise ValueError('A2 planning output must contain product_name, price, rating, node_ids')
        ids=draft.get('node_ids')
        if not isinstance(ids,dict):raise ValueError('node_ids must be an object')
        chosen=[]
        for field in ('product_name','price','rating'):
            node_id=ids.get(field)
            if field=='rating' and draft.get('rating') is None:
                if node_id is not None:raise ValueError('rating node_id must be null when rating is null')
                continue
            if type(node_id) is not int or node_id<0:raise ValueError(f'{field} node_id must be a nonnegative integer')
            chosen.append(node_id)
        grounded=await self.env.dom(index,'inspect',node_ids=list(dict.fromkeys(chosen)))
        p2=(ROOT/'prompts/a2_finalize_verified.txt').read_text(encoding='utf-8')
        final_messages=[{'role':'system','content':p2},{'role':'user','content':json.dumps({'draft':draft,'grounded_nodes':grounded},ensure_ascii=False)}]
        attempts=1+self.config.get('plan_verify_repairs',0);last=None
        for attempt in range(attempts):
            raw2=await self.client.complete(final_messages)
            try:
                record=validate_record_shape(parse_json_object(raw2))
                return selectors_from_catalog(record,grounded)
            except Exception as exc:
                last=exc
                if attempt+1>=attempts:break
                final_messages += [{'role':'assistant','content':raw2},{'role':'user','content':json.dumps({'format_error':str(exc),'instruction':'Return corrected final JSON using only the grounded nodes.'},ensure_ascii=False)}]
        raise RuntimeError(f'A2 final output invalid after bounded repair: {last}')
    async def run(self,limit):
        records=[]
        for index in range(limit):
            try:records.append(await self.extract_card(index))
            except Exception as exc:self.errors.append({'card_index':index,'error':str(exc)})
            save_progress(self,records)
        return {'records':records}
