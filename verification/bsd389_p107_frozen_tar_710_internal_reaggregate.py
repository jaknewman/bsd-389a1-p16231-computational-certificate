#!/usr/bin/env python3
"""Read-only DIRECT tar.gz K107 archive audit: all 710 payloads + dot product.

Unlike an archive SHA-only gate, this script reads the historical frozen
tarball member by member *without extracting files or re-running 71 billion
terms*. It reconstructs a complete exact Kurihara sum from all chunk W390
vectors and a SHA-pinned actual 390-entry Manin table.

The old verification/kurihara_k107_final_audit.py works on an extracted
outdir and needs --table and --native. This new one works directly in the
tar.gz (and, when absent, can take --table, --native externally).

IMPORTANT: It checks coverage, per-block SHA, dot products and aggregation
of RECORDED data, not the entire C++ iteration or the global correctness
of normalized modular symbols. It does not prove full BSD or all-p Sha.

Usage:
 python -u verification/bsd389_p107_frozen_tar_710_internal_reaggregate.py \
   --output ~/bsd389_p107_frozen_tar_710_internal_reaggregate.json
If M390 table not inside tar.gz, append --table /exact/path/to/table.txt .
No destructive extraction and no native executable replay.
"""
import argparse
import hashlib
import json
import pathlib
import re
import tarfile

P, Q1, Q2 = 107, 369793, 383917
N = Q1 * Q2
HALF = (N - 1) // 2
CHUNKS = 710
STEP = 100_000_000
ARCHIVE_SHA = "b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754"
TABLE_SHA = "00cdb5cd7ad9c7093877836412a77fe3f67985aa2e1878ddd03b8092ab90ee2f"
NATIVE_SHA = "dfe879e69947b51b9762f6c72772ea80c56a8c7dfb8efe3a4823414cfa7e16b4"
W_SHA = "ee3fa1f5fca6de2b04300cbcc042e00e1a19a0e060adb24d2f3b90afabc0f8d0"

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()

def digest(data):
    return hashlib.sha256(data).hexdigest()

