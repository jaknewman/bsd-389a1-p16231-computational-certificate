#!/usr/bin/env python3
"""Second independently indexed Sage/eclib level-2 A2 coefficient engine.

Original V61 indexed pairs x=a+p*b and inferred exponent u using Fermat
quotients. This algorithm enumerates exponent u DIRECTLY, constructs
x=omega(a)*(1+p)^u mod p^2, and accumulates binom(u,2)*m(x/p^2)
with an entirely different iterator and separate per-a checkpoints.

No V54/V61 chunk state is read during calculation. Archived V61 block
comparisons, if present, are exclusively post-computation cross-checks.

Run with Sage-activated Python:
  python -u verification/independent_p16231_level2_u_enumeration.py pilot
  python -u verification/independent_p16231_level2_u_enumeration.py first-block
  python -u verification/independent_p16231_level2_u_enumeration.py all

Resume a partial first-block/all run simply by rerunning the same command.
Potentially expensive: all = 8,115 * 16,229 individual eclib values.
"""
from pathlib import Path
import hashlib
import json
import os
import sys
import time

from sage.all import EllipticCurve, QQ, ZZ

P=16231
P2=P*P
HALF=(P-1)//2
BINOM_SUM=P*(P-1)*(P-2)//6
HERE=Path.home()/"bsd389_independent_level2_u"
ARCHIVE=Path.home()/"bsd389-c01-v14-production/v61_a2_p2_checkpoints"
VERSION="BSD389-LEVEL2-DIRECT-U-V1"

def report(*args):
    print(*args,flush=True)

