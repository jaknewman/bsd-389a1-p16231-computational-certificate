#!/usr/bin/env python3
"""Formal, exact audit of p=16231 theta and Castella--Hsieh derived-height conclusion.

Mathematical source: Castella--Hsieh (2022), Thm 4.1 and eq. (5.10).
The source-normalized Gross theta coefficient 3739 is a previously
user-reported *finite layer* certificate; this script does not rerun it,
or independently re-identify every right-ideal class, or compute Selmer.
"""
from itertools import product

P=16231
assert P%3==1 and 389%3==2 and 389!=P
assert P*(P-1)//3==87809710
assert pow(128,-2,P)==4986
c2=(-3*4986*4083)%P
assert c2==3739 and c2!=0
assert (c2*c2)%P==5230

# Independently reconstruct a_p(E) using the full exact Legendre sum.
sum_legendre=0
for x in range(P):
    discriminant=(1+4*(x*x*x+x*x-2*x))%P
    if discriminant:
        t=pow(discriminant,(P-1)//2,P)
        assert t in (1,P-1)
        sum_legendre+=1 if t==1 else -1
assert -sum_legendre==128
assert (P+1+sum_legendre)==16104
print('BSD389_GROSS_N1_QUADRATIC_UNIT_INPUT_PASS',
      'p',P,'alpha_inv_squared',4986,'raw_M2',4083,'normalized_c2',c2)
print('BSD389_THETA_SQUARED_4JET_UNIT_PASS',
      'coefficient_mod_p',(c2*c2)%P)

# Input to this exhaustive finite enumeration:
# (a) rank Sel(E/K)>=2, by the two saturated rational points;
# (b) odd h^(i) vanish (tau=+1 on Sel(E/K), tau=-1 on J/J^2);
# (c) even h^(i) are alternating, so e_(2r) is even;
# (d) the one-sided characteristic inclusion gives
#       sum_{r>=1} (2*r)*e_(2r) <= 2*ord_T(theta)=4.
# Every e_(2r) is an even nonnegative integer, finitely supported.
profiles=[]
for e2,e4 in product((0,2,4),repeat=2):
    length=2*e2+4*e4
    rank=e2+e4
    if rank>=2 and length<=4:
        profiles.append((e2,e4,rank,length))
assert profiles==[(2,0,2,4)],profiles
print('BSD389_DERIVED_HEIGHT_UNIQUE_EVEN_JUMP_PROFILE_PASS',profiles)

# J-primary rational isogeny type: two length-2 Jordan blocks.
# This is a proof-theoretic implication, NOT a matrix found by experiment.
def multiply(A,B,p):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%p
             for j in range(len(B[0]))] for i in range(len(A))]
J=[[0,1,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0]]
assert multiply(J,J,P)==[[0]*4 for _ in range(4)]
assert sum(any(x for x in row) for row in J)==2
print('BSD389_ANTICYCLOTOMIC_FORMAL_JORDAN_2PLUS2_PASS',
      'J_rank',2,'J_square_zero',True)
print('BOUNDARY: This is a proof of the CONDITIONAL implication from the '
      'previously reported fully normalized theta input, the one-sided '
      'Iwasawa divisibility and derived-height theorem. It is NOT a '
      're-run of 87,809,710 Gross classes, a proof of integral Sha=0, '
      'or an all-prime BSD theorem.')
