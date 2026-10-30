#!/usr/bin/env python3
"""BSD 389a1: independently certify nonzero L(E^(-3),1), and optionally a
conductor-53 ring-class toric character test. Intended for Sage's Python.

No BSD conjecture is used. If toric coefficients are supplied, their order
must be c_j for successive powers of the chosen generator of Cl(O_53),
with chi(generator)=zeta_18^5. This script does NOT validate that ordering.
"""
import argparse
import json
from sage.all import EllipticCurve, QQ, ZZ, RealIntervalField, PolynomialRing, GF


def twist_nonvanishing():
    E = EllipticCurve(QQ, [0, 1, 1, -2, 0])
    Et = E.quadratic_twist(-3)
    assert E.conductor() == 389
    assert Et.conductor() == 3501, Et.conductor()
    assert Et.root_number() == 1, Et.root_number()
    assert E.root_number() == 1
    N = 50
    A = E.anlist(N + 1)
    R = RealIntervalField(160)
    c = 2 * R.pi() / R(3501).sqrt()
    sm = R(0)
    for n in range(1, N + 1):
        chi = 0 if n % 3 == 0 else 1 if n % 3 == 1 else -1
        sm += (2 * R(A[n]) * chi / n) * (-c * n).exp()
    # For every n, |a_n| <= d(n)*sqrt(n) <= 2*n.
    # Central-value approximation (root number +1) and geometric tail:
    # |L(E^(-3),1)-sm| <= 4*sum_{n>N} exp(-c*n).
    tail = 4 * (-c * (N + 1)).exp() / (1 - (-c).exp())
    lower = sm.lower() - tail.upper()
    upper = sm.upper() + tail.upper()
    assert lower > 0, (lower, upper)
    print('BSD389_TWIST_MINUS3_CONDUCTOR', Et.conductor())
    print('BSD389_TWIST_MINUS3_ROOT_NUMBER', Et.root_number())
    print('BSD389_TWIST_MINUS3_INTERVAL', lower, upper)
    print('BSD389_TWIST_MINUS3_NONZERO_CERTIFIED_PASS')
    print('BSD389_LOCAL_K_p', {'p': 16231, 'p_split_K': 16231 % 3 == 1,
          '389_inert_K': 389 % 3 == 2, 'chi53_class_order': (53 + 1) // 3})


def toric_nonvanishing(filename):
    with open(filename, encoding='utf8') as f:
        data = json.load(f)
    coefficients = data['coefficients'] if isinstance(data, dict) else data
    if len(coefficients) != 18 or any(ZZ(x) != x for x in coefficients):
        raise ValueError('Need exactly 18 integers in correct ring-class order')
    c = list(map(ZZ, coefficients))
    Z = PolynomialRing(QQ, 'X')
    X = Z.gen()
    polynomial = sum(QQ(c[j]) * X**j for j in range(18))
    phi18 = X**6 - X**3 + 1
    remainder = polynomial % phi18
    # 19 splits completely in Q(zeta_18), and 13 = 2^5 mod 19 has order 18.
    mod19 = int(sum(c[j] * pow(13, j, 19) for j in range(18)) % 19)
    assert 13**18 % 19 == 1 and all(pow(13, 18 // z, 19) != 1 for z in (2, 3))
    print('CHI53_CLASS_CHARACTER_ORDER', 18)
    print('CHI53_MOD19_TORIC_WITNESS', mod19)
    print('CHI53_EXACT_CYCLOTOMIC_REMAINDER', remainder)
    if remainder != 0:
        print('CHI53_TORIC_PERIOD_NONZERO_ALGEBRAIC_PASS')
        print('BOUNDARY: Waldspurger requires correct orientation, optimal embeddings and toric test vector; anticyclotomic theta order 2 remains separate')
    else:
        print('CHI53_TORIC_PERIOD_ZERO_FOR_THE_SUPPLIED_COEFFICIENTS')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--toric-json', help='JSON list of 18 integers, indexed by powers of selected ideal class generator')
    args = parser.parse_args()
    twist_nonvanishing()
    if args.toric_json:
        toric_nonvanishing(args.toric_json)
    else:
        print('CHI53_TORIC_PERIOD_WAITING_FOR_18_CLASS_COEFFICIENTS')


if __name__ == '__main__':
    main()
