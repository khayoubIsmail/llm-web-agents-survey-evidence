import copy
import pytest
from lxml import html
from r1.common import ROOT,config,read_json
from r1.evaluation import score

@pytest.fixture
def data():
    site='site_01';g=read_json(ROOT/'gold'/f'{site}.json')['records']
    return g,html.fromstring((ROOT/'snapshots'/site/'index.html').read_text(encoding='utf-8')),config()['sites'][site]

def test_gold_perfect_all_sites():
    for site,sc in config()['sites'].items():
        g=read_json(ROOT/'gold'/f'{site}.json')['records'];d=html.fromstring((ROOT/'snapshots'/site/'index.html').read_text(encoding='utf-8'))
        r,_=score({'records':g},g,d,sc)
        assert r['strict_field_f1']==r['verified_provenance_precision']==r['record_f1']==r['schema_adherence']==r['task_success']==1

def test_empty_is_failure(data):
    g,d,c=data;r,_=score({'records':[]},g,d,c)
    assert r['strict_field_f1']==r['record_recall']==r['task_success']==r['verified_provenance_precision']==0

def test_old_price_penalized(data):
    g,d,c=data;p=copy.deepcopy(g);p[0]['price']['amount']=79.99
    r,_=score({'records':p},g,d,c)
    assert r['field_fp']==r['field_fn']==1
    assert r['unsupported_field_count']==1

def test_duplicate_is_false_positive(data):
    g,d,c=data;p=copy.deepcopy(g)+[copy.deepcopy(g[0])]
    r,_=score({'records':p},g,d,c)
    assert r['record_recall']==1 and r['record_precision']==10/11
    assert r['field_fp']==4

def test_wrong_selector_pair_and_quote(data):
    g,d,c=data;p=copy.deepcopy(g)
    p[0]['evidence']['price']['css']=p[1]['evidence']['price']['css']
    p[1]['evidence']['product_name']['text_quote']='fabricated'
    r,_=score({'records':p},g,d,c)
    assert r['strict_field_f1']==1 and r['verified_provenance_precision']<1 and r['selector_pair_coverage']<1

def test_null_hallucination(data):
    g,d,c=data;p=copy.deepcopy(g);p[2]['rating']=4.9;p[2]['evidence']['rating']=copy.deepcopy(g[0]['evidence']['rating'])
    r,_=score({'records':p},g,d,c)
    assert r['field_fp']==1 and r['null_rating_accuracy']==0

def test_missing_required_field_and_extra(data):
    g,d,c=data;p=copy.deepcopy(g);del p[0]['price']['currency'];p[0]['brand']='LEICKE'
    r,_=score({'records':p},g,d,c)
    assert r['schema_adherence']==0 and r['non_schema_field_count']==1 and r['field_fn']==1

def test_duplicate_names_reordered():
    site='site_03';g=read_json(ROOT/'gold'/f'{site}.json')['records'];d=html.fromstring((ROOT/'snapshots'/site/'index.html').read_text())
    r,_=score({'records':list(reversed(g))},g,d,config()['sites'][site])
    assert r['strict_field_f1']==1 and r['verified_provenance_precision']==1

def test_malformed_record(data):
    g,d,c=data;r,_=score({'records':[None,{},'bad',{'price':[]}]},g,d,c)
    assert r['schema_adherence']==0 and r['task_success']==0
