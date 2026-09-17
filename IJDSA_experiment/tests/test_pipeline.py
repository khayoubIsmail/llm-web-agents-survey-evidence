import copy
import pytest
from r1.common import ROOT,read_json,write_json,verify_freeze,config
from r1.evaluation import evaluate

def test_complete_evaluation_and_partial_gate(tmp_path):
    run_root=tmp_path/'runs';out=tmp_path/'results';frozen=verify_freeze();schedule=read_json(ROOT/'execution_schedule.json')
    for e in schedule:
        folder=run_root/e['agent']/e['site']/f'run_{e["rep"]:02d}';gold=read_json(ROOT/'gold'/f'{e["site"]}.json')['records']
        write_json(folder/'output.json',{'records':copy.deepcopy(gold)})
        write_json(folder/'metadata.json',{'finished':True,'freeze_sha256':frozen,'status':'completed','latency_seconds':1,'input_tokens':100,'output_tokens':100,'tool_actions':1,'browser_actions':0})
    rows=evaluate(run_root=run_root,result_root=out)
    assert len(rows)==9 and all(r['n_runs']==12 and r['strict_field_f1_mean']==1 and r['strict_field_f1_micro']==1 for r in rows)
    e=schedule[0];folder=run_root/e['agent']/e['site']/f'run_{e["rep"]:02d}'
    write_json(folder/'output.json',{'records':[]});write_json(folder/'metadata.json',{'finished':True,'freeze_sha256':frozen,'status':'failed'})
    rows=evaluate(run_root=run_root,result_root=out)
    assert next(r for r in rows if r['agent']==e['agent'])['task_success_mean']==11/12
    (folder/'metadata.json').unlink()
    with pytest.raises(RuntimeError,match='not finished'):evaluate(run_root=run_root,result_root=out)
    evaluate(allow_partial=True,run_root=run_root,result_root=out)
    assert read_json(out/'evaluation_manifest.json')['partial'] is True