def digest(record):
    return hashlib.sha256(json.dumps(
        record,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def file_for(a):
    return HERE/f"a_{a:05d}.json"

def encode_rational_modp2(v):
    q=QQ(v)
    numerator=int(q.numerator())
    denominator=int(q.denominator())
    if denominator%P==0:
        raise ArithmeticError(
            "Unexpected p-divisible rational modular-symbol denominator")
    return numerator*pow(denominator,-1,P2)%P2

def get_existing(a):
    path=file_for(a)
    if not path.is_file():return None
    data=json.loads(path.read_text())
    chk=data.pop("sha256",None)
    assert chk==digest(data),("record digest",a)
    assert data["version"]==VERSION and data["a"]==a
    assert 0<=data["raw_f2_mod_p2"]<P2
    assert 0<=data["f1_mod_p2"]<P2
    assert data["evaluations"]==P-2
    data["sha256"]=chk
    return data

def create_new(a,modsym):
    begin=time.monotonic()
    # Frobenius Teichmueller lift, valid because a^p is the unique
    # p-1 root of unity lifting a modulo p^2.
    omega=pow(a,P,P2)
    assert omega%P==a
    assert pow(omega,P-1,P2)==1
    f1=encode_rational_modp2(modsym(QQ(a)/P))
    raw=0
    # For n=2, (1+p)^u = 1+pu modulo p^2: no Fermat
    # quotient mapping and no pair index b anywhere in this loop.
    for u in range(2,P):
        x=omega*(1+P*u)%P2
        assert x%P==a
        coeff=u*(u-1)//2
        value=encode_rational_modp2(modsym(QQ(x)/P2))
        raw=(raw+coeff*value)%P2
    rec={"version":VERSION,"a":a,"evaluations":P-2,
         "raw_f2_mod_p2":raw,"f1_mod_p2":f1,
         "input":"Sage eclib L_ratio; omega=a^p mod p^2; gamma=(1+p)"}
    chk=digest(rec)
    rec["sha256"]=chk
    path=file_for(a)
    tmp=path.with_name(path.name+".tmp."+str(os.getpid()))
    with tmp.open("w") as f:
        json.dump(rec,f,sort_keys=True)
        f.write("\n")
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp,path)
    assert get_existing(a)==rec
    report("INDEPENDENT_U_A_CHECKPOINT_PASS",a,"raw_mod_p2",raw,
           "elapsed_s",round(time.monotonic()-begin,3))
    return rec

def archive_compare_first_block(records):
    # This is an EXTERNAL oracle, not an input to any mathematical sum.
    candidate=ARCHIVE/"p2_a_00001_00032.json"
    if not candidate.is_file():
        report("INDEPENDENT_U_ARCHIVE_COMPARISON_SKIPPED",
               "original first block missing")
        return
    archived=json.loads(candidate.read_text())
    current_raw=sum(rec["raw_f2_mod_p2"] for rec in records)%P2
    current_f1=sum(rec["f1_mod_p2"] for rec in records)%P2
    assert (archived["lo"],archived["hi"])==(1,33)
    assert current_raw==archived["f2_raw_mod_p2"], (
        "independent first block mismatch",current_raw,
        archived["f2_raw_mod_p2"])
    assert current_f1==archived["f1_sum_mod_p2"], (
        "first block F1 mismatch",current_f1,
        archived["f1_sum_mod_p2"])
    report("INDEPENDENT_U_FIRST_BLOCK_V61_AGREEMENT_PASS",
           current_raw,current_f1,"pairs",32*P)

def run(mode):
    assert mode in ("pilot","first-block","all")
    HERE.mkdir(parents=True,exist_ok=True)
    E=EllipticCurve("389a1")
    lp=E.padic_lseries(ZZ(P),implementation="eclib")
    assert E.is_ordinary(P) and E.ap(P)==128
    assert E.real_components()==2
    assert lp._quotient_of_periods_to_twist(1)==1
    f=lp.modular_symbol
    alpha=int(lp.alpha(prec=6).lift())%P2
    assert alpha==179060520
    stop=2 if mode=="pilot" else (33 if mode=="first-block" else HALF+1)
    reports=[]
    acc=0
    s1=0
    t0=time.monotonic()
    for a in range(1,stop):
        rec=get_existing(a)
        if rec is None:rec=create_new(a,f)
        else:report("INDEPENDENT_U_A_CHECKPOINT_REUSED_PASS",a)
        reports.append(rec)
        acc=(acc+rec["raw_f2_mod_p2"])%P2
        s1=(s1+rec["f1_mod_p2"])%P2
        if a%32==0 or a==stop-1:
            report("INDEPENDENT_U_PROGRESS",a,"/",stop-1,
                   "raw_f2",acc,"f1",s1,
                   "elapsed_min",round((time.monotonic()-t0)/60,2))
    if mode=="pilot":
        report("INDEPENDENT_U_ONE_A_PILOT_PASS","a=1",
               "raw_f2_mod_p2",acc)
        return
    archive_compare_first_block(reports[:32])
    if mode=="first-block":
        report("INDEPENDENT_U_FIRST_32_A_COMPLETE_PASS",32*P)
        return
    assert len(reports)==HALF
    assert acc%P==0
    inv=pow(alpha,-1,P2)
    lower=inv*(BINOM_SUM%P2)*s1%P2
    A2=pow(inv,2,P2)*(acc-lower)%P2
    report("INDEPENDENT_U_FULL_A2_LEVEL2_MODP2",A2)
    report("INDEPENDENT_U_FULL_A2_LEVEL2_OVER_P",
           A2//P if A2%P==0 else "NOT_DIVISIBLE")
    if A2!=19460969:
        raise ArithmeticError(
            "independent level2 result disagrees with V61 19460969")
    assert A2//P==1199
    report("INDEPENDENT_U_FULL_LEVEL2_1199P_PASS","terms",HALF*P)
    report("BOUNDARY: independent cyclotomic u-indexing and original "
           "Sage/eclib modular symbol implementation; not a different "
           "elliptic modular-symbol oracle.")

if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("usage: python -u independent_p16231_level2_u_enumeration.py pilot|first-block|all")
    run(sys.argv[1])
