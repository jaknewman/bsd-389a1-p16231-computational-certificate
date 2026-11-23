#!/usr/bin/env python3
"""Actual mixed Mazur-Tate moments at p5 and p11, showing raw jet mismatch.

Full finite sums from the independently archived 390 Manin edge vector,
not synthetic weights. The direct EULER jet shift is valid for a NORMED
Euler-product expression; it cannot be applied to the unmodified
Mazur-Tate theta of conductor q1*q2.

Requires only standard-library Python and the neighboring authentic
Kurihara/Manin verification code.
"""
import hashlib
import json
from math import comb, gcd
from time import monotonic

from bsd389_p11_Kurihara_Plucker_non_decomposability_gate import (
    kurihara, logs, modular_symbol,
)

EXPECTED = {
    (5, 41, 61): [
        [0,0,0,0,0],
        [0,4,4,2,0],
        [0,0,4,2,1],
        [0,4,2,3,2],
        [0,1,3,2,4],
    ],
    (11,397,991): [
        [0,0,0,0,8],
        [0,1,1,3,10],
        [0,9,2,7,0],
        [0,4,5,2,9],
        [6,2,8,0,1],
    ],
}

def moments(p, q1, q2, maxdegree=4):
    n=q1*q2
    assert (q1-1)%(2*p)==0 and (q2-1)%(2*p)==0
    g1,L1=logs(q1,p)
    g2,L2=logs(q2,p)
    assert (g1,g2)==((6,2) if p==5 else (5,6))
    out=[[0]*(maxdegree+1) for _ in range(maxdegree+1)]
    powers=[[comb(j,d) if j>=d else 0 for d in range(maxdegree+1)]
            for j in range(p)]
    nweighted=0
    for a in range(1,(n-1)//2+1):
        r1,r2=a%q1,a%q2
        if not r1 or not r2:continue
        u=int(L1[r1]);v=int(L2[r2])
        val=(2*modular_symbol(a,n,p))%p
        if not val:continue
        nweighted+=1
        bu,bv=powers[u],powers[v]
        for i in range(maxdegree+1):
            if not bu[i]:continue
            for j in range(maxdegree+1):
                if bv[j]:
                    out[i][j]=(out[i][j]+val*bu[i]*bv[j])%p
    return out,nweighted

for p,q1,q2 in EXPECTED:
    t=monotonic()
    mat,nonzero=moments(p,q1,q2)
    assert mat==EXPECTED[(p,q1,q2)]
    d,roots,_=kurihara(q1,q2,p)
    assert mat[1][1]==d
    assert d==(4 if p==5 else 1)
    assert mat[3][3]!=(4 if p==5 else 1)
    digest=hashlib.sha256(
        json.dumps(mat,sort_keys=True,separators=(',',':')).encode()
    ).hexdigest()
    print('GENUINE_FULL_MAZUR_TATE_MIXED_JET_MATRIX_PASS',
          p,q1,q2,'nonzero_symbols',nonzero,
          'M11',mat[1][1],'M33',mat[3][3],
          'matrix_sha256',digest,
          'seconds',round(monotonic()-t,2),flush=True)
print('COUNTERTEST_PASS_RAW_THETA_M33_NE_M11_NO_NAIVE_EULER_JET_INVERSION')
print('SCOPE_FORMAL_NORMED_SERIES_DIVISION_NOT_IDENTIFIED_WITH_TRUE_CONDUCTOR_MAP')
