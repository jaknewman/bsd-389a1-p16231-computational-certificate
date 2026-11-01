#!/usr/bin/env python3
"""Tiny direct Sage/eclib verification of ONE p-independent modular-symbol unit.

For E=389a1, in the certified Neron-period / L_ratio convention:
    m_E^+(382/389) = m_E^+(7/389) = -1,
    m_E^+(384/389) = m_E^+(5/389) = -2.
A single symbol -1 is enough to certify classical-symbol nonvanishing
at EVERY rational prime p, including p=2,3,389.

This is NOT a nonzero two-prime Kurihara number, Selmer Fitt_2
certificate, derived Euler system, or a proof of Sha finiteness/BSD.

Run from the Sage-enabled Python environment:
    python -u verification/bsd389_single_cusp_global_unit.py
"""

from sage.all import EllipticCurve, QQ, ZZ

N = 389
VALUES = {
    382: -1, 384: -2,
    7: -1, 5: -2,
}


def main():
    E = EllipticCurve(QQ, [0, 1, 1, -2, 0])
    assert int(E.conductor()) == N and int(E.discriminant()) == N
    assert int(E.real_components()) == 2
    symbols = {
        "sage": E.modular_symbol(
            sign=+1, implementation="sage", normalize="L_ratio"),
        "eclib": E.modular_symbol(sign=+1, implementation="eclib"),
    }
    total = 0
    for name, symbol in symbols.items():
        for a, expected in VALUES.items():
            result = QQ(symbol(QQ(a) / N))
            assert result == expected, (
                "NORMALIZATION_OR_VALUE_MISMATCH", name, a, result, expected)
            total += 1
            print(
                "ONE_CUSP_DIRECT_VALUE_PASS",
                "oracle", name, "a", a, "value", result,
                flush=True
            )
        assert QQ(symbol(QQ(382)/N)) == QQ(symbol(QQ(7)/N))
        assert QQ(symbol(QQ(384)/N)) == QQ(symbol(QQ(5)/N))
    assert total == 8
    assert (VALUES[382] - VALUES[384]) == 1
    assert ZZ(VALUES[7]).is_unit()
    print(
        "ONE_CUSP_BOTH_SAGE_ECLIB_8_DIRECT_VALUES_PASS",
        "checks", total, flush=True
    )
    print("ONE_CUSP_EXACT_BEZOUT_PASS", "(-1)-(-2)=1", flush=True)
    print("ONE_CUSP_P_UNIFORM_CLASSICAL_SYMBOL_UNIT_PASS",
          "m_plus(7/389)=-1", "all_rational_primes", flush=True)
    print("BOUNDARY_NO_TWO_PRIME_KURIHARA_OR_SHA_FITTING_IMPLICATION", flush=True)


if __name__ == "__main__":
    main()
