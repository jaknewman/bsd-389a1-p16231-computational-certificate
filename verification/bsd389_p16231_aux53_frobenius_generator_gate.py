#!/usr/bin/env python3
"""Exact finite certificate: 16231-Frobenius topologically generates
the pro-53 anticyclotomic quotient for K=Q(sqrt(-3)).

No Sage, external package or numerical p-adic logarithm.
A norm-one parameter u=pi/pi_bar=pi^2/16231 is evaluated mod53^2.
Its 54th power is 1+53*(8+16*omega), a NONZERO tangent in
the 1-dimensional local norm-one 53-adic Lie group. Thus its
pro-53 component is a topological generator, and every nontrivial
53-power-order ringclass character chi has chi(pbar_16231)!=1.
"""
P=16231
Q=53
MOD=Q*Q
assert P%3==1 and Q%3==2
assert 145*145-145*51+51*51==P

def mul(x,y,m):
    a,b=x;c,d=y
    return ((a*c-b*d)%m,(a*d+b*c-b*d)%m)

def power(x,n,m):
    z=(1,0)
    while n:
        if n&1:z=mul(z,x,m)
        x=mul(x,x,m)
        n//=2
    return z

pi=(145,51)
pi_bar=(94,-51)
assert mul(pi,pi_bar,MOD)==(P%MOD,0)
u=tuple(t*pow(P,-1,MOD)%MOD for t in mul(pi,pi,MOD))
assert u==(2306,269)
assert power(u,54,Q)==(1,0)
u54=power(u,54,MOD)
assert u54==(425,848)
a=(u54[0]-1)//Q
b=u54[1]//Q
assert (a,b)==(8,16)
assert (2*a-b)%Q==0       # norm-one infinitesimal
assert (a,b)!=(0,0)       # NONZERO 53-direction
assert power(u,54*Q,MOD)==(1,0)

# The rational 16231-isogeny would contradict Mazur (16231>163).
# Tate inertia has a p-element since v_389(Delta_min)=1,
# which, with irreducibility, forces SL2(F_p) by Dickson.
Delta=(-4**2*(-3)-8*(-4)**3-27+9*4*(-4))
assert Delta==389

def ap53():
    s=0
    for x in range(Q):
        d=(1+4*(x*x*x+x*x-2*x))%Q
        if d:
            s+=1 if pow(d,(Q-1)//2,Q)==1 else -1
    return -s
assert ap53()==-6
print("AUX53_K_INERT_AND_P16231_SPLIT_PASS")
print("AUX53_PI_NORM_P16231_PASS",pi,"NORM",P)
print("AUX53_E_AP53_ORDINARY_PASS",ap53())
print("AUX53_TARGET_P_DMIN389_VAL1_PASS",Delta)
print("AUX53_FROBENIUS_NORMONE_53SQUARE_PASS",u)
print("AUX53_FROBENIUS_POWER54_FIRST_LAYER_PASS",u54)
print("AUX53_FROBENIUS_PRO53_TANGENT_NONZERO_PASS",a,b)
print("AUX53_FROBENIUS_TOPOLOGICAL_GENERATOR_CERTIFIED_BY_LOCAL_GROUP")
print("BOUNDARY_CHARACTER_L_NONVANISHING_REQUIRES_CHIDA_HSIEH_THEOREM_D")
