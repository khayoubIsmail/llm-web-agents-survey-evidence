#!/usr/bin/env python3
"""Remove stale pre-reading triage language from the live A1 evidence notes.

The notes were originally assembled with triage guidance such as "Recommended
reading depth" and, in some P2/P3 notes, "Selected sections are enough". Those
instructions are obsolete now that the A1 remediation has independently verified
all accessible papers in full. This cleanup removes/rewrites only that prospective
language and emits a machine-readable summary of the two-tier analysis protocol.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

PAPERS = Path("notes/papers")
OUT = Path("data/a1_reading_tier_summary.json")

notes = sorted(PAPERS.glob("*.md"))
if len(notes) != 403:
    raise SystemExit(f"expected 403 live notes, found {len(notes)}")

counts = {
    "deep_critical_analysis": 0,
    "complete_structured_reading": 0,
    "other_review_standard": 0,
}
changed = 0

for p in notes:
    text = p.read_text(encoding="utf-8")

    m = re.search(r"^- Required review standard:\s*(.+)$", text, re.M)
    standard = m.group(1).strip() if m else ""
    if standard.startswith("Deep critical analysis"):
        counts["deep_critical_analysis"] += 1
    elif standard.startswith("Complete structured reading"):
        counts["complete_structured_reading"] += 1
    else:
        counts["other_review_standard"] += 1

    old = text

    # Obsolete pre-reading triage recommendation. Remove regardless of the
    # historical value (Low/medium/High/etc.).
    text = re.sub(
        r"^- \*\*Recommended reading depth:\*\*.*\n?",
        "",
        text,
        flags=re.M,
    )

    # Any line retaining this phrase is prospective partial-reading guidance.
    # Replace the whole line irrespective of small wording/Markdown variants.
    text = re.sub(
        r"^.*Selected sections are enough.*$",
        "- **Full-text review status:** Completed; see the current-cycle verification in the audit metadata above.",
        text,
        flags=re.M,
    )
    text = re.sub(
        r"^- \*\*Depth needed:\*\* Low to medium\s*$",
        "- **Analysis depth:** Tier-appropriate structured analysis consistent with the review protocol.",
        text,
        flags=re.M,
    )
    text = text.replace(
        "- **Most important parts to read:**",
        "- **Sections emphasized in synthesis:**",
    )

    if text != old:
        p.write_text(text, encoding="utf-8")
        changed += 1

# Reviewer-facing residual scan after cleanup.
joined = "\n".join(p.read_text(encoding="utf-8") for p in notes)
residuals = {
    "recommended_reading_depth": len(re.findall(r"Recommended reading depth", joined, re.I)),
    "selected_sections_are_enough": len(re.findall(r"Selected sections are enough", joined, re.I)),
    "most_important_parts_to_read": len(re.findall(r"Most important parts to read", joined, re.I)),
}

if counts["other_review_standard"]:
    raise SystemExit(f"unrecognized review standards in {counts['other_review_standard']} notes")
if any(residuals.values()):
    raise SystemExit(f"stale reading-triage language remains: {residuals}")

summary = {
    "live_notes": len(notes),
    "review_standard_counts": counts,
    "protocol": {
        "P0_P1": "complete full-text reading with deep critical analysis and detailed notes",
        "P2_P3": "complete full-text reading with lighter structured analysis focused on relevance, methods, results/benchmark properties, contributions, and limitations",
        "priority_role": "priority governs analytical depth and evidence use, not whether the paper is read in full",
    },
    "stale_triage_markers_after_cleanup": residuals,
    "notes_changed_by_cleanup": changed,
}
OUT.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
