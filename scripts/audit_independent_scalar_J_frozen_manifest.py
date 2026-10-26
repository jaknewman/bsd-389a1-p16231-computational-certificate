#!/usr/bin/env python3
"""Verify the 2026-10-26 immutable 2nd full scalar J run evidence manifest.

No external Python libraries. Reads 7 real on-machine artifacts and checks
their exact SHA256 against a versioned JSON manifest in this repository.
It does NOT recompute the complete J sum or directly invoke Sage p-adic L.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()
MANIFEST=ROOT/"results/independent_scalar_J_frozen_sha256_manifest_2026-10-26.json"

def demand(condition,message):
    if not condition:
        raise RuntimeError(message)

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as inp:
        for chunk in iter(lambda:inp.read(1048576),b""):
            h.update(chunk)
    return h.hexdigest()

def locate(spec):
    base={"repo":ROOT,"home":HOME,"tmp":Path("/tmp")}
    demand(spec["location"] in base,"unknown manifest file location")
    relative=Path(spec["path"])
    demand(not relative.is_absolute() and ".." not in relative.parts,
           "unsafe manifest relative path")
    return base[spec["location"]]/relative

def main():
    m=json.loads(MANIFEST.read_text())
    demand(m["schema"]=="bsd389.independent_scalar_J.frozen_evidence.v1",
           "manifest schema changed")
    assert m["target"]==dict(
        curve="389a1",p=16231,expected_pairs=263429130,
        J_mod_p=4486,checkpoint_count=264,
        checkpoint_last_pair=263429130)
    demand(m["full_pipeline_exit_codes"]==[0,0,0],
           "recorded pipeline failure")
    demand(m["provenance_audit_exit_codes"]==[0,0],
           "recorded provenance-check failure")
    demand(len(m["input_files"])==7,"incorrect number of pinned files")
    actual={}
    for name,spec in sorted(m["input_files"].items()):
        path=locate(spec)
        demand(path.is_file(),"missing frozen evidence file: "+str(path))
        digest=sha256(path)
        demand(digest==spec["sha256"],
               name+" HAS CHANGED: expected "+spec["sha256"]+", got "+digest)
        actual[name]=path
        print("FROZEN_J_SHA256_PASS",name,digest,flush=True)
    data=actual["completed_checkpoint"].read_text().strip().split()
    demand(data==[
        "BSD389_INDEPENDENT_SCALAR_J_V1",
        "0","263429130","263429130","4486"
    ],"frozen checkpoint fields mismatch")
    print("FROZEN_J_CHECKPOINT_PASS pairs=263429130 J_mod_p=4486",
          flush=True)
    log=actual["completed_log"].read_text(errors="replace")
    for k in ("checkpoint","terminal","full"):
        demand(m["markers"][k] in log, "missing "+k+" full-run marker")
    check=[tuple(int(z) for z in x) for x in re.findall(
        r"INDEPENDENT_SCALAR_CHECKPOINT_PASS next=(\d+) "
        r"sum_mod_p=(\d+) of=(\d+)",log)]
    expected_pairs=list(range(1000000,263000001,1000000))
    expected_pairs.append(263429130)
    demand(len(check)==264,"wrong number of logged checkpoints")
    demand([r[0] for r in check]==expected_pairs,
           "full checkpoint pair coverage is not contiguous")
    demand(all(r[2]==263429130 and 0<=r[1]<16231 for r in check),
           "invalid checkpoint modulus/domain")
    demand(check[-1]==(263429130,4486,263429130),
           "wrong final checkpoint")
    for marker in ("INDEPENDENT_SCALAR_ALL_BASIS_MOMENTS_PASS 1087544",
                  "INDEPENDENT_SCALAR_ALL_390_REP_MOMENTS_PASS "
                  "slots=6330480 expanded_relation_terms=31571240",
                  "INDEPENDENT_SCALAR_TEICH_TABLE_PASS 16230"):
        demand(marker in log,"missing basis preparation: "+marker)
    demand("INDEPENDENT_SCALAR_GLOBAL_J_MISMATCH" not in log and
           "INDEPENDENT_SCALAR_J_FAIL " not in log,
           "run log contains an algorithm failure")
    print("FROZEN_J_ALL_264_CHECKPOINTS_PASS",flush=True)
    print("FROZEN_J_263429130_PAIRS_J4486_EVIDENCE_PASS",flush=True)
    print("BOUNDARY: frozen full-run file consistency only; not an "
          "independent recomputation of J or direct p_primary_bound.",flush=True)

if __name__=="__main__":
    try:
        main()
    except Exception as exc:
        print("FROZEN_J_EVIDENCE_FAIL",type(exc).__name__,str(exc),
              file=sys.stderr,flush=True)
        raise
