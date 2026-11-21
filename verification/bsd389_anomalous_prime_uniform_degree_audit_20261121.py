#!/usr/bin/env python3
"""Finite, exact audit of E389a1 anomalies and published finite coverage.

Only point counts and inventory are computed here. The deduction
mu_p=2 for these primes uses the separately proved Stein-Wuthrich,
Castella-Sano and Kim theorems, not an enumerated Kurihara sum.
"""
from math import isqrt
LIMIT=48859
EXCLUDED_BAD_OR_SUPERSINGULAR=(107,389,599,1049,2957,6661,8263,
                              9397,9551,14633,15101,28591,30671,
                              30869,31799,34781,36263,45161)
EXCEPTION_ORDINARY=16231
ANOMALOUS=(859,1213,1493,1951)

def sieve(n):
    prime=bytearray(b'\x01')*n
    prime[:2]=b'\x00\x00'
    for k in range(2,isqrt(n-1)+1):
        if prime[k]:prime[k*k:n:k]=b'\x00'*len(range(k*k,n,k))
    return {i for i in range(n) if prime[i]}

def ap(p):
    v=0
    for x in range(p):
        d=(1+4*(x*x*x+x*x-2*x))%p
        if d==0:continue
        k=pow(d,(p-1)//2,p)
        assert k in (1,p-1)
        v+=(1 if k==1 else -1)
    return -v

def run():
    primes=sieve(LIMIT)
    assert len(primes)==5024
    assert len(EXCLUDED_BAD_OR_SUPERSINGULAR)==18
    assert set(EXCLUDED_BAD_OR_SUPERSINGULAR).issubset(primes)
    assert EXCEPTION_ORDINARY in primes
    good={p for p in primes if p>=5 and p!=389}
    assert len(good)==5021
    ordinary_cover=good-set(EXCLUDED_BAD_OR_SUPERSINGULAR)-{EXCEPTION_ORDINARY}
    assert len(ordinary_cover)==5003
    certified=ordinary_cover|{107}
    assert len(certified)==5004
    remaining=sorted(good-certified)
    assert len(remaining)==17
    for p in ANOMALOUS:
        assert p in ordinary_cover
        a=ap(p)
        cardinal=p+1-a
        assert a==1 and cardinal==p
        print('BSD389_ANOMALOUS_PRIME_PASS','p',p,'a_p',a,'E_Fp',cardinal)
    print('BSD389_PUBLISHED_FINITE_RANGE_INVENTORY_PASS',
          'good_p_ge5',len(good),'SW_ordinary_cover',len(ordinary_cover),
          'plus_separately_certified_107',len(certified),
          'good_exceptions',remaining)
    print('BOUNDARY: no all-large-p bound; published Sha theorem is an input.')

if __name__=='__main__':run()
