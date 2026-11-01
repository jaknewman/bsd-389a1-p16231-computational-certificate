#!/usr/bin/env python3
"""Rank-two Mordell-Weil wedge is integral, but not by itself a Sha bound.

No Sage required. Checks rational points P1=(-1,1), P2=(0,-1)
on E:y^2+y=x^3+x^2-2x, then tests a *synthetic* free rank-2
module carrying the formally primitive wedge e1 ^ e2.

In the synthetic local Selmer-dual model X_p = Z_p^2 + (Z_p/p)^2,
the SAME primitive free wedge is present, yet Fitt_2(X_p)=p^2 Z_p.
This proves that a primitive wedge of global rational-point
generators, on its own, is not a higher Euler/Kolyvagin system and
cannot establish Sha[p]=0.

This script does NOT compute actual Selmer groups or Sha(389a1).
"""
import argparse
from itertools import combinations
from math import gcd


P1 = (-1, 1)
P2 = (0, -1)


def on_curve(point):
    x, y = point
    return y*y + y == x*x*x + x*x - 2*x


def fitt2_synthetic_generator(p):
    # R^2 + R/(p) + R/(p) has presentation R^2 --D--> R^4
    # where D=[[0,0],[0,0],[p,0],[0,p]] (matrix as rows).
    matrix = [(0,0), (0,0), (p,0), (0,p)]
    minors = [a[0]*b[1] - a[1]*b[0] for a,b in combinations(matrix,2)]
    g = 0
    for v in minors:
        g = gcd(g,v)
    return g


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--primes', default='5,107,599,16231',
                        help='comma-separated primes; for quick illustrations')
    args = parser.parse_args()
    assert on_curve(P1) and on_curve(P2)
    print('MW_WEDGE_BOTH_RATIONAL_POINTS_ON_389A1_PASS',P1,P2,flush=True)
    # The source/input assertion that P1,P2 form a full MW Z-basis
    # is NOT proved by this script. Once certified independently,
    # e1 ^ e2 generates Lambda^2_Z(E(Q)/torsion).
    print('MW_WEDGE_INTEGRAL_BASIS_GENERATOR_EXACT',
          'det_identity',1,'conditional_on_proven_full_MW_basis',flush=True)
    for p in [int(x.strip()) for x in args.primes.split(',') if x.strip()]:
        assert p >= 2
        wedge_coefficient = 1
        local_fitt = fitt2_synthetic_generator(p)
        assert gcd(wedge_coefficient,p)==1
        assert local_fitt==p*p
        assert local_fitt>1
        print('SYNTHETIC_PRIMITIVE_WEDGE_NOT_SHA_BOUND_PASS',
              'p',p,'wedge_unit',wedge_coefficient,
              'fake_Fitt2_generator',local_fitt,flush=True)
    print('BOUNDARY_SYNTHETIC_MODULE_NOT_ACTUAL_SELMER_OR_SHA',flush=True)
    print('REMAINING_REQUIREMENT_ACTUAL_GLOBAL_EULER_SYSTEM_AND_INTEGRAL_FITTING_COMPARISON',
          flush=True)


if __name__=='__main__':
    main()
