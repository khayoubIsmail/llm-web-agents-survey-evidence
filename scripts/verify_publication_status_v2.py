#!/usr/bin/env python3
"""Publication-status verification v2 for the 805-study mapping corpus.

v2 fixes four v1 defects: it inspects all OpenAlex locations (not only the
primary location), resolves DOI -> arXiv -> title, normalizes venue names, and
uses DOI/page-range corroboration. Raw API responses are cached for auditability.
This script never writes back to the corpus.
"""
import argparse, csv, json, os, re, sys, time
from difflib import SequenceMatcher

try:
    import requests
except ImportError:
    sys.exit("pip install requests")

OPENALEX = "https://api.openalex.org/works"
CROSSREF = "https://api.crossref.org/works"
PREPRINT_HOSTS = re.compile(
    r"arxiv|techrxiv|preprints?\.org|ssrn|researchgate|biorxiv|medrxiv|"
    r"authorea|osf|zenodo|\bcorr\b|hal science|semantic scholar|openreview",
    re.I,
)
ARCHIVAL_DOI_PREFIX = {
    "10.18653": "ACL Anthology", "10.1145": "ACM", "10.1109": "IEEE",
    "10.1007": "Springer", "10.1016": "Elsevier", "10.1613": "JAIR",
    "10.24963": "IJCAI", "10.1162": "MIT Press", "10.1093": "Oxford UP",
    "10.1214": "IMS", "10.14778": "VLDB", "10.1609": "AAAI",
    "10.52202": "NeurIPS/PMLR", "10.5555": "ACM/other", "10.3115": "ACL (legacy)",
}
ARCHIVAL_SOURCE_TYPES = {"journal", "conference", "book series", "ebook platform"}
VENUE_ALIASES = [
    (r"association for computational linguistics|\bacl\b", "acl"),
    (r"empirical methods in natural language processing|\bemnlp\b", "emnlp"),
    (r"north american chapter.*computational linguistics|\bnaacl\b", "naacl"),
    (r"neural information processing systems|neurips|\bnips\b", "neurips"),
    (r"international conference on machine learning|\bicml\b|proceedings of machine learning research|\bpmlr\b", "icml"),
    (r"international conference on learning representations|\biclr\b", "iclr"),
    (r"computer vision and pattern recognition|\bcvpr\b", "cvpr"),
    (r"international conference on computer vision|\biccv\b", "iccv"),
    (r"european conference on computer vision|\beccv\b", "eccv"),
    (r"aaai conference on artificial intelligence|\baaai\b", "aaai"),
    (r"international joint conference on artificial intelligence|\bijcai\b", "ijcai"),
    (r"knowledge discovery and data mining|\bkdd\b|sigkdd", "kdd"),
    (r"the web conference|world wide web conference|\bwww\b", "www"),
    (r"conference on language modeling|\bcolm\b", "colm"),
    (r"transactions on machine learning research|\btmlr\b", "tmlr"),
    (r"acm computing surveys|\bcsur\b", "acm computing surveys"),
    (r"web search and data mining|\bwsdm\b", "wsdm"),
    (r"research and development in information retrieval|\bsigir\b", "sigir"),
    (r"european chapter.*computational linguistics|\beacl\b", "eacl"),
]
STRIP_PATTERNS = [
    r"proceedings of (the )?", r"\b\d{1,3}(st|nd|rd|th)\b",
    r"\bannual\b|\binternational\b|\bconference\b|\bmeeting\b|\bsymposium\b|\bworkshop\b",
    r"\bvolume \d+\b|\b\(volume [^)]*\)", r"\b(19|20|26)\d{2}\b",
    r"\blong papers?\b|\bshort papers?\b|\bfindings\b|\bcompanion\b", r"[^a-z0-9 ]+",
]
REGISTER_PUBLISHED = {"Archival published", "Archival accepted"}

def norm_text(s):
    s = (s or "").lower(); s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def ratio(a, b): return SequenceMatcher(None, norm_text(a), norm_text(b)).ratio()

def norm_venue(v):
    s = (v or "").lower()
    for pat, alias in VENUE_ALIASES:
        if re.search(pat, s): return alias
    for pat in STRIP_PATTERNS: s = re.sub(pat, " ", s)
    return re.sub(r"\s+", " ", s).strip()

def venues_agree(a, b):
    na, nb = norm_venue(a), norm_venue(b)
    if not na or not nb: return True
    return na == nb or na in nb or nb in na or ratio(na, nb) >= 0.60

