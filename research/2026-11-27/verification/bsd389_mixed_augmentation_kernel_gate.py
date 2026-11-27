#!/usr/bin/env python3
"""Monomial audit of the fully mixed augmentation kernel in Fp[Cp^r].

Independent of BSD: all immediate projections set a variable Ti=0.
Their common kernel consists precisely of monomials with all Ti present.
"""
from itertools import product

for p, r in [(5, 2), (5, 4), (7, 4)]:
    basis = list(product(range(p), repeat=r))
    assert len(basis) == p**r
    # Kernels of the r projection maps, represented by basis indices.
    kernels = [{m for m in basis if m[i] > 0} for i in range(r)]
    mixed = set.intersection(*kernels)
    monomial_ideal = {m for m in basis if all(e >= 1 for e in m)}
    assert mixed == monomial_ideal
    assert len(mixed) == (p - 1)**r
    # IK is the span of fully mixed monomials with at least one exponent >1.
    IK = {m for m in mixed if sum(m) > r}
    assert mixed - IK == {(1,) * r}
    # Changing only the completely mixed generator leaves every pi_i unchanged,
    # but changes precisely the lowest fully mixed coefficient.
    delta = (1,) * r
    for i in range(r):
        assert delta in kernels[i]
    for c in range(p):
        initial = {}
        changed = {delta: c} if c else {}
        for i in range(r):
            project = lambda f: {m: a for m,a in f.items() if m[i] == 0}
            assert project(initial) == project(changed)
        assert changed.get(delta, 0) == c
    print('MIXED_KERNEL_EXACT_PASS', 'p', p, 'r', r,
          'ambient_dimension', len(basis), 'intersection_dimension', len(mixed),
          'lowest_quotient_dimension', len(mixed - IK))
print('NORM_PROJECTIONS_DO_NOT_DETERMINE_FULLY_MIXED_KURIHARA_COEFFICIENT_PASS')
print('BOUNDARY: finite group ring proof, not a rank-two Selmer contraction')
