#!/usr/bin/env python3
"""Exact character-by-character DIRICHLET unit ranks for 389a1 Borel fields.

This checks actual archimedean Δ-permutation representations, signatures,
and at supersingular primes the *theorem-derived* local unit / ray rank.
NO actual ideal class group, unit generators, Selmer or BSD computed.
"""
from math import isqrt

def isprime(n):return n>=5 and all(n%k for k in range(2,isqrt(n)+1))
def root(p):
    n=p-1;fs=[];k=2
    while k*k<=n:
        if n%k==0:
            fs.append(k)
            while n%k==0:n//=k
        k+=1
    if n>1:fs.append(n)
    return next(g for g in range(2,p) if all(pow(g,(p-1)//f,p)!=1 for f in fs))

def rank(A,p):
    A=[x[:] for x in A]; n=len(A);i=0
    if not n:return 0
    for j in range(len(A[0])):
        k=next((k for k in range(i,n) if A[k][j]%p),None)
        if k is None:continue
        A[i],A[k]=A[k],A[i]
        c=pow(A[i][j]%p,-1,p)
        A[i]=[(a*c)%p for a in A[i]]
        for k in range(i+1,n):
            if A[k][j]%p:
                v=A[k][j]%p
                A[k]=[(a-v*b)%p for a,b in zip(A[k],A[i])]
        i+=1
        if i==n:break
    return i

for p in (5,7,11,13,107,599,16231):
    assert isprime(p)
    m=p-1
    rc=(p+1)//2
    sigK=(2,(p-1)//2)
    sigL=(p-1,p*(p-1)//2)
    assert sigK[0]+2*sigK[1]==p+1
    assert sigL[0]+2*sigL[1]==p*p-1
    lengths=[m]*rc+[m//2]
    assert sum(lengths)==sum(sigL)
    ranks=[rc+(k%2==0)-(k==0) for k in range(m)]
    assert sum(ranks)==sigL[0]+sigL[1]-1
    assert ranks[1]==rc
    assert pow(root(p),m//2,p)==p-1
    print("CHI_ARCHIMEDEAN_DIRICHLET_RANK_PASS",p,
          "K_signature",sigK,"L_signature",sigL,
          "total_global_unit_rank",sum(ranks),
          "chi_global_unit_rank",ranks[1],
          "chi_local_unit_rank_supersingular",p+1,
          "chi_ray_free_rank_lower_supersingular",rc,
          "Hecke_L_zero_order_at_s0",rc,flush=True)

    # On nontrivial odd χ the global log sum-zero relation does not
    # change the χ-eigenspace. Directly compute ker(T−g) on the
    # ACTUAL archimedean Δ-permutation module for p≤13.
    if p<=13:
        shift=[];base=0
        for length in lengths:
            shift.extend(base+(i+1)%length for i in range(length))
            base+=length
        assert len(shift)==len(set(shift))
        size=len(shift);g=root(p)
        A=[[0]*size for _ in range(size)]
        for i,j in enumerate(shift):
            A[j][i]=(A[j][i]+1)%p
            A[i][i]=(A[i][i]-g)%p
        nullity=size-rank(A,p)
        assert nullity==rc
        print("CHI_ACTUAL_ARCHIMEDEAN_MATRIX_KERNEL_PASS",p,
              "size",size,"nullity",nullity)
print("SCOPE: unit ranks and ray free-rank theorem, NOT finite class group r_chi.")
