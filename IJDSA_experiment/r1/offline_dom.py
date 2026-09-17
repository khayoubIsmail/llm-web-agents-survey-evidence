from pathlib import Path
from lxml import html, etree
from .common import ROOT

ATTRS=('aria-label','aria-description','title','alt','data-test','itemprop','content')
EXCLUDED={'script','style','noscript','svg','template'}

def norm(s): return ' '.join((s or '').split())

def _element_children(parent):
    return [c for c in parent if isinstance(c.tag,str)] if parent is not None else []

def selector_paths(node):
    parts=[];cur=node
    while cur is not None and isinstance(cur.tag,str):
        tag=cur.tag.lower()
        parent=cur.getparent()
        sibs=[c for c in _element_children(parent) if c.tag.lower()==tag] if parent is not None else [cur]
        idx=sibs.index(cur)+1
        parts.append((tag,idx));cur=parent
    parts.reverse()
    css=' > '.join(f'{tag}:nth-of-type({idx})' for tag,idx in parts)
    xpath='/'+'/'.join(f'{tag}[{idx}]' for tag,idx in parts)
    return {'css':css,'xpath':xpath}

def _is_excluded(node,card):
    cur=node
    while cur is not None:
        if isinstance(cur.tag,str) and cur.tag.lower() in EXCLUDED:return True
        if cur is card:return False
        cur=cur.getparent()
    return False

def attrs(node):
    return {a:node.get(a) for a in ATTRS if node.get(a) is not None}

def select_cards(doc, selector):
    if selector == "article[data-test='mms-product-card']":
        return doc.xpath("//article[@data-test='mms-product-card']")
    if selector == 'a.card.productBox':
        return doc.xpath("//a[contains(concat(' ', normalize-space(@class), ' '), ' card ') and contains(concat(' ', normalize-space(@class), ' '), ' productBox ')]")
    if selector == "div[data-component-type='s-search-result']":
        return doc.xpath("//div[@data-component-type='s-search-result']")
    raise ValueError(f'Unsupported frozen-task card selector: {selector}')

def own_text(node):
    chunks=[]
    if node.text:chunks.append(node.text)
    for child in node:
        if child.tail:chunks.append(child.tail)
    return norm(' '.join(chunks))

class OfflineDOM:
    def __init__(self, site, site_config):
        self.site=site;self.site_config=site_config
        source=(ROOT/'snapshots'/site/'index.html').read_text(encoding='utf-8')
        self.doc=html.fromstring(source)
        sel=site_config['card_selector']
        self.cards=select_cards(self.doc, sel)[:site_config['limit']]
        if len(self.cards)<site_config['limit']:
            raise RuntimeError(f'{site}: expected {site_config["limit"]} cards, found {len(self.cards)}')
        self.actions=0
    def _all(self,index):
        card=self.cards[index]
        return [card]+[n for n in card.iterdescendants() if isinstance(n.tag,str)]
    def inspect(self,index,node_ids):
        self.actions+=1
        all_nodes=self._all(index);card=self.cards[index];out=[]
        for node_id in node_ids:
            if type(node_id) is not int or node_id<0 or node_id>=len(all_nodes): raise ValueError('Invalid node_id')
            n=all_nodes[node_id]
            if _is_excluded(n,card): raise ValueError('Excluded node_id')
            out.append({'node_id':node_id,'tag':n.tag.lower(),**selector_paths(n),'text_quote':norm(n.text_content()),'attributes':attrs(n)})
        return out
    def read(self,index,offset=0,limit=60):
        self.actions+=1
        all_nodes=self._all(index);card=self.cards[index];nodes=[]
        for node_id,n in enumerate(all_nodes):
            if _is_excluded(n,card):continue
            text=own_text(n);a=attrs(n)
            if not text and not a:continue
            parent=n.getparent();parent_id=all_nodes.index(parent) if parent in all_nodes else -1
            nodes.append({'node_id':node_id,'tag':n.tag.lower(),'parent_node_id':parent_id,'text':text,'attributes':a})
        return {'card_index':index,'total_cards':len(self.cards),'total_nodes':len(nodes),'offset':offset,'next_offset':offset+limit if offset+limit<len(nodes) else None,'nodes':nodes[offset:offset+limit]}
    async def dom(self,index,action='read',offset=0,node_ids=None):
        if action=='inspect':return self.inspect(index,node_ids or [])
        if action=='read':return self.read(index,offset)
        raise ValueError('Unknown action')
    def snapshot(self,index):
        self.actions+=1
        all_nodes=self._all(index);card=self.cards[index];catalog=[]
        for node_id,n in enumerate(all_nodes):
            if _is_excluded(n,card):continue
            text=norm(n.text_content());a=attrs(n)
            if not text and not a:continue
            catalog.append({'node_id':node_id,'tag':n.tag.lower(),**selector_paths(n),'text_quote':text,'attributes':a})
        outer=etree.tostring(card,encoding='unicode',method='html')
        return {'card_index':index,'total_cards':len(self.cards),'outer_html':outer,'evidence_catalog':catalog}
