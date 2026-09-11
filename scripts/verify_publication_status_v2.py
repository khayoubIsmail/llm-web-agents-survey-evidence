#!/usr/bin/env python3
"""Hardened publication-status verification for the 805-study mapping corpus.

Safeguards: title-consistent identifier resolution, direct DataCite validation
for arXiv DOIs, multi-hit title search, continued search past preprints,
OpenAlex/Crossref/DBLP corroboration, retry/backoff, and per-row provenance.
This script never edits the register.
"""
import argparse, csv, json, os, re, sys, time
from difflib import SequenceMatcher
from urllib.parse import quote

try:
    import requests
except ImportError:
    sys.exit("pip install requests")

OPENALEX = "https://api.openalex.org/works"
CROSSREF = "https://api.crossref.org/works"
DBLP = "https://dblp.org/search/publ/api"
DATACITE = "https://api.datacite.org/dois"
DIRECT_MATCH_MIN = 0.80
SEARCH_MATCH_MIN = 0.92
STRONG_MATCH_MIN = 0.97
REGISTER_PUBLISHED = {"Archival published", "Archival accepted"}
PREPRINT_HOSTS = re.compile(
    r"arxiv|techrxiv|preprints?\.org|ssrn|researchgate|biorxiv|medrxiv|"
    r"authorea|osf|zenodo|\bcorr\b|hal science|semantic scholar|openreview",
    re.I,
)
ARCHIVAL_TYPES = {"journal", "conference", "book series", "ebook platform"}
ARCHIVAL_DOI_PREFIX = {
    "10.18653": "ACL Anthology", "10.1145": "ACM", "10.1109": "IEEE",
    "10.1007": "Springer", "10.1016": "Elsevier", "10.1613": "JAIR",
    "10.24963": "IJCAI", "10.1162": "MIT Press", "10.1093": "Oxford UP",
    "10.1214": "IMS", "10.14778": "VLDB", "10.1609": "AAAI",
    "10.52202": "NeurIPS/PMLR", "10.5555": "ACM/other", "10.3115": "ACL legacy",
}
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
STRIP_VENUE = [
    r"proceedings of (the )?", r"\b\d{1,3}(st|nd|rd|th)\b",
    r"\bannual\b|\binternational\b|\bconference\b|\bmeeting\b|\bsymposium\b|\bworkshop\b",
    r"\bvolume \d+\b|\b\(volume [^)]*\)", r"\b(19|20|26)\d{2}\b",
    r"\blong papers?\b|\bshort papers?\b|\bfindings\b|\bcompanion\b", r"[^a-z0-9 ]+",
]


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", (s or "").lower())).strip()


def similarity(a, b):
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def clean_title(t):
    return re.sub(r"([A-Za-z0-9])-\s+", r"\1: ", t or "").strip()


def norm_venue(v):
    s = (v or "").lower()
    for pattern, alias in VENUE_ALIASES:
        if re.search(pattern, s):
            return alias
    for pattern in STRIP_VENUE:
        s = re.sub(pattern, " ", s)
    return re.sub(r"\s+", " ", s).strip()


def venues_agree(a, b):
    a, b = norm_venue(a), norm_venue(b)
    return not a or not b or a == b or a in b or b in a or similarity(a, b) >= 0.60


def extract_doi(s):
    m = re.search(r"10\.\d{4,9}/[^\s,;\"']+", s or "")
    return m.group(0).rstrip(".") if m else None


def extract_arxiv(s):
    m = re.search(r"arxiv[:\s]*(\d{4}\.\d{4,5})", s or "", re.I)
    if not m:
        m = re.search(r"\b(\d{4}\.\d{4,5})\b", s or "")
    return m.group(1) if m else None


class Cache:
    def __init__(self, path):
        self.path = path; os.makedirs(path, exist_ok=True)
    def file(self, key):
        return os.path.join(self.path, re.sub(r"[^A-Za-z0-9_.-]", "_", key)[:150] + ".json")
    def get(self, key):
        try:
            return json.load(open(self.file(key), encoding="utf-8"))
        except Exception:
            return None
    def put(self, key, value):
        try:
            json.dump(value, open(self.file(key), "w", encoding="utf-8"))
        except Exception:
            pass


