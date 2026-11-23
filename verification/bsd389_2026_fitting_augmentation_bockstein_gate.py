#!/usr/bin/env python3
"""Exact algebraic test of Fitt0 theta^2 versus augmentation Fitt2.

These are ABSTRACT Iwasawa modules; this script does not compute
Selmer groups, Gross points or BSD.
"""
from itertools import combinations
from math import gcd
from sympy import Matrix, Symbol

T = Symbol("T")

def verify(p, e):
    assert p >= 3 and e >= 0
    v = p**e
    A = Matrix([[v, T, 0, 0],
                [T, 0, 0, 0],
                [0, 0, v, T],
                [0, 0, T, 0]])
    assert A.det(method="berkowitz").expand() == T**4
    A0 = A.subs(T, 0)
    minors = [abs(int(A0.extract(i, j).det()))
              for i in combinations(range(4), 2)
              for j in combinations(range(4), 2)]
    fitt2 = 0
    for m in minors:
        fitt2 = gcd(fitt2, m)
    assert fitt2 == p**(2*e)
    N = Matrix([[0, -v, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, -v],
                [0, 0, 0, 0]])
    assert N*N == Matrix.zeros(4)
    beta = Matrix([[-v, 0], [0, -v]])
    assert beta.det() == fitt2
    assert A0.rank() == 2
    return f"p={p} e={e}: Fitt0=(T^4), theta=T^2, Fitt2_at_T0=({fitt2}), det_beta={fitt2}"

def local_p11():
    def ap(p):
        pts = 1 + sum(
            (y*y+y-x*x*x-x*x+2*x) % p == 0
            for x in range(p) for y in range(p))
        return p+1-pts
    assert ap(2) == -2 and ap(11) == -4
    assert pow((-43)%11,5,11) == 1
    assert pow((-43)%389,194,389) == 388
    assert pow((-4)%11,5,11) == 10
    print("P11_K_MINUS43_SPLIT_INERT_AND_FROBENIUS_DISCRIMINANT_PASS")

if __name__ == "__main__":
    local_p11()
    for p in (5,11):
        for e in (0,1,2,4):
            print("EXACT_ABSTRACT_COUNTEREXAMPLE_PASS",verify(p,e))
    print("BOUNDARY: NO GENUINE SELMER DATA AND NO BSD PROOF")
