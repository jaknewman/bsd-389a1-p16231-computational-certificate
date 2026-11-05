#!/usr/bin/env python3
"""Exact first anti-cyclotomic p-layer generator at K=Q(sqrt(-3)), p=16231.

Construct a character Pic(O_(p^2)) -> F_p from the split local CRT ratio:
    ell_p(a+b*omega) =
       ((( (a+b*r0)/(a+b*r1) mod p^2 )^(p-1) - 1) mod p^2)/p mod p.
Here r0,r1 are the two Hensel lifts of omega^2+omega+1 to mod p^2.

It kills rational scalars and all six O_K units; K has class number 1,
so it factors through the ring class group, whose order is p(p-1)/3.
The norm-19 element g=5+3omega has ell_p(g)=5415, nonzero.
Thus [g]^((p-1)/3) generates the canonical kernel
Pic(O_(p^2)) -> Pic(O_p), a cyclic group of order p.

This is exact arithmetic on *ring classes*, not Gross-point evaluations,
not an embedding into the Brandt algebra and not the CH theta derivative.
"""
from math import gcd

P=16231
MOD=P*P
OMEGA_ROOTS_P=(6044,10186)

def omega_roots_mod_p2():
    ans=[]
    for r in OMEGA_ROOTS_P:
        assert (r*r+r+1)%P==0
        derivative=(2*r+1)%P
        assert derivative
        k=(-((r*r+r+1)//P)*pow(derivative,-1,P))%P
        x=(r+k*P)%MOD
        assert (x*x+x+1)%MOD==0
        ans.append(x)
    assert len(set(ans))==2
    assert (sum(ans)+1)%MOD==0 and (ans[0]*ans[1])%MOD==1
    return tuple(ans)

ROOTS=omega_roots_mod_p2()

def multiply(x,y):
    a,b=x;c,d=y
    return ((a*c-b*d)%MOD,(a*d+b*c-b*d)%MOD)

def power(x,n):
    assert n>=0
    z=(1,0)
    while n:
        if n&1:z=multiply(z,x)
        x=multiply(x,x)
        n//=2
    return z

def ringclass_log(x):
    a,b=x
    r0,r1=ROOTS
    u0=(a+b*r0)%MOD
    u1=(a+b*r1)%MOD
    assert u0%P!=0 and u1%P!=0, ("NOT_LOCAL_UNIT",x)
    w=u0*pow(u1,-1,MOD)%MOD
    v=pow(w,P-1,MOD)
    assert v%P==1
    return ((v-1)//P)%P

def local_ratio(x):
    a,b=x
    r0,r1=ROOTS
    u0=(a+b*r0)%MOD
    u1=(a+b*r1)%MOD
    assert u0%P and u1%P
    return u0*pow(u1,-1,MOD)%MOD

def main():
    assert P%3==1 and 389%3==2
    assert gcd(P,389*19)==1
    print("FIRST_LAYER_SPLIT_HENSEL_ROOTS_PASS", list(ROOTS),flush=True)
    hp=(P-1)//3
    h_p2=P*hp
    assert hp==5410 and h_p2==87809710
    print("FIRST_LAYER_RINGCLASS_ORDER_RATIO_PASS",hp,h_p2,P,flush=True)

    # Global unit group O_K^x=mu_6; scalars cancel in the CRT ratio.
    omega=(0,1)
    unitset={power(omega,k) for k in range(3)}
    unitset|={multiply((-1,0),u) for u in list(unitset)}
    assert len(unitset)==6
    assert all(ringclass_log(u)==0 for u in unitset)
    for scalar in (1,2,19,P-1,P+1,5234):
        assert scalar%P
        assert ringclass_log((scalar,0))==0
    print("FIRST_LAYER_LOG_KILLS_SCALARS_AND_MU6_PASS",flush=True)

    # The prime of norm 19 used for the earlier conductor-53 orbit is
    # the ideal represented by g or its conjugate; signs invert the log.
    g=(5,3)
    gc=(2,-3)
    assert 5*5-5*3+3*3==19
    assert multiply(g,gc)==(19,0)
    t=ringclass_log(g)
    assert t==5415 and ringclass_log(gc)==(-t)%P
    print("NORM19_FROBENIUS_LOCAL_LOG_PASS",t,flush=True)
    print("NORM19_CONJUGATE_NEGATES_LOG_PASS",flush=True)

    # Raising to h(O_p) kills the prime-to-p ring class quotient.
    G=power(g,hp)
    ell=ringclass_log(G)
    assert ell==(hp*t)%P==14426
    assert ell!=0
    w=local_ratio(G)
    # In quotient by the six global units, [G] has exact order p.
    # For p split, global unit ratios are precisely mu_3 (order 3).
    assert pow(w,3,MOD)!=1
    assert pow(w,3*P,MOD)==1
    assert (pow(w,3,MOD)-1)%P==0
    assert pow(ell,-1,P)==15071
    print("NORM19_POWER_5410_FIRST_P_LAYER_GENERATOR_PASS",list(G),flush=True)
    print("NORM19_FIRST_LAYER_LOG_AND_INVERSE_PASS",ell,15071,flush=True)

    # Castella–Hsieh use u=1+p.  The element 12089+p*omega
    # represents this ratio in the split local coordinates.
    U=(12089,P)
    assert local_ratio(U)==1+P
    assert ringclass_log(U)==P-1
    # Equality in Pic(O_(p^2)) means CRT ratios differ by mu_3.
    # U=G^1160 and G=U^1805 in the canonical order-p kernel.
    assert 1160*ell%P==P-1
    assert 1160*1805%P==1
    ratio=local_ratio(U)*pow(pow(local_ratio(G),1160,MOD),-1,MOD)%MOD
    assert pow(ratio,3,MOD)==1
    print("CH_STANDARD_U_1_PLUS_P_LOCAL_RATIO_PASS",local_ratio(U),flush=True)
    print("NORM19_GENERATOR_TO_CH_U_POWER_PASS",1160,flush=True)
    print("CH_U_TO_NORM19_GENERATOR_POWER_PASS",1805,flush=True)
    # If gamma_G=gamma_U^1805 and F_G(T)=c2_G*T²+O(T³):
    # F_U(T)=F_G((1+T)^1805-1) and c2_U=1805²*c2_G.
    assert (1805*1805)%P==11825
    assert (1160*1160)%P==14658
    assert (11825*14658)%P==1
    print("THETA_SECOND_COEFFICIENT_COORDINATE_FACTOR_MODP_PASS",11825,flush=True)

    # Exhaustively audit all p powers with independent modular CRT logarithm.
    v=(1,0)
    checked=set()
    for i in range(P):
        x=ringclass_log(v)
        expected=(i*ell)%P
        assert x==expected, ("DISCRETE_LAYER_MISMATCH",i,x,expected)
        assert x not in checked,("LAYER_DUPLICATE",i,x)
        checked.add(x)
        v=multiply(v,G)
    assert len(checked)==P
    assert ringclass_log(v)==0
    assert pow(local_ratio(v),3,MOD)==1
    print("NORM19_FIRST_P_LAYER_COMPLETE_16231_LOG_ORBIT_PASS",len(checked),flush=True)
    print("NORM19_FIRST_LAYER_CANONICAL_COORDINATE_SCALE_INVERSE",15071,flush=True)
    print("BOUNDARY_GENERATOR_IS_OF_RINGCLASS_GALOIS_LAYER_NOT_GROSS_POINT_VALUES",flush=True)
    print("BOUNDARY_THETA_DERIVATIVE_AND_SHA_NOT_PROVED",flush=True)

if __name__=="__main__":
    main()
