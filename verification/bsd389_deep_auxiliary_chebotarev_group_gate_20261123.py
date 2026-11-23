#!/usr/bin/env python3
"""Independent finite-group audit: arbitrary-depth Kurihara auxiliary availability.

Group counts only. Theorems of Serre and Chebotarev are cited externally;
no two-prime Kurihara derivative is asserted nonzero.
"""
from math import gcd

assert 112**3 % 389 == 249
print("NON_CM_RATIONAL_NONINTEGRAL_J_INVARIANT_PASS", f"{112**3}/389")

def count_centralizer_brute(p, k):
    m = p**k
    count = 0
    for a in range(m):
        for b in range(m):
            for c in range(m):
                for d in range(m):
                    # AU = UA, U=[[1,1],[0,1]], iff c=0,a=d.
                    if c % m or (a-d) % m:
                        continue
                    if gcd((a*d-b*c) % m, p) == 1:
                        count += 1
    return count

for p,k in ((3,1),(3,2),(5,1),(5,2)):
    G = p**(4*(k-1))*(p*p-1)*(p*p-p)
    C = p**(2*k-1)*(p-1)
    assert count_centralizer_brute(p,k) == C
    assert G % C == 0
    print("EXACT_UNIPOTENT_CENTRALIZER_BRUTE_PASS",p,k,"CENT",C,"CLASS",G//C)

for p in (11,107,599):
    for k in (1,2,3):
        G=p**(4*(k-1))*(p*p-1)*(p*p-p)
        C=p**(2*k-1)*(p-1)
        assert G % C == 0 and G//C==p**(2*k-2)*(p*p-1)
print("ALL_P_K_EXACT_DENSITY_ALGEBRA_PASS")
print("BOUNDARY_EXTERNAL_SERRE_CHEBOTAREV__NO_KURIHARA_NONVANISHING")
