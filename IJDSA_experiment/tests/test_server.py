from urllib.request import urlopen
from urllib.error import HTTPError
import pytest
from r1.server import serve

def test_only_snapshots_are_served():
    with serve(0) as base:
        for s in ['site_01','site_02','site_03','site_04']:
            with urlopen(base+'/'+s+'/') as r:
                assert r.status==200
                assert "connect-src 'none'" in r.headers['Content-Security-Policy']
        for path in ['/','/gold/site_01.json','/site_01/gold.json','/site_01/../gold.json','/%2e%2e/.env','/.env','/freeze_manifest.json','/site_01/source_manifest.json']:
            with pytest.raises(HTTPError) as e:urlopen(base+path)
            assert e.value.code==404