def file_hash(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(part)
    return h.hexdigest()

def pick_unique(d, label):
    assert len(d) == 1, ("AMBIGUOUS_OR_MISSING_" + label, list(d))
    return next(iter(d.values()))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", type=pathlib.Path, default=pathlib.Path.home() /
                    "bsd389_k107_certificate_COMPLETE_20261028.tar.gz")
    ap.add_argument("--table", type=pathlib.Path, default=None,
                    help="optional external ORIGINAL 393-integer M390 table")
    ap.add_argument("--native", type=pathlib.Path, default=None,
                    help="optional original C++ executable, only SHA-checked")
    ap.add_argument("--output", type=pathlib.Path, default=pathlib.Path.home() /
                    "bsd389_p107_frozen_tar_710_internal_reaggregate.json")
    args = ap.parse_args()
    archive = args.archive.expanduser()
    assert archive.is_file(), ("MISSING_FROZEN_ARCHIVE", str(archive))
    got = file_hash(archive)
    assert got == ARCHIVE_SHA, ("FROZEN_ARCHIVE_MISMATCH", got)
    print("K107_TAR_ORIGINAL_ARCHIVE_SHA256_PASS", got, flush=True)

    chunks, configs, finals = {}, {}, {}
    table_bytes = native_bytes = None
    regular_members, skipped_large = 0, []
    paths = []
    # Stream once; random access in a gzipped tar would repeatedly
    # decompress earlier members, so r|gz is intentional.
    with tarfile.open(archive, mode="r|gz") as tar:
        for member in tar:
            if not member.isfile():
                continue
            regular_members += 1
            name = member.name
            paths.append(name)
            basename = pathlib.PurePosixPath(name).name
            match = re.fullmatch(r"chunk_(\d{6})\.json", basename)
            relevant = bool(match) or basename in ("config.json", "FINAL_COMPLETE.json")
            # SHA-identify any embedded original table/binary rather than
            # guessing filenames. Never unpack executable files to disk.
            if member.size > 12_000_000:
                skipped_large.append((name, member.size))
                if relevant:
                    raise AssertionError(("OVERSIZED_REQUIRED_JSON", name, member.size))
                continue
            source = tar.extractfile(member)
            assert source is not None
            raw = source.read()
            assert len(raw) == member.size
            checksum = digest(raw)
            if checksum == TABLE_SHA:
                assert table_bytes is None, "DUPLICATE_ORIGINAL_TABLE"
                table_bytes = raw
            if checksum == NATIVE_SHA:
                assert native_bytes is None, "DUPLICATE_ORIGINAL_NATIVE"
                native_bytes = raw
            if match:
                idx = int(match.group(1))
                assert 0 <= idx < CHUNKS and idx not in chunks, (
                    "DUPLICATE_OR_INVALID_CHUNK", idx, name)
                chunks[idx] = (name, json.loads(raw))
            elif basename == "config.json":
                assert name not in configs
                configs[name] = json.loads(raw)
            elif basename == "FINAL_COMPLETE.json":
                assert name not in finals
                finals[name] = json.loads(raw)

    assert len(chunks) == CHUNKS, (
        "MISSING_ARCHIVED_CHUNKS", len(chunks), sorted(set(range(CHUNKS)) - set(chunks))[:12])
    config = pick_unique(configs, "CONFIG")
    final = pick_unique(finals, "FINAL")
    print("K107_TAR_ALL_CHUNKS_PRESENT_PASS", CHUNKS,
          "regular_members", regular_members, "large_skipped", len(skipped_large),
          flush=True)

    table_source = "embedded_archived_table"
    if table_bytes is None and args.table is not None:
        path = args.table.expanduser()
        table_bytes = path.read_bytes()
        table_source = str(path)
    if table_bytes is None:
        print("K107_TAR_M390_TABLE_REQUIRED_FOR_INDEPENDENT_DOT_CHECK",
              "--table /exact/path/to/original/table.txt", flush=True)
        print("K107_TAR_POSSIBLE_MEMBERS", paths[:20], flush=True)
        raise AssertionError("M390_BYTES_NOT_EMBEDDED_AND_NO_EXTERNAL_TABLE")
    assert digest(table_bytes) == TABLE_SHA, "M390_TABLE_SHA256_MISMATCH"
    fields = table_bytes.split()
    assert len(fields) == 393 and tuple(map(int, fields[:3])) == (P,Q1,Q2)
    M = list(map(int, fields[3:]))
    assert len(M) == 390 and all(0 <= x < P for x in M)
    print("K107_TAR_M390_ORIGINAL_TABLE_SHA256_PASS",
          TABLE_SHA, "source", table_source, flush=True)

    if native_bytes is None and args.native is not None:
        native = args.native.expanduser()
        assert file_hash(native) == NATIVE_SHA, "NATIVE_BINARY_SHA256_MISMATCH"
        native_source = str(native)
    elif native_bytes is not None:
        native_source = "embedded_archived_binary"
    else:
        native_source = "not_embedded; config_hash_only"
    assert native_bytes is None or digest(native_bytes) == NATIVE_SHA
    print("K107_TAR_NATIVE_IDENTITY_STATUS", native_source, flush=True)

    expected_config = {
        "p": P, "q1": Q1, "q2": Q2, "n": N,
        "half": HALF, "chunk_size": STEP, "chunks": CHUNKS,
        "table_sha256": TABLE_SHA, "exe_sha256": NATIVE_SHA
    }
    for k, value in expected_config.items():
        assert config.get(k) == value, ("CONFIG_MISMATCH", k, config.get(k), value)
    print("K107_TAR_CONFIG_EXACT_PARAMETER_AND_HASH_PASS", flush=True)

    W = [0] * 390
    half_sum = units = weights = edges = 0
    minstart, lastend = 1, 0
    for i in range(CHUNKS):
        name, payload = chunks[i]
        assert isinstance(payload, dict)
        copy = dict(payload)
        inner_digest = copy.pop("payload_sha256")
        assert inner_digest == digest(canonical(copy)), ("CHUNK_PAYLOAD_HASH", i)
        start = 1 + STEP * i
        end = min(start + STEP - 1, HALF)
        checks = {
            "index": i, "start": start, "end": end,
            "p": P, "q1": Q1, "q2": Q2, "n": N,
            "table_sha256": TABLE_SHA, "exe_sha256": NATIVE_SHA
        }
        for k, value in checks.items():
            assert copy.get(k) == value, ("CHUNK_HEADER", i, k)
        terms = copy.get("W390")
        assert isinstance(terms, list) and len(terms) == 390
        assert all(type(v) is int and 0 <= v < P for v in terms)
        residue = copy.get("contraction")
        assert type(residue) is int and residue == sum(a*b for a,b in zip(M,terms)) % P, (
            "BLOCK_INDEPENDENT_DOT", i, residue
        )
        n_units, n_weights, n_edges = (copy[k] for k in ("units", "weights", "edges"))
        assert all(type(t) is int and t >= 0 for t in
                   (n_units,n_weights,n_edges))
        assert n_weights <= n_units <= end - start + 1, ("COUNTS",i)
        assert start == lastend + 1, ("COVERAGE_GAP", i)
        lastend = end
        half_sum = (half_sum + residue) % P
        units += n_units
        weights += n_weights
        edges += n_edges
        W = [(x+y)%P for x,y in zip(W,terms)]
        if (i+1) % 100 == 0 or i+1 == CHUNKS:
            print("K107_TAR_PAYLOAD_REAGGREGATION_PROGRESS",i+1,"/",CHUNKS,flush=True)
    assert lastend == HALF
    assert half_sum == sum(a*b for a,b in zip(M,W))%P == 17
    assert (2*half_sum)%P == 34
    assert digest(canonical(W)) == W_SHA
    print("K107_TAR_710_INDIVIDUAL_HASHES_AND_CONTIGUOUS_COVERAGE_PASS",
          "first",minstart,"last",lastend,flush=True)
    print("K107_TAR_710_INDEPENDENT_DOT_PRODUCTS_PASS",710,flush=True)
    print("K107_TAR_GLOBAL_W390_VECTOR_SHA256_PASS",W_SHA,flush=True)
    print("K107_TAR_RECONSTRUCTED_KURIHARA_HALF17_DELTA34_PASS",
          "half",half_sum,"delta",(2*half_sum)%P,flush=True)

    expected_final = {
        "complete": True, "chunks_verified": 710,
        "half_contraction": 17, "kurihara_delta": 34,
        "W390": W, "W390_sha256": W_SHA,
        "units":units,"weights":weights,"edges":edges
    }
    for k, value in expected_final.items():
        assert final.get(k) == value, ("FINAL_RECORD", k)
    print("K107_TAR_FINAL_COMPLETE_AGREES_INDEPENDENT_REAGGREGATION_PASS",
          flush=True)

    report = {
        "curve":"389a1", "p":P, "q1":Q1, "q2":Q2,"n":N,
        "archive":str(archive),"archive_sha256":ARCHIVE_SHA,
        "table_source":table_source, "table_sha256":TABLE_SHA,
        "native_source":native_source, "native_sha256_from_config":NATIVE_SHA,
        "chunk_count":CHUNKS, "coverage":[1,HALF],
        "total_units":units,"total_weights":weights,"total_edges":edges,
        "global_W390_sha256":W_SHA,"half_contraction":17,
        "delta_mod107":34,"full_payload_audit":"PASS",
        "scope":("Reads and verifies the frozen JSON payloads and archived "
                 "aggregate; does NOT reexecute 71e9-term native loops, "
                 "independently verify the Manin algorithm or establish "
                 "Sha outside Kim theorem prerequisites.")
    }
    out = args.output.expanduser()
    out.parent.mkdir(parents=True,exist_ok=True)
    encoded = canonical(report)
    out.write_bytes(encoded+b"\n")
    print("K107_TAR_INNER_AUDIT_JSON_SHA256",digest(encoded),flush=True)
    print("K107_TAR_INNER_AUDIT_REPORT",out,flush=True)
    print("BOUNDARY_FROZEN_DATA_REAGGREGATED_NOT_FULL_NATIVE_REPLAY_OR_UNIFORM_SHA",
          flush=True)

if __name__ == "__main__":
    main()
