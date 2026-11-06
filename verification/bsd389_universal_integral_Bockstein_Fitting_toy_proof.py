#!/usr/bin/env python3
"""Universal polynomial audit over Z[p,T] for ABSTRACT rank-two toy Selmer modules.
No Sage, sympy, curve-specific inputs or previous certificates. NOT a BSD proof.
"""
from itertools import combinations, permutations
ZERO={}
ONE={(0,0):1}
P={(1,0):1}
T={(0,1):1}
T2={(0,2):1}

def add(x,y):
    d=dict(x)
    for m,c in y.items():
        d[m]=d.get(m,0)+c
        if not d[m]: del d[m]
    return d

def neg(x): return {m:-c for m,c in x.items()}

def mul(x,y):
    d={}
    for (a,b),c in x.items():
        for (u,v),e in y.items():
            m=(a+u,b+v)
            d[m]=d.get(m,0)+c*e
    return {m:c for m,c in d.items() if c}

def det(M):
    n=len(M); z=ZERO
    for perm in permutations(range(n)):
        term=ONE
        for i,j in enumerate(perm): term=mul(term,M[i][j])
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        z=add(z,neg(term) if inversions%2 else term)
    return z

def minors(M,k):
    n=len(M)
    return {tuple(sorted(det([[M[i][j] for j in cols] for i in rows]).items()))
            for rows in combinations(range(n),k)
            for cols in combinations(range(n),k)}

def signature(*terms):
    return {tuple(sorted(x.items())) for x in terms}

def at0(x):
    return {m:c for m,c in x.items() if m[1]==0}

G=[[ZERO for j in range(4)] for i in range(4)]
for i,x in enumerate((ONE,ONE,T2,T2)): G[i][i]=x
B=[[P,T,ZERO,ZERO],[T,ZERO,ZERO,ZERO],
   [ZERO,ZERO,P,T],[ZERO,ZERO,T,ZERO]]
assert det(G)==det(B)=={(0,4):1}
assert signature(ONE)<=minors(G,2)
assert minors(B,2)==signature(ZERO,{(2,0):1},{(1,1):1},{(0,2):1},{(0,2):-1})
G0=[[at0(x) for x in row] for row in G]
B0=[[at0(x) for x in row] for row in B]
assert minors(G0,2)==signature(ZERO,ONE)
assert minors(B0,2)==signature(ZERO,{(2,0):1})
print("UNIVERSAL_INITIAL_FITTING_BOTH (T^4)")
print("UNIVERSAL_SECOND_FITTING_GOOD (1)")
print("UNIVERSAL_SECOND_FITTING_BAD (p^2,pT,T^2)")
print("AUGMENTATION_COKERNEL_GOOD Zp^2")
print("AUGMENTATION_COKERNEL_BAD Zp^2_plus_(Z/p)^2")
print("DERIVED_BOCKSTEIN_DET_GOOD 1")
print("DERIVED_BOCKSTEIN_DET_BAD p^2")
print("NOT_A_CURVE_SELmer_OR_BSD_PROOF")
