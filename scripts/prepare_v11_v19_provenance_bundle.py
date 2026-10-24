#!/usr/bin/env python3
"""Read-only freezer for V11 build provenance and V19 archive audit.

Copies only the three small original sources/JSON reports, records SHA-256 of
the two historical log files, and saves short tails for examination. Neither
the chunk corpus nor the checkpoint corpus is copied or rewritten.

Run from the repository's working copy:
  python scripts/prepare_v11_v19_provenance_bundle.py
Review historical/provenance/* BEFORE staging/committing.
"""
from pathlib import Path
from collections import deque
from shutil import copyfile
import hashlib
import json
import sys

ROOT = Path.home() / "bsd389-c01-v14-production"
DEST = Path(__file__).resolve().parents[1] / "historical" / "provenance"
REPORT_SHA = "a9b853ee30d95bb48565bc99c35799dcc40c57b2bc8b9915792b81e72e3e9371"
FINAL_SHA = "5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e"
FINAL_COUNTS = {
    "pairs": 263429130,
    "expected_chunks": 514511,
    "checkpoints": 4019,
    "all_rows": 9759143225,
}
ORIGINALS = (
    "v11_provenance_report_2026-10-19.json",
    "v19_independent_chain_audit_progress.json",
    "bsd389_audit_chaine_v19.py",
)
LOGS = (
    "v19_chain_preflight.log",
    "v19_chain_full.log",
)

def sha_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()

def main():
    if sys.byteorder != "little":
        print("WARNING: non-little-endian host (hash checks unaffected)")
    assert ROOT.is_dir(), f"missing source folder: {ROOT}"
    srcs = [ROOT / name for name in (*ORIGINALS, *LOGS)]
    for f in srcs:
        assert f.is_file(), f"missing historical file: {f}"

    checksums = {f.name: sha_file(f) for f in srcs}
    assert checksums[ORIGINALS[0]] == REPORT_SHA, (
        "HISTORICAL_V11_REPORT_SHA_MISMATCH", checksums[ORIGINALS[0]]
    )

    log_path = ROOT / "v19_chain_full.log"
    tail = deque(maxlen=45)
    final_marks = []
    with log_path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            tail.append(line.rstrip("\n"))
            if "V19_FULL_CHUNK_TO_CHECKPOINT_CHAIN_PASS" in line:
                final_marks.append(line.strip())

    assert final_marks, "V19_FULL_CHAIN_PASS_MARKER_MISSING"
    final = final_marks[-1]
    assert ("final_sha256 " + FINAL_SHA) in final, "V19_FINAL_HASH_MISMATCH"
    for key, value in FINAL_COUNTS.items():
        assert (key + " " + str(value)) in final, ("V19_FINAL_COUNT_MISMATCH", key)

    # All input checks have passed. Only now create output files.
    DEST.mkdir(parents=True, exist_ok=True)
    for name in ORIGINALS:
        src = ROOT / name
        dst = DEST / name
        if dst.exists():
            assert dst.read_bytes() == src.read_bytes(), ("DESTINATION_CONFLICT", dst)
        else:
            copyfile(src, dst)
        print("V11_V19_ORIGINAL_IMPORTED_PASS", name, checksums[name], flush=True)

    full_tail = DEST / "v19_chain_full.log.tail.txt"
    excerpt = "\n".join(tail).rstrip("\n") + "\n"
    if full_tail.exists():
        assert full_tail.read_text() == excerpt, "EXCERPT_CONFLICT"
    else:
        full_tail.write_text(excerpt)

    manifest = {
        "provenance_scope": "historical source/report SHA preservation plus bounded log excerpt",
        "original_root": str(ROOT),
        "sha256": checksums,
        "original_log_byte_counts": {name:(ROOT/name).stat().st_size for name in LOGS},
        "log_excerpt_lines": len(tail),
        "v19_final_marker": final,
        "terminal_snapshot_status": "V19_FULL_CHUNK_TO_CHECKPOINT_CHAIN_PASS",
        "not_certified": [
            "independent mathematical recomputation of all C01 chunks",
            "unconditional theorem on Sha or full BSD",
        ],
    }
    mf = DEST / "v11_v19_archive_manifest.json"
    payload = json.dumps(manifest, sort_keys=True, indent=2) + "\n"
    if mf.exists():
        assert mf.read_text() == payload, "MANIFEST_CONFLICT"
    else:
        mf.write_text(payload)

    print("V19_COMPLETE_LOG_FROZEN_SHA256", checksums["v19_chain_full.log"],flush=True)
    print("V19_FULL_CHAIN_LAST_PASS", final,flush=True)
    print("V11_V19_PROVENANCE_BUNDLE_PREPARED_PASS",flush=True)
    print("REVIEW_CONTENT_BEFORE_GIT_PUSH",flush=True)
    print("BOUNDARY: no independent recalculation of 263429130 C01 pair outputs",flush=True)

if __name__ == "__main__":
    main()
