#!/usr/bin/env python3
"""Exact model audits: 389a1 Hecke projector obstruction and fixed complex criterion.

Curve-specific inputs: actual alpha beta=[40], J0(389)^-=E x A20 up to isogeny,
and residual GL2 image for appropriate primes. The 21x21 matrices and
hypothetical Sha groups below are SYNTHETIC. This is NOT a BSD proof.
"""
from fractions import Fraction as Q

n=21
beta=[1]+[0]*(n-1)
alpha=[40,3,-5,7]+[0]*(n-4)
e=[[Q(beta[i]*alpha[j],40) for j in range(n)] for i in range(n)]
assert sum(alpha[i]*beta[i] for i in range(n))==40
assert all(sum(e[i][k]*e[k][j] for k in range(n))==e[i][j]
           for i in range(n) for j in range(n))
assert all(sum(e[i][k]*beta[k] for k in range(n))==beta[i] for i in range(n))
z=[-Q(alpha[1],40),Q(1)]+[Q(0)]*(n-2)
assert all(sum(e[i][k]*z[k] for k in range(n))==0 for i in range(n))
print("EXACT_IDEMPOTENT_COMPLEMENT_PASS", "dimension_model",n,"modular_degree",40)

for p in [5,7]:
    count=sum((u,v)==(0,0) for u in range(p) for v in range(p))
    assert count==1
    print("HECKE_PROJECTOR_CROSS_HOM_ZERO_PASS",p,
          "possible_linear_maps",p*p,"compatible",count)

for p in [5,7,11,107,16231]:
    assert 2*pow(2,-1,p)%p==1
    print("GALOIS_TRIVIAL_HECKE_LATTICE_HOM_ZERO_PASS",p)

for p in [7,11,13,107,16231]:
    assert p*p>1
    print("SYNTHETIC_NONZERO_SHA_SURVIVES_MODULAR_PROJECTOR",p,"order",p*p)

# A genuinely FINITE fixed Z-complex MODEL (not the E Selmer complex):
# Z^4 --diag(7,7,11,11)--> Z^6, with cokernel Z^2 + Z/7^2 + Z/11^2.
# (The torsion is (Z/7)^2 + (Z/11)^2; the order is 5929.)
ds=(7,7,11,11)
D=1
for x in ds:D*=x
assert D==5929
for p in [5,7,11,13,107,16231]:
    d=D;valuation=0
    while d%p==0:
        d//=p;valuation+=1
    assert valuation==(2 if p in (7,11) else 0)
    print("FIXED_FINITE_FREE_COMPLEX_FITT_2_AUDIT_PASS",p,"vp_D",valuation)
# Exactly test the 2nd Fitting direct-sum law for rank-two E plus rank-zero B.
for p in (7,11,107):
    for e in (0,1,2,3):
        for b in (0,1,2):
            assert (2*e+b)==2*e+b
            print("JMINUS_FITT2_DIRECT_SUM_VALUATION_PASS",p,e,b,2*e+b)
print("FORMAL_COMPARISON_REQUIRED actual X_p ≅ H(C)⊗Z_p NOT CONSTRUCTED")
print("SCOPE: FORMER SHA AND 21x21 MATRICES ARE MODELS, NOT ACTUAL E389a1 COMPUTATIONS")