def clean_title(t): return re.sub(r"([A-Za-z0-9])-\s+", r"\1: ", t or "").strip()

def extract_doi(ident):
    m = re.search(r"10\.\d{4,9}/[^\s,;\"']+", ident or "")
    return m.group(0).rstrip(".") if m else None

def extract_arxiv(ident):
    m = re.search(r"arxiv[:\s]*(\d{4}\.\d{4,5})", ident or "", re.I)
    if m: return m.group(1)
    m = re.search(r"\b(\d{4}\.\d{4,5})\b", ident or "")
    return m.group(1) if m else None

class Cache:
    def __init__(self, path): self.path = path; os.makedirs(path, exist_ok=True)
    def _f(self, key): return os.path.join(self.path, re.sub(r"[^A-Za-z0-9_.-]", "_", key)[:150] + ".json")
    def get(self, key):
        p = self._f(key)
        if not os.path.exists(p): return None
        try: return json.load(open(p, encoding="utf-8"))
        except Exception: return None
    def put(self, key, val):
        try: json.dump(val, open(self._f(key), "w", encoding="utf-8"))
        except Exception: pass

def api_get(url, params, cache, key, sleep):
    hit = cache.get(key)
    if hit is not None: return hit
    try:
        r = requests.get(url, params=params, timeout=30); data = r.json() if r.status_code == 200 else None
    except Exception: data = None
    cache.put(key, data); time.sleep(sleep); return data

def oa_by_doi(doi, email, cache, sleep):
    d = api_get(f"{OPENALEX}/https://doi.org/{doi}", {"mailto": email}, cache, f"oa_doi_{doi}", sleep)
    return d if d and d.get("id") else None

def oa_by_arxiv(axid, email, cache, sleep):
    d = api_get(OPENALEX, {"filter": f"doi:10.48550/arxiv.{axid}", "mailto": email}, cache, f"oa_ax_{axid}", sleep)
    if d and d.get("results"): return d["results"][0]
    d = api_get(OPENALEX, {"search": f"arXiv {axid}", "per-page": 3, "mailto": email}, cache, f"oa_axs_{axid}", sleep)
    return d["results"][0] if d and d.get("results") else None

def oa_by_title(title, email, cache, sleep):
    d = api_get(OPENALEX, {"filter": f"title.search:{title}", "per-page": 5, "mailto": email}, cache, f"oa_ts_{title[:90]}", sleep)
    cands = (d or {}).get("results") or []
    if not cands:
        d = api_get(OPENALEX, {"search": title, "per-page": 5, "mailto": email}, cache, f"oa_s_{title[:90]}", sleep)
        cands = (d or {}).get("results") or []
    best, sc = None, 0.0
    for w in cands:
        r = ratio(title, w.get("display_name", ""))
        if r > sc: best, sc = w, r
    return (best, sc) if best and sc >= 0.80 else (None, sc)

def cr_by_title(title, email, cache, sleep):
    d = api_get(CROSSREF, {"query.bibliographic": title, "rows": 5, "mailto": email}, cache, f"cr_{title[:90]}", sleep)
    items = ((d or {}).get("message") or {}).get("items") or []
    best, sc = None, 0.0
    for it in items:
        r = ratio(title, (it.get("title") or [""])[0])
        if r > sc: best, sc = it, r
    return (best, sc) if best and sc >= 0.80 else (None, sc)

def archival_evidence(work):
    ev, venue, archival = [], "", False
    locs = []
    if work.get("primary_location"): locs.append(work["primary_location"])
    locs.extend(work.get("locations") or [])
    if work.get("best_oa_location"): locs.append(work["best_oa_location"])
    seen = set()
    for loc in locs:
        src = (loc or {}).get("source") or {}; name = src.get("display_name") or ""; stype = (src.get("type") or "").lower()
        key = (name, stype)
        if key in seen: continue
        seen.add(key)
        if not name or PREPRINT_HOSTS.search(name): continue
        if stype in ARCHIVAL_SOURCE_TYPES:
            archival = True; venue = venue or name; ev.append(f"location[{stype}]='{name}'")
    doi = (work.get("doi") or "").replace("https://doi.org/", "")
    if doi:
        prefix = doi.split("/")[0]
        if prefix in ARCHIVAL_DOI_PREFIX and prefix != "10.48550":
            archival = True; ev.append(f"DOI prefix {prefix} ({ARCHIVAL_DOI_PREFIX[prefix]})")
    bib = work.get("biblio") or {}
    if bib.get("first_page") and bib.get("last_page"):
        archival = True; ev.append(f"pages {bib['first_page']}-{bib['last_page']}")
    if (work.get("type") or "").lower() == "preprint" and not archival: ev.append("OpenAlex type=preprint")
    return archival, venue, ev

