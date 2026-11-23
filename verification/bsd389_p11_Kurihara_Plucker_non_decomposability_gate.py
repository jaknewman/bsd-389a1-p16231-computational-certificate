#!/usr/bin/env python3
"""Authentic E389a1 two-prime Kurihara Plucker failure at p=11.

Independent standard-library computation of six complete Kurihara sums from
the separately archived 390-integer Manin vector (not fabricated weights).
Includes direct local E(F_q) arithmetic and p5/p11 source-normalization
anchors. The nonzero Pfaffian disproves any rank-two decomposable
two-auxiliary-prime exterior-factorization, even after per-q unit rescaling.
It does NOT imply a global Sha bound or exact BSD.
"""
from itertools import combinations
from math import gcd
from time import monotonic

from bsd389_supersingular_p2_signed_moments_exact import N, V, INV

assert N == 389 and len(V) == 390 and V[389] == 0
PRIMES = [397, 991, 1321, 3389]
EXPECTED = {
    (397,991):1, (397,1321):9, (397,3389):4,
    (991,1321):10, (991,3389):7, (1321,3389):2,
}

def primitive_root(q):
    n=q-1; divisors=[]; d=2
    while d*d<=n:
        if n%d==0:
            divisors.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:divisors.append(n)
    return next(g for g in range(2,q)
                if all(pow(g,(q-1)//d,q)!=1 for d in divisors))

def logs(q,p):
    g=primitive_root(q)
    tab=bytearray(q)
    x=1
    for j in range(q-1):
        tab[x]=j%p
        x=x*g%q
    assert x==1
    return g,tab

def modular_symbol(a,n,p):
    pn,pd,ln,ld=1,0,0,1
    u,v=n,a
    acc=V[N]
    while v:
        quot,rem=divmod(u,v)
        u,v=v,rem
        nn=quot*ln+pn
        nd=quot*ld+pd
        det=ln*nd-nn*ld
        assert det in (1,-1)
        c,d=(ld,nd) if det==1 else (nd,ld)
        c%=N; d%=N
        acc+=det*V[d*INV[c]%N if c else N]
        pn,pd,ln,ld=ln,ld,nn,nd
    assert (ln,ld)==(a,n)
    return acc%p

def kurihara(q1,q2,p=11):
    n=q1*q2
    assert n%2 and (q1-1)%(2*p)==(q2-1)%(2*p)==0
    g1,L1=logs(q1,p)
    g2,L2=logs(q2,p)
    val=0;weighted=0
    for a in range(1,(n-1)//2+1):
        r1,r2=a%q1,a%q2
        if not r1 or not r2:continue
        weight=L1[r1]*L2[r2]%p
        if weight:
            val=(val+weight*modular_symbol(a,n,p))%p
            weighted+=1
    return 2*val%p,(g1,g2),weighted

def cardinality(q):
    s=1
    for x in range(q):
        discr=(1+4*(x*x*x+x*x-2*x))%q
        s+=1 if discr==0 else 2 if pow(discr,(q-1)//2,q)==1 else 0
    return s

def add(A,B,q):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if x==u and (y+v+1)%q==0:return None
    if x==u:
        inv=pow(2*y+1,-1,q)
        slope=(3*x*x+2*x-2)*inv%q
        nu=(-x*x*x-2*x-y)*inv%q
    else:
        inv=pow(u-x,-1,q)
        slope=(v-y)*inv%q
        nu=(y*u-v*x)*inv%q
    X=(slope*slope-1-x-u)%q
    Y=(-slope*X-nu-1)%q
    assert (Y*Y+Y-X*X*X-X*X+2*X)%q==0
    return X,Y

def mul(n,A,q):
    out=None
    while n:
        if n&1:out=add(out,A,q)
        A=add(A,A,q)
        n>>=1
    return out

def local(q):
    n=cardinality(q)
    assert q%11==1 and n%11==0 and n%121!=0
    P=mul(n//11,(-1,1),q)
    Q=mul(n//11,(0,-1),q)
    assert P is not None and Q is not None
    assert mul(11,P,q) is None and mul(11,Q,q) is None
    coords=[i for i in range(11) if mul(i,P,q)==Q]
    assert len(coords)==1
    return (1,coords[0]),n

def pfaff(D):
    a,b,c,d=PRIMES
    return (D[(a,b)]*D[(c,d)] -
            D[(a,c)]*D[(b,d)] +
            D[(a,d)]*D[(b,c)])%11

def main():
    clock=monotonic()
    # Match two independently archived E389a1 p5 and p11 Sage/eclib sums.
    delta5,roots5,_=kurihara(41,61,5)
    delta11,roots11,_=kurihara(397,991)
    assert (delta5,roots5)==(4,(6,2))
    assert (delta11,roots11)==(1,(5,6))
    print("ECLIB_P5_P11_KURIHARA_NORMALIZATION_REGRESSIONS_PASS",flush=True)
    rows={}
    for q in PRIMES:
        rows[q],n=local(q)
        print("INDEPENDENT_LOCAL_E11_ROW_PASS",q,n,rows[q],flush=True)
    assert [rows[q] for q in PRIMES]==[(1,10),(1,7),(1,2),(1,8)]
    D={}; W={}
    for a,b in combinations(PRIMES,2):
        residue,roots,count=kurihara(a,b)
        det=(rows[a][0]*rows[b][1]-rows[a][1]*rows[b][0])%11
        assert residue==EXPECTED[(a,b)]
        assert det!=0
        D[(a,b)]=residue
        W[(a,b)]=det
        print("EXHAUSTIVE_TWO_PRIME_KURIHARA_AND_MW_WEDGE_PASS",
              a,b,"root",roots,"nonzero_weights",count,
              "delta",residue,"wedge",det,flush=True)
    assert pfaff(W)==0
    assert pfaff(D)==1
    print("MW_LOCAL_DECOMPOSABLE_PLUCKER_PASS",0,flush=True)
    print("TRUE_KURIHARA_NONDECOMPOSABLE_PFAFFIAN_PASS",1,"RANK",4,flush=True)
    print("NO_FIXED_TWO_VECTOR_DETERMINANT_MODEL_EVEN_WITH_LOCAL_UNIT_SCALING")
    print("SECONDS",round(monotonic()-clock,2),flush=True)
    print("BOUNDARY_NO_UNIFORM_SHA_BOUND_OR_FULL_BSD")

if __name__=="__main__":
    main()
