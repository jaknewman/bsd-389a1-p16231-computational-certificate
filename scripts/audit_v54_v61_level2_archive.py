#!/usr/bin/env python3
"""Independent read-only verification of every archived V54/V61 level-2 chunk.

The script hashes and recomposes the frozen chunk-level output. It does NOT
rerun 131,714,565 Sage/eclib modular-symbol evaluations, and level 3 remains
conditional on the C01 comparison. Outputs no modified archive files.
"""
from pathlib import Path
import argparse
import hashlib
import json

P = 16231
P2 = P * P
HALF = (P - 1)//2
BATCH = 32
ROOT = Path.home() / "bsd389-c01-v14-production"
D54 = ROOT / "v54_a2_checkpoints"
D61 = ROOT / "v61_a2_p2_checkpoints"

def canonical(record):
    return hashlib.sha256(json.dumps(
        {k:v for k,v in record.items() if k != "sha256"},
        sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def verify54(lo,hi):
    path = D54 / f"a_{lo:05d}_{hi-1:05d}.json"
    d = json.loads(path.read_text())
    assert (d["lo"],d["hi"],d["count"]) == (lo,hi,(hi-lo)*P), ("V54 coordinates", path)
    value = d["sum_mod_p"]
    assert 0 <= value < P
    expected=hashlib.sha256(
        f"389a1|{P}|{lo}|{hi}|{value}|{(hi-lo)*P}|v54".encode()
    ).hexdigest()
    assert d["sha256"]==expected, ("V54 digest", path)
    return d

def verify61(lo,hi,v54):
    path = D61 / f"p2_a_{lo:05d}_{hi-1:05d}.json"
    d = json.loads(path.read_text())
    assert d["sha256"]==canonical(d), ("V61 digest",path)
    assert d["version"]=="V61-A2-N2-P2"
    assert (d["lo"],d["hi"],d["pair_count"])==(lo,hi,(hi-lo)*P)
    assert 0 <= d["evaluations"] <= d["pair_count"]
    assert 0 <= d["f2_raw_mod_p2"] < P2
    assert 0 <= d["f1_sum_mod_p2"] < P2
    assert 0 <= d["alpha_mod_p2"] < P2
    assert d["v54_raw_mod_p"]==v54["sum_mod_p"],("checkpoint V54",path)
    assert d["f2_raw_mod_p2"] % P == v54["sum_mod_p"],("residue V54",path)
    assert (d["alpha_mod_p2"]**2-128*d["alpha_mod_p2"]+P)%P2==0,("alpha root",path)
    assert d["alpha_mod_p2"]%P==128
    return d

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=ROOT)
    args=parser.parse_args()
    global D54,D61
    D54=args.root/"v54_a2_checkpoints"
    D61=args.root/"v61_a2_p2_checkpoints"

    n=0
    sum54=sum61=sumf1=evals=0
    alphas=set()
    for lo in range(1,HALF+1,BATCH):
        hi=min(lo+BATCH,HALF+1)
        x=verify54(lo,hi)
        y=verify61(lo,hi,x)
        n+=1
        sum54=(sum54+x["sum_mod_p"])%P
        sum61=(sum61+y["f2_raw_mod_p2"])%P2
        sumf1=(sumf1+y["f1_sum_mod_p2"])%P2
        evals+=y["evaluations"]
        alphas.add(y["alpha_mod_p2"])
    assert len(alphas)==1
    alpha=next(iter(alphas))
    assert n==254,("number of blocks",n)
    assert sum54==0 and sum61%P==sum54
    v54_summary=json.loads((D54/"v54_a2_result.json").read_text())
    assert (v54_summary["a_covered"],v54_summary["terms"],
            v54_summary["raw_half_sum_mod_p"],v54_summary["a2_mod_p"]) == (
               HALF, HALF*P,sum54,0)
    v61_summary=json.loads((D61/"v61_a2_p2_result.json").read_text())
    assert v61_summary["sha256"]==canonical(v61_summary)
    assert (v61_summary["a_covered"],v61_summary["pair_count"],
            v61_summary["raw_f2_mod_p2"],v61_summary["sum_f1_mod_p2"],
            v61_summary["alpha_mod_p2"]) == (HALF,HALF*P,sum61,sumf1,alpha)
    inv=pow(alpha,-1,P2)
    binom_sum=P*(P-1)*(P-2)//6
    lower=inv*(binom_sum%P2)*sumf1%P2
    a2=inv*inv*(sum61-lower)%P2
    assert a2==v61_summary["a2_n2_mod_p2"]==1199*P
    assert (sum61,sumf1,lower)==(79629286,0,0)
    assert a2%P==0
    correction=4486*pow(4*128*128,-1,P)%P
    assert correction==8335
    a3=(a2+P*correction)%P2
    assert a3==v61_summary["a2_n3_mod_p2_CONDITIONAL"]==9534*P
    assert v61_summary["c01_delta_over_p_mod_p_CONDITIONAL"]==correction
    assert v61_summary["ratio_to_v56_leading_CONDITIONAL"]==1
    print("V54_V61_ALL_CHUNK_DIGESTS_PASS",n,n,flush=True)
    print("V54_V61_ALL_CHUNK_MODP_REDUCTIONS_PASS",n,flush=True)
    print("V54_V61_TOTAL_PAIR_COUNT",HALF*P,flush=True)
    print("V61_EVALUATIONS",evals,flush=True)
    print("V61_ALPHA_MOD_P2",alpha,flush=True)
    print("V61_RAW_F2_MOD_P2",sum61,flush=True)
    print("V61_LOWER_TERM_MOD_P2",lower,flush=True)
    print("V61_A2_N2_MOD_P2",a2,flush=True)
    print("V61_A2_N2_OVER_P_MOD_P",a2//P,flush=True)
    print("V61_A2_N3_OVER_P_CONDITIONAL",a3//P,flush=True)
    print("V54_V61_ARCHIVE_RECOMPOSITION_PASS",flush=True)
    print("BOUNDARY: existing chunk calculations verified, but eclib values not independently reevaluated",flush=True)
    print("BOUNDARY: C01 bridge and full BSD not established by this audit",flush=True)

if __name__=="__main__":
    main()
