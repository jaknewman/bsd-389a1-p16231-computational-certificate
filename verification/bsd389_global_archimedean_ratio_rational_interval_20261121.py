#!/usr/bin/env python3
"""Certified BSD leading-term *numerical ratio* for E389a1, not identity.

Requires two self-contained exact-rational certificate modules in the same
folder. The sole external bound is the user's previous Sage Arb verified
L''(E,1)/2 enclosure, conservatively widened to rational decimal endpoints.
All other arithmetic uses Fraction, integer isqrt, gcd and exact Bezout.
"""
from pathlib import Path
from fractions import Fraction as F
from runpy import run_path

HERE=Path(__file__).resolve().parent
P=run_path(str(HERE/'bsd389_real_period_exact_rational_agm_20261121.py'),
           run_name='IMPORT_PERIOD')
H=run_path(str(HERE/'bsd389_canonical_regulator_exact_duplication_20261121.py'),
           run_name='IMPORT_HEIGHTS')

def period_interval():
    e3=P['root_interval'](-3,-1)
    e2=P['root_interval'](0,F(1,2))
    e1=P['root_interval'](F(1,2),2)
    delta=e1-e3
    b=((e1-e2)/delta).sqrt()
    a=P['Iv'](1)
    for _ in range(12):a,b=(a+b)/2,(a*b).sqrt()
    agm=P['Iv'](b.lo,a.hi)
    pi=P['atan_bound'](5,80)*16-P['atan_bound'](239,30)*4
    omega=pi*2/(delta.sqrt()*agm)
    return omega

def regulator_interval(n=10):
    C=H['verify_bezout']()
    hp=H['point_height'](-1,n,C)
    hq=H['point_height'](0,n,C)
    hpq=H['point_height'](4,n,C)
    # Heights H(.)=lim h(x(2^n .))/4^n =2*canonical h(.).
    # BSD pairing diag H(P),H(Q), off diag [H(P+Q)-H(P)-H(Q)]/2.
    cross=(hpq-hp-hq)/2
    return hp*hq-cross.square()

def main():
    omega=period_interval()
    hreg=regulator_interval()
    reg=P['Iv'](hreg.lo,hreg.hi)
    # Proven user-executed Arb ball for L''/2 was
    # [0.7593165002884268 +/- 7.81e-17]. We widen conservatively.
    L=P['Iv'](F('0.7593165002884267'),F('0.7593165002884269'))
    # E real components 2, Tamagawa 1, torsion 1, saturated MW basis.
    ratio=L/(omega*reg)
    for name,v,digits in [('PERIOD',omega,45),('REGULATOR',reg,12),
                          ('RATIO',ratio,12)]:
        lo,hi=P['decimal_bounds'](v,digits)
        print(f'BSD389_CERTIFIED_{name}_LOWER',lo)
        print(f'BSD389_CERTIFIED_{name}_UPPER',hi)
    assert F('0.9999')<ratio.lo<ratio.hi<F('1.0001')
    assert ratio.lo<F(1)<ratio.hi
    print('BSD389_ARCHIMEDEAN_BSD_RATIO_CERTIFIED_NEAR_ONE_PASS')
    print('THEOREM: If the exact strong BSD leading-term identity is true, '
          'its predicted positive integer order #Sha must be 1.')
    print('BOUNDARY: ratio is only rigorously near one, NOT exactly one. '
          'It cannot prove the full Sha finite or the complex leading-term equality.')

if __name__=='__main__':main()
