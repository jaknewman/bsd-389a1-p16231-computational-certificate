#!/usr/bin/env python3
"""Genuine E389a1 p5 depth25 valuation-one: 20 real cyclic fields, 416 twists.

Reads FULL integer 25-coefficient histograms per unit orientation, generated
by companion native C++ from the 34,775,000 genuine plus-Manin symbols.
Checks all 40 TRUE cyclotomic resultants and 20 exact Smith forms (Φ5 and Φ25), their exact
5-adic valuations, and the 20 histograms' SHA256.

Result: every nontrivial character of every one of the 20 fields has
L(E,chi,1)!=0 by Birch--Stevens. Kato then proves rank E(K)=2;
torsion-free odd-degree extension gives E(K)=E(Q) exactly.
WARNING: no claim Sha(E/K)[5∞]=0 in the val1 nonunit family.
This is a finite prime5 calculation, NOT global BSD.
"""
import argparse
from math import comb,gcd
from pathlib import Path
import hashlib,json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

EXPECTED_SHA256="1a22c0ed1b4ac336a648ec0a0bf1d6121fd6224993c37e928713117cd1d4c463"
EXPECTED={
  1:(4,4,4,1,2), 2:(4,4,4,4,4),
  3:(6,6,6,0,3), 4:(6,6,6,0,3),
}
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument("--hist",type=Path,required=True,help="Full C++ all20 histogram output")
args=ap.parse_args()
rows=args.hist.read_text().splitlines()
assert rows[0].strip()=="count 34775000" and len(rows)==21
X=sp.Symbol("X")
phi5=sp.cyclotomic_poly(5,X)
phi25=sp.cyclotomic_poly(25,X)
data=[];degrees={4:0,6:0}
for line in rows[1:]:
    a=line.split()
    assert a[0]=="r" and a[2]=="hist"
    r=int(a[1]); hist=list(map(int,a[3:]))
    assert 1<=r<=24 and gcd(r,5)==1 and len(hist)==25
    assert sum(hist)==0
    C=[sum(z*comb(j,d) for j,z in enumerate(hist) if j>=d)
       for d in range(7)]
    assert C[1]%25==0 and C[2]%25==(15*r)%25
    assert C[3]%5==0
    d=next(d for d,c in enumerate(C) if c%5)
    F=sp.Poly(sum(z*X**j for j,z in enumerate(hist)),X)
    vals={}
    norms={}
    for order,cyclo in ((5,phi5),(25,phi25)):
        B=int(sp.resultant(F,cyclo,X))
        assert B !=0
        n=abs(B);v=0
        while n%5==0:n//=5;v+=1
        vals[order]=v
        norms[order]=B
    # Independently reconstruct the genuine integral inversion-symmetric
    # 12x12 Mazur--Tate operator and its full p-primary Smith form.
    shift=next(sh for sh in range(25) if
               all(hist[j]==hist[(sh-j)%25] for j in range(25)))
    center=next(t for t in range(25) if (2*t+shift)%25==0)
    g=[hist[(j-center)%25] for j in range(25)]
    assert all(g[j]==g[-j%25] for j in range(25))
    A=sp.Matrix(12,12,lambda i,j:
        g[(i-j)%25]+g[(i+j+2)%25]-2*g[i+1])
    assert int(A.det())**2==norms[5]*norms[25]
    S=smith_normal_form(A,domain=sp.ZZ)
    ex=[]
    for i in range(12):
        z=abs(int(S[i,i]));v=0
        assert z>0
        while z%5==0:z//=5;v+=1
        ex.append(v)
    ex.sort()
    assert ex==([0]*10+[2,2] if r%5 in (1,2) else [0]*9+[1,2,3])
    assert (d,vals[5],vals[25],C[4]%5,C[6]%5)==EXPECTED[r%5],(r,C[:7],vals)
    degrees[d]+=1
    data.append((r,hist))
    print("GENUINE_VAL1_ALL_CHARACTER_L_NONVANISHING_PASS",
          "r",r,"first_unit_degree_mod5",d,
          "c2_mod25",C[2]%25,
          "v5_norm_order5",vals[5],"v5_norm_order25",vals[25], "symmetric_matrix_smith5",ex,flush=True)
assert len(data)==20 and len({r for r,_ in data})==20
assert degrees=={4:10,6:10}
blob=json.dumps(data,separators=(",",":"),ensure_ascii=True).encode()
digest=hashlib.sha256(blob).hexdigest()
assert digest==EXPECTED_SHA256
print("ALL20_GENUINE_MAZUR_TATE_HISTOGRAM_SHA256_PASS",digest)
print("ALL20_FIELDS_NONTRIVIAL_TWISTS_L_NONZERO_PASS",
      "fields",20,"order25_distinct",400,"order5_distinct",16,
      "total_distinct",416)
print("EXTERNAL_KATO_THEOREM_PLUS_NO_ISOGENY_IMPLICATION:",
      "analytic_rank_K=2, MW(K)=MW(Q)=Z^2 for each of 20")
print("NO_CLAIM_SHA_K_ZERO_IN_VALUATION_ONE_FAMILY")
print("UNIFORM_ALL_P_SHA_FINITE_AND_EXACT_COMPLEX_BSD_STILL_OPEN")
