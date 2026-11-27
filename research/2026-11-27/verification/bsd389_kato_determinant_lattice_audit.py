#!/usr/bin/env python3
"""Exact rank-two determinant-lattice test, not a Selmer computation.

C^(1)=Zp^4 -> C^(2)=Zp^2, differential [0 0 p^e 0; 0 0 0 p^e].
H^1=Zp^2; H^2=(Z/p^e)^2. Its maximal minor has p-adic
valuation 2e, which is the determinant-line index in wedge^2 H^1.
"""
from itertools import combinations

def v_p(n,p):
    if n == 0: return None
    n=abs(n);v=0
    while n%p==0: n//=p;v+=1
    return v

for p in (5,7,107,599,1049,2003):
    for e in (0,1,2,3):
        m=p**e
        d=[[0,0,m,0],[0,0,0,m]]
        minors=[]
        for i,j in combinations(range(4),2):
            minors.append(d[0][i]*d[1][j]-d[0][j]*d[1][i])
        nonzero=[x for x in minors if x!=0]
        assert nonzero==[m*m],(p,e,minors)
        index=v_p(nonzero[0],p)
        assert index==2*e
        # cokernel(D) = (Z/p^e)^2, kernel free on first two basis vectors
        assert all(row[0]==row[1]==0 for row in d)
        primitive=(index==0)
        print("DETERMINANT_LATTICE_MODEL_PASS",
              "p",p,"e",e,"H1_RANK",2,
              "H2_ORDER",m*m,"LATTICE_INDEX_VAL",index,
              "ETA_KATO_PRIMITIVE_MODEL",primitive)
print("BKS_DETERMINANT_INDEX_DEPENDS_ON_H2_TORSION_PASS")
print("BOUNDARY: This is a model, not actual p-Selmer/H2 of 389a1.")
