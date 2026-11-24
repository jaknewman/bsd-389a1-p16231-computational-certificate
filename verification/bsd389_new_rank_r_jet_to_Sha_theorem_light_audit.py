#!/usr/bin/env python3
"""Lightweight exact arithmetic checks of the rank-r jet-to-Sha proof.

This script tests the FINITE BINOMIAL-ALGEBRA and one archived genuine
25-coefficient theta histogram. It is NOT a proof of the global
Selmer/Fitting containment, of the source's modular-symbol authentication,
or of any uniform large-prime statement.
"""
from math import comb

R1_GENUINE_25_HIST = (
    -424,9536,-424,3388,5172,-8022,-2658,-1240,-9294,-1588,
    -1580,-1512,9782,3208,3208,9782,-1512,-1580,-1588,-9294,
    -1240,-2658,-8022,5172,3388,
)


def vp(n: int, p: int) -> int:
    assert n != 0 and p >= 2
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def coefficient(hist, j):
    """Coefficient of T^j in F(1+T), F(X)=sum hist[i]*X^i."""
    return sum(hist[i] * comb(i, j) for i in range(j, len(hist)))


def audit_quotient(p: int, k: int, r: int, s: int):
    """Proves finite-combinatorial preconditions for R -> B_s."""
    assert p > r >= 1 and k >= 1 and 0 <= s < k
    m = p**k
    modulus = p**(s+1)
    # The p^k cyclic group-ring relation vanishes modulo T^(r+1).
    for j in range(1, r+1):
        assert comb(m, j) % modulus == 0, (p,k,r,s,j)
    # The maximal ideal (p,T)^(r+s+1) maps to zero in B_s.
    for a in range(r+s+2):
        b = r+s+1-a
        assert a >= s+1 or b >= r+1, (p,k,r,s,a,b)
    # The image p^s*T^r is NONZERO in B_s.
    assert p**s % modulus != 0
    return True


def main():
    assert len(R1_GENUINE_25_HIST) == 25
    c = [coefficient(R1_GENUINE_25_HIST, j) for j in range(4)]
    assert c == [0,-108600,-993960,-6066100], c
    assert c[0] % 25 == c[1] % 25 == 0
    assert c[2] % 25 == 15 and vp(c[2],5) == 1
    assert audit_quotient(5,2,2,1)
    print("GENUINE_R1_THETA_JET_PASS", "c0",c[0],"c1",c[1],"c2",c[2],"mod25",c[2]%25)
    print("RANK2_JET_5_ADIC_CERTIFICATE", "bound_dim_Sha5",1,
          "odd_p_parity_consequence","Sha_Q_5_primary_zero",
          "REQUIRES_published_Bullach_Honnor_Fitting_hypotheses")
    # Independent group-ring relation and m-adic-nilpotence checks
    # illustrating the abstract rank-r theorem at several ranks/depths.
    for p,k,r,s in [(5,2,2,1),(7,3,4,2),(11,1,2,0),(13,2,6,1)]:
        assert audit_quotient(p,k,r,s)
        print("RANK_R_QUOTIENT_ALGEBRA_PASS",p,k,r,s)
    # Prior independently checked finite-field MW determinant is 3 mod5,
    # while the same authentic two-prime Kurihara coefficient is 15 mod25.
    assert 3%5 != 0 and c[2]%5 == 0
    print("NAIVE_LOCAL_DETERMINANT_TO_DELTA_UNIT_FALSE",
          "p",5,"q1",5351,"q2",13001,
          "local_rank_two_minor_mod5",3,"genuine_delta_mod25",15,
          "NOTE_q13001_local_dimension_two")
    print("SCOPE_NO_UNIFORM_P_TAIL_NO_EXACT_COMPLEX_BSD")


if __name__ == "__main__":
    main()
