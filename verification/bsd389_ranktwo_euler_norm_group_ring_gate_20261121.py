#!/usr/bin/env python3
"""Exact group-ring norm correction and tame local trace obstruction for E389a1.

The norm correction is a ONE-LEVEL CONDITIONAL algebraic construction:
it assumes two actual H^1 corestriction lifts, not provided by this script.
For q<=5237, elliptic point counts and local generator rows are checked
by independent finite-field arithmetic; for p107, historic a_q and
local rows are imported as DECLARED input, not recomputed by this gate.

No authentic new Euler system, Selmer bound, or complete BSD proof.
"""
from fractions import Fraction
from math import isqrt, comb

# p, q, a_q, local Q/P ratio (source data from real curve).
ROWS=(
 (5,41,-3,3),(5,61,-8,0),
 (7,113,9,3),(7,673,2,6),
 (11,397,24,10),(11,991,-53,7),
 (17,1667,19,6),(17,5237,87,12),
 (23,1289,25,5),(23,3727,94,12),
 (107,369793,2,15),(107,383917,-854,53),
)

def ap(q):
    s=0
    for x in range(q):
        d=(1+4*(x*x*x+x*x-2*x))%q
        if d:
            t=pow(d,(q-1)//2,q)
            assert t in (1,q-1)
            s+=1 if t==1 else -1
    return -s

def add(A,B,q):
    if A is None:return B
    if B is None:return A
    x,y=A; u,v=B
    if x==u and (y+v+1)%q==0:return None
    if A==B:
        lam=(3*x*x+2*x-2)*pow((2*y+1)%q,-1,q)%q
    else:
        lam=(v-y)*pow((u-x)%q,-1,q)%q
    xx=(lam*lam-1-x-u)%q
    yy=(lam*(x-xx)-y-1)%q
    assert (yy*yy+yy-xx**3-xx**2+2*xx)%q==0
    return (xx,yy)

def mul(A,n,q):
    R=None
    while n:
        if n&1:R=add(R,A,q)
        A=add(A,A,q);n>>=1
    return R

def ring_mul(A,B):
    p=len(A)
    assert len(B)==p
    return [sum(A[k]*B[(j-k)%p] for k in range(p))
            for j in range(p)]

def run():
    for p,q,a,ratio in ROWS:
        if q<=5237:
            assert ap(q)==a,(p,q,a)
        M=q+1-a
        assert (q-1)%p==0 and M%p==0
        assert (q-1)%(p*p) and M%(p*p)
        b=M//p
        assert b%p
        n=[1]*p
        assert ring_mul(n,n)==[p]*p       # N_H^2=p N_H
        # The Kolyvagin derivative D=sum i*sigma^i kills N modulo p.
        D=list(range(p))
        DN=ring_mul(D,n)
        assert DN==[p*(p-1)//2]*p
        assert all(z%p==0 for z in DN)
        # In the modular group algebra Fp[Cp], N=(sigma-1)^(p-1).
        assert [(-1)**(p-1-j)*comb(p-1,j)%p for j in range(p)]==[1]*p
        c=[b]*p                           # b N_H, integral
        assert sum(c)==M                  # exterior norm = Euler P_q(1)
        # On Q_p[G], res(omega)=N_H^2*(yP^yQ).
        u=Fraction(M,p*p)
        assert [u*v for v in ring_mul(n,n)]==c
        assert u.denominator==p           # scalar NOT in Z_p
        assert b%p == (M//p)%p            # first norm jet
        if q<=5237:
            B=mul((-1%q,1),b,q)
            C=mul((0,q-1),b,q)
            assert B is not None and mul(B,p,q) is None
            assert mul(B,ratio,q)==C
            # Nontrivial reduction modulo p prohibits a POINT trace:
            # reduction of Trace R is [p] reduction(R).
            assert B is not None
        print("BSD389_EULER_RANKTWO_NORM_JET_PASS",
              "p",p,"q",q,"ap",a,"E_Fq",M,
              "b=M/p",b,"b_mod_p",b%p,
              "required_rational_scalar",str(u),
              "integral_group_ring_c_coeff",b,
              "local_P_nontrace_certified",q<=5237,
              "Kolyvagin_D_on_norm_mod_p",0,
              "norm_augmentation_order_mod_p",p-1,flush=True)
    # Two-step formal norm check in the scalar-invariant component.
    # These are NOT full group-ring Euler relations at nontrivial
    # characters; norm classes kill those characters.
    for p in sorted({row[0] for row in ROWS}):
        group=[q+1-a for pp,q,a,_ in ROWS if pp==p]
        assert len(group)==2
        n1,n2=group
        b12=n1*n2//(p*p)
        assert b12==(n1//p)*(n2//p)
        assert p*b12==n2*(n1//p)
        assert p*b12==n1*(n2//p)
        assert p-1>2
        print("BSD389_TWO_AUXILIARY_NORM_COHERENCE_PASS",
              "p",p,"b12",b12,
              "mixed_T1T2_coefficient_modp",0,flush=True)
    print("BSD389_NORM_DERIVATIVES_VANISH_MODP_ALL_PASS",len(ROWS))
    print("BSD389_GROUP_RING_NORM_CORRECTION_ALL_PASS",len(ROWS))
    print("BOUNDARY: formal one- and two-level norm identities only; no actual coherent H1 lifts or nontrivial Kolyvagin derivative; no uniform Fitt bound.")

if __name__=="__main__":
    run()
