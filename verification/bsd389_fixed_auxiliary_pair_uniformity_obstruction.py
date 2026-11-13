#!/usr/bin/env python3
"""Proof-grade independent arithmetic for fixed-auxiliary p-admissibility.

No Sage required. No Kurihara sums, Selmer groups or BSD claims.
"""
from math import gcd, isqrt

PAIRS = [
    (41, 61, 5, (-3, -8)),
    (113, 673, 7, (9, 2)),
    (369793, 383917, 107, (2, -854)),
]


def is_prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))


def trace_aq(q):
    assert q != 389 and q % 2 and is_prime(q)
    total = 0
    for x in range(q):
        disc = (4*x*x*x + 4*x*x - 8*x + 1) % q
        if disc == 0:
            continue
        legendre = pow(disc, (q - 1) // 2, q)
        assert legendre in (1, q - 1)
        total += 1 if legendre == 1 else -1
    return -total


def prime_divisors(n):
    n = abs(n)
    ans = []
    for k in range(2, isqrt(n) + 1):
        if n % k == 0:
            ans.append(k)
            while n % k == 0:
                n //= k
    if n > 1:
        ans.append(n)
    return ans


for q1, q2, p, traces in PAIRS:
    a1, a2 = trace_aq(q1), trace_aq(q2)
    assert (a1, a2) == traces
    A1, A2 = gcd(q1-1, a1-2), gcd(q2-1, a2-2)
    D = gcd(A1, A2)
    assert p in prime_divisors(D)
    assert all((q-1) % p == (a-2) % p == 0
               for q, a in ((q1, a1), (q2, a2)))
    print("FIXED_PAIR_EXACT_ADMISSIBILITY_PASS",
          "q", (q1,q2), "a_q", (a1,a2),
          "A_q", (A1,A2), "D_pair", D,
          "eligible_prime_divisors", prime_divisors(D))
print("FINITELY_MANY_P_PER_FIXED_PAIR_PROVED_BY_GCD_FORMULA")
print("NO_UNIFORM_SHA_OR_BSD_CLAIM")
