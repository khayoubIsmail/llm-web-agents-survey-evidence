from collections import Counter
from r1.common import config,read_json,ROOT
from agents import REGISTRY

def test_full_3x3_matrix_and_schedule():
    cfg=config();schedule=read_json(ROOT/'execution_schedule.json')
    assert set(cfg['architectures'])=={'A1','A2','A3'}
    assert set(cfg['models'])=={'gemma','qwen','kimi'}
    assert len(cfg['agents'])==9
    assert set(REGISTRY)==set(cfg['architectures'])
    combos={(v['architecture'],v['model_key']) for v in cfg['agents'].values()}
    assert len(combos)==9
    assert combos=={(a,m) for a in cfg['architectures'] for m in cfg['models']}
    assert len(schedule)==108
    assert len({(e['agent'],e['site'],e['rep']) for e in schedule})==108
    counts=Counter(e['agent'] for e in schedule)
    assert set(counts.values())=={12}
    assert sorted(e['run_index'] for e in schedule)==list(range(1,109))

def test_only_a3_uses_playwright_mcp():
    cfg=config()
    assert cfg['architectures']['A1']['environment']=='offline_dom'
    assert cfg['architectures']['A2']['environment']=='offline_dom'
    assert cfg['architectures']['A3']['environment']=='playwright_mcp'
    assert cfg['architectures']['A3']['uses_playwright_mcp'] is True
