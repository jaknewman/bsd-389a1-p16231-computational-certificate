#!/usr/bin/env python3
"""E389a1 p11 SIX-prime authentic Kurihara skew matrix and Pfaffian 4.

Default: independently audit frozen 15 pair residues and full E(Fq) local
Kummer rows, all 15 Plucker relations, and 6x6 rank over F11.
--full: recompute ALL 15 genuine plus modular-symbol Kurihara sums from
the authenticated integer 390-Manin vector, using the shared 4-prime
source-normalization regression implementation. This is slower.
The skew matrix is defined with orientation by INCREASING q. The result
rules out a naive 2D exterior/local-determinant or 4D two-wedge model,
NOT arbitrary conductor-dependent Euler-system comparison formulas.
"""
import argparse
import hashlib
from itertools import combinations
from functools import lru_cache
from time import monotonic

from bsd389_p11_Kurihara_Plucker_non_decomposability_gate import (
    kurihara, local, V,
)

Q=(397,991,1321,2113,3389,3433)
EXPECTED={
 (397,991):1, (397,1321):9, (397,2113):3,
 (397,3389):4, (397,3433):7,
 (991,1321):10, (991,2113):0, (991,3389):7,
 (991,3433):9, (1321,2113):8, (1321,3389):2,
 (1321,3433):5, (2113,3389):10, (2113,3433):5,
 (3389,3433):1,
}
EXPECTED_LOCAL={
 397:(374,(1,10)), 991:(1045,(1,7)), 1321:(1320,(1,2)),
 2113:(2167,(1,7)), 3389:(3465,(1,8)), 3433:(3421,(1,9)),
}

def oriented(M,i,j):
    if i==j:return 0
    if i<j:return M[(Q[i],Q[j])]%11
    return -M[(Q[j],Q[i])]%11

def rank_mod11(A):
    B=[[int(z)%11 for z in row] for row in A]
    r=0
    for j in range(len(B[0])):
        pivot=next((i for i in range(r,len(B)) if B[i][j]),None)
        if pivot is None:continue
        B[r],B[pivot]=B[pivot],B[r]
        inv=pow(B[r][j],-1,11)
        B[r]=[v*inv%11 for v in B[r]]
        for i in range(len(B)):
            if i!=r and B[i][j]:
                c=B[i][j]
                B[i]=[(x-c*y)%11 for x,y in zip(B[i],B[r])]
        r+=1
        if r==len(B):break
    return r

def pfaffian(A):
    @lru_cache(None)
    def f(inds):
        if not inds:return 1
        x=inds[0]
        return sum(
            (-1)**(j+1)*A[x][inds[j]]*
            f(inds[1:j]+inds[j+1:])
            for j in range(1,len(inds))
        )%11
    return f(tuple(range(len(A))))

def evaluate(full):
    assert len(V)==390
    digest=hashlib.sha256(bytes(x+2 for x in V)).hexdigest()
    assert digest=="31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee"
    rows={}
    for q in Q:
        row,n=local(q)
        assert EXPECTED_LOCAL[q]==(n,row)
        rows[q]=row
    print("SIX_GENUINE_E11_LOCAL_KUMMER_ROWS_PASS",rows,flush=True)
    if full:
        p5,roots,_=kurihara(41,61,5)
        p11,roots11,_=kurihara(397,991,11)
        assert (p5,roots)==(4,(6,2))
        assert (p11,roots11)==(1,(5,6))
        print("SAGE_ECLIB_KURIHARA_P5_P11_ANCHORS_PASS",flush=True)
    D={};W={}
    for a,b in combinations(Q,2):
        value=EXPECTED[(a,b)]
        if full:
            actual,roots,weighted=kurihara(a,b,11)
            assert actual==value,(a,b,actual,value)
            print("P11_COMPLETE_GENUINE_KURIHARA_PAIR_PASS",
                  a,b,value,"roots",roots,"weighted",weighted,flush=True)
        D[(a,b)]=value
        W[(a,b)]=(rows[a][0]*rows[b][1]-rows[a][1]*rows[b][0])%11
    A=[[oriented(D,i,j) for j in range(6)] for i in range(6)]
    B=[[oriented(W,i,j) for j in range(6)] for i in range(6)]
    assert pfaffian(A)==4
    assert rank_mod11(A)==6
    assert pfaffian(B)==0 and rank_mod11(B)==2
    print("GLOBAL_KURIHARA_SIX_BY_SIX_PFAFFIAN_4_RANK_6_PASS",flush=True)
    print("RATIONAL_MW_LOCAL_WEDGE_PFAFFIAN_0_RANK_2_PASS",flush=True)
    ranks=[]
    for scalar in range(11):
        C=[[(A[i][j]-scalar*B[i][j])%11 for j in range(6)]
           for i in range(6)]
        pf=pfaffian(C)
        assert pf==(4+5*scalar)%11
        r=rank_mod11(C)
        assert r==(4 if scalar==8 else 6)
        ranks.append(r)
    print("NO_SINGLE_MW_WEDGE_PLUS_ONE_OTHER_WEDGE_FOR_ANY_SCALAR_PASS",
          "Pf(Delta-lambda*W)=4+5*lambda","ranks",ranks,flush=True)
    print("CERTIFICATE_MODE",("FULL_SIX_PAIR_AUTHENTIC_RECOMPUTATION" if full
                              else "FROZEN_RESULTS_MATRIX_AUDIT_ONLY"),flush=True)
    print("SCOPE_NO_UNIFORM_SHA_VANISHING_OR_BSD_PROOF",flush=True)

def main():
    args=argparse.ArgumentParser(description=__doc__)
    args.add_argument("--full",action="store_true")
    t=args.parse_args()
    start=monotonic()
    evaluate(t.full)
    print("SECONDS",round(monotonic()-start,2),flush=True)

if __name__=="__main__":main()
