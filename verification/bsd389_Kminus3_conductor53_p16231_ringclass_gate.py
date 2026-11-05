#!/usr/bin/env python3
"""Pure Python certificate: K=Q(sqrt(-3)), ring class conductor 53, p=16231.

Checks finite field arithmetic, ring class quotient, generator order 18,
class of a prime over p, and ordinary Frobenius a_p(E)=128 for 389a1.

No Sage, no analytic L-values, no theta derivative, no Sha conclusion.
"""
from math import gcd

F = 53
P = 16231

def mul(x, y):
    # omega^2+omega+1=0 in F_(53^2)
    a, b = x
    c, d = y
    return ((a*c-b*d) % F, (a*d+b*c-b*d) % F)

def power(x, n):
    assert n >= 0
    z = (1, 0)
    while n:
        if n & 1:
            z = mul(z, x)
        x = mul(x, x)
        n >>= 1
    return z

def norm(a, b):
    return a*a - a*b + b*b

# Since 53 == 2 mod 3, t^2+t+1 has no F53 root.
assert F % 3 == 2
# Units mu_6 of Z[omega] and rational scalars produce a group of size 156.
omega = (0, 1)
minus1 = (F-1, 0)
units = [(1,0), minus1, omega, mul(minus1, omega),
         power(omega, 2), mul(minus1, power(omega,2))]
H = {mul((s, 0), u) for s in range(1, F) for u in units}
assert len(H) == 156
assert (F*F-1)//len(H) == 18
print("RINGCLASS_MINUS3_CONDUCTOR53_ORDER_PASS", 18, flush=True)

# g=5+3 omega has norm 19 and generates the cyclic class group C18.
g = (5, 3)
assert norm(*g) == 19
assert power(g, 18) in H
assert power(g, 9) not in H
assert power(g, 6) not in H
print("RINGCLASS_NORM19_GENERATOR_ORDER18_PASS", flush=True)

# p splits, represented by pi=145+51 omega of norm p.
pi = (145, 51)
assert norm(*pi) == P
assert P % 3 == 1 and 389 % 3 == 2
print("K_MINUS3_389_INERT_P16231_SPLIT_PASS", flush=True)

# Explicit congruence pi == 25*g^4 modulo conductor 53,
# hence the ring class of pbar is [g]^(+/-4), of exact order 9.
assert (pi[0] % F, pi[1] % F) == mul((25, 0), power(g, 4))
assert power(g, 4) not in H
assert power(g, 12) not in H
assert power(g, 36) in H
assert 18 // gcd(18, 4) == 9
print("RINGCLASS_PI_EQUALS_25_G4_MOD53_PASS", flush=True)
print("RINGCLASS_P16231_FROBENIUS_ORDER9_PASS", flush=True)

# For primitive psi of order 18, tau acts by inversion and
# chi=psi/psi^tau=psi^2 has order 9.
# chi(pbar)=zeta18^(+/-8), a primitive 9th root, so !=1.
assert 18 // gcd(18, 8) == 9
print("CASTELLA_HSIEH_CHI_PBAR_NONTRIVIAL_PASS", flush=True)

# E389a1: y^2+y=x^3+x^2-2x. Count points by quadratic discriminant.
def frobenius_trace(p):
    total = 0
    for x in range(p):
        delta = (1 + 4*(x*x*x+x*x-2*x)) % p
        if delta:
            chi = pow(delta, (p-1)//2, p)
            assert chi in (1, p-1)
            total += 1 if chi == 1 else -1
    return -total

ap = frobenius_trace(P)
assert ap == 128 and ap % P != 0
assert P + 1 - ap == 16104
print("E389A1_AP16231_ORDINARY_PASS", ap, flush=True)

print("RINGCLASS_53_P16231_ARITHMETIC_CERTIFICATE_PASS", flush=True)
print("BOUNDARY_L_E_MINUS3_AND_L_E_OVER_K_CHI_NONVANISHING_NOT_PROVED", flush=True)
print("BOUNDARY_ANTICYCLOTOMIC_THETA_ORDER2_NOT_PROVED", flush=True)
print("BOUNDARY_SHA_P16231_NOT_PROVED", flush=True)
