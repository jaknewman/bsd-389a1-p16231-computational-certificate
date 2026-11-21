#!/usr/bin/env python3
"""Certified 389a1 rank-2 archimedean BSD ratio, without invoking BSD.

Regulator from local Tate series, 35 terms and fixed 100-decimal outward
rational interval arithmetic; period from the independent archived 55-digit
rational root/AGM certificate; analytic L''/2 from the user-executed rigorous
Sage Arb interval, widened outward to safe exact decimal endpoints.

Rationality/denominator inference is CONDITIONAL; neither rationality nor
BSD nor full Tate-Shafarevich finiteness is claimed or tested here.
"""
from bsd389_fast_tate_series_regulator_certificate_20261121 import (Iv, S, regulator, rounded)
from fractions import Fraction as F

PERIOD_LO = '4.9804251217101101506427155838846049203121163606791400801'
PERIOD_HI = '4.9804251217101101506427155838846049203121163606791400802'
LSTAR_LO = '0.7593165002884267'
LSTAR_HI = '0.7593165002884269'

if __name__=='__main__':
    R=regulator(35)
    Omega=Iv(PERIOD_LO,PERIOD_HI)
    Lstar=Iv(LSTAR_LO,LSTAR_HI)
    quotient=Lstar/(Omega*R)
    lo,hi=rounded(quotient,17)
    print('BSD389_CERTIFIED_REAL_PERIOD_55_DIGITS',PERIOD_LO,PERIOD_HI)
    print('BSD389_CERTIFIED_LSTAR_16_DIGITS',LSTAR_LO,LSTAR_HI)
    print('BSD389_CERTIFIED_BSD_RATIO_LOWER_17_DIGITS',lo)
    print('BSD389_CERTIFIED_BSD_RATIO_UPPER_17_DIGITS',hi)
    assert F(lo)<F(1)<F(hi)
    assert quotient.lo < S < quotient.hi
    # Farey gap: if a positive rational a/b is not 1 and b<=B,
    # then |a/b-1| >= 1/B. This threshold is independent of Sha.
    B=5_000_000_000_000_000
    assert (quotient.hi-S)*B < S
    assert (S-quotient.lo)*B < S
    print('BSD389_FAREY_RATIONALITY_BRIDGE_PASS',
          'if_quotient_a_over_b_reduced_and_b_at_most',B,'then_a_equals_b')
    print('BSD389_TATE_FAST_ARCHIMEDEAN_RATIO_PASS')
    print('BOUNDARY: does NOT prove rationality, bounded denominator, '
          'complex BSD identity, or global Sha finiteness.')
