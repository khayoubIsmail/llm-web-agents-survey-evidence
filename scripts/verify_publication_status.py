#!/usr/bin/env python3
"""
verify_publication_status.py
----------------------------
Cross-checks every record in the 805-study mapping corpus against OpenAlex
(and Crossref as fallback) and reports disagreements with the register.

Run locally -- needs outbound network to api.openalex.org / api.crossref.org.

    pip install requests
    python verify_publication_status.py \
        --corpus data/studies_805_mapping_corpus.csv \
        --out data/publication_status_verification.csv \
        --email you@uca.ac.ma

Output columns:
    record_id, title, register_status, register_venue, register_identifier,
    found_title, found_venue, found_type, found_year, found_doi,
    openalex_id, title_match, VERDICT, notes

VERDICT values:
    OK                  register and external source agree
    UPGRADE             register says preprint/unconfirmed, source says published
    DOWNGRADE           register says published/accepted, source says preprint only
    VENUE_MISMATCH      both published, but venue differs materially
    NO_MATCH            could not find the work -- verify by hand
    NEEDS_REVIEW        ambiguous, look at it yourself

Nothing is written back to the register. This produces evidence for a human
decision; it does not decide anything.
"""

import argparse, csv, json, re, sys, time
from difflib import SequenceMatcher

try:
    import requests
except ImportError:
    sys.exit("pip install requests")

OPENALEX = "https://api.openalex.org/works"
CROSSREF = "https://api.crossref.org/works"

PREPRINT_HOSTS = re.compile(
    r"arxiv|techrxiv|preprints?\.org|ssrn|researchgate|biorxiv|medrxiv|"
    r"authorea|osf\.io|hal\.|zenodo|corr\b",
    re.I,
)
REGISTER_PUBLISHED = {"Archival published", "Archival accepted"}


def norm(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def clean_title(t: str) -> str:
    """Register titles use '-' where ':' belongs, e.g. 'ADAM- A Systematic...'."""
    t = re.sub(r"([A-Za-z0-9])-\s+", r"\1: ", t or "")
    return t.strip()


def openalex_lookup(title: str, email: str):
    params = {"search": title, "per-page": 5, "mailto": email}
    try:
        r = requests.get(OPENALEX, params=params, timeout=30)
        if r.status_code != 200:
            return None
        results = r.json().get("results", [])
    except Exception:
        return None
    best, best_score = None, 0.0
    for w in results:
        sc = ratio(title, w.get("display_name", ""))
        if sc > best_score:
            best, best_score = w, sc
    if not best or best_score < 0.82:
        return None
    loc = best.get("primary_location") or {}
    src = loc.get("source") or {}
    return {
        "found_title": best.get("display_name", ""),
        "found_venue": src.get("display_name", "") or "",
        "found_type": best.get("type", "") or "",
        "found_year": best.get("publication_year", "") or "",
        "found_doi": (best.get("doi") or "").replace("https://doi.org/", ""),
        "openalex_id": best.get("id", ""),
        "is_preprint": bool(
            best.get("type") == "preprint"
            or PREPRINT_HOSTS.search(src.get("display_name", "") or "")
        ),
        "title_match": round(best_score, 3),
    }


def crossref_lookup(title: str, email: str):
    params = {"query.bibliographic": title, "rows": 5, "mailto": email}
    try:
        r = requests.get(CROSSREF, params=params, timeout=30)
        if r.status_code != 200:
            return None
        items = r.json()["message"]["items"]
    except Exception:
        return None
    best, best_score = None, 0.0
    for it in items:
        t = (it.get("title") or [""])[0]
        sc = ratio(title, t)
        if sc > best_score:
            best, best_score = it, sc
    if not best or best_score < 0.82:
        return None
    venue = (best.get("container-title") or [""])[0]
    return {
        "found_title": (best.get("title") or [""])[0],
        "found_venue": venue,
        "found_type": best.get("type", ""),
        "found_year": (best.get("issued", {}).get("date-parts", [[""]])[0] or [""])[0],
        "found_doi": best.get("DOI", ""),
        "openalex_id": "",
        "is_preprint": bool(
            best.get("type") == "posted-content" or PREPRINT_HOSTS.search(venue)
        ),
        "title_match": round(best_score, 3),
    }


def verdict(reg_status: str, reg_venue: str, hit) -> tuple:
    if hit is None:
        return "NO_MATCH", "not found in OpenAlex or Crossref; verify by hand"

    reg_pub = reg_status in REGISTER_PUBLISHED
    ext_pub = not hit["is_preprint"] and bool(hit["found_venue"])

    if reg_pub and not ext_pub:
        return (
            "DOWNGRADE",
            f"register says '{reg_status}' but external source shows "
            f"preprint/no venue ({hit['found_venue'] or 'none'})",
        )
    if not reg_pub and ext_pub:
        return (
            "UPGRADE",
            f"register says '{reg_status}' but external source shows "
            f"published in '{hit['found_venue']}'",
        )
    if reg_pub and ext_pub:
        if reg_venue.strip() and ratio(reg_venue, hit["found_venue"]) < 0.45:
            return (
                "VENUE_MISMATCH",
                f"register venue '{reg_venue}' vs external '{hit['found_venue']}'",
            )
        if not reg_venue.strip():
            return "NEEDS_REVIEW", f"register venue empty; external says '{hit['found_venue']}'"
        return "OK", ""
    return "OK", "both treat it as preprint"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--email", required=True, help="your email, for API politeness pools")
    ap.add_argument("--sleep", type=float, default=0.15)
    ap.add_argument("--limit", type=int, default=0, help="stop after N rows (for testing)")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.corpus, encoding="utf-8-sig")))
    idk = list(rows[0].keys())[0]
    out_rows, tally = [], {}

    for i, x in enumerate(rows, 1):
        if args.limit and i > args.limit:
            break
        title = clean_title(x.get("title", ""))
        reg_status = x.get("status_category", "")
        reg_venue = x.get("venue", "")

        hit = openalex_lookup(title, args.email)
        if hit is None:
            hit = crossref_lookup(title, args.email)

        v, note = verdict(reg_status, reg_venue, hit)
        tally[v] = tally.get(v, 0) + 1

        out_rows.append({
            "record_id": x[idk],
            "title": title,
            "register_status": reg_status,
            "register_venue": reg_venue,
            "register_identifier": x.get("identifier", ""),
            "found_title": hit["found_title"] if hit else "",
            "found_venue": hit["found_venue"] if hit else "",
            "found_type": hit["found_type"] if hit else "",
            "found_year": hit["found_year"] if hit else "",
            "found_doi": hit["found_doi"] if hit else "",
            "openalex_id": hit["openalex_id"] if hit else "",
            "title_match": hit["title_match"] if hit else "",
            "VERDICT": v,
            "notes": note,
        })

        if i % 25 == 0:
            print(f"  ...{i}/{len(rows)}", file=sys.stderr)
        time.sleep(args.sleep)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)

    print(f"\nWrote {args.out} ({len(out_rows)} rows)\n")
    for k in sorted(tally, key=lambda z: -tally[z]):
        print(f"  {tally[k]:5d}  {k}")
    print(
        "\nReview DOWNGRADE and NEEDS_REVIEW first -- those are records the register\n"
        "claims are published but external sources do not confirm.\n"
        "Then UPGRADE -- records wrongly left out of the published/accepted pool.\n"
        "NO_MATCH needs manual checking; automated absence is not evidence."
    )


if __name__ == "__main__":
    main()
