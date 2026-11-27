#!/usr/bin/env python3
"""Determinantal and Bockstein exact algebra audit for rank-two Selmer models.

Model only: the finite group (Z/p^e)^2 is paired and its Fitting determinant
has v_p = 2e. In F_p[Y]/(Y^p), multiplication by Y^2 is not invertible.
Neither algebraic model implies a claim about the actual Sha of 389a1.
"""
for p in (5, 7, 11):
    for e in (0, 1, 2, 3):
        n = p**e
        det = n*n
        t = det
        valuation = 0
        while t % p == 0:
            valuation += 1
            t //= p
        assert t == 1 and valuation == 2*e
        dim_sha_p = 0 if e == 0 else 2
        # For p>2, the map Y^i -> Y^(i+2) is nonzero iff i<=p-3.
        rank = sum(i + 2 < p for i in range(p))
        assert rank == p-2 and p-rank == 2
        print("PAIRED_SELMER_MODEL", "p", p, "e", e,
              "finite_order", det, "length", valuation,
              "dim_p_torsion", dim_sha_p,
              "Euler_second_jet_rank", rank,
              "Euler_second_jet_kernel", p-rank,
              "unimodular", det % p != 0)
print("SECOND_EULER_JET_NONINVERTIBILITY_PASS")
print("SELFMER_DETERMINANT_PARITY_PASS")
print("BOUNDARY: formal countermodel, not Sha=0 proof")