def api_get(url, params, cache, key, sleep):
    cached = cache.get(key)
    if cached is not None:
        return cached
    slow_api = url.startswith((CROSSREF, DBLP))
    pause = max(float(sleep), 1.05) if slow_api else float(sleep)
    email = (params or {}).get("mailto", "")
    headers = {"User-Agent": f"llm-web-agents-survey-evidence/2.2 ({email or 'publication-verifier'})"}
    for attempt in range(3):
        try:
            r = requests.get(url, params=params, headers=headers, timeout=15)
            if r.status_code == 200:
                data = r.json(); cache.put(key, data); time.sleep(pause); return data
            if r.status_code not in {429, 500, 502, 503, 504}:
                time.sleep(pause); return None
            try: wait = float(r.headers.get("Retry-After", ""))
            except Exception: wait = min(2 ** attempt, 8)
            time.sleep(max(pause, wait))
        except Exception:
            time.sleep(max(pause, min(2 ** attempt, 6)))
    return None


def matching_hits(items, title, getter, threshold=SEARCH_MATCH_MIN):
    hits = []
    for item in items or []:
        score = similarity(title, getter(item))
        if score >= threshold:
            hits.append((item, score))
    return sorted(hits, key=lambda x: x[1], reverse=True)


def oa_doi(doi, email, cache, sleep):
    d = api_get(f"{OPENALEX}/https://doi.org/{doi}", {"mailto": email}, cache, f"oa_doi_{doi}", sleep)
    return d if d and d.get("id") else None


def oa_arxiv_hits(axid, title, email, cache, sleep):
    found = []
    d = api_get(OPENALEX, {"filter": f"doi:10.48550/arxiv.{axid}", "mailto": email}, cache, f"oa_ax_{axid}", sleep)
    found += matching_hits((d or {}).get("results") or [], title, lambda x: x.get("display_name", ""), DIRECT_MATCH_MIN)
    if found: return found
    d = api_get(OPENALEX, {"search": f"arXiv {axid}", "per-page": 8, "mailto": email}, cache, f"oa_axs_{axid}", sleep)
    return matching_hits((d or {}).get("results") or [], title, lambda x: x.get("display_name", ""), DIRECT_MATCH_MIN)


def oa_title_hits(title, email, cache, sleep):
    combined = []
    d = api_get(OPENALEX, {"filter": f"title.search:{title}", "per-page": 10, "mailto": email}, cache, f"oa_ts_{title[:90]}", sleep)
    combined += (d or {}).get("results") or []
    d = api_get(OPENALEX, {"search": title, "per-page": 10, "mailto": email}, cache, f"oa_s_{title[:90]}", sleep)
    combined += (d or {}).get("results") or []
    return matching_hits(combined, title, lambda x: x.get("display_name", ""))


def cr_doi(doi, email, cache, sleep):
    if (doi or "").lower().startswith("10.48550/"): return None
    d = api_get(f"{CROSSREF}/{quote(doi, safe='')}", {"mailto": email}, cache, f"cr_doi_{doi}", sleep)
    msg = (d or {}).get("message")
    return msg if isinstance(msg, dict) else None


def cr_title_hits(title, email, cache, sleep):
    d = api_get(CROSSREF, {"query.bibliographic": title, "rows": 10, "mailto": email}, cache, f"cr2_{title[:90]}", sleep)
    items = ((d or {}).get("message") or {}).get("items") or []
    return matching_hits(items, title, lambda x: (x.get("title") or [""])[0])


def strip_html(s):
    return re.sub(r"<[^>]+>", "", s or "")


def dblp_title_hits(title, cache, sleep):
    d = api_get(DBLP, {"q": title, "format": "json", "h": 10}, cache, f"dblp2_{title[:90]}", sleep)
    hits = ((((d or {}).get("result") or {}).get("hits") or {}).get("hit") or [])
    items = [(h or {}).get("info") or {} for h in hits]
    return matching_hits(items, title, lambda x: strip_html(x.get("title", "")))


