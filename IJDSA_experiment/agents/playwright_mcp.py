import json
from r1.common import ROOT
from .utils import validate_record_shape,selectors_from_catalog,save_progress,parse_json_object

class PlaywrightMCPReActAgent:
    """A3: iterative ReAct-style extraction through real Playwright MCP read/inspect browser tools."""
    def __init__(self,client,environment,config,run_dir):
        self.client=client;self.browser=environment;self.config=config;self.run_dir=run_dir;self.errors=[]
    async def extract_card(self,index):
        prompt=(ROOT/'prompts/a3_playwright_mcp_react.txt').read_text(encoding='utf-8')
        observation=await self.browser.dom(index)
        messages=[{'role':'system','content':prompt},{'role':'user','content':json.dumps({'assigned_card_index':index,'observation':observation},ensure_ascii=False)}]
        inspected=[]
        for turn in range(self.config['max_turns_per_card']):
            raw=await self.client.complete(messages);messages.append({'role':'assistant','content':raw})
            try:
                action=parse_json_object(raw)
                if action.get('action')=='final':
                    if not inspected:raise ValueError('Inspect evidence nodes before finalizing')
                    record=validate_record_shape(action.get('record'))
                    return selectors_from_catalog(record,inspected)
                if action.get('action')=='inspect':
                    ids=action.get('node_ids')
                    if not isinstance(ids,list) or not 1<=len(ids)<=8 or not all(type(i) is int and i>=0 for i in ids):raise ValueError('node_ids must contain 1-8 nonnegative integers')
                    observation=await self.browser.dom(index,'inspect',node_ids=ids);inspected.extend(observation)
                elif action.get('action')=='read':
                    offset=action.get('offset',0)
                    if type(offset) is not int or not 0<=offset<=10000:raise ValueError('Invalid offset')
                    observation=await self.browser.dom(index,'read',offset=offset)
                else:raise ValueError('Use read, inspect, or final action')
                feedback={'tool_result':observation,'remaining_turns':self.config['max_turns_per_card']-turn-1,'note':'inspect and finalize before turns run out'}
            except Exception as exc:
                feedback={'error':str(exc),'remaining_turns':self.config['max_turns_per_card']-turn-1}
            messages.append({'role':'user','content':json.dumps(feedback,ensure_ascii=False)})
        raise RuntimeError('A3 card turn budget exhausted')
    async def run(self,limit):
        records=[]
        for index in range(limit):
            try:records.append(await self.extract_card(index))
            except Exception as exc:self.errors.append({'card_index':index,'error':str(exc)})
            save_progress(self,records)
        return {'records':records}
