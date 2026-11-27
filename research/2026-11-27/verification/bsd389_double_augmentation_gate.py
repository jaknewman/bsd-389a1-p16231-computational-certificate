#!/usr/bin/env python3
"""Exact integer certificate for double augmentation zero of Kolyvagin Euler factors.

Curve 389a1: y^2+y=x^3+x^2-2x.
This verifies local polynomial identities ONLY, not global Selmer contraction.
"""
from math import isqrt

def prime(q):
    if q < 2: return False
    for d in range(2, isqrt(q)+1):
        if q%d==0:return False
    return True

def trace(q):
    assert prime(q) and q!=389
    s=0
    for x in range(q):
        v=(1+4*(x*x*x+x*x-2*x))%q
        s += 0 if v==0 else (1 if pow(v,(q-1)//2,q)==1 else -1)
    return -s

def vp(n,p):
    if n==0:return None
    k=0
    while n%p==0:
        n//=p;k+=1
    return k

samples=[(5,41,1),(5,61,1),(5,131,1),(5,251,1),(7,113,1),(7,673,1),(7,1429,1),(7,2423,1),
         (5,5351,2),(5,10651,2),(7,9311,2)]
print('EXACT_DOUBLE_AUGMENTATION_EULER_FACTOR_TESTS')
for p,q,m in samples:
    a=trace(q)
    A=q+1-a # point count
    B=2*q-a # linear term in Y
    assert q%p==1 and a%p==2%p and A%p==0 and B%p==0
    assert q%(p**m)==1 and A%(p**m)==0 and B%(p**m)==0,(p,q,m,A,B)
    assert q%(p**m)==1 # leading coefficient q ≡1
    assert 2*q%p!=0
    assert 1-a+q==A
    print('P',p,'Q',q,'LEVEL',m,'AP',a,'EPOINTS',A,'VP_EPOINTS',vp(A,p),
          'P(1)',A,'Pprime(1)',B,'HALF_Pdoubleprime(1)',q,
          'SECOND_JET_UNIT',q%p)
print('DOUBLE_ZERO_AT_AUGMENTATION_MOD_P_POWER_PASS',len(samples))
print('BOUNDARY: the quadratic Euler symbol is unit; global integral contraction is NOT proved')