def datacite_arxiv(axid, title, cache, sleep):
    doi = f"10.48550/arXiv.{axid}"
    d = api_get(f"{DATACITE}/{doi}", {}, cache, f"dc_ax_{axid}", sleep)
    attrs = ((d or {}).get("data") or {}).get("attributes") or {}
    found = ((attrs.get("titles") or [{}])[0].get("title") or "").strip()
    if not found or similarity(title, found) < DIRECT_MATCH_MIN:
        return None
    return {
        "source": "datacite:arxiv", "score": similarity(title, found), "archival": False,
        "venue": "arXiv", "evidence": [f"DataCite arXiv DOI {doi}"], "title": found,
        "year": attrs.get("publicationYear", ""), "doi": attrs.get("doi", doi),
        "type": ((attrs.get("types") or {}).get("resourceTypeGeneral") or "Preprint"), "openalex_id": "",
    }


def oa_evidence(work):
    archival, venue, ev, seen = False, "", [], set()
    locs = ([work.get("primary_location")] if work.get("primary_location") else []) + (work.get("locations") or [])
    if work.get("best_oa_location"): locs.append(work["best_oa_location"])
    for loc in locs:
        src = (loc or {}).get("source") or {}; name = src.get("display_name") or ""; typ = (src.get("type") or "").lower()
        if (name, typ) in seen: continue
        seen.add((name, typ))
        if name and not PREPRINT_HOSTS.search(name) and typ in ARCHIVAL_TYPES:
            archival, venue = True, venue or name; ev.append(f"location[{typ}]='{name}'")
    doi = (work.get("doi") or "").replace("https://doi.org/", ""); prefix = doi.split("/")[0] if doi else ""
    if prefix in ARCHIVAL_DOI_PREFIX and prefix != "10.48550":
        archival = True; ev.append(f"DOI prefix {prefix} ({ARCHIVAL_DOI_PREFIX[prefix]})")
    bib = work.get("biblio") or {}
    if bib.get("first_page") and bib.get("last_page"):
        archival = True; ev.append(f"pages {bib['first_page']}-{bib['last_page']}")
    if (work.get("type") or "").lower() == "preprint" and not archival: ev.append("OpenAlex type=preprint")
    return archival, venue, ev


def cr_evidence(item):
    venue = (item.get("container-title") or [""])[0]; typ = (item.get("type") or "").lower()
    archival = typ in {"proceedings-article", "journal-article", "book-chapter"} and bool(venue) and not PREPRINT_HOSTS.search(venue)
    ev = [f"crossref type={typ} venue='{venue}'"] if archival else []
    if typ == "posted-content": ev.append("crossref type=posted-content (preprint)")
    return archival, venue, ev


def dblp_evidence(item):
    venue = strip_html(item.get("venue") or ""); typ = (item.get("type") or "").lower()
    archival = typ in {"conference and workshop papers", "journal articles"} and bool(venue) and norm(venue) != "corr"
    ev = [f"dblp type='{item.get('type','')}' venue='{venue}'"] if archival else []
    if venue and norm(venue) == "corr": ev.append("dblp venue=CoRR (preprint)")
    return archival, venue, ev


def candidate(kind, item, title, score=None):
    if not item: return None, None
    if kind.startswith("openalex"):
        found = item.get("display_name", ""); s = similarity(title, found) if score is None else float(score)
        if s < DIRECT_MATCH_MIN: return None, f"{kind}: title mismatch {s:.3f} -> {found}"
        archival, venue, ev = oa_evidence(item)
        return {"source": kind, "score": s, "archival": archival, "venue": venue, "evidence": ev, "title": found,
                "year": item.get("publication_year", ""), "doi": (item.get("doi") or "").replace("https://doi.org/", ""),
                "type": item.get("type", ""), "openalex_id": item.get("id", "")}, None
    if kind.startswith("crossref"):
        found = (item.get("title") or [""])[0]; s = similarity(title, found) if score is None else float(score)
        if s < DIRECT_MATCH_MIN: return None, f"{kind}: title mismatch {s:.3f} -> {found}"
        archival, venue, ev = cr_evidence(item); year = (item.get("issued", {}).get("date-parts", [[""]])[0] or [""])[0]
        return {"source": kind, "score": s, "archival": archival, "venue": venue, "evidence": ev, "title": found,
                "year": year, "doi": item.get("DOI", ""), "type": item.get("type", ""), "openalex_id": ""}, None
    found = strip_html(item.get("title") or ""); s = similarity(title, found) if score is None else float(score)
    if s < DIRECT_MATCH_MIN: return None, f"{kind}: title mismatch {s:.3f} -> {found}"
    archival, venue, ev = dblp_evidence(item); ee = item.get("ee") or ""
    if isinstance(ee, list): ee = " ".join(map(str, ee))
    return {"source": kind, "score": s, "archival": archival, "venue": venue, "evidence": ev, "title": found,
            "year": item.get("year", ""), "doi": extract_doi(str(ee)) or "", "type": item.get("type", ""), "openalex_id": ""}, None


