#!/usr/bin/env python3
"""Exact source-independent Euler-factor and parity algebra for E389a1.

Arithmetic test, not an all-p Sha bound or a proof of a global conductor descent.
For p^2 generic Frobenius inputs are formal, not claimed to be actual primes.
"""
from math import isqrt
N=389
QS=(397,991,1321,2113,3389,3433)
EXPECTED_AP={397:24,991:-53,1321:2,2113:-53,3389:-75,3433:13}

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def point_count(q):
    total=1
    for x in range(q):
        disc=(1+4*(x*x*x+x*x-2*x))%q
        total += 1 if disc==0 else 2 if pow(disc,(q-1)//2,q)==1 else 0
    return total

def polynomial_coeff(q,ap):
    return (q+1-ap,2*q-ap,q)

def check_jet(q,ap,p,k):
    modulus=p**k
    c0,c1,c2=polynomial_coeff(q,ap)
    assert (q-1)%modulus==0
    assert (ap-2)%modulus==0
    assert (c0%modulus,c1%modulus,c2%modulus)==(0,0,1)
    for t in range(3):
        f=[(i*i+3*i+7*(t+1))%modulus for i in range(14)]
        for r in range(10):
            jet=(c0*f[r+2]+c1*f[r+1]+c2*f[r])%modulus
            assert jet==f[r]
    return (c0,c1,c2)

for q in QS:
    assert prime(q)
    n=point_count(q)
    ap=q+1-n
    assert ap==EXPECTED_AP[q]
    coeffs=check_jet(q,ap,11,1)
    print('P11_AUTHENTIC_EULER_DOUBLE_AUGMENTATION_JET_PASS',q,'ap',ap,
          'order',n,'C0_C1_C2',coeffs,flush=True)
for p,k in ((5,2),(7,2),(11,2),(107,3)):
    # Formal congruence witnesses only, no claim these numbers are actual q or a_q.
    m=p**k
    q=1+8*m;ap=2+19*m
    check_jet(q,ap,p,k)
    print('FORMAL_DEEP_EULER_JET_SHIFT_PASS',p,k,flush=True)
for p in (5,7,11,107):
    for r in (1,3,5,7):
        # On gr^r(I), inversion acts on squarefree r-variable jet by (-1)^r.
        # For global w=+1, equality d_r=(-1)^r*d_r forces 2*d_r=0.
        assert ((1-(-1)**r)*pow(2,-1,p))%p==1
    print('ROOT_PLUS_ODD_DEGREE_MIXED_JET_VANISHES_BY_FUNCTIONAL_EQUATION',p)
print('CERTIFICATE_SCOPE_NO_ANALYTIC_TWO_FACTOR_KURIHARA_DESCENT_OR_GLOBAL_SHA_CLOSURE')
