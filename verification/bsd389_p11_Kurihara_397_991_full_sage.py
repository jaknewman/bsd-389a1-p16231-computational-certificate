#!/usr/bin/env python3
"""Full authentic p11 two-prime Kurihara number, E389a1, q397*991=393427.

Requires Sage/eclib and the repo's existing (already p5,p7-regressed)
kurihara_manin_390_fast and kurihara_390_weight_aggregation modules.
This is an EXHAUSTIVE 196713-representative calculation, not a pilot.
If nonzero modulo11, Kim's theorem (with its hypotheses) proves Sha[11∞]=0.
"""
import argparse
import hashlib
import json
import math
import time
from pathlib import Path
from sage.all import QQ, ZZ, GF, EllipticCurve, is_prime
from sage.libs.eclib.newforms import ECModularSymbol
from kurihara_manin_390_fast import table_390, symbol_by_manin, dlog
from kurihara_390_weight_aggregation import edges

P,Q1,Q2=11,397,991
N=Q1*Q2
HALF=(N-1)//2

def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def red(v,p):
    v=QQ(v)
    den=int(v.denominator())
    assert den%p
    return int(v.numerator())*pow(den,-1,p)%p

def local(E):
    rows=[]
    data=[]
    for q,ap in ((397,24),(991,-53)):
        assert is_prime(q) and q%P==1 and ZZ(E.ap(q))==ap
        assert (q+1-ap)%P==0
        C=E.change_ring(GF(q))
        n=int(C.cardinality())
        assert n==q+1-ap and (n//P)%P
        h=n//P
        A=h*C([-1,1])
        B=h*C([0,-1])
        assert A!=C(0) and B!=C(0)
        assert P*A==C(0) and P*B==C(0)
        solutions=[i for i in range(P) if i*A==B]
        assert len(solutions)==1
        k=solutions[0]
        rows.append([1,k])
        data.append({"q":q,"ap":ap,"E_Fq_order":n,"h":h,
                     "hP":[int(A[0]),int(A[1])],
                     "hQ":[int(B[0]),int(B[1])],
                     "coordinates":[1,k]})
    assert rows==[[1,10],[1,7]]
    det=(rows[1][1]-rows[0][1])%P
    assert det==8
    assert ZZ(E.ap(P))==-4
    assert P+1-int(E.ap(P))==16
    print("P11_LOCAL_WEDGE_PASS",rows,"DET",det,flush=True)
    return data

def p5_anchor(sym):
    table=table_390(sym,5)
    a,g=dlog(41,5)
    b,h=dlog(61,5)
    total=0
    for t in range(1,1251):
        x,y=t%41,t%61
        if x and y:
            w=a[x]*b[y]%5
            if w:
                total=(total+w*symbol_by_manin(t,2501,5,table))%5
    delta=2*total%5
    assert delta==4,("P5_PUBLISHED_NORMALIZATION_MISMATCH",delta)
    print("KIM_P5_PUBLISHED_EXAMPLE_ANCHOR_PASS",delta,flush=True)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,
                        default=Path.home()/"bsd389_p11_kurihara_397_991_full.json")
    args=parser.parse_args()
    assert N==393427 and HALF==196713
    assert (Q1-1)%(2*P)==0 and (Q2-1)%(2*P)==0
    started=time.monotonic()
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    local_data=local(E)
    sym=ECModularSymbol(E,sign=1)
    p5_anchor(sym)
    table=table_390(sym,P)
    vals=[*table[0],table[1]]
    assert len(vals)==390
    sample=(1,2,3,5,7,17,41,103,409,1001,2003,5003,99991)
    for t in sample:
        assert math.gcd(t,N)==1
        direct=red(sym(QQ(t)/N),P)
        assert direct==symbol_by_manin(t,N,P,table)
        assert direct==red(sym(QQ(N-t)/N),P)
    print("P11_ECLIB_SYMBOL_13_SPOTCHECK_AND_SIGN_PLUS_PASS",flush=True)
    log1,g1=dlog(Q1,P)
    log2,g2=dlog(Q2,P)
    W=[0]*390
    direct=0
    units=weighted=edgenum=0
    print("P11_KURIHARA_FULL_START","N",N,"HALF",HALF,
          "PRIMITIVE_ROOTS",(g1,g2),flush=True)
    for a in range(1,HALF+1):
        r1,r2=a%Q1,a%Q2
        if not r1 or not r2: continue
        units+=1
        weight=int(log1[r1])*int(log2[r2])%P
        if not weight: continue
        weighted+=1
        direct=(direct+weight*symbol_by_manin(a,N,P,table))%P
        for j,sgn in edges(a,N):
            W[j]=(W[j]+sgn*weight)%P
            edgenum+=1
        if a%50000==0:
            print("P11_KURIHARA_PROGRESS",a,"/",HALF,flush=True)
    contracted=sum(x*y for x,y in zip(W,vals))%P
    assert direct==contracted,("390_VECTOR_CONTRACTION_MISMATCH",direct,contracted)
    delta=2*contracted%P
    result=dict(status="P11_KURIHARA_FULL_COMPLETE",
                curve="389a1",p=P,q1=Q1,q2=Q2,n=N,
                half_representatives=HALF,
                q_local_data=local_data,local_wedge_det_mod11=8,
                primitive_roots=[int(g1),int(g2)],
                manin390=vals,W390=W,
                manin390_sha256=digest(vals),W390_sha256=digest(W),
                count_units=units,count_nonzero_weights=weighted,
                count_edges=edgenum,
                direct_manin_half_sum=direct,weight_contract_half_sum=contracted,
                delta_mod11=delta,delta_unit=bool(delta),
                scope="A nonzero delta proves Sha(E/Q)[11^infinity]=0 under Kim's residual/Manin/Tamagawa hypotheses; a zero delta for this pair does not.")
    dest=args.output
    temp=dest.with_suffix(dest.suffix+".tmp")
    temp.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    temp.replace(dest)
    print("P11_FULL_WEIGHTED_MANIN_CONTRACTION_PASS",contracted,flush=True)
    print("P11_KURIHARA_DELTA_COMPLETE",delta,"NONZERO",bool(delta),flush=True)
    print("P11_390_TABLE_SHA256",result["manin390_sha256"],flush=True)
    print("P11_W390_SHA256",result["W390_sha256"],flush=True)
    print("P11_OUTPUT",dest,flush=True)
    print("P11_DURATION",round(time.monotonic()-started,3),flush=True)
    if delta:
        print("P11_TWO_PRIME_KIM_UNIT_GATE_PASS_SHA11_ZERO_UNDER_THEOREM_HYPOTHESES",flush=True)
    else:
        print("P11_PAIR_ZERO__NO_SHA_CONCLUSION__TRY_ANOTHER_PAIR",flush=True)

if __name__=="__main__":main()
