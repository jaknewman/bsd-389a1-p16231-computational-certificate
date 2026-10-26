#!/usr/bin/env python3
"""Read-only verifier of every independently evaluated n=2 cyclotomic-u row.

No Sage import, no V61 values used in constructing the new independent sum.
Runs an SHA-256 audit of each of 8,115 new per-a checkpoints, recomposes
R2, R1, and A2^(2) modulo p^2, and THEN compares EVERY old V61 32-row
chunk after independently validating its record SHA. Thus a separate
8,115-row evidence audit and a 254/254 cross-implementation block check.

BOUNDARY: does NOT re-evaluate Sage/eclib modular symbols. The primary
second global computation is verification/independent_p16231_level2_u_enumeration.py.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys

P = 16231
P2 = P * P
HALF = (P - 1) // 2
BLOCK = 32
ALPHA = 179060520
VERSION = "BSD389-LEVEL2-DIRECT-U-V1"
EXPECTED_INPUT = "Sage eclib L_ratio; omega=a^p mod p^2; gamma=(1+p)"
DEFAULT_ROWS = Path.home() / "bsd389_independent_level2_u"
DEFAULT_OLD = Path.home() / "bsd389-c01-v14-production/v61_a2_p2_checkpoints"
DEFAULT_LOG = Path.home() / "bsd389_level2_u_full.log"

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as inp:
        for buf in iter(lambda: inp.read(1 << 20), b""):
            h.update(buf)
    return h.hexdigest()

def canonical(record):
    return hashlib.sha256(json.dumps(
        record,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def require(ok, message):
    if not ok:
        raise AssertionError(message)

def audit_row(a, directory):
    path = directory / ("a_%05d.json" % a)
    require(path.is_file(), "missing u checkpoint "+str(path))
    d = json.loads(path.read_text())
    digest = d.pop("sha256", None)
    require(digest == canonical(d), "failed row checksum a="+str(a))
    require(set(d) == {"version","a","evaluations","raw_f2_mod_p2",
                        "f1_mod_p2","input"}, "unexpected row keys a="+str(a))
    require(d["a"] == a and d["version"] == VERSION, "invalid row identity")
    require(d["evaluations"] == P-2, "incorrect symbol count")
    require(d["input"] == EXPECTED_INPUT, "unexpected input normalization")
    for key in ("raw_f2_mod_p2", "f1_mod_p2"):
        require(isinstance(d[key],int) and 0<=d[key]<P2,
                "invalid row modular residue")
    return d["raw_f2_mod_p2"], d["f1_mod_p2"], digest

def audit_old_chunk(lo, hi, total_r2, total_r1, old_dir):
    path=old_dir/("p2_a_%05d_%05d.json" % (lo,hi-1))
    require(path.is_file(), "missing V61 chunk "+str(path))
    d=json.loads(path.read_text())
    digest=d.pop("sha256",None)
    require(digest==canonical(d), "V61 old chunk SHA mismatch "+str(path))
    require(d.get("version")=="V61-A2-N2-P2", "wrong V61 version")
    require(d["lo"]==lo and d["hi"]==hi, "incorrect V61 range")
    require(d["pair_count"]==(hi-lo)*P, "wrong old pair count")
    require(d["alpha_mod_p2"]==ALPHA, "old alpha mismatch")
    require(d["f2_raw_mod_p2"]==total_r2, "independent u vs V61 R2 mismatch in "+str(path))
    require(d["f1_sum_mod_p2"]==total_r1, "independent u vs V61 R1 mismatch in "+str(path))
    require(d["v54_raw_mod_p"]==total_r2 % P,
            "independent u vs V54 mod-p mismatch in "+str(path))
    return digest

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--rows",type=Path,default=DEFAULT_ROWS)
    ap.add_argument("--old-v61",type=Path,default=DEFAULT_OLD)
    ap.add_argument("--log",type=Path,default=DEFAULT_LOG)
    args=ap.parse_args()
    require(args.rows.is_dir(), "missing new independent-u row folder")
    require(args.old_v61.is_dir(), "missing old V61 archive folder")
    source=Path(__file__).resolve().parents[1]/"verification/independent_p16231_level2_u_enumeration.py"
    require(source.is_file(),"missing independent-u source")
    print("INDEPENDENT_U_AUDIT_SOURCE_SHA256",sha(source),flush=True)
    count=len(list(args.rows.glob("a_?????.json")))
    require(count==HALF, "expected exactly 8115 u-index checkpoint files, got "+str(count))

    total2=total1=0
    pair_count=eval_count=chunk_count=0
    block2=block1=0
    root=hashlib.sha256()
    old_root=hashlib.sha256()
    for a in range(1,HALF+1):
        v2,v1,digest=audit_row(a,args.rows)
        root.update(("%05d %s\n" % (a,digest)).encode())
        total2=(total2+v2)%P2
        total1=(total1+v1)%P2
        block2=(block2+v2)%P2
        block1=(block1+v1)%P2
        pair_count+=P
        eval_count+=P-2
        if a%BLOCK==0 or a==HALF:
            lo=a-a%BLOCK+1 if a%BLOCK else a-BLOCK+1
            if a==HALF and a%BLOCK:
                lo=HALF-(HALF%BLOCK)+1
            digest_old=audit_old_chunk(lo,a+1,block2,block1,args.old_v61)
            old_root.update(("%05d:%05d %s\n" % (lo,a+1,digest_old)).encode())
            chunk_count+=1
            if chunk_count%50==0 or a==HALF:
                print("INDEPENDENT_U_CHECKPOINT_AUDIT_PROGRESS",
                      a,HALF,"v61_blocks",chunk_count,flush=True)
            block1=block2=0

    require(pair_count==131714565,"wrong total indexed residues")
    require(eval_count==131698335,"wrong total eclib evaluations")
    require(chunk_count==254,"wrong number of compared V61 blocks")
    require((total2,total1)==(79629286,0),
            "new full raw sums disagree with expected trusted result")
    require(ALPHA%P==128 and (ALPHA*ALPHA-128*ALPHA+P)%P2==0,
            "ordinary root invalid")
    lower=(pow(ALPHA,-1,P2)*(P*(P-1)*(P-2)//6)*total1)%P2
    A2=(pow(ALPHA,-2,P2)*(total2-lower))%P2
    require(lower==0 and A2==19460969==1199*P,
            "n2 leading coefficient mismatch")
    print("INDEPENDENT_U_ALL_8115_CHECKPOINTS_PASS",flush=True)
    print("INDEPENDENT_U_ALL_254_V61_BLOCKS_AGREE_PASS",flush=True)
    print("INDEPENDENT_U_INDEXED_RESIDUES",pair_count,flush=True)
    print("INDEPENDENT_U_ECLIB_NONZERO_TERMS",eval_count,flush=True)
    print("INDEPENDENT_U_RAW_F2_MOD_P2",total2,flush=True)
    print("INDEPENDENT_U_F1_MOD_P2",total1,flush=True)
    print("INDEPENDENT_U_A2_N2_MOD_P2",A2,flush=True)
    print("INDEPENDENT_U_A2_N2_OVER_P_MOD_P",A2//P,flush=True)
    print("INDEPENDENT_U_8115_CHECKPOINTS_COMBINED_SHA256",root.hexdigest(),flush=True)
    print("INDEPENDENT_U_254_OLD_V61_BLOCKS_COMBINED_SHA256",old_root.hexdigest(),flush=True)
    if args.log.is_file():
        log=args.log.read_text(errors="replace")
        require("INDEPENDENT_U_FULL_LEVEL2_1199P_PASS terms 131714565" in log,
                "final PASS marker missing from independent-u run log")
        require("INDEPENDENT_U_PROGRESS 8115 / 8115 raw_f2 79629286 f1 0" in log,
                "final full progress absent")
        print("INDEPENDENT_U_COMPLETE_RUN_LOG_SHA256",sha(args.log),flush=True)
    else:
        print("INDEPENDENT_U_RUN_LOG_NOT_FOUND",str(args.log),flush=True)
    print("INDEPENDENT_U_FULL_1199P_EVIDENCE_AND_V61_254_BLOCK_AGREEMENT_PASS",flush=True)
    print("BOUNDARY: recomposition and cross-algorithm checkpoints, "
          "NOT new independent Sage/eclib symbol evaluations.",flush=True)

if __name__=="__main__":
    try:
        main()
    except Exception as e:
        print("INDEPENDENT_U_EVIDENCE_AUDIT_FAIL",repr(e),file=sys.stderr,flush=True)
        raise
