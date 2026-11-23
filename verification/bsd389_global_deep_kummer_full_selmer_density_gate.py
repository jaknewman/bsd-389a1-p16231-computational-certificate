#!/usr/bin/env python3
"""Exact finite arithmetic for depth-k Selmer Chebotarev axis selectors.

Verifies group class/centralizer cardinalities, Kummer fiber counts and
one-axis density at small (p,k,s). Does NOT prove Serre, Sah or Chebotarev,
or prove Kurihara nonvanishing, nor compute Sha.
"""
from fractions import Fraction
from itertools import product
from math import gcd


def group_cardinality(p, k):
    return p**(4 * (k-1)) * (p*p - 1) * (p*p - p)


def centralizer_cardinality(p, k):
    return p**(2*k-1) * (p-1)


def brute_centralizer(p, k):
    m = p**k
    count = 0
    for a,b,c,d in product(range(m),repeat=4):
        # centralizer of U=[[1,1],[0,1]]: c=0 and d=a;
        # require invertible determinant modulo p.
        if c == 0 and d == a and gcd(a,p) == 1:
            count += 1
    return count


def check(p,k,s,with_brute=False):
    G=group_cardinality(p,k)
    C=centralizer_cardinality(p,k)
    assert G%C==0
    conjugacy_class=G//C
    assert conjugacy_class==p**(2*k-2)*(p*p-1)
    if with_brute:
        assert brute_centralizer(p,k)==C
    # In V/(U-I)V, the quotient is the second vector coordinate.
    # For s cocycles the local quotient has p**s patterns.
    quotient_patterns=tuple(product(range(p),repeat=s))
    favorable=sum(w[0]!=0 and all(x==0 for x in w[1:])
                  for w in quotient_patterns)
    assert favorable==p-1
    # Each quotient pattern has p**s lifts in V**s.
    favorable_in_full_fiber=favorable*p**s
    total_in_full_fiber=p**(2*s)
    density=Fraction(conjugacy_class*favorable_in_full_fiber,
                     G*total_in_full_fiber)
    expected=Fraction(1,p**(2*k+s-1))
    assert density==expected
    print('DEEP_FULL_SELMER_AXIS_DENSITY_PASS',
          f'p={p}',f'k={k}',f's={s}',
          f'conjugacy_size={conjugacy_class}',
          f'centralizer={C}',f'fiber={total_in_full_fiber}',
          f'favorable={favorable_in_full_fiber}',
          f'density={density}')


for args in [(3,1,2,True),(3,2,2,True),
             (5,1,3,True),(5,2,2,True),
             (7,2,2,False),(11,2,2,False),
             (11,2,4,False)]:
    check(*args)
print('BOUNDARY_NO_DELTA_UNIT_OR_GLOBAL_SHA_CONCLUSION')
