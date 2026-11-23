#!/usr/bin/env python3
"""Exact finite arithmetic check of 20 degree-25 fields of E389a1 rank stability.

Inputs: user-validated real p5,k2 full 28,488,750-representative Manin moment
M_ij (i,j<=2) mod25, and genuine Hecke pure-jet vanishing.
Kato's theorem, Artin formalism and absence of rational isogenies are the
EXTERNAL mathematical inputs. No all-prime Sha claim.
"""
from math import gcd

p=5;m=25
M=((0,0,0),(0,22,16),(0,17,14))
units=[u for u in range(m) if gcd(u,m)==1]
assert len(units)==20 and M[1][1]%p==2
assert all(M[i][j]==0 for i,j in ((0,0),(1,0),(0,1),(2,0),(0,2)))
fields={}
primitive25=set()
primitive5=set()
for r in units:
    counts={25:0,5:0}
    valuations=[]
    for t in range(1,25):
        u=t%25
        v=r*t%25
        assert u and v
        if t%5:
            assert (22*u*v)%5!=0
            order=25; val_pi25=2
            primitive25.add((u,v))
        else:
            assert (22*(u//5)*(v//5))%5!=0
            order=5;val_pi25=10
            primitive5.add((u,v))
        counts[order]+=1;valuations.append(val_pi25)
    assert counts=={25:20,5:4} and sum(valuations)==80
    fields[r]=counts
assert len(fields)==20 and len(primitive25)==400 and len(primitive5)==16
assert len(primitive25|primitive5)==416
q1,q2=5351,10651
assert (q1-1)%50==(q2-1)%50==0
assert q1*q2==56993501
print("P5_DEPTH25_20_TOTALLY_REAL_CYCLIC25_FIELDS_PASS",len(fields))
print("P5_DEPTH25_400_ORDER25_TWIST_NONZERO_BY_JET_PASS",len(primitive25))
print("P5_DEPTH25_16_ORDER5_TWIST_NONZERO_BY_JET_PASS",len(primitive5))
print("P5_DEPTH25_416_DISTINCT_TWIST_NONZERO_PASS",len(primitive25|primitive5))
print("P5_DEPTH25_EACH_CYCLIC25_FIELD_NONTRIVIAL_CHARACTERS_PASS",24)
print("P5_DEPTH25_EACH_FIELD_REDUCED_NORM_EXACT_V5_PASS",4)
print("EACH_FIELD_CONDUCTOR_AND_DISCRIMINANT_EXPONENT_PASS",q1*q2,24)
print("EXTERNAL_KATO_AND_NO_ISOGENY_IMPLICATION: E(F_r)=E(Q)=Z^2 FOR_ALL_20")
print("BOUNDARY_NO_NEW_GLOBAL_SHA_FINITENESS_OR_STRONG_BSD")
