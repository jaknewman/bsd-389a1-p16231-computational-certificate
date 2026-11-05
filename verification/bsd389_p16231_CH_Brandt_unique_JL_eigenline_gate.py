#!/usr/bin/env python3
"""Prove 389a1 Brandt eigenspace is unique and integrally primitive.
Exact rational linear algebra on 33x33 Hecke operators, no Gross enumeration.
"""
from sage.all import EllipticCurve, BrandtModule, QQ, ZZ, matrix, identity_matrix, vector, gcd

E=EllipticCurve("389a1")
BM=BrandtModule(389,base_ring=QQ)
reps=list(BM.right_ideals())
assert len(reps)==33
V=vector(QQ,(0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,
             -1,0,0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0))
assert V.length()==33 and gcd([ZZ(t) for t in V])==1
print("CH_JL_INTEGER_PRIMITIVE_BRANDT_V_PASS",flush=True)
I=identity_matrix(QQ,33)
matrices=[]
for ell in (2,3,5,7):
    A=BM.hecke_matrix(ell)
    lam=ZZ(E.ap(ell))
    assert A*V==lam*V and V*A==lam*V
    matrices.append(A-lam*I)
    print("CH_JL_EXACT_HECKE_EQUALITY_PASS",
          ell,"A_P",lam,flush=True)
stack=matrix(QQ,0,33)
for A in matrices:
    stack=stack.stack(A)
    rank=stack.rank()
    null=33-rank
    print("CH_JL_COMMON_HECKE_EIGENSPACE",len(range(0,stack.nrows()//33)),
          "DIM",null,flush=True)
assert 33-stack.rank()==1,(
    "CH_JL_JOINT_HECKE_EIGENSPACE_NOT_UNIQUE",33-stack.rank())
nullvec=stack.right_kernel().basis()[0]
assert nullvec!=0
# All rational eigenvectors for these primes are multiples of V,
# and the primitive integral lattice on this line is Z*V.
pivot=next(k for k in range(33) if V[k]!=0)
assert nullvec==(nullvec[pivot]/V[pivot])*V
print("CH_JL_UNIQUE_RATIONAL_HEKCE_LINE_PASS",
      "DIM",1,"PRIMITIVE_GCD",1,flush=True)
print("BOUNDARY_GLOBAL_ADELIC_GROSS_RIGHT_IDEAL_IDENTIFICATION_STILL_TO_WRITE",flush=True)
