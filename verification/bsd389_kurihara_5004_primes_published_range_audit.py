#!/usr/bin/env python3
"""389a1 below p<48859: bounded-range source audit and exact prime inventory.

EXTERNAL MATHEMATICAL INPUTS, NOT PROVED OR RECOMPUTED HERE:
  Stein--Wuthrich 2013 Theorem 12.3, 5005 ordinary primes p<48859
  except p16231; separately archived user Sage p107 Sha upper bound;
  Kim Theorem 1.8 and Castella--Sano 2026 Theorem B.

DERIVED, NOT EXPLICITLY CALCULATED: two-prime mod-p Kurihara unit exists
for each of 5004 good primes p>=5 in the covered finite range.
All arithmetic counts and the finite p-torsion annihilator are exact.
"""
from math import prod, isqrt

B=48859
SUPER=(107,599,1049,2957,6661,8263,9397,9551,14633,15101,
       28591,30671,30869,31799,34781,36263,45161)
BAD=389
ORDINARY_EXC=16231

sieve=bytearray(b'\x01')*B
sieve[:2]=b'\x00\x00'
for k in range(2,isqrt(B-1)+1):
    if sieve[k]:
        sieve[k*k:B:k]=b'\x00'*(((B-1-k*k)//k)+1)
P=[k for k in range(5,B) if sieve[k]]
S=set(P)
assert len(P)==5022
assert len(SUPER)==17 and all(q in S for q in SUPER)
assert BAD in S and ORDINARY_EXC in S

EXCLUDED=set(SUPER)|{BAD,ORDINARY_EXC}
assert len(EXCLUDED)==19
ORDINARY_CERT=S-EXCLUDED
assert len(ORDINARY_CERT)==5003

# 107: the existing independently archived Sage proof-mode p-primary bound.
CERT=ORDINARY_CERT|{107}
assert len(CERT)==5004
GOOD=S-{BAD}
assert len(GOOD)==5021
LEFT=GOOD-CERT
assert LEFT==({ORDINARY_EXC}|(set(SUPER)-{107}))
assert len(LEFT)==17
ALL_LOW_NONCERT=S-CERT
assert len(ALL_LOW_NONCERT)==18 and BAD in ALL_LOW_NONCERT

D=prod(sorted(ALL_LOW_NONCERT))
assert D==627863883549010692613176172370737913398606747759161305426648442740476277
print('STEIN_WUTHRICH_THEOREM_INPUT__NOT_RECOMPUTED ordinary_covered_5plus',len(ORDINARY_CERT))
print('LOW_RANGE_PRIME_COUNTS_PASS','all_primes_p_ge5',len(P),'good_primes',len(GOOD))
print('KIM_CASTELLA_SANO_EXISTENCE_COROLLARY',
      'good_p_ge5_with_two_prime_unit_existence',len(CERT))
print('GOOD_UNCOVERED_PRIMES_BELOW_48859',sorted(LEFT))
print('BOUNDED_RANGE_SHA_P_TORSION_ANNIHILATOR',D)
print('BOUNDARY: NOT a certificate for p>=48859; NOT an annihilator of exceptional p-power torsion')
print('BOUNDARY: NO UNIFORM ALL-LARGE-p BOUND AND NO COMPLEX BSD')
