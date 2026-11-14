#!/usr/bin/env python3
"""Exact GL2(Z/p^2) lift counts for p^2-admissible Kurihara auxiliaries.

Under surjective rho_(E,p^2) the rational-prime densities come by Chebotarev.
No Selmer, Kurihara-sum, or BSD conclusions are computed by this script.
"""
from fractions import Fraction


def gl2_order(p):
    return p * (p - 1)**2 * (p + 1)


def counts(p):
    g = gl2_order(p)
    regular_base = p*p - 1
    scalar_base = 1
    lifts_regular = p*p
    lifts_scalar = p*p*p
    total_regular = regular_base * lifts_regular
    total_scalar = scalar_base * lifts_scalar
    denominator = g * p**4
    return {
        'p': p, 'modp_regular': regular_base,
        'modp_scalar': scalar_base,
        'lifts_per_regular': lifts_regular,
        'lifts_per_scalar': lifts_scalar,
        'absolute_p2_regular_density': Fraction(total_regular, denominator),
        'absolute_p2_scalar_density': Fraction(total_scalar, denominator),
        'absolute_p2_any_density': Fraction(total_regular+total_scalar, denominator),
        'regular_given_p2_admissible': Fraction(total_regular, total_regular+total_scalar),
        'absolute_vp1_and_regular_density': Fraction(1, p*p),
    }


def exhaustive_lift_count(p):
    """Independently enumerate all p^2 lifts above mod-p trace=2, det=1."""
    candidates = []
    for a in range(p):
        for b in range(p):
            for c in range(p):
                d = (2-a) % p
                if (a*d-b*c) % p == 1:
                    candidates.append((a,b,c,d))
    assert len(candidates) == p*p
    nr_reg = nr_scalar = 0
    for a,b,c,d in candidates:
        k_trace = ((a+d-2)//p) % p
        k_det = ((a*d-b*c-1)//p) % p
        scalar = (a,b,c,d) == (1,0,0,1)
        cnt = 0
        for alpha in range(p):
            for beta in range(p):
                for gamma in range(p):
                    for delta in range(p):
                        if (k_trace+alpha+delta) % p:
                            continue
                        if (k_det+d*alpha+a*delta-c*beta-b*gamma) % p:
                            continue
                        cnt += 1
        assert cnt == (p**3 if scalar else p**2), (p,(a,b,c,d),cnt)
        if scalar:
            nr_scalar += cnt
        else:
            nr_reg += cnt
    assert nr_reg==(p*p-1)*p*p and nr_scalar==p**3
    return nr_reg, nr_scalar


for p in (5,7,11,107,16231):
    c=counts(p)
    assert c['absolute_p2_regular_density'] == Fraction(1, p**3*(p-1))
    assert c['regular_given_p2_admissible'] == Fraction(p*p-1, p*p+p-1)
    if p in (5,7):
        r,s=exhaustive_lift_count(p)
        assert r==(p*p-1)*p*p and s==p**3
        print('EXHAUSTIVE_MOD_P2_FROBENIUS_LIFTS_PASS',p,'regular_lifts',r,'scalar_lifts',s)
    print('EXACT_P2_AUXILIARY_CHEBOTAREV_FORMULA',p,
          'regular_absolute',c['absolute_p2_regular_density'],
          'scalar_absolute',c['absolute_p2_scalar_density'],
          'all_absolute',c['absolute_p2_any_density'],
          'regular_conditional',c['regular_given_p2_admissible'],
          'regular_vp_point_count_exactly_one',c['absolute_vp1_and_regular_density'])
print('SCOPE: FINITE_MATRIX_COUNT_ONLY; NO SHA OR BSD CLAIM')
