#!/usr/bin/env python3
"""SageMath 10.9 p=599 supersingular precision/cost gate. No Sha computation.

The code-source formula for positive-degree coefficients is
  _prec_bounds(n, prec)[j] = 2*e_j(n-1) - (n+2),
where e_j(m) is the minimum valuation of binomial(p**m, k) for k<=j.
At j=2 for odd p, e_2(m)=m, hence the generic precision is n-4.
Sage's direct series(n, prec=3) loop evaluates (p-1)*p**(n-1)
measures. A positive generic T^2 precision first appears at n=5.
"""
from math import comb
P=599
Q1=6912461
Q2=13963889
HALF=(Q1*Q2-1)//2
UNITS=(Q1-1)*(Q2-1)//2
assert HALF==48262419060414
assert UNITS==48262408622240
assert Q1%P==Q2%P==1

def vp(n,p):
    i=0
    while n and n%p==0:
        n//=p
        i+=1
    return i

print('K599_PRECISION_SOURCE_FORMULA p=599 rank=2 supersingular_alpha_adic_bound=n-4')
for n in (2,3,4,5):
    e=min(vp(comb(P**(n-1),j),P) for j in (1,2))
    assert e==n-1
    alpha_bound=2*e-(n+2)
    calls=(P-1)*P**(n-1)
    print(f'K599_PADIC_SOURCE_LEVEL n={n} T2_alpha_precision_bound={alpha_bound} measure_evaluations={calls}')
assert (P-1)*P**4==76985418245398
print('K599_GENERIC_POSITIVE_T2_ALPHA_PRECISION_FIRST_AT_N5_PASS')
print('K599_N5_EXCEEDS_KURIHARA_HALF_UNITS', (P-1)*P**4, 'VERSUS', UNITS)
print('K599_NO_GLOBAL_SHA_OR_KURIHARA_CERTIFICATE')
