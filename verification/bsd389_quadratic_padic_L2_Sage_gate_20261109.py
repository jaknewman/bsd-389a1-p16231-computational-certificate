#!/usr/bin/env python3
"""Sage 10.x diagnostic: rank-two cyclotomic p-adic L gate for E=389a1.

Usage:
  python -u verification/bsd389_quadratic_padic_L2_Sage_gate_20261109.py --p 5
  python -u verification/bsd389_quadratic_padic_L2_Sage_gate_20261109.py --p 16231 --skip-regulator

NOT RUN in the assistant runtime: Sage is unavailable. Certifying a nonzero
quadratic L_p coefficient proves finiteness of Sha[p∞] by Kato and
Perrin-Riou--Schneider; computing its order further requires compatible
height normalization and the proven ordinary main conjecture. No uniform
Sha or complex BSD theorem claimed.
"""
import argparse
from sage.all import EllipticCurve, QQ, ZZ

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--p',type=int,default=5)
    parser.add_argument('--series-precision',type=int,default=3)
    parser.add_argument('--regulator-precision',type=int,default=7)
    parser.add_argument('--skip-regulator',action='store_true')
    args=parser.parse_args()
    p=ZZ(args.p)
    if not p.is_prime() or p<5 or p==389:
        raise ValueError('Require p>=5, prime, good (p!=389)')
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    assert E.conductor()==389 and E.discriminant()==389
    a=ZZ(E.ap(p))
    if a%p==0:
        raise ValueError('Ordinary primes only; supersingular not covered')
    n=p+1-a
    print('BSD389_LOCAL_P',p,'a_p',a,'points',n,'anomalous',n%p==0,flush=True)
    lp=E.padic_lseries(p)
    series=lp.series(args.series_precision)
    print('BSD389_L_SERIES',series,flush=True)
    ell2=series[2]
    print('BSD389_L2',ell2,flush=True)
    if not ell2:
        print('NO_CERTIFICATE_INSUFFICIENT_PRECISION_OR_COEFF_ZERO',flush=True)
        return
    if hasattr(ell2,'precision_absolute'):
        print('BSD389_L2_PRECISION_ABSOLUTE',ell2.precision_absolute(),flush=True)
    vl=ZZ(ell2.valuation())
    print('KATO_PR_SCHNEIDER_SHA_P_FINITE_FROM_CERTIFIED_L2',p,'valuation',vl,flush=True)
    if args.skip_regulator:
        print('NO_SHA_ORDER_CLAIM_WITHOUT_REGULATOR',flush=True)
        return
    R=E.padic_regulator(p,args.regulator_precision)
    print('BSD389_SAGE_UNNORMALIZED_REGULATOR',R,flush=True)
    if not R:
        print('NO_REGULATOR_CERTIFICATE_INSUFFICIENT_PRECISION',flush=True)
        return
    vr=ZZ(R.valuation())-2 # normalize cyclotomic gamma chi(gamma)=1+p; rank 2
    ve=2*ZZ(n).valuation(p)
    e=vl-vr-ve
    print('BSD389_VALUATION_BRIDGE_CANDIDATE','v_L2',vl,
          'v_reg_gamma',vr,'v_euler',ve,'v_Sha_predicted',e,flush=True)
    if e<0 or e%2:
        print('WARNING_PRECISION_OR_HEIGHT_NORMALIZATION_MISMATCH',flush=True)
    elif e==0:
        print('SHA_P_ZERO_IF_ALL_NORMALIZATIONS_AND_MAIN_CONJECTURE_MATCH',p,flush=True)
    else:
        print('SHA_P_ORDER_P_POWER_IF_SOURCE_NORMALIZATION_MATCH',p,e,flush=True)
    print('BOUNDARY_NO_UNIFORM_SHA_NO_COMPLEX_BSD',flush=True)

if __name__=='__main__':main()
