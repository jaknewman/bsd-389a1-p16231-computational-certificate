#!/usr/bin/env python3
"""Precision-two cyclotomic L2 test for E389a1 via Pollack--Stevens.

This file is PREPARED BUT NOT EXECUTED HERE (Sage unavailable).
Examples on a Sage-equipped host:
    python -u verification/bsd389_p16231_quadratic_L2_pollack_stevens_Sage_gate_20261109.py --p 5
    python -u verification/bsd389_p16231_quadratic_L2_pollack_stevens_Sage_gate_20261109.py --p 16231 --precision 6

The previously independently computed standard L2(16231) vanishes mod16231.
Published regulator has valuation exactly 1 (Stein 2007, Q4).
A certified L2 valuation exactly 1, after source normalization checks, would
give Sha(E/Q)[16231^infinity]=0 via ordinary Iwasawa and PR-Schneider.
"""
import argparse
from sage.all import EllipticCurve, QQ, ZZ


def main():
    args = argparse.ArgumentParser()
    args.add_argument("--p", type=int, default=16231)
    args.add_argument("--precision", type=int, default=6)
    cfg = args.parse_args()
    p = ZZ(cfg.p)
    if not p.is_prime() or p < 5 or p == 389:
        raise ValueError("good prime p>=5, p!=389 required")
    E = EllipticCurve(QQ, [0, 1, 1, -2, 0])
    assert E.conductor() == 389 and E.discriminant() == 389
    a_p = ZZ(E.ap(p))
    if not a_p % p:
        raise ValueError("ordinary primes only")
    if p == 16231:
        assert a_p == 128 and p + 1 - a_p == 16104
    print("BSD389_OMS_PRECHECK", "p", p, "ap", a_p,
          "order_EFp", p + 1 - a_p, "precision_cap", cfg.precision, flush=True)
    L = E.padic_lseries(p, implementation="pollackstevens",
                        precision=ZZ(cfg.precision))
    series = L.series(3)
    l2 = series[2]
    print("BSD389_OMS_SERIES", series, flush=True)
    print("BSD389_OMS_L2", l2, flush=True)
    prec = l2.precision_absolute() if hasattr(l2, "precision_absolute") else None
    print("BSD389_OMS_L2_ABS_PRECISION", prec, flush=True)
    if prec is None or prec < 2:
        print("NO_CERTIFICATE_INSUFFICIENT_PRECISION", flush=True)
        return
    v = l2.valuation()
    print("BSD389_OMS_L2_VALUATION", v, flush=True)
    if v >= prec:
        print("NO_CERTIFICATE_L2_ZERO_AT_CURRENT_PRECISION", flush=True)
        return
    if p == 16231 and v == 1:
        print("BSD389_16231_L2_OVER_P_UNIT_CERTIFIED", l2/p, flush=True)
        print("SHA16231_ZERO_IF_SOURCE_ORDINARY_MAIN_CONJECTURE_AND_PADIC_REG_NORMALIZATION_MATCH",flush=True)
    elif p == 16231 and v >= 2:
        print("BSD389_16231_L2_DIVISIBLE_BY_P2_NOT_SHA_ZERO_CERTIFICATE",flush=True)
    elif p == 16231:
        print("ERROR_CONTRADICTS_INDEPENDENT_CLASSICAL_L2_MODP_ZERO",flush=True)
    else:
        print("OTHER_PRIME_VALUATION_CERTIFIED", p, v, flush=True)
    print("BOUNDARY_NO_UNIFORM_SHA_OR_COMPLEX_BSD",flush=True)


if __name__ == "__main__":
    main()
