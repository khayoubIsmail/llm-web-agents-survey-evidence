#!/usr/bin/env python3
"""Export the verified historical note sources referenced by the paper audit.

The exported Markdown files are byte-for-byte copies of the supplied review
archive.  A record-level manifest links each source snapshot to its canonical
paper note and records a SHA-256 digest for independent verification.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from collections import Counter
from pathlib import Path, PurePosixPath


NO_SOURCE = "no reliable paper-specific source note"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def safe_source_path(root: Path, value: str) -> tuple[PurePosixPath, Path]:
    relative = PurePosixPath(value)
    if relative.is_absolute() or ".." in relative.parts:
        raise SystemExit(f"Unsafe source path: {value}")
    if relative.suffix.lower() != ".md":
        raise SystemExit(f"Source is not Markdown: {value}")
    source = (root / Path(*relative.parts)).resolve()
    try:
        source.relative_to(root)
    except ValueError as exc:
        raise SystemExit(f"Source escapes archive root: {value}") from exc
    if not source.is_file():
        raise SystemExit(f"Missing source file: {value}")
    return relative, source


def line_count(content: bytes) -> int:
    if not content:
        return 0
    return content.count(b"\n") + (0 if content.endswith(b"\n") else 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    rows = read_csv(args.audit)
    sourced_rows = [row for row in rows if row["original_note_source"] != NO_SOURCE]
    source_counts = Counter(row["original_note_source"] for row in sourced_rows)

    args.output_root.mkdir(parents=True, exist_ok=True)
    file_metadata: dict[str, dict[str, str | int]] = {}
    for source_path in sorted(source_counts):
        relative, source = safe_source_path(source_root, source_path)
        content = source.read_bytes()
        if b"\x00" in content:
            raise SystemExit(f"Refusing binary-looking source: {source_path}")
        try:
            content.decode("utf-8-sig")
        except UnicodeDecodeError as exc:
            raise SystemExit(f"Source is not valid UTF-8: {source_path}") from exc

        destination = args.output_root / Path(*relative.parts)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
        file_metadata[source_path] = {
            "repository_source": (
                PurePosixPath("notes/original_sources") / relative
            ).as_posix(),
            "source_sha256": hashlib.sha256(content).hexdigest(),
            "source_bytes": len(content),
            "source_lines": line_count(content),
        }

    manifest_rows: list[dict[str, str | int]] = []
    for row in sorted(sourced_rows, key=lambda item: int(item["record_id"])):
        source_path = row["original_note_source"]
        metadata = file_metadata[source_path]
        manifest_rows.append(
            {
                "record_id": int(row["record_id"]),
                "title": row["title"],
                "priority": row["priority"],
                "final_note": row["note_file"],
                "original_source": source_path,
                "repository_source": metadata["repository_source"],
                "source_sha256": metadata["source_sha256"],
                "source_bytes": metadata["source_bytes"],
                "source_lines": metadata["source_lines"],
                "records_mapped_to_source": source_counts[source_path],
                "source_layout": (
                    "shared/merged" if source_counts[source_path] > 1 else "standalone"
                ),
            }
        )

    args.manifest_output.parent.mkdir(parents=True, exist_ok=True)
    with args.manifest_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=manifest_rows[0].keys(), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(manifest_rows)

    print(f"audit_records={len(rows)}")
    print(f"records_with_original_source={len(sourced_rows)}")
    print(f"unique_original_source_files={len(file_metadata)}")
    print(f"shared_original_source_files={sum(count > 1 for count in source_counts.values())}")
    print(f"exported_bytes={sum(int(item['source_bytes']) for item in file_metadata.values())}")


if __name__ == "__main__":
    main()
