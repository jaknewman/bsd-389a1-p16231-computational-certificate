#!/usr/bin/env python3
"""E389a1 p=7: exact finite-field audit and adversarial Kurihara regression.

Only finite-field computations are new. Archived Kurihara values 0 and 2
come from results/bsd389_k7_hecke_zero_nonzero_dual_PASS_2026-10-29.md
and are NOT recomputed by this script. No global BSD/Sha claim.
"""
from math import gcd, isqrt

P = 7
ARCHIVED_PAIRS = ((113, 281, 9, -12, 0), (113, 673, 9, 2, 2))
def isprime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def trace(q):
    assert q%2 and q!=389 and isprime(q)
    s=0
    for x in range(q):
        d=(4*x*x*x+4*x*x-8*x+1)%q
        if d:
            z=pow(d,(q-1)//2,q)
            assert z in (1,q-1)
            s+=(1 if z==1 else -1)
    return -s

def val_unit(n,p):
    assert n>0
    v=0
    while n%p==0:
        n//=p
        v+=1
    return v,n%p

for q1,q2,a1,a2,delta_archived in ARCHIVED_PAIRS:
    assert (trace(q1),trace(q2))==(a1,a2)
    n1,n2=q1+1-a1,q2+1-a2
    v1,u1=val_unit(n1,P)
    v2,u2=val_unit(n2,P)
    v_mix,u_mix=val_unit(n1*n2,P)
    assert v_mix==v1+v2 and u_mix==u1*u2%P and u_mix!=0
    i1=gcd(q1-1,a1-q1-1)
    i2=gcd(q2-1,a2-q2-1)
    assert val_unit(i1,P)[0]==val_unit(i2,P)[0]==1
    assert (n1,n2)==((105,294) if q2==281 else (105,672))
    assert (v_mix,u_mix,delta_archived)==(
        (3,6,0) if q2==281 else (2,5,2))
    print("P7_MIXED_OLDFORM_LOCAL_AUDIT_PASS",
          "pair",(q1,q2),"aq",(a1,a2),
          "points",(n1,n2),"vp_mixed",v_mix,
          "saturated_mixed_unit_mod7",u_mix,
          "vp_Kurihara_auxiliary_I_n_sum",1,
          "archived_delta_mod7",delta_archived)

# Direct, witness-based verification E(F_281)[7] ≅ (Z/7)^2.
q=281
def ec_add(Pt,Qt):
    if Pt is None:return Qt
    if Qt is None:return Pt
    x,y=Pt; u,v=Qt
    if x==u and (y+v+1)%q==0:return None
    if x==u:
        d=(2*y+1)%q
        if d==0:return None
        lam=((3*x*x+2*x-2)*pow(d,-1,q))%q
    else:
        lam=((v-y)*pow((u-x)%q,-1,q))%q
    intercept=(y-lam*x)%q
    new_x=(lam*lam-1-x-u)%q
    return(new_x,(-lam*new_x-intercept-1)%q)

def ec_mul(Pt,n):
    out=None
    while n:
        if n&1:out=ec_add(out,Pt)
        Pt=ec_add(Pt,Pt)
        n//=2
    return out

def on_curve(Pt):
    x,y=Pt
    return (y*y+y-x*x*x-x*x+2*x)%q==0

R,S=(20,74),(22,61)
assert on_curve(R) and on_curve(S)
assert ec_mul(R,7) is None and ec_mul(S,7) is None
subgroup_R={ec_mul(R,k) for k in range(7)}
assert len(subgroup_R)==7 and S not in subgroup_R
assert ec_add(R,S)==(210,36)
assert q+1-trace(q)==294
print("P7_FULL_RATIONAL_TORSION_AT_281_PASS",
      "independent_generators",R,S,
      "E_F281_7_torsion_order",49,
      "local_Kummer_dim",2)
print("P7_KUMMER_DIMENSION_CONTRAST_PASS",
      "q113",1,"q281",2,"q673",1)
print("COUNTEREXAMPLE_LOCAL_SATURATED_UNIT_NOT_KURIHARA_UNIT_PASS")
print("SCOPE_DELTAS_FROM_ARCHIVED_SAGE_USER_RUN_NO_NEW_KURIHARA_SUM_NO_SHA_OR_BSD_CLAIM")
