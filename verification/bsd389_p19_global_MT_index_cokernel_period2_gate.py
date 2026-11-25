#!/usr/bin/env python3
"""Exact p=19 reduction cokernel/lattice certificate for 389a1 (stdlib).

Tests group orders, full finite-field cyclic logs of P,Q, cokernel=1,
an integral restricted-MW lattice basis, and the regulator index identity.

The last comparison to quadratic modular symbols is a CONSISTENCY CHECK
assuming the separately proposed local Neron/Tate height normalisation.
No proof of Kato/BSD leading-term equality is asserted.
"""
from math import gcd, isqrt
from itertools import combinations

def add(A,B,q):
    if A is None: return B
    if B is None: return A
    x,y=A;u,v=B
    if x==u and (y+v+1)%q==0:return None
    lam=((3*x*x+2*x-2)*pow(2*y+1,-1,q)
         if x==u else (v-y)*pow((u-x)%q,-1,q))%q
    nu=(y-lam*x)%q
    X=(lam*lam-1-x-u)%q
    return (X,(-lam*X-nu-1)%q)

def mul(A,k,q):
    R=None
    while k:
        if k&1:R=add(R,A,q)
        A=add(A,A,q);k//=2
    return R

def points(q):
    ans=1
    for x in range(q):
        D=(1+4*(x*x*x+x*x-2*x))%q
        ans+=1 if D==0 else (2 if pow(D,(q-1)//2,q)==1 else 0)
    return ans

def primefactors(n):
    ret=[];d=2
    while d*d<=n:
        if n%d==0:
            ret.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:ret.append(n)
    return ret

def logs(q,n,G):
    assert points(q)==n
    assert mul(G,n,q) is None
    assert all(mul(G,n//d,q) is not None for d in primefactors(n))
    table={None:0};T=None
    for k in range(1,n):
        T=add(T,G,q)
        assert T not in table
        table[T]=k
    assert len(table)==n
    return table[(q-1,1)],table[(0,q-1)]

p=19
q1,n1,G1=2243,2261,(2,883)
q2,n2,G2=3877,3781,(0,0)
a1,b1=logs(q1,n1,G1)
a2,b2=logs(q2,n2,G2)
assert ((a1,b1),(a2,b2))==((2144,2163),(3439,3780))
C=[(n1,0),(0,n2),(a1,a2),(b1,b2)]
minors=[abs(x*v-u*y) for (x,y),(u,v) in combinations(C,2)]
J=gcd(*minors)
assert J==1,(J,minors)
B=[(1995,2071),(-2261,1938)]
for a,b in B:
    assert (a1*a+b1*b)%n1==0
    assert (a2*a+b2*b)%n2==0
index=B[0][0]*B[1][1]-B[0][1]*B[1][0]
assert index==n1*n2==8548841
M1,M2=n1//p,n2//p
h=index//(p*p)
assert h==M1*M2==23681 and J*h==M1*M2

# CHECK ONLY: previously computed independent local reduced-Tate weights
# (17,18) plus the STILL-INDEPENDENTLY-UNAUDITED local tame height bridge.
w1,w2=17,18
alpha1=w1*pow(M1,-1,p)%p
alpha2=w2*pow(M2,-1,p)%p
assert (alpha1,alpha2)==(11,2)
Hdet=alpha1*alpha2%p
assert Hdet==3
reg_integral=h*Hdet%p
assert reg_integral==2
project_modular_jet=4   # independently calculated complete Manin sum
assert 2*J*reg_integral%p==project_modular_jet

print("P19_ACTUAL_GLOBAL_REDUCTION_J_S_1_PASS",
      "orders",(n1,n2),"logs",((a1,b1),(a2,b2)),
      "integral_kernel_basis",B,"det",index,
      "J_S",J,"prime_to_p_index",h)
print("P19_PERIOD_NORMALIZATION_CONSISTENCY_PASS",
      "proposed_height_det",Hdet,
      "proposed_full_MT_reg",reg_integral,
      "project_modular_jet",project_modular_jet,
      "real_period_normalization_factor",2)
print("BOUNDARY: exact index/cokernel; global Kato-to-regulator equality "
      "NOT proved; local tame comparison still needs independent verification")
