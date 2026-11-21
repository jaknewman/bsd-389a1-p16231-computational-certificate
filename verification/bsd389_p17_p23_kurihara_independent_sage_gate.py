#!/usr/bin/env python3
"""INDEPENDENT Sage/eclib origin audit for p17/p23 Kurihara units.

NOT EXECUTED AS PART OF THE COMMITTED CERTIFICATE (2026-11-21).
Run under Sage 10.9's python, from the repo root:
    python -u verification/bsd389_p17_p23_kurihara_independent_sage_gate.py --p 17
    python -u verification/bsd389_p17_p23_kurihara_independent_sage_gate.py --p 23

Unlike the pure-Python full sums, this script reconstructs all 390
Neron-normalized source modular symbols from Sage/eclib, checks their
scalar relation with the frozen archived vector, compares genuine
rational cusp values at independent samples, then does a complete
plus-symmetry-reduced sum. If the scalar is !=1, the expected numeric
delta scales by a p-unit; only nonvanishing is canonical.
"""
import argparse
import math
import runpy
import time
from pathlib import Path
from sage.all import EllipticCurve, QQ
from sage.libs.eclib.newforms import ECModularSymbol
from kurihara_manin_390_fast import table_390, symbol_by_manin, dlog

DATA={17:(1667,5237,4), 23:(1289,3727,17)}

def main():
    ar=argparse.ArgumentParser()
    ar.add_argument("--p",type=int,required=True,choices=DATA.keys())
    a=ar.parse_args()
    p=a.p
    q1,q2,frozen_delta=DATA[p]
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    assert E.conductor()==389 and E.tamagawa_product()==1
    assert p != 389 and E.ap(p)%p
    assert E.ap(q1)%p==2 and E.ap(q2)%p==2
    assert q1%p==q2%p==1
    assert (q1-1)//2%p==(q2-1)//2%p==0

    source=runpy.run_path(str(Path(__file__).with_name(
      "bsd389_p11_three_kurihara_independent_standard_python_20261121.py"
    )), run_name="INDEPENDENT_SAGE_IMPORT")
    frozen=source["V"]
    print("SAGE_SOURCE_RECONSTRUCTION_START",p,flush=True)
    phi=ECModularSymbol(E,sign=1)
    tab=table_390(phi,p)
    reconstructed=[*tab[0],tab[1]]
    assert len(reconstructed)==len(frozen)==390
    idx=next(i for i,v in enumerate(frozen) if v%p)
    scale=int(reconstructed[idx])*pow(int(frozen[idx]),-1,p)%p
    assert scale!=0
    assert all(int(u)%p==scale*int(v)%p
               for u,v in zip(reconstructed,frozen))
    print("SAGE_390_SOURCE_VECTOR_UNIT_SCALAR_PASS",
          "p",p,"scale",scale,"entries",390,flush=True)

    n=q1*q2
    for r in (1,2,3,7,23,193,1009,3079,n-1):
        if not math.gcd(r,n)==1:continue
        actual=QQ(phi(QQ(r)/n))
        den=int(actual.denominator())
        assert den%p
        direct=int(actual.numerator())*pow(den,-1,p)%p
        via=symbol_by_manin(r,n,p,tab)
        assert direct==via,(p,r,direct,via)
    print("SAGE_DIRECT_CUSPS_MATCH_MANIN_PASS",p,flush=True)

    g1,L1=dlog(q1,p);g2,L2=dlog(q2,p)
    moment=[0,0,0,0];counter=0;t=time.monotonic()
    for r in range(1,n//2+1):
        b,c=r%q1,r%q2
        if not b or not c:continue
        v=int(symbol_by_manin(r,n,p,tab))
        u,w=L1[b],L2[c]
        moment[0]=(moment[0]+v)%p
        moment[1]=(moment[1]+u*v)%p
        moment[2]=(moment[2]+w*v)%p
        moment[3]=(moment[3]+u*w*v)%p
        counter+=1
        if r%1000000==1:
            print("SAGE_KURIHARA_PROGRESS",p,r,round(time.monotonic()-t,3),flush=True)
    assert 2*counter==(q1-1)*(q2-1)
    moment=[2*v%p for v in moment]
    assert moment==[0,0,0,scale*frozen_delta%p],(p,moment,scale)
    print("SAGE_KURIHARA_INDEPENDENT_FULL_PASS",p,"q",(q1,q2),
          "roots",(g1,g2),"units",2*counter,"source_scale",scale,
          "moments",moment,flush=True)
    print("BOUNDARY: specific-prime p17/p23 certificates, not all-prime BSD.")
if __name__=="__main__":
    main()
