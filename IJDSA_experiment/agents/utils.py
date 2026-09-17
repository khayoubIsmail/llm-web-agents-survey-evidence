import json
from r1.common import write_json

REQUIRED_FIELDS = ('product_name', 'price', 'rating')

def validate_record_shape(record):
    if not isinstance(record, dict):
        raise ValueError('record must be an object')
    if set(record) != {'product_name','price','rating','evidence'}:
        raise ValueError('record must contain exactly product_name, price, rating, evidence')
    if not isinstance(record.get('product_name'), str) or not record['product_name'].strip():
        raise ValueError('product_name must be a non-empty string')
    price = record.get('price')
    if not isinstance(price, dict) or set(price) != {'amount','currency'}:
        raise ValueError('price must contain exactly amount and currency')
    if type(price.get('amount')) not in (int,float):
        raise ValueError('price.amount must be numeric')
    if price.get('currency') != 'EUR':
        raise ValueError('price.currency must be EUR')
    rating = record.get('rating')
    if rating is not None and (type(rating) not in (int,float) or not (0 <= rating <= 5)):
        raise ValueError('rating must be null or a number from 0 to 5')
    evidence = record.get('evidence')
    if not isinstance(evidence, dict):
        raise ValueError('evidence must be an object')
    expected = {'product_name','price'} | ({'rating'} if rating is not None else set())
    if set(evidence) != expected:
        raise ValueError('evidence keys must match non-null fields')
    for field in expected:
        ev=evidence[field]
        if not isinstance(ev,dict): raise ValueError(f'{field} evidence must be an object')
        if not isinstance(ev.get('css'),str) or not ev['css'].strip(): raise ValueError(f'{field}: css required')
        if not isinstance(ev.get('xpath'),str) or not ev['xpath'].strip(): raise ValueError(f'{field}: xpath required')
        if not isinstance(ev.get('text_quote'),str) or not ev['text_quote'].strip(): raise ValueError(f'{field}: text_quote required')
        if ev.get('attribute') not in (None,'aria-label','aria-description','title','alt','content'):
            raise ValueError(f'{field}: unsupported attribute')
    return record

def selectors_from_catalog(record, catalog):
    pairs={(n['css'],n['xpath']) for n in catalog}
    ev=record['evidence']
    for field in ('product_name','price','rating'):
        if field=='rating' and record.get('rating') is None: continue
        item=ev[field]
        if (item['css'],item['xpath']) not in pairs:
            raise ValueError(f'{field}: CSS/XPath pair must be copied from supplied evidence catalog')
    return record

def save_progress(agent, records):
    write_json(agent.run_dir/'output.json', {'records':records})
    write_json(agent.run_dir/'card_errors.json', agent.errors)

def parse_json_object(raw):
    obj=json.loads(raw)
    if not isinstance(obj,dict): raise ValueError('Return one JSON object only')
    return obj
