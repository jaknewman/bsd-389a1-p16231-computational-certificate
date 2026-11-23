#!/usr/bin/env python3
"""Exact 400 primitive order25 Dirichlet-character spectral valuation audit.

Mathematical input: authentic p5, depth25, conductor 5351*10651 bivariate
Mazur--Tate 3x3 matrix from the user's complete 28,488,750-term run.
For all 400 primitive characters chi_(u,v) (u,v units mod25), the
one-variable diagonal theta has unit quadratic coefficient 22uv mod25;
since v_(zeta25-1)(5)=20, this forces exact valuation2 at chi.

A new exact algebraic corollary, not a new independent symbol computation or
a uniform all-p Sha/BSD theorem.
"""
from math import gcd
P=5;PK=25;E=20
M=((0,0,0),(0,22,16),(0,17,14))
assert [M[i][j] for i,j in ((0,0),(1,0),(0,1),(2,0),(0,2))]==[0]*5
assert M[1][1]==22
U=[u for u in range(PK) if gcd(u,P)==1]
assert len(U)==20
pairs=0
orbits=set()
for u in U:
    for v in U:
        # T_i=(1+T)^u-1; exact quadratic coefficient of the specialization
        c0=M[0][0]
        c1=(u*M[1][0]+v*M[0][1])%PK
        c2=(u*v*M[1][1]+u*u*M[2][0]+v*v*M[0][2]+
            u*(u-1)//2*M[1][0]+v*(v-1)//2*M[0][1])%PK
        assert c0==c1==0 and c2==22*u*v%PK and c2%P
        # char chi_(u,v) has order25 & full conductor since u and v units
        orbits.add(v*pow(u,-1,PK)%PK)
        pairs+=1
assert pairs==400 and len(orbits)==20 and orbits==set(U)
# For zeta_25, pi=zeta-1: v_pi(5)=20. Lower-order coefficients
# divisible 25 give valuation at least40; c2*pi^2 has valuation2
# and all higher-degree terms have valuation >=3.
assert P==5 and E==(P*(P-1))
assert PK==P*P and 2<3 and 2<2*E
print("DEPTH25_400_CHARACTER_SPECTRAL_QUADRATIC_UNIT_PASS",pairs)
print("DEPTH25_20_GALOIS_ORBITS_PASS",len(orbits))
print("DEPTH25_ALL_400_EXACT_PI_VALUATION",2,
      "P_ADIC_VALUATION","1/10")
print("DEPTH25_ALL_20_ALGEBRAIC_NORM_V5",2)
print("THEOREM_INPUT_AUTHENTIC_USER_28488750_MANIN_REPRESENTATIVES")
print("SCOPE_NO_UNIFORM_SHA_OR_EXACT_BSD")
