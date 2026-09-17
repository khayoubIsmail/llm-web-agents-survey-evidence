from pathlib import Path
import hashlib, json, os
from datetime import datetime, timezone
from dotenv import load_dotenv
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / '.env')

def now():
    return datetime.now(timezone.utc).isoformat()

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    tmp.replace(path)

def config():
    return read_json(ROOT / 'config.json')

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def frozen_paths():
    paths = [ROOT/'config.json', ROOT/'execution_schedule.json', ROOT/'requirements.txt', ROOT/'package-lock.json', ROOT/'docs'/'PROTOCOL.md']
    for folder, glob in [('snapshots','site_*/index.html'),('gold','*.json'),('prompts','*.txt'),('schema','*.json'),('r1','*.py'),('agents','*.py'),('r1','*.js')]:
        paths.extend((ROOT/folder).glob(glob))
    paths.append(ROOT/'experiment.py')
    return sorted(set(paths))

def freeze():
    if any((ROOT/'runs').glob('**/metadata.json')):
        raise RuntimeError('Existing formal runs: archive them before changing the protocol/freeze.')
    data = {'created_at':now(), 'sha256':{str(p.relative_to(ROOT)).replace('\\','/'):digest(p) for p in frozen_paths()}}
    write_json(ROOT/'freeze_manifest.json', data)
    return data

def verify_freeze():
    ref = read_json(ROOT/'freeze_manifest.json')['sha256']
    expected = {str(p.relative_to(ROOT)).replace('\\','/') for p in frozen_paths()}
    if expected != set(ref):
        raise RuntimeError('Frozen file set differs from manifest. Review and explicitly re-freeze.')
    bad = [p for p,h in ref.items() if not (ROOT/p).exists() or digest(ROOT/p)!=h]
    if bad: raise RuntimeError('Freeze mismatch: '+', '.join(bad))
    return digest(ROOT/'freeze_manifest.json')


def error_text(exc):
    if isinstance(exc, BaseExceptionGroup):
        return '; '.join(error_text(e) for e in exc.exceptions)
    return f'{type(exc).__name__}: {exc}'
