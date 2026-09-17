// Trusted, read-only DOM tool; no model-generated JavaScript is executed.
(args) => {
  const cards = [...document.querySelectorAll(args.card_selector)];
  const card = cards[args.card_index];
  if (!card) throw new Error('Card index outside listing');
  const all = [card, ...card.querySelectorAll('*')];
  const norm = s => (s || '').replace(/\s+/g, ' ').trim();
  const excluded = n => !!n.closest('script,style,noscript,svg,template');
  const attrs = n => Object.fromEntries(['aria-label','aria-description','title','alt','data-test','itemprop','content'].filter(a=>n.hasAttribute(a)).map(a=>[a,n.getAttribute(a)]));
  const paths = n => {
    let parts=[];
    while(n && n.nodeType===1) {
      const tag=n.localName;
      const sibs=n.parentElement?[...n.parentElement.children].filter(e=>e.localName===tag):[n];
      parts.unshift({tag, i:sibs.indexOf(n)+1});n=n.parentElement;
    }
    return {css:parts.map(p=>`${p.tag}:nth-of-type(${p.i})`).join(' > '), xpath:'/'+parts.map(p=>`${p.tag}[${p.i}]`).join('/')};
  };
  if (args.action==='inspect') {
    return args.node_ids.map(id=> {
      const n=all[id];if(!n || excluded(n)) throw new Error('Invalid node_id');
      return {node_id:id,tag:n.localName,...paths(n),text_quote:norm(n.textContent),attributes:attrs(n)};
    });
  }
  const nodes=all.flatMap((n,id)=> {
    if(excluded(n))return [];
    const own=norm([...n.childNodes].filter(c=>c.nodeType===3).map(c=>c.textContent).join(' '));
    const a=attrs(n);
    if(!own && !Object.keys(a).length)return [];
    return [{node_id:id,tag:n.localName,parent_node_id:all.indexOf(n.parentElement),text:own,attributes:a}];
  });
  const offset=args.offset||0, limit=60;
  return {card_index:args.card_index, total_cards:cards.length, total_nodes:nodes.length,offset,next_offset:offset+limit<nodes.length?offset+limit:null,nodes:nodes.slice(offset,offset+limit)};
}