def provider(source):
    return (source or "").split(":", 1)[0]


def strong_archival(c, all_archival):
    providers = {provider(x["source"]) for x in all_archival}
    if len(providers) >= 2: return True
    if c["source"] in {"crossref:doi"}: return True
    if c["source"] in {"crossref:title", "dblp:title"} and float(c.get("score") or 0) >= STRONG_MATCH_MIN: return True
    return False


def choose(candidates, reg_venue):
    archival = [c for c in candidates if c["archival"]]
    pool = archival or candidates
    if archival and reg_venue:
        agreeing = [c for c in archival if c.get("venue") and venues_agree(reg_venue, c["venue"])]
        if agreeing: pool = agreeing
    priority = {"crossref:doi": 7, "dblp:title": 6, "crossref:title": 5, "openalex:doi": 4,
                "openalex:title": 3, "datacite:arxiv": 2, "openalex:arxiv": 1}
    return max(pool, key=lambda c: (bool(c.get("venue")), float(c.get("score") or 0), priority.get(c["source"], 0)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--cache", default="verification_cache"); ap.add_argument("--email", required=True)
    ap.add_argument("--sleep", type=float, default=0.12); ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args(); cache = Cache(a.cache)
    rows = list(csv.DictReader(open(a.corpus, encoding="utf-8-sig"))); idk = list(rows[0])[0]; out, tally = [], {}

    for i, row in enumerate(rows, 1):
        if a.limit and i > a.limit: break
        rid, title = row[idk], clean_title(row.get("title", "")); status = row.get("status_category", "")
        venue_reg = (row.get("venue", "") or "").strip(); ident = row.get("identifier", "") or ""
        reg_pub = status in REGISTER_PUBLISHED; doi, axid = extract_doi(ident), extract_arxiv(ident)
        candidates, rejected, seen = [], [], set()

        def add(c, err=None):
            if err: rejected.append(err)
            if not c: return
            key = (norm(c.get("title")), (c.get("doi") or "").lower(), norm(c.get("venue")), c["source"])
            if key not in seen: seen.add(key); candidates.append(c)

        if axid:
            add(datacite_arxiv(axid, title, cache, a.sleep))
        if doi:
            add(*candidate("openalex:doi", oa_doi(doi, a.email, cache, a.sleep), title))
            add(*candidate("crossref:doi", cr_doi(doi, a.email, cache, a.sleep), title))
        if axid and not any(c["source"] == "openalex:doi" for c in candidates):
            for item, sc in oa_arxiv_hits(axid, title, a.email, cache, a.sleep):
                add(*candidate("openalex:arxiv", item, title, sc))

        direct_archival = [c for c in candidates if c["archival"]]
        need_search = not direct_archival or not any(c.get("venue") and (not venue_reg or venues_agree(venue_reg, c["venue"])) for c in direct_archival)
        if need_search:
            for item, sc in oa_title_hits(title, a.email, cache, a.sleep): add(*candidate("openalex:title", item, title, sc))
            for item, sc in cr_title_hits(title, a.email, cache, a.sleep): add(*candidate("crossref:title", item, title, sc))
            for item, sc in dblp_title_hits(title, cache, a.sleep): add(*candidate("dblp:title", item, title, sc))

        archival_all = [c for c in candidates if c["archival"]]
        archival_strong = [c for c in archival_all if strong_archival(c, archival_all)]
        archival_effective = list(archival_strong)
        if reg_pub:
            for c in archival_all:
                exact = float(c.get("score") or 0) >= STRONG_MATCH_MIN
                venue_confirms = bool(venue_reg and c.get("venue") and venues_agree(venue_reg, c["venue"]))
                bibliographic_confirms = any(e.startswith("pages ") or e.startswith("DOI prefix ") for e in (c.get("evidence") or []))
                # For an already-archival register row, an exact-title OpenAlex record
                # with page-range/archival-DOI evidence can confirm publication even
                # when OpenAlex omits the venue name. This does not promote preprints.
                if exact and (venue_confirms or bibliographic_confirms):
                    if c not in archival_effective: archival_effective.append(c)

        if candidates:
            selected = choose(archival_effective or candidates, venue_reg); arch = bool(archival_effective)
            found_venue, found_title = selected.get("venue", ""), selected.get("title", "")
            found_year, found_doi = selected.get("year", ""), selected.get("doi", "")
            found_type, oaid = selected.get("type", ""), selected.get("openalex_id", "")
            via, title_score = selected["source"], round(float(selected.get("score") or 0), 3)
            evidence = []
            for c in archival_effective or [selected]:
                for e in c.get("evidence") or []:
                    tagged = f"{c['source']}: {e}"
                    if tagged not in evidence: evidence.append(tagged)
        else:
            arch = False; found_venue = found_title = found_year = found_doi = found_type = oaid = ""
            via, title_score, evidence = "unresolved", "", []

        weak_archival = [c for c in archival_all if c not in archival_effective]
        if not candidates:
            verdict, note = "NO_MATCH", "no title-consistent match in DataCite, OpenAlex, Crossref, or DBLP; verify manually"
        elif reg_pub and arch:
            venues = list(dict.fromkeys(c.get("venue", "").strip() for c in archival_effective if c.get("venue", "").strip()))
            if not venue_reg:
                verdict, note = "VENUE_MISSING", f"register venue blank; archival venue '{found_venue or (venues[0] if venues else '')}'"
            elif not venues or any(venues_agree(venue_reg, v) for v in venues): verdict, note = "OK_ARCHIVAL", ""
            else: verdict, note = "VENUE_MISMATCH", f"register '{venue_reg}' vs external archival venues {venues}"
        elif reg_pub:
            verdict, note = "DOWNGRADE", "register claims archival; no strong title-consistent archival evidence found"
        elif arch:
            verdict, note = "UPGRADE", f"register '{status}'; strong archival evidence '{found_venue}'"
        else:
            verdict, note = "OK_PREPRINT", ""
            if weak_archival:
                note = "uncorroborated OpenAlex-only archival signal ignored pending manual verification: " + " | ".join(c.get("venue") or c.get("doi") or c["source"] for c in weak_archival)

        tally[verdict] = tally.get(verdict, 0) + 1
        out.append({
            "record_id": rid, "title": title, "register_status": status, "register_venue": venue_reg,
            "register_identifier": ident, "resolved_via": via, "title_match": title_score, "found_title": found_title,
            "found_venue": found_venue, "found_type": found_type, "found_year": found_year, "found_doi": found_doi,
            "openalex_id": oaid, "candidate_sources": " | ".join(c["source"] for c in candidates),
            "candidate_count": len(candidates), "archival_candidate_count": len(archival_all),
            "strong_archival_candidate_count": len(archival_effective),
            "rejected_title_mismatches": " | ".join(rejected), "archival_evidence": " | ".join(evidence),
            "VERDICT": verdict, "notes": note,
        })
        if i % 50 == 0: print(f"...{i}/{len(rows)}", file=sys.stderr)

    with open(a.out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    print(f"Wrote {a.out} ({len(out)} rows)")
    for k in sorted(tally, key=lambda x: -tally[x]): print(f"{tally[k]:5d} {k}")


if __name__ == "__main__": main()