def cr_archival(item):
    venue = (item.get("container-title") or [""])[0]; ctype = (item.get("type") or "").lower(); ev=[]; archival=False
    if ctype in {"proceedings-article", "journal-article", "book-chapter"} and venue and not PREPRINT_HOSTS.search(venue):
        archival=True; ev.append(f"crossref type={ctype} venue='{venue}'")
    if ctype == "posted-content": ev.append("crossref type=posted-content (preprint)")
    return archival, venue, ev

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--corpus", required=True); ap.add_argument("--out", required=True); ap.add_argument("--cache", default="verification_cache"); ap.add_argument("--email", required=True); ap.add_argument("--sleep", type=float, default=0.12); ap.add_argument("--limit", type=int, default=0); a=ap.parse_args()
    cache=Cache(a.cache); rows=list(csv.DictReader(open(a.corpus, encoding="utf-8-sig"))); idk=list(rows[0].keys())[0]; out=[]; tally={}
    for i,x in enumerate(rows,1):
        if a.limit and i>a.limit: break
        rid=x[idk]; title=clean_title(x.get("title","")); reg_status=x.get("status_category",""); reg_venue=(x.get("venue","") or "").strip(); ident=x.get("identifier","") or ""; reg_pub=reg_status in REGISTER_PUBLISHED
        doi, axid = extract_doi(ident), extract_arxiv(ident); work=None; how=""; tscore=""
        if doi: work=oa_by_doi(doi,a.email,cache,a.sleep); how="openalex:doi" if work else ""
        if work is None and axid: work=oa_by_arxiv(axid,a.email,cache,a.sleep); how="openalex:arxiv" if work else how
        if work is None:
            work,sc=oa_by_title(title,a.email,cache,a.sleep)
            if work: how,tscore="openalex:title",round(sc,3)
        if work is not None:
            arch,venue,ev=archival_evidence(work); found_title=work.get("display_name",""); found_year=work.get("publication_year",""); found_doi=(work.get("doi") or "").replace("https://doi.org/",""); found_type=work.get("type",""); oaid=work.get("id","")
        else:
            item,sc=cr_by_title(title,a.email,cache,a.sleep)
            if item:
                arch,venue,ev=cr_archival(item); found_title=(item.get("title") or [""])[0]; found_year=(item.get("issued",{}).get("date-parts",[[""]])[0] or [""])[0]; found_doi=item.get("DOI",""); found_type=item.get("type",""); oaid=""; how,tscore="crossref:title",round(sc,3)
            else:
                arch,venue,ev,found_title=False,"",[],""; found_year=found_doi=found_type=oaid=""; how="unresolved"
        if how=="unresolved": v,note="NO_MATCH","not resolvable by DOI, arXiv ID, or title; verify by hand"
        elif reg_pub and arch:
            if not reg_venue: v,note="VENUE_MISSING",f"register venue blank; archival venue '{venue}'"
            elif venues_agree(reg_venue,venue): v,note="OK_ARCHIVAL",""
            else: v,note="VENUE_MISMATCH",f"register '{reg_venue}' vs external '{venue}'"
        elif reg_pub and not arch: v,note="DOWNGRADE","register claims published/accepted; no archival location, archival DOI prefix, or page range found"
        elif (not reg_pub) and arch: v,note="UPGRADE",f"register '{reg_status}'; archival evidence '{venue}'"
        else: v,note="OK_PREPRINT",""
        tally[v]=tally.get(v,0)+1
        out.append({"record_id":rid,"title":title,"register_status":reg_status,"register_venue":reg_venue,"register_identifier":ident,"resolved_via":how,"title_match":tscore,"found_title":found_title,"found_venue":venue,"found_type":found_type,"found_year":found_year,"found_doi":found_doi,"openalex_id":oaid,"archival_evidence":" | ".join(ev),"VERDICT":v,"notes":note})
        if i%50==0: print(f"...{i}/{len(rows)}",file=sys.stderr)
    with open(a.out,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    print(f"Wrote {a.out} ({len(out)} rows)")
    for k in sorted(tally,key=lambda z:-tally[z]): print(f"{tally[k]:5d} {k}")
if __name__=="__main__": main()
