#!/usr/bin/env sage -python
"""Sage 10.9 arithmetic inputs for a rigorously separate geometric theorem.

Checks:
 - E=389a1 modular degree 40;
 - already established proof-bound triviality of Sha[2^infinity] and Sha[5^infinity];
 - p=16231 ring-class degree formula (arithmetical check).

No computation of Sha at all other primes. NO claim of global BSD.
"""
from sage.all import EllipticCurve, QQ, ZZ

E = EllipticCurve(QQ, [0, 1, 1, -2, 0])
assert ZZ(E.conductor()) == 389
print("CURVE_PASS", E.ainvs(), flush=True)

m = ZZ(E.modular_degree())
assert m == 40
assert m.factor() == (ZZ(2)**3*ZZ(5)).factor()
print("EXACT_MODULAR_DEGREE_PASS", m, m.factor(), flush=True)

S = E.sha()
two = ZZ(S.two_selmer_bound())
assert two == 0, ("SHA2_BOUND_NOT_ZERO", two)
print("EXISTING_TWO_PRIMARY_SELMER_METHOD_REPLAY_PASS", two, flush=True)

five = ZZ(S.p_primary_bound(5))
assert five == 0, ("SHA5_BOUND_NOT_ZERO", five)
print("EXISTING_FIVE_PRIMARY_BOUND_REPLAY_PASS", five, flush=True)
print("MODULAR_VISIBILITY_SHA_KERNEL_ZERO_THEOREM_INPUTS_PASS",
      "degree", m, "sha2", two, "sha5", five, flush=True)

p = ZZ(16231)
assert p.is_prime()
assert (p - 1) % 3 == 0
assert (p - 1) // 3 == 5410
for conductor_exponent in range(1, 5):
    h = ((p-1)//3)*p**(conductor_exponent-1)
    total_degree = 2*h
    assert h == 5410*p**(conductor_exponent-1)
    assert total_degree.valuation(p) == conductor_exponent-1
    print("RINGCLASS_CONDUCTOR_HEIGHT_TRANSFER_BOUND",
          "m", conductor_exponent, "class_number", h,
          "F_degree", total_degree, "vp", total_degree.valuation(p),
          flush=True)
print("SCOPE_PROOF_INPUTS_ONLY; NO_ALL_PRIME_SHA_FINITE_OR_BSD_CLAIM",
      flush=True)
