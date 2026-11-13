#!/usr/bin/env python3
"""Exact small-group/algebra audit for ring-class p-power-degree transfer.

Does NOT compute Sha, ring class fields, Heegner classes or verify Kim's theorem.
"""
from math import gcd

p = 16231
h_p = 5410
h_p2 = 87809710
extension_degree = 2 * h_p2
assert h_p2 == h_p * p
assert gcd(h_p, p) == 1
assert extension_degree == 175619420
assert extension_degree % p == 0 and extension_degree % (p * p) != 0
print('RINGCLASS_P16231_EXACT_DEGREE_PASS', 'h_p', h_p, 'h_p2', h_p2,
      'F_over_Q', extension_degree, 'v_p', 1)

# Model G = (C25 x C12) semidirect C2, conjugation acts by inversion.
# Explicitly check the Hall subgroup H = C12 semidirect C2.
p_toy, d_prime_to_p = 5, 12
m_p = 25
G = [(a, b, e) for a in range(m_p)
     for b in range(d_prime_to_p) for e in range(2)]
H = {(0, b, e) for b in range(d_prime_to_p) for e in range(2)}

def mul(g, h):
    a, b, e = g
    c, d, f = h
    s = (-1) ** e
    return ((a + s * c) % m_p, (b + s * d) % d_prime_to_p, e ^ f)

assert (0, 0, 0) in H
assert all(mul(g, h) in H for g in H for h in H)
assert len(G) == 600 and len(H) == 24 and len(G) // len(H) == 25
cosets = {frozenset(mul(g, h) for h in H) for g in G}
assert len(cosets) == 25 and len(set().union(*cosets)) == len(G)
print('DIHEDRAL_HALL_PPRIME_SUBGROUP_PASS', 'G_order', len(G),
      'H_order', len(H), 'index', len(cosets))
print('TRANSFER_BOUND_CONDITIONAL_ON_SPLITTING: kernel_restriction_is_p_torsion_for_specific_F')
print('SCOPE_NO_SHA_COMPUTATION_NO_BSD_CLAIM')
