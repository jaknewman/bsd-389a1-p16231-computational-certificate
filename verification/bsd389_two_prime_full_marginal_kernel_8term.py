#!/usr/bin/env python3
"""Exact 8-term universal obstruction: FULL Hecke marginals never determine M11.

In R=F_p[C_(q1-1) x C_(q2-1)], put
    s=X^(h1/2)*Y^(h2/2), s^2=1,
    H=(1+s)*(1-X)*(1-Y).
Then H has exactly 8 signed CRT-exponent coefficients:
  * sign-plus invariant: s*H=H;
  * H(X,1)=H(1,Y)=0 EXACTLY (not just truncated jets);
  * [TU]H(1+T,1+U)=2 mod p, a p-UNIT for every odd p.

Therefore for any sign-plus Theta, adding (d-M11)/2 * H
preserves BOTH ENTIRE MARGINAL POLYNOMIALS and sign-plus symmetry,
but changes M11 to an arbitrary desired value d in F_p.
This is a universal algebraic failure of marginal-only inference.
H is SYNTHETIC, not shown to satisfy all modular-symbol/Hecke
eigenrelations across levels or to come from the actual elliptic curve.

No Sage needed. Historical triples are (5,41,61),(7,113,673),
(107,369793,383917); only 8 terms are manipulated, not huge arrays.
"""

import argparse
from collections import defaultdict

DEFAULT_TRIPLES = ((5, 41, 61), (7, 113, 673),
                   (107, 369793, 383917))


def eight_term_H(h1, h2):
    assert h1 % 2 == h2 % 2 == 0 and h1 > 2 and h2 > 2
    terms = defaultdict(int)
    for shift in (0, 1):
        for dk in (0, 1):
            for dl in (0, 1):
                key = ((dk + shift * (h1 // 2)) % h1,
                       (dl + shift * (h2 // 2)) % h2)
                terms[key] += (-1) ** (dk + dl)
    terms = {k: v for k, v in terms.items() if v}
    assert len(terms) == 8
    return terms


def moment(terms, p, a, b):
    return sum(pow(k % p, a, p) * pow(l % p, b, p) * z
               for (k, l), z in terms.items()) % p


def verify(p, q1, q2):
    assert p % 2 == 1 and p >= 3 and (q1 - 1) % p == 0
    assert (q2 - 1) % p == 0
    h1, h2 = q1 - 1, q2 - 1
    terms = eight_term_H(h1, h2)

    # Multiplication by s is the simultaneous minus involution.
    for (k, l), value in terms.items():
        shifted = ((k + h1//2) % h1, (l + h2//2) % h2)
        assert terms[shifted] == value

    marginal1, marginal2 = defaultdict(int), defaultdict(int)
    for (k, l), value in terms.items():
        marginal1[k] += value
        marginal2[l] += value
    assert all(v == 0 for v in marginal1.values())
    assert all(v == 0 for v in marginal2.values())

    assert moment(terms, p, 0, 0) == 0
    assert moment(terms, p, 1, 0) == 0
    assert moment(terms, p, 0, 1) == 0
    assert moment(terms, p, 1, 1) == 2 % p
    # Check binomial(k,2) and binomial(l,2) pure Taylor terms.
    pure20 = sum((k*(k-1)//2)*v
                 for (k, l), v in terms.items()) % p
    pure02 = sum((l*(l-1)//2)*v
                 for (k, l), v in terms.items()) % p
    assert pure20 == pure02 == 0

    print("FULL_MARGINAL_KERNEL_8TERM_SIGN_PLUS_PASS",
          "p", p, "q1", q1, "q2", q2,
          "support", len(terms), flush=True)
    print("FULL_MARGINAL_KERNEL_BOTH_WHOLE_MARGINALS_ZERO_PASS",
          "p", p, "nonzero_rows", 0, "nonzero_cols", 0, flush=True)
    print("FULL_MARGINAL_KERNEL_M11_EQUALS_2_UNIT_PASS",
          "p", p, "M11", moment(terms, p, 1, 1), flush=True)

    # For ANY prior M11 in Fp, this algebraic perturbation can set
    # the coefficient to ANY new target without changing marginals.
    for old in range(p):
        for desired in range(p):
            scalar = ((desired - old) * pow(2, -1, p)) % p
            assert (old + 2*scalar) % p == desired
    print("FULL_MARGINAL_KERNEL_ARBITRARY_M11_TUNING_PASS",
          "p", p, "tested_pairs", p*p, flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, default=None)
    parser.add_argument("--q1", type=int, default=None)
    parser.add_argument("--q2", type=int, default=None)
    args = parser.parse_args()
    if any(v is not None for v in (args.p, args.q1, args.q2)):
        assert all(v is not None for v in (args.p, args.q1, args.q2))
        triples = ((args.p, args.q1, args.q2),)
    else:
        triples = DEFAULT_TRIPLES
    for triple in triples:
        verify(*triple)
    print("BOUNDARY_PURE_GROUP_RING_NO_FULL_EIGENLINE_OR_SHA_RESULT", flush=True)


if __name__ == "__main__":
    main()
