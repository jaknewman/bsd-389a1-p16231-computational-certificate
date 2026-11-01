#!/usr/bin/env python3
"""Short independent local check for p=5, q1=41, q2=61.

No Sage, eclib, 2400-symbol replay, or access to a Manin table.
Counts E(F_q) independently for E:y^2+y=x^3+x^2-2x;
checks a_41=-3,a_61=-8 and admissibility modulo 5;
computes CRT root logs d1,d2 and the low Taylor coefficients
of the exact Hecke marginal operator a_q-X^d-X^{-d}.

This checks input arithmetic and the *algebraic predicted zeros*
M00,M10,M20,M01,M02 for every integral normalized modular
symbol satisfying the usual Hecke relation. It DOES NOT recompute
the actual mixed coefficient M11=4, which was independently
computed on the user's Sage Ubuntu server.
"""


def ap(q):
    assert q > 2
    points = 1  # point at infinity
    for x in range(q):
        rhs = (x*x*x + x*x - 2*x) % q
        discriminant = (1 + 4*rhs) % q
        if discriminant == 0:
            points += 1
        elif pow(discriminant, (q-1)//2, q) == 1:
            points += 2
    return q+1-points


def root_log(g, x, q):
    powers = [pow(g,k,q) for k in range(q-1)]
    assert len(set(powers)) == q-1
    return powers.index(x % q)


def binomial2(k):
    return k*(k-1)//2


def factor_jet(a, d, p):
    """Coefficients 1,T,T^2 in a-(1+T)^d-(1+T)^(-d)."""
    # Binomial identity valid for negative exponent as formal series.
    return (
        (a-2)%p,
        (-d+d)%p,
        (-binomial2(d)-binomial2(-d))%p
    )


def main():
    p,q1,q2,g1,g2=5,41,61,6,2
    a1,a2=ap(q1),ap(q2)
    assert (a1,a2)==(-3,-8)
    assert q1%p==q2%p==1
    assert (a1-(q1+1))%p==0
    assert (a2-(q2+1))%p==0
    print("P5_HECKE_INDEPENDENT_POINTCOUNTS_PASS",
          "a41",a1,"a61",a2,flush=True)

    d1=root_log(g1,q2,q1)
    d2=root_log(g2,q1,q2)
    assert (d1,d2)==(34,54)
    first=factor_jet(a2,d1,p)
    second=factor_jet(a1,d2,p)
    assert first==second==(0,0,4)
    print("P5_HECKE_MARGINAL_GROUP_RING_FACTOR_JETS_PASS",
          "log61_mod41",d1,"log41_mod61",d2,
          "first",first,"second",second,flush=True)

    # At prime q_i: theta_q_i(1)=(a_q_i-2)*m_plus(0).
    # It is zero mod p for ANY p-integral value of m_plus(0)
    # because q_i are p-admissible. Therefore each partial
    # marginal contains I_i^3; no numerical symbol is needed.
    for m0 in range(p):
        theta1_const=((a1-2)*m0)%p
        theta2_const=((a2-2)*m0)%p
        assert theta1_const==theta2_const==0
        # Let theta_i=theta_const+t_i*T+u_i*T^2+...
        # for arbitrary t_i,u_i. Product with (0,0,4)
        # has zero coefficients through degree 2.
        for t in range(p):
            for u in range(p):
                for jet, constant in ((first,theta1_const),
                                      (second,theta2_const)):
                    c0,c1,c2=jet
                    product0=c0*constant%p
                    product1=(c0*t+c1*constant)%p
                    product2=(c0*u+c1*t+c2*constant)%p
                    assert (product0,product1,product2)==(0,0,0)
    print("P5_HECKE_PURE_QUADRATIC_MOMENTS_FORCED_ZERO_PASS",
          "M00",0,"M10",0,"M20",0,"M01",0,"M02",0,flush=True)
    print("P5_MIXED_M11_HISTORICAL_USER_RUN",4,
          "NOT_RECOMPUTED_BY_THIS_LOCAL_AUDIT",flush=True)
    print("BOUNDARY_UNIVERSAL_HECKE_JET_STRUCTURE_NOT_UNIFORM_M11_NONVANISHING",
          flush=True)


if __name__=="__main__":
    main()
