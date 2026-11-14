#!/usr/bin/env python3
"""389a1: independent exact local finite-field input for Kurihara degree theorem.

The equality mu_p=2+dim_Fp Sha[p] is a published-theorem deduction:
Kim Theorem 1.10 + Castella--Sano Theorem B + exact Kummer sequence.
This script verifies only local E(F_p) cardinalities and NOT Kurihara/Sha.
"""
from math import isqrt
expected={5:(-3,9),7:(-5,13),11:(-4,16),
          13:(-3,17),107:(0,108),16231:(128,16104)}
def isprime(n):
    return n>=2 and all(n%k for k in range(2,isqrt(n)+1))
def points(q):
    assert q%2 and isprime(q) and q!=389
    n=1
    for x in range(q):
        d=(4*x*x*x+4*x*x-8*x+1)%q
        if d==0:n+=1
        elif pow(d,(q-1)//2,q)==1:n+=2
    return n
for p,(ap,order) in expected.items():
    n=points(p)
    assert n==order and p+1-n==ap and n%p
    print('BSD389_EXACT_NONANOMALOUS_LOCAL_PRIME_PASS',p,
          'a_p',ap,'E_Fp_points',n,'p_local_torsion_zero',True)
print('SCOPE_LOCAL_REDUCTION_ONLY_NOT_A_KURIHARA_UNIT_CERTIFICATE')
print('P13_EXISTENCE_THEOREM_INPUT: archive Sha_13_ZERO + Kim1.10 + Castella-Sano_B')
