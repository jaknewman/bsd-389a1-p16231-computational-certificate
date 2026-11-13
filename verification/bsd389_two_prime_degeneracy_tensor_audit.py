#!/usr/bin/env python3
"""Exact six F_q point counts and two-prime oldform tensor audit for 389a1.

Only elementary arithmetic: not Sha, Selmer, an Euler system or BSD.
"""
from math import isqrt
SAMPLES = (
    (5, 41, 61, -3, -8),
    (7, 113, 673, 9, 2),
    (107, 369793, 383917, 2, -854),
)

def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n)+1))

def trace(q):
    assert q % 2 and prime(q) and q != 389
    total = 0
    for x in range(q):
        d = (4*x*x*x + 4*x*x - 8*x + 1) % q
        if d:
            z = pow(d, (q-1)//2, q)
            assert z in (1, q-1)
            total += 1 if z==1 else -1
    return -total

def D(q,a):
    return [[q+1,a],[a,q+1]]

def tensor(A,B):
    return [[A[i//2][j//2]*B[i%2][j%2] for j in range(4)]
            for i in range(4)]

def rank_mod(A,p):
    A = [[z%p for z in row] for row in A]
    r = 0
    for c in range(len(A[0])):
        piv = next((i for i in range(r,len(A)) if A[i][c]),None)
        if piv is None:
            continue
        A[r],A[piv] = A[piv],A[r]
        z=pow(A[r][c],-1,p)
        A[r]=[(x*z)%p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[(A[i][j]-z*A[r][j])%p for j in range(len(A[0]))]
        r+=1
    return r

def valuation(x,p):
    v=0
    while x%p==0:
        v+=1; x//=p
    return v

for p,q1,q2,a1,a2 in SAMPLES:
    assert prime(p) and (trace(q1),trace(q2))==(a1,a2)
    M1,M2=D(q1,a1),D(q2,a2)
    T=tensor(M1,M2)
    n1,n2=q1+1-a1,q2+1-a2
    assert q1%p==q2%p==1 and a1%p==a2%p==2
    assert rank_mod(M1,p)==rank_mod(M2,p)==rank_mod(T,p)==1
    assert valuation(n1,p)==valuation(n2,p)==1
    mixed=(1,-1,-1,1)
    assert tuple(sum(row[j]*mixed[j] for j in range(4)) for row in T)==tuple(
        n1*n2*z for z in mixed)
    print("TWO_PRIME_DEGENERACY_TENSOR_PASS", "p",p,"q",q1,q2,
          "Fq_orders",n1,n2,"rank_modp",1,
          "mixed_eigenvalue_val",valuation(n1*n2,p),
          "normalized_smith_valuations",(0,1,1,2),
          "full_pairing_extra_modular_degree_v",valuation(40,p))
print("SCOPE_NORMALIZED_OLDFORM_LINEAR_ALGEBRA_ONLY_NO_SHA_BSD_CLAIM")
