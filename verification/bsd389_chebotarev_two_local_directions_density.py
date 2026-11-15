#!/usr/bin/env python3
"""Exact finite-group Chebotarev density formulas for E389a1.

Arithmetic interpretation requires residual image GL2(Fp) and full
two-point Kummer translation image E[p]^2; this program proves only
the exact finite-group counts, not actual Kurihara nonvanishing.
"""
from fractions import Fraction as F


def densities(p):
    assert p >= 5
    g = p * (p-1) * (p-1) * (p+1)
    candidates = p*p  # trace 2, determinant 1
    scalar = 1
    nontrivial = p*p-1
    assert candidates == scalar + nontrivial
    admissible = F(candidates, g)
    good = F(nontrivial, g)
    bad = F(scalar, g)
    assert good == F(1, p*(p-1))
    conditional_one_dim = F(p*p-1, p*p)
    two_rows = F((p*p-1)*(p*p-p), p**4)
    assert two_rows == (1-F(1,p*p)) * (1-F(1,p))
    absolute_two_prime = good * good * two_rows
    return g, admissible, good, bad, conditional_one_dim, two_rows, absolute_two_prime


def exact_test(p):
    count = nontriv = 0
    for a in range(p):
        for b in range(p):
            for c in range(p):
                d = (2-a) % p
                if (a*d-b*c) % p != 1:
                    continue
                count += 1
                if (a,b,c,d) != (1,0,0,1):
                    nontriv += 1
    assert count == p*p and nontriv == p*p-1
    det_nonzero = sum(1 for a in range(p) for b in range(p)
                      for c in range(p) for d in range(p)
                      if (a*d-b*c) % p != 0)
    assert det_nonzero == (p*p-1)*(p*p-p)
    return count, nontriv, det_nonzero


for p in (5,7,107,16231):
    size, admiss, good, bad, cond, pair, abs_pair = densities(p)
    if p <= 7:
        count,u,rows = exact_test(p)
        print('EXHAUSTIVE_GL2_AND_MATRIX_DETERMINANT_PASS',p,count,u,rows)
    print('CHEBOTAREV_EXACT_DENSITY',p,
          'GL2_order',size,'admissible',str(admiss),
          'unipotent_nontrivial',str(good),
          'scalar',str(bad),'conditional_local_dim1',str(cond),
          'conditional_two_MW_rows_unit',str(pair),
          'absolute_ordered_two_prime_density',str(abs_pair))
print('SCOPE_KUMMER_LOCAL_DETECTION_ONLY_NOT_KURIHARA_NONVANISHING_OR_BSD')
