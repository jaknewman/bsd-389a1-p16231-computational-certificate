#!/usr/bin/env python3
"""An independent MW localization determinant for three certified Kurihara pairs.

E=389a1: y^2+y=x^3+x^2-2x, MW points P=(-1,1), Q=(0,-1).
For p=5,7,107 and the HISTORICAL two-prime Kurihara auxiliaries,
evaluate P,Q directly on E(F_q), then project by [#E(F_q)/p]
to the local order-p quotient. Each chosen q has p||#E(F_q).
Make the 2x2 matrix of the two images and check its determinant
is a nonzero element of Fp, INDEPENDENT of modular-symbol computations.

Checking the historical p107 Kurihara witness archive SHA256 is OPTIONAL.
A hash matches saved bytes; it does NOT prove the witness algorithm.

This is NOT a uniform theorem for all p nor does local invertibility
by itself prove Sha[p]=0. With a GENUINE nonzero degree-two delta,
appropriate residual/Manin/local conditions, and Kim's theorem on the
mod-p Selmer localization, this is a strong independent local check.
"""
import argparse
import hashlib
import json
from pathlib import Path

P=(-1,1)
Q=(0,-1)
CASES=(
  (5,(41,61),((1,3),(1,0)),2,4),
  (7,(113,673),((1,3),(1,6)),3,2),
  (107,(369793,383917),((1,15),(1,53)),38,34),
)
P107_ARCHIVE_SHA=("b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754")

def isprime(q):
    if q<2:return False
    if q%2==0:return q==2
    d=3
    while d*d<=q:
        if q%d==0:return False
        d+=2
    return True

def oncurve(P,q):
    if P is None:return True
    x,y=P
    return (y*y+y-x*x*x-x*x+2*x)%q==0

def add(A,B,q):
    if A is None:return B
    if B is None:return A
    assert oncurve(A,q) and oncurve(B,q)
    x,y=A;u,v=B
    if x==u and (y+v+1)%q==0:return None
    if A==B:
        den=(2*y+1)%q
        if den==0:return None
        slope=(3*x*x+2*x-2)*pow(den,-1,q)%q
    else:
        slope=(v-y)*pow((u-x)%q,-1,q)%q
    x3=(slope*slope-x-u-1)%q
    y3=(slope*(x-x3)-y-1)%q
    R=(x3,y3)
    assert oncurve(R,q)
    return R

def mul(n,A,q):
    assert n>=0 and oncurve(A,q)
    R=None
    while n:
        if n&1:R=add(R,A,q)
        A=add(A,A,q)
        n>>=1
    return R

def aq(q):
    count=0
    for x in range(q):
        disc=(1+4*(x*x*x+x*x-2*x))%q
        if disc:
            leg=pow(disc,(q-1)//2,q)
            assert leg in (1,q-1)
            count+=(1 if leg==1 else -1)
    return -count

def coordinate_row(p,q):
    assert isprime(q) and q!=389 and q%p==1
    trace=aq(q)
    order=q+1-trace
    assert (trace-q-1)%p==0
    assert order%p==0 and order%(p*p)!=0
    cofactor=order//p
    U=mul(cofactor,(P[0]%q,P[1]%q),q)
    V=mul(cofactor,(Q[0]%q,Q[1]%q),q)
    base=U if U is not None else V
    assert base is not None and mul(p,base,q) is None
    logs={mul(k,base,q):k for k in range(p)}
    assert len(logs)==p and logs[None]==0
    assert U in logs and V in logs
    row=(logs[U],logs[V])
    print("MW_KURIHARA_LOCAL_ROW_PASS","p",p,"q",q,
          "a_q",trace,"E_Fq_order",order,"cofactor",cofactor,
          "row",row,flush=True)
    return row,{
        "q":q,"a_q":trace,"E_Fq_order":order,"cofactor":cofactor,
        "P_scaled":list(U) if U is not None else None,
        "Q_scaled":list(V) if V is not None else None,
        "generator":list(base),"row":list(row)
    }

def main():
    pa=argparse.ArgumentParser()
    pa.add_argument("--output",type=Path,
                    default=Path.home()/"bsd389_MW_local_determinants_5_7_107.json")
    pa.add_argument("--verify-p107-archive",action="store_true")
    pa.add_argument("--p107-archive",type=Path,
                    default=Path.home()/"bsd389_k107_certificate_COMPLETE_20261028.tar.gz")
    args=pa.parse_args()
    results=[]
    for p,qs,expected_rows,expected_det,historical_delta in CASES:
        assert isprime(p)
        local_order=p+1-aq(p)
        assert local_order%p!=0,("LOCAL_P_TORSION_GATE_MISSING",p,local_order)
        print("MW_KURIHARA_LOCAL_P_TORSION_ZERO_PASS",
              "p",p,"E_Fp_order",local_order,flush=True)
        rows=[]
        infos=[]
        for q in qs:
            r,info=coordinate_row(p,q)
            rows.append(r);infos.append(info)
        det=(rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0])%p
        assert tuple(rows)==expected_rows,(p,rows,expected_rows)
        assert det==expected_det and det!=0,(p,det)
        print("MW_KURIHARA_TWO_LOCAL_IMAGES_BASIS_PASS",
              "p",p,"auxiliaries",qs,"matrix",rows,
              "det",det,"inverse",pow(det,-1,p),flush=True)
        results.append({
            "p":p,"auxiliaries":list(qs),"E_Fp_order":local_order,
            "local_groups":infos,"matrix":[list(row) for row in rows],
            "det_mod_p":det,
            "det_inverse_mod_p":pow(det,-1,p),
            "delta_HISTORICAL_NOT_RECOMPUTED_BY_THIS_PROGRAM":historical_delta
        })
    archive={"verified":False}
    if args.verify_p107_archive:
        path=args.p107_archive.expanduser()
        assert path.is_file(),("MISSING_P107_ARCHIVE",str(path))
        h=hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda:f.read(1024*1024),b""):
                h.update(chunk)
        digest=h.hexdigest()
        assert digest==P107_ARCHIVE_SHA,("FROZEN_P107_ARCHIVE_MISMATCH",digest)
        archive={"verified":True,"sha256":digest,"path":str(path)}
        print("MW_KURIHARA_P107_FROZEN_ARCHIVE_SHA_PASS",digest,flush=True)
        print("MW_KURIHARA_P107_KIM_GATE_CONDITIONAL",
              "historical_delta",34,"local_determinant",38,
              "requires_mathematically_valid_archive_and_Kim_hypotheses",
              flush=True)
    record={
        "curve":"389a1","weierstrass_model":[0,1,1,-2,0],
        "MW_points":["(-1,1)","(0,-1)"],
        "cases":results,"archive107":archive,
        "scope":("Three exact MW local Kummer images at historical "
                 "Kurihara auxiliary pairs. This alone is NOT Sha "
                 "vanishing, uniform rank-two nonvanishing, or BSD.")
    }
    encoded=json.dumps(record,sort_keys=True,
                       separators=(",",":"),ensure_ascii=True).encode()
    out=args.output.expanduser()
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_bytes(encoded+b"\n")
    print("MW_KURIHARA_LOCAL_JSON_SHA256",hashlib.sha256(encoded).hexdigest(),flush=True)
    print("MW_KURIHARA_LOCAL_REPORT",out,flush=True)
    print("BOUNDARY_LOCAL_MW_DETERMINANTS_NOT_ALL_P_SHA_OR_BSD",flush=True)

if __name__=="__main__":
    main()
