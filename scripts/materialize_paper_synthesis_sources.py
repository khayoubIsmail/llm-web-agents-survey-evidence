#!/usr/bin/env python3
"""Materialize one clean paper-specific synthesis-source file per normalized note.

The normalized corpus stores provenance metadata plus a detailed analysis body.
This script extracts that body into notes/original_sources/<record_id>.md while
preserving the canonical normalized note in notes/papers/<record_id>.md.
It also writes a deterministic SHA-256 manifest for the 403 source files.
"""

from __future__ import annotations

import csv
import hashlib
import re
import shutil
from pathlib import Path

PAPERS = Path("notes/papers")
OUT = Path("notes/original_sources")
MANIFEST = Path("data/paper_synthesis_source_manifest.csv")
EXPECTED = 403
MARKER = "<!-- note-body-start -->"


def audit_value(text: str, label: str) -> str:
    m = re.search(rf"^- {re.escape(label)}:\s*(.*)$", text, flags=re.MULTILINE)
    return m.group(1).strip() if m else ""


def title_from_note(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("normalized note has no level-1 title")


def shift_headings(body: str, levels: int) -> str:
    out = []
    in_fence = False
    fence = ""
    for line in body.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            token = stripped[:3]
            if not in_fence:
                in_fence, fence = True, token
            elif token == fence:
                in_fence, fence = False, ""
            out.append(line)
            continue
        if not in_fence:
            m = re.match(r"^(#{2,6})(\s+.*)$", line)
            if m:
                n = max(1, len(m.group(1)) - levels)
                line = "#" * n + m.group(2)
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


def source_text(normalized: str) -> str:
    if MARKER not in normalized:
        raise ValueError("normalized note is missing note-body-start marker")
    title = title_from_note(normalized)
    body = normalized.split(MARKER, 1)[1].lstrip("\r\n")

    # Historical paper-specific notes were nested two heading levels under
    # '# title' -> '## Analysis' during normalization. Recover that original
    # hierarchy when the body already starts with a paper-title heading.
    first_heading = next((ln for ln in body.splitlines() if ln.startswith("#")), "")
    if first_heading.startswith("### Paper "):
        rendered = shift_headings(body, 2)
    else:
        # Current-cycle remediations start directly with analytical sections.
        # Give them the same source-file shape: one H1 paper title followed by
        # H2/H3 analytical sections.
        rendered = f"# {title}\n\n" + shift_headings(body, 1)

    provenance = audit_value(normalized, "Content provenance")
    full_text = audit_value(normalized, "Full-text status")
    prefix = (
        "<!-- paper-specific-synthesis-source -->\n"
        f"<!-- provenance: {provenance} -->\n"
        f"<!-- full-text-status: {full_text} -->\n"
    )
    return prefix + rendered


def main() -> None:
    notes = sorted(PAPERS.glob("*.md"))
    if len(notes) != EXPECTED:
        raise SystemExit(f"expected {EXPECTED} normalized notes; found {len(notes)}")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    rows = []
    ids = set()
    for note in notes:
        rid = int(note.stem)
        if rid in ids:
            raise SystemExit(f"duplicate record id {rid}")
        ids.add(rid)

        normalized = note.read_text(encoding="utf-8")
        rendered = source_text(normalized)
        dest = OUT / note.name
        dest.write_text(rendered, encoding="utf-8", newline="\n")
        payload = dest.read_bytes()

        rows.append(
            {
                "record_id": rid,
                "normalized_note": note.as_posix(),
                "synthesis_source": dest.as_posix(),
                "content_provenance": audit_value(normalized, "Content provenance"),
                "full_text_status": audit_value(normalized, "Full-text status"),
                "claim_use_status": audit_value(normalized, "Claim-use status"),
                "source_bytes": len(payload),
                "source_lines": rendered.count("\n"),
                "source_sha256": hashlib.sha256(payload).hexdigest(),
            }
        )

    generated = sorted(OUT.glob("*.md"))
    if len(generated) != EXPECTED or {int(p.stem) for p in generated} != ids:
        raise SystemExit("source-layer record IDs do not exactly match normalized-note IDs")

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "record_id",
        "normalized_note",
        "synthesis_source",
        "content_provenance",
        "full_text_status",
        "claim_use_status",
        "source_bytes",
        "source_lines",
        "source_sha256",
    ]
    with MANIFEST.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"materialized {len(generated)} paper-specific synthesis sources")
    print(f"manifest: {MANIFEST}")


if __name__ == "__main__":
    main()
