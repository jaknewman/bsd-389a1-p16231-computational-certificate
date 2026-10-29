#!/usr/bin/env python3
"""Proof certificate for Sha(389a1/Q)[2^infinity]=0 using full 2-descent.

Run in an activated SageMath Python environment:
  python -u verification/bsd389_sha_two_primary_exact.py

Mathematical proof:
  The Simon 2-descent returns a proven lower bound r_low for rank E(Q)
  and a proven upper bound s_up for dim_F2 Sel_2(E/Q).
  For 389a1 the expected output is (r_low, s_up)=(2,2).
  The curve has E(Q)[2]=0 since the 2-division polynomial
       4*x^3 + 4*x^2 - 8*x + 1
  has no rational roots. Therefore
       2 <= rank E(Q) <= dim Sel_2 <= 2.
  From 0 -> E(Q)/2E(Q) -> Sel_2 -> Sha[2] -> 0
  it follows Sha[2]=0; hence Sha[2^infinity]=0.

The program checks the theorem's FINITE computational input via Sage;
it is not a formal proof of Sage's implementation. No other p or
complex BSD leading coefficient is implied.
"""
from sage.all import EllipticCurve, QQ, ZZ, PolynomialRing
import json
from pathlib import Path


def main():
    E = EllipticCurve(QQ, [0, 1, 1, -2, 0])
    assert ZZ(E.conductor()) == 389

    R = PolynomialRing(QQ, 'x')
    x = R.gen()
    division2 = 4*x**3 + 4*x**2 - 8*x + 1
    assert not division2.roots(ring=QQ), 'A rational 2-torsion point was found'
    assert ZZ(E.two_torsion_rank()) == 0
    print('BSD389_RATIONAL_2_TORSION_ZERO_PASS', flush=True)
    # An additional cheap finite-field classification: 107 is supersingular.
    # This does NOT recertify the much larger Kurihara computation.
    assert ZZ(E.ap(107)) == 0
    print('BSD389_P107_SUPERSINGULAR_A107_ZERO_PASS', flush=True)

    print('BSD389_SIMON_TWO_DESCENT_START', flush=True)
    low, upper, points = E.simon_two_descent(verbose=0)
    low, upper = int(low), int(upper)
    print('BSD389_SIMON_TWO_DESCENT_BOUNDS', low, upper, flush=True)
    print('BSD389_SIMON_TWO_DESCENT_POINTS', list(map(str, points)), flush=True)
    if (low, upper) != (2, 2):
        raise RuntimeError('2-descent did not recover (2,2); do not assert Sha[2]=0')
    print('BSD389_2_SELMER_DIMENSION_EXACT_PASS', 2, flush=True)
    print('BSD389_SHA_2_TORSION_ZERO_PROVED_FROM_DESCENT_PASS', flush=True)
    print('BSD389_SHA_2_PRIMARY_ZERO_PROVED_FROM_DESCENT_PASS', flush=True)
    print('BOUNDARY: This does not show Sha[p^infinity]=0 for odd p, '
          'global Sha finiteness, or the exact complex leading coefficient.', flush=True)
    report = {
        'curve': '389a1',
        'model': [0,1,1,-2,0],
        'method': 'Sage E.simon_two_descent',
        'two_torsion_rank': 0,
        'rank_lower_bound': low,
        'two_selmer_dimension_upper_bound': upper,
        'two_selmer_dimension': 2,
        'sha_two_torsion': 'zero',
        'sha_two_primary': 'zero',
        'conclusion': 'BSD389_SHA_2_PRIMARY_ZERO_PROVED_FROM_DESCENT_PASS'
    }
    out = Path.home()/'bsd389_sha_two_primary_exact_report.json'
    out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('BSD389_SHA_2_REPORT', out, flush=True)

if __name__ == '__main__':
    main()