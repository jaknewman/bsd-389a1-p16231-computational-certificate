#!/usr/bin/env python3
"""Stratified C01 V11 binary-vs-original-archive replay, read-only.

Regenerates a deterministic sample of existing [L,R) V19 chunk files
using the historically byte-identical SHA-pinned V11 executable.
Does not modify any archived chunk/checkpoint; temporary outputs live
outside the archive. This is independent producer replay on a SAMPLE,
not a rerun or proof for every one of 514511 chunks.

Usage:
  python -u scripts/audit_v19_stratified_producer.py
  python -u scripts/audit_v19_stratified_producer.py --random 12 --strata 12
"""
import argparse
import hashlib
import json
import random
import re
import subprocess
import tempfile
from pathlib import Path

P = 16231
STEP = 512
TOTAL = P*(P-1)
NCHUNKS = (TOTAL+STEP-1)//STEP
HOME = Path.home()
ROOT = HOME / "bsd389-c01-v14-production"
CHUNKS = ROOT / "chunks"
BIN = HOME / "bsd389-c01-v11-test/bsd389_c01_v11_aggregated"
EXPORT = HOME / "bsd389-portable-c01-v2/data/bsd389_tame_relation_export_p16231.json"
REPORT = ROOT / "v11_provenance_report_2026-10-19.json"
BINARY_SHA = "31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63"
EXPORT_SHA = "9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8"
FINAL_STATE_SHA = "5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e"

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def planned_samples(random_count, strata):
    assert random_count>=0 and strata>=2
    anchors={0,1,2,3,NCHUNKS//4,NCHUNKS//2,
             NCHUNKS//2+1,(3*NCHUNKS)//4,NCHUNKS-3,
             NCHUNKS-2,NCHUNKS-1}
    evenly={round((NCHUNKS-1)*i/(strata-1)) for i in range(strata)}
    rng=random.Random("BSD389-C01-V19-p16231-deterministic-v1")
    random_indices=set()
    while len(random_indices)<random_count:
        random_indices.add(rng.randrange(NCHUNKS))
    selection=sorted(anchors|evenly|random_indices)
    return selection

def check_or_raise(condition,label):
    if not condition:
        raise AssertionError(label)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--random",type=int,default=24,
                    help="deterministic additional pseudo-random archived chunks")
    ap.add_argument("--strata",type=int,default=25,
                    help="number of equal-domain spread anchors")
    ap.add_argument("--timeout",type=int,default=90,
                    help="maximum seconds per native 512-pair chunk")
    args=ap.parse_args()
    check_or_raise(args.random>=0 and args.strata>=2 and args.timeout>0,
                   "bad sample parameters")
    check_or_raise(NCHUNKS==514511,"unexpected expected chunk count")
    check_or_raise(digest(BIN)==BINARY_SHA,"V11 executable SHA mismatch")
    check_or_raise(digest(EXPORT)==EXPORT_SHA,"relation export SHA mismatch")
    report=json.loads(REPORT.read_text())
    check_or_raise(report["reproducible_binary"] is True,
                   "historical byte-identical rebuild not reported")
    check_or_raise(report["artifact_digest"]["binary"]==BINARY_SHA,
                   "provenance report binary digest")
    check_or_raise(report["artifact_digest"]["final_state"]==FINAL_STATE_SHA,
                   "provenance report checkpoint digest")
    selected=planned_samples(args.random,args.strata)
    print("V19_STRATIFIED_SAMPLE_COUNTS",
          "unique",len(selected),"total_archived_chunks",NCHUNKS,flush=True)

    count=0
    exceptional_e0=0
    exceptional_e1=0
    with tempfile.TemporaryDirectory(prefix="bsd389_v19_producer_probe_") as d:
        out=Path(d)/"replayed_chunk.tsv"
        for k in selected:
            L=k*STEP
            R=min(L+STEP,TOTAL)
            name=f"{L}_{R}.tsv"
            chunk=CHUNKS/name
            sidecar=CHUNKS/(name+".sha256")
            check_or_raise(chunk.is_file() and sidecar.is_file(),
                           f"missing archived chunk/sidecar {name}")
            side=sidecar.read_text().split()
            check_or_raise(len(side)==2 and side[1]==name,
                           f"bad sidecar metadata {name}")
            archived_sha=digest(chunk)
            check_or_raise(side[0]==archived_sha,
                           f"archived sidecar SHA mismatch {name}")
            run=subprocess.run(
                [str(BIN),str(EXPORT),str(L),str(R),str(out)],
                capture_output=True,text=True,check=True,timeout=args.timeout
            )
            rerun_sha=digest(out)
            check_or_raise(rerun_sha==archived_sha
                           and out.read_bytes()==chunk.read_bytes(),
                           f"replayed bytes differ {name}")
            match=re.search(r"V11_EXCEPTION_AUDIT E0=(\d+) E1=(\d+)",
                            run.stderr)
            check_or_raise(match is not None and "V11_AGGREGATE_PASS" in run.stderr,
                           f"missing original native PASS marker {name}")
            exceptional_e0+=int(match.group(1))
            exceptional_e1+=int(match.group(2))
            count+=1
            print("V19_NATIVE_ARCHIVE_CHUNK_BYTES_PASS",
                  count,len(selected),L,R,archived_sha,flush=True)
    print("V19_STRATIFIED_PRODUCER_REPLAY_PASS",count,
          "pairs_covered",sum(min((k+1)*STEP,TOTAL)-k*STEP for k in selected),
          "exceptional_E0",exceptional_e0,"exceptional_E1",exceptional_e1,
          flush=True)
    print("BOUNDARY: only selected chunks were re-produced; the 514511-chunk",
          "archived recomposition was already audited separately",flush=True)
    print("BOUNDARY: sample is deterministic, not a formal probabilistic confidence bound",
          flush=True)

if __name__=="__main__":
    main()
