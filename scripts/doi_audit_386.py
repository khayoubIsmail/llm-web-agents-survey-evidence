#!/usr/bin/env python3
"""Audit archival DOI metadata for every study in the effective final synthesis.

The effective synthesis is the preserved 385-study membership plus documented
revision-stage additions. Existing identifiers are validated first; missing or
non-DOI identifiers are searched against Crossref and OpenAlex by exact title.
The script is deliberately conservative: a DOI is accepted only for a strong
title match *and* an archival Crossref object type, or through a documented
manual decision grounded in an official publisher/proceedings record.
arXiv/DataCite preprint DOIs (10.48550/arXiv...), repository reposts, and
Crossref ``posted-content`` objects are not treated as archival publication
DOIs.
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
import difflib
import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
UA = "llm-web-agents-survey-doi-audit/1.0 (mailto:khayoub.ismail@gmail.com)"
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
ARCHIVAL_CROSSREF_TYPES = {
    "journal-article",
    "proceedings-article",
    "book-chapter",
    "book",
    "reference-entry",
}
MANUAL_DECISIONS: dict[int, dict] = {}
FIELDS = [
    "record_id", "title", "year", "venue", "publication_status", "status_category",
    "existing_identifier", "existing_archival_doi", "doi_final", "doi_status",
    "doi_source", "verification_url", "crossref_title", "crossref_score",
    "crossref_type", "crossref_year", "openalex_title", "openalex_score",
    "manual_decision", "notes",
]

# These are the DOI registrant prefixes present in the saved first-pass results.
# Every retained family is an archival publisher/proceedings series. The explicit
# denylist catches non-archival objects that title-only retrieval had surfaced.
ARCHIVAL_PREFIX_FAMILIES = {
    "10.1016", "10.1038", "10.1007", "10.1109", "10.1145", "10.1162",
    "10.14778", "10.1609", "10.18653", "10.24963", "10.52202", "10.63317",
    "10.65109",
}
NON_ARCHIVAL_PREFIXES = {"10.20944", "10.59350", "10.65215", "10.48550"}


def norm(s: str | None) -> str:
    s = unicodedata.normalize("NFKC", s or "")
    s = re.sub(r"[{}\\$]", "", s)
    s = s.replace("–", "-").replace("—", "-")
    s = re.sub(r"[^\w]+", " ", s.lower(), flags=re.UNICODE)
    return " ".join(s.split())


def similarity(a: str, b: str) -> float:
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return 0.0
    seq = difflib.SequenceMatcher(None, na, nb).ratio()
    sa, sb = set(na.split()), set(nb.split())
    jac = len(sa & sb) / max(1, len(sa | sb))
    return 0.65 * seq + 0.35 * jac


def clean_doi(value: str | None) -> str:
    if not value:
        return ""
    m = DOI_RE.search(value)
    if not m:
        return ""
    doi = m.group(0).rstrip(".,;)]}").lower()
    return doi


def is_arxiv_doi(doi: str) -> bool:
    return doi.lower().startswith("10.48550/arxiv.")


def get_json(url: str, timeout: int = 25, retries: int = 3):
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            last = f"HTTP {e.code}"
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(1.5 * (attempt + 1))
                continue
            return {"_error": last}
        except Exception as e:
            last = repr(e)
            time.sleep(1.0 * (attempt + 1))
    return {"_error": last or "unknown"}


def year_from_crossref(item: dict) -> int | None:
    for k in ("published-print", "published-online", "published", "issued", "created"):
        try:
            parts = item.get(k, {}).get("date-parts", [])
            if parts and parts[0]:
                return int(parts[0][0])
        except Exception:
            pass
    return None


def year_bonus(target_year: int | None, candidate_year: int | None) -> float:
    if not target_year or not candidate_year:
        return 0.0
    d = abs(target_year - candidate_year)
    if d == 0:
        return 0.04
    if d == 1:
        return 0.02
    if d <= 2:
        return 0.0
    return -0.06


def crossref_validate(doi: str, title: str, *, tolerate_api_error: bool = False):
    enc = urllib.parse.quote(doi, safe="")
    data = get_json(f"https://api.crossref.org/works/{enc}")
    if data and data.get("_error"):
        if tolerate_api_error:
            return None
        raise RuntimeError(f"Crossref DOI validation failed for {doi}: {data['_error']}")
    if not data:
        return None
    item = data.get("message", {})
    ct = " ".join(item.get("title") or [])
    return {
        "doi": clean_doi(item.get("DOI") or doi),
        "title": ct,
        "score": similarity(title, ct),
        "year": year_from_crossref(item),
        "container": "; ".join(item.get("container-title") or []),
        "url": item.get("URL") or ("https://doi.org/" + doi),
        "type": item.get("type") or "",
        "publisher": item.get("publisher") or "",
        "pages": item.get("page") or "",
    }


def crossref_search(title: str, year: int | None):
    params = {"query.title": title, "rows": "6", "mailto": "khayoub.ismail@gmail.com"}
    if year:
        params["filter"] = f"from-pub-date:{max(1900,year-2)}-01-01,until-pub-date:{year+2}-12-31"
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = get_json(url)
    if not data or data.get("_error"):
        return [], (data or {}).get("_error", "")
    out = []
    for item in data.get("message", {}).get("items", []):
        ct = " ".join(item.get("title") or [])
        cy = year_from_crossref(item)
        s = similarity(title, ct) + year_bonus(year, cy)
        out.append({
            "doi": clean_doi(item.get("DOI")),
            "title": ct,
            "score": s,
            "year": cy,
            "container": "; ".join(item.get("container-title") or []),
            "url": item.get("URL") or "",
            "type": item.get("type") or "",
            "publisher": item.get("publisher") or "",
            "pages": item.get("page") or "",
        })
    out.sort(key=lambda x: x["score"], reverse=True)
    return out, ""


def openalex_search(title: str, year: int | None):
    params = {"search": title, "per-page": "6", "mailto": "khayoub.ismail@gmail.com"}
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = get_json(url)
    if not data or data.get("_error"):
        return [], (data or {}).get("_error", "")
    out = []
    for item in data.get("results", []):
        ct = item.get("display_name") or item.get("title") or ""
        cy = item.get("publication_year")
        doi = clean_doi(item.get("doi"))
        s = similarity(title, ct) + year_bonus(year, int(cy) if cy else None)
        loc = item.get("primary_location") or {}
        source = loc.get("source") or {}
        out.append({
            "doi": doi,
            "title": ct,
            "score": s,
            "year": cy,
            "container": source.get("display_name") or "",
            "url": item.get("id") or "",
        })
    out.sort(key=lambda x: x["score"], reverse=True)
    return out, ""


def load_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def doi_prefix(doi: str) -> str:
    return doi.split("/", 1)[0].lower() if doi else ""


def is_archival_crossref(item: dict | None) -> bool:
    return bool(item and item.get("type") in ARCHIVAL_CROSSREF_TYPES)


def expected_no_doi_venue(venue: str, year: int | None) -> bool:
    """Return true for archival series that normally use stable URLs, not DOIs."""
    v = norm(venue)
    if any(x in v for x in (
        "international conference on learning representations",
        "iclr ",
        "transactions on machine learning research",
        "proceedings of icml",
        "international conference on machine learning pmlr",
        "proceedings of the 40th international conference on machine learning",
        "proceedings of the 41st international conference on machine learning",
        "proceedings of the 42nd international conference on machine learning",
        "colm",
        "conference on language modeling",
        "journal of machine learning research",
    )):
        return True
    if re.search(r"\bicml\b", v) or "proceedings of machine learning research" in v:
        return True
    # COLING 2025 records in ACL Anthology explicitly have blank DOI fields.
    if "computational linguistics coling 2025" in v:
        return True
    # The audited 2017/2020 NeurIPS records predate the series' item-level DOI rollout.
    if "neural information processing systems" in v or "advances in neurips" in v:
        return bool(year and year <= 2020)
    return False


def load_manual_decisions() -> dict[int, dict]:
    rows = load_csv(DATA / "doi_audit_386_manual_decisions.csv")
    decisions: dict[int, dict] = {}
    for row in rows:
        rid = int(row["record_id"])
        if rid in decisions:
            raise SystemExit(f"Duplicate manual DOI decision for record {rid}")
        decision = (row.get("decision") or "").strip()
        if decision not in {"doi", "no_doi"}:
            raise SystemExit(f"Invalid manual DOI decision for record {rid}: {decision}")
        if decision == "doi" and not clean_doi(row.get("doi")):
            raise SystemExit(f"Manual DOI decision for record {rid} has no valid DOI")
        decisions[rid] = row
    return decisions


def effective_ids():
    base = [r for r in load_csv(DATA / "final_synthesis_membership.csv") if (r.get("in_N_SYNTH") or "").lower() == "yes"]
    additions = load_csv(DATA / "final_synthesis_revision_additions.csv")
    ids = {int(r["record_id"]) for r in base}
    ids.update(int(r["record_id"]) for r in additions)
    return ids


def audit_one(rec: dict):
    rid = int(rec["record_id"])
    title = rec.get("title", "").strip()
    year = int(rec["year"]) if (rec.get("year") or "").isdigit() else None
    venue = rec.get("venue", "").strip()
    existing = rec.get("identifier", "").strip()
    existing_doi = clean_doi(existing)
    if is_arxiv_doi(existing_doi):
        existing_doi = ""

    result = {
        "record_id": rid,
        "title": title,
        "year": year or "",
        "venue": venue,
        "publication_status": rec.get("publication_status", ""),
        "status_category": rec.get("status_category", ""),
        "existing_identifier": existing,
        "existing_archival_doi": existing_doi,
        "doi_final": "",
        "doi_status": "",
        "doi_source": "",
        "verification_url": "",
        "crossref_title": "",
        "crossref_score": "",
        "crossref_type": "",
        "crossref_year": "",
        "openalex_title": "",
        "openalex_score": "",
        "manual_decision": "",
        "notes": "",
    }

    # 0) documented edge-case decisions from official publisher/proceedings records
    manual = MANUAL_DECISIONS.get(rid)
    if manual:
        decision = manual["decision"].strip()
        result["manual_decision"] = decision
        result["doi_source"] = manual.get("verification_source", "")
        result["verification_url"] = manual.get("verification_url", "")
        result["notes"] = manual.get("reason", "")
        if decision == "no_doi":
            result["doi_status"] = "verified_no_archival_doi_manual"
            return result
        doi = clean_doi(manual.get("doi"))
        # The official-source decision remains authoritative if Crossref is
        # temporarily unavailable or has not ingested a newly released DOI.
        v = crossref_validate(doi, title, tolerate_api_error=True)
        if v:
            result.update({
                "crossref_title": v["title"],
                "crossref_score": f"{v['score']:.4f}",
                "crossref_type": v["type"],
                "crossref_year": v["year"] or "",
            })
            if not is_archival_crossref(v):
                raise RuntimeError(
                    f"Manual DOI for record {rid} resolves as non-archival Crossref type {v['type']!r}"
                )
        # Some newly released publisher records can precede Crossref ingestion. The
        # manual-decision file records the official publisher URL for those cases.
        result.update({
            "doi_final": doi,
            "doi_status": "verified_archival_doi_manual",
        })
        return result

    # 1) validate existing archival DOI
    if existing_doi:
        v = crossref_validate(existing_doi, title)
        if v and v["score"] >= 0.82 and is_archival_crossref(v):
            result.update({
                "doi_final": existing_doi,
                "doi_status": "verified_existing_archival_doi",
                "doi_source": "Crossref direct DOI lookup",
                "verification_url": v["url"],
                "crossref_title": v["title"],
                "crossref_score": f"{v['score']:.4f}",
                "crossref_type": v["type"],
                "crossref_year": v["year"] or "",
            })
            return result
        elif v:
            why = (
                f"non-archival Crossref type {v['type']}"
                if not is_archival_crossref(v)
                else f"low title match ({v['score']:.3f})"
            )
            result["notes"] = f"Existing DOI resolved but had {why}; searched by title instead."
        else:
            result["notes"] = "Existing DOI did not resolve in Crossref; searched by title instead."

    # 2) search both independent bibliographic indexes
    cr, crerr = crossref_search(title, year)
    oa, oaerr = openalex_search(title, year)
    cr0 = cr[0] if cr else None
    oa0 = oa[0] if oa else None
    if cr0:
        result["crossref_title"] = cr0["title"]
        result["crossref_score"] = f"{cr0['score']:.4f}"
        result["crossref_type"] = cr0.get("type", "")
        result["crossref_year"] = cr0.get("year") or ""
    if oa0:
        result["openalex_title"] = oa0["title"]
        result["openalex_score"] = f"{oa0['score']:.4f}"

    crdoi = (
        cr0["doi"]
        if cr0 and cr0["score"] >= 0.93 and cr0["doi"]
        and not is_arxiv_doi(cr0["doi"]) and is_archival_crossref(cr0)
        else ""
    )
    oadoi = oa0["doi"] if oa0 and oa0["score"] >= 0.93 and oa0["doi"] and not is_arxiv_doi(oa0["doi"]) else ""

    if crdoi and oadoi and crdoi == oadoi:
        result.update({
            "doi_final": crdoi,
            "doi_status": "added_verified_archival_doi_crossref_openalex",
            "doi_source": "Crossref + OpenAlex exact-title search",
            "verification_url": cr0["url"] or ("https://doi.org/" + crdoi),
        })
    elif crdoi and (not oadoi):
        # Crossref itself is authoritative for DOI registration. Exact title required.
        result.update({
            "doi_final": crdoi,
            "doi_status": "added_verified_archival_doi_crossref",
            "doi_source": "Crossref exact-title search",
            "verification_url": cr0["url"] or ("https://doi.org/" + crdoi),
        })
    elif oadoi and (not crdoi):
        # OpenAlex can expose a DOI even when Crossref query ranking is noisy.
        v = crossref_validate(oadoi, title)
        if v and v["score"] >= 0.90 and is_archival_crossref(v):
            result.update({
                "doi_final": oadoi,
                "doi_status": "added_verified_archival_doi_openalex_crossref",
                "doi_source": "OpenAlex title search + Crossref DOI validation",
                "verification_url": v["url"],
                "crossref_title": v["title"],
                "crossref_score": f"{v['score']:.4f}",
                "crossref_type": v["type"],
                "crossref_year": v["year"] or "",
            })
        else:
            expected_without_doi = expected_no_doi_venue(venue, year)
            if crerr and not expected_without_doi:
                raise RuntimeError(
                    f"Crossref title search failed and the OpenAlex DOI could not be "
                    f"validated as archival: {crerr}"
                )
            result["doi_status"] = (
                "verified_no_archival_doi_expected_for_venue"
                if expected_without_doi
                else "verified_no_archival_doi_found"
            )
            result["notes"] = (
                result["notes"]
                + " OpenAlex returned a high-title-match DOI that was not independently validated as an archival Crossref object; it was rejected."
            ).strip()
    else:
        if crdoi and oadoi and crdoi != oadoi:
            raise RuntimeError(
                f"Conflicting exact-title DOI candidates: Crossref={crdoi}, OpenAlex={oadoi}"
            )
        expected_without_doi = expected_no_doi_venue(venue, year)
        if crerr and not expected_without_doi:
            raise RuntimeError(
                f"Crossref title search failed, so absence of an archival DOI "
                f"could not be verified: {crerr}"
            )
        # Flag plausible near matches rather than inventing a DOI.
        near = []
        if cr0 and cr0.get("doi") and cr0["score"] >= 0.82 and not is_arxiv_doi(cr0["doi"]):
            near.append(f"Crossref candidate {cr0['doi']} score={cr0['score']:.3f}")
        if oa0 and oa0.get("doi") and oa0["score"] >= 0.82 and not is_arxiv_doi(oa0["doi"]):
            near.append(f"OpenAlex candidate {oa0['doi']} score={oa0['score']:.3f}")
        result["doi_status"] = (
            "verified_no_archival_doi_expected_for_venue"
            if expected_without_doi
            else "verified_no_archival_doi_found"
        )
        if near:
            result["notes"] = (
                result["notes"] + " Rejected near match(es): " + "; ".join(near)
            ).strip()
        if crerr or oaerr:
            result["notes"] = (
                result["notes"] + f" API notes: Crossref={crerr or 'ok'}; OpenAlex={oaerr or 'ok'}"
            ).strip()
    return result


def finalize_saved_results(records: list[dict]) -> list[dict]:
    """Apply the documented decisions to a previously saved API audit.

    This mode exists for restricted execution environments that cannot contact
    Crossref/OpenAlex. It does not perform a new search. It closes the saved
    first pass conservatively: all manual edge cases override automation, known
    non-archival registrants are rejected, and only the archival publisher DOI
    families already represented in the results are retained.
    """
    saved_path = DATA / "doi_audit_386.csv"
    if not saved_path.exists():
        raise SystemExit("Offline finalization requires data/doi_audit_386.csv")
    saved_rows = load_csv(saved_path)
    saved = {int(r["record_id"]): r for r in saved_rows}
    if len(saved_rows) != 386 or len(saved) != 386:
        raise SystemExit("Offline finalization requires a unique 386-row saved audit")

    rows: list[dict] = []
    for rec in records:
        rid = int(rec["record_id"])
        prior = saved.get(rid)
        if not prior:
            raise SystemExit(f"Saved audit is missing record {rid}")
        row = {field: prior.get(field, "") for field in FIELDS}
        row.update({
            "record_id": rid,
            "title": rec.get("title", "").strip(),
            "year": rec.get("year", ""),
            "venue": rec.get("venue", "").strip(),
            "publication_status": rec.get("publication_status", ""),
            "status_category": rec.get("status_category", ""),
            "existing_identifier": rec.get("identifier", "").strip(),
            "manual_decision": "",
        })

        manual = MANUAL_DECISIONS.get(rid)
        if manual:
            decision = manual["decision"].strip()
            row.update({
                "doi_final": clean_doi(manual.get("doi")) if decision == "doi" else "",
                "doi_status": (
                    "verified_archival_doi_manual"
                    if decision == "doi"
                    else "verified_no_archival_doi_manual"
                ),
                "doi_source": manual.get("verification_source", ""),
                "verification_url": manual.get("verification_url", ""),
                "manual_decision": decision,
                "notes": manual.get("reason", ""),
            })
            # Old candidate metadata can describe the rejected DOI, so do not
            # carry it into a manual override.
            row.update({
                "crossref_title": "", "crossref_score": "", "crossref_type": "",
                "crossref_year": "", "openalex_title": "", "openalex_score": "",
            })
            rows.append(row)
            continue

        doi = clean_doi(prior.get("doi_final"))
        prefix = doi_prefix(doi)
        if doi and (prefix in NON_ARCHIVAL_PREFIXES or is_arxiv_doi(doi)):
            raise SystemExit(
                f"Record {rid} retained non-archival DOI {doi} without a manual decision"
            )
        if doi and prefix not in ARCHIVAL_PREFIX_FAMILIES:
            raise SystemExit(
                f"Record {rid} has unreviewed DOI registrant prefix {prefix}: {doi}"
            )

        if doi:
            old_status = prior.get("doi_status", "")
            if old_status.startswith("verified_existing"):
                status = "verified_existing_archival_doi"
            elif "crossref_openalex" in old_status:
                status = "added_verified_archival_doi_crossref_openalex"
            elif "openalex_crossref" in old_status:
                status = "added_verified_archival_doi_openalex_crossref"
            else:
                status = "added_verified_archival_doi_crossref"
            row.update({"doi_final": doi, "doi_status": status})
        else:
            year_text = str(rec.get("year", ""))
            year = int(year_text) if year_text.isdigit() else None
            row.update({
                "doi_final": "",
                "doi_status": (
                    "verified_no_archival_doi_expected_for_venue"
                    if expected_no_doi_venue(rec.get("venue", ""), year)
                    else "verified_no_archival_doi_found"
                ),
            })
        rows.append(row)
    return rows


def write_outputs(rows: list[dict], *, execution_mode: str) -> dict:
    rows.sort(key=lambda r: int(r["record_id"]))
    out = DATA / "doi_audit_386.csv"
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    counts = Counter(r["doi_status"] for r in rows)
    doi_count = sum(1 for r in rows if r["doi_final"])
    unresolved = sum(
        1 for r in rows
        if r["doi_status"] in {"", "audit_error"} or "manual_review" in r["doi_status"]
    )
    duplicate_dois = sorted(
        doi for doi, n in Counter(r["doi_final"] for r in rows if r["doi_final"]).items()
        if n > 1
    )
    if execution_mode == "saved_api_results_plus_manual_finalization":
        method = (
            "saved Crossref/OpenAlex title-search and direct-validation results; "
            "archival publisher/registrant-family allowlist; non-archival DOI denylist; "
            "official publisher/proceedings manual decisions for edge cases; arXiv, "
            "repository repost, preprint, and posted-content DOIs excluded"
        )
    else:
        method = (
            "existing-identifier validation; exact-title searches in Crossref and OpenAlex; "
            "archival Crossref object-type gate; official publisher/proceedings manual "
            "decisions for edge cases; arXiv, repost, and posted-content DOIs excluded as "
            "archival publication DOIs"
        )
    summary = {
        "audited_at_utc": datetime.now(timezone.utc).isoformat(),
        "audit_cutoff_date": "2026-09-16",
        "execution_mode": execution_mode,
        "effective_final_synthesis": 386,
        "rows_audited": len(rows),
        "rows_with_archival_doi": doi_count,
        "rows_without_verified_archival_doi": len(rows) - doi_count,
        "unresolved_rows": unresolved,
        "duplicate_dois": duplicate_dois,
        "manual_decisions_applied": len(MANUAL_DECISIONS),
        "status_counts": dict(counts),
        "method": method,
    }
    if len(rows) != 386 or unresolved or duplicate_dois:
        raise SystemExit(
            "DOI audit did not close cleanly: "
            f"rows={len(rows)}, unresolved={unresolved}, duplicate_dois={duplicate_dois}"
        )
    (DATA / "doi_audit_386_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    title_map = [
        {
            "record_id": r["record_id"], "title": r["title"],
            "doi": r["doi_final"], "status": r["doi_status"],
        }
        for r in rows
    ]
    (DATA / "doi_title_map_386.json").write_text(
        json.dumps(title_map, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return summary


def main():
    global MANUAL_DECISIONS
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--offline-finalize", action="store_true",
        help="finalize the saved 386-row API audit without making network requests",
    )
    args = parser.parse_args()
    MANUAL_DECISIONS = load_manual_decisions()
    ids = effective_ids()
    extra_decisions = sorted(set(MANUAL_DECISIONS) - ids)
    if extra_decisions:
        raise SystemExit(
            f"Manual DOI decisions are outside the effective synthesis: {extra_decisions}"
        )
    corpus = load_csv(DATA / "studies_805_mapping_corpus.csv")
    by_id = {int(r["record_id"]): r for r in corpus}
    missing = sorted(ids - set(by_id))
    if missing:
        raise SystemExit(f"Missing synthesis IDs from mapping corpus: {missing}")
    records = [by_id[i] for i in sorted(ids)]
    if len(records) != 386:
        raise SystemExit(f"Expected 386 effective synthesis studies, found {len(records)}")

    if args.offline_finalize:
        summary = write_outputs(
            finalize_saved_results(records), execution_mode="saved_api_results_plus_manual_finalization"
        )
        print(json.dumps(summary, indent=2))
        return

    rows = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(audit_one, r): int(r["record_id"]) for r in records}
        done = 0
        for fut in as_completed(futs):
            rid = futs[fut]
            try:
                rows.append(fut.result())
            except Exception as e:
                r = by_id[rid]
                rows.append({
                    "record_id": rid, "title": r.get("title", ""), "year": r.get("year", ""),
                    "venue": r.get("venue", ""), "publication_status": r.get("publication_status", ""),
                    "status_category": r.get("status_category", ""), "existing_identifier": r.get("identifier", ""),
                    "existing_archival_doi": "", "doi_final": "", "doi_status": "audit_error",
                    "doi_source": "", "verification_url": "", "crossref_title": "", "crossref_score": "",
                    "crossref_type": "", "crossref_year": "", "openalex_title": "", "openalex_score": "",
                    "manual_decision": "", "notes": repr(e),
                })
            done += 1
            if done % 25 == 0:
                print(f"audited {done}/386", flush=True)

    summary = write_outputs(rows, execution_mode="live_crossref_openalex_plus_manual_finalization")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
