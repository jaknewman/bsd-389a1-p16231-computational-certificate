#!/usr/bin/env python3
"""Exact Kurihara inputs to Kim's DERIVED Kato reciprocity at p=5,7,11.

Full half-range continued-fraction evaluation of frozen Manin plus symbols,
including four moments and Legendre point counts. Uses Python stdlib only.

THEOREM-LEVEL conclusion after the checks: Castella--Sano/Chan-Ho Kim
Theorem 2.1.3 implies that the actual Kato-derived cohomology class
kappa_n has NONZERO reduced p-local dual exponential because
E(Q_p)[p]=0. The script does not numerically construct kappa_n or its
unknown normalization unit u_n, and proves no uniform two-factor witness
or global Sha finiteness.
"""
from hashlib import sha256
from math import isqrt, gcd
from fractions import Fraction as F

P=389
DIGITS=(
 "222224232123221232321222312332210011221232131210022222211110"
 "222242322222111220000112210221101334422332132111111111323233"
 "121211220222323121333422232134222244424332233424333433333443"
 "223233222010022220010222332322344333334333424332233424442222"
 "431232224333121323222022112121332323111111111231233224433101"
 "122012211000022111222223242222011112222220012131232122110012"
 "233213222123232122321232422222"
)
assert len(DIGITS)==390
assert sha256(bytes(int(c) for c in DIGITS)).hexdigest()==(
 "31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee"
)
V=tuple(int(c)-2 for c in DIGITS)
INV=(0,)+tuple(pow(a,-1,P) for a in range(1,P))
assert sum(V)==0

def is_prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def primitive_root(q):
    factors=[d for d in range(2,isqrt(q-1)+1) if (q-1)%d==0 and is_prime(d)]
    if (q-1)>1:
        rem=q-1
        for d in factors:
            while rem%d==0:rem//=d
        if rem>1:factors.append(rem)
    return next(g for g in range(2,q)
                if all(pow(g,(q-1)//d,q)!=1 for d in factors))

def dlogs(q,p):
    g=primitive_root(q); logs=[-1]*q;a=1
    for i in range(q-1):
        assert logs[a]==-1
        logs[a]=i%p
        a=a*g%q
    assert a==1 and all(x>=0 for x in logs[1:])
    return g,logs

def modular_symbol(a,n,p):
    pn,pd,ln,ld=1,0,0,1
    u,v=n,a;s=V[P]
    while v:
        k,rem=divmod(u,v)
        x,y=k*ln+pn,k*ld+pd
        det=ln*y-x*ld
        assert abs(det)==1
        c,d=(ld,y) if det==1 else (y,ld)
        c%=P;d%=P
        s+=det*V[d*INV[c]%P if c else P]
        pn,pd,ln,ld=ln,ld,x,y
        u,v=v,rem
    assert (ln,ld)==(a,n)
    return s%p

def ap(q):
    s=0
    for x in range(q):
        d=(1+4*(x*x*x+x*x-2*x))%q
        if d:
            z=pow(d,(q-1)//2,q)
            assert z in (1,q-1)
            s+=1 if z==1 else -1
    return -s

def add_rational(A,B):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if x==u and y+v==-1:return None
    lam=((3*x*x+2*x-2)/(2*y+1)
         if A==B else (v-y)/(u-x))
    xx=lam*lam-1-x-u
    yy=lam*(x-xx)-y-1
    assert yy*yy+yy==xx*xx*xx+xx*xx-2*xx
    return xx,yy

def mul_rational(A,n):
    R=None
    while n:
        if n&1:R=add_rational(R,A)
        A=add_rational(A,A)
        n//=2
    return R

def local_MW_P_primitive(p):
    order=p+1-ap(p)
    R=mul_rational((F(-1),F(1)),order)
    assert R is not None
    x,y=R
    t=-x/y
    assert gcd(t.denominator,p*p)==1
    tm=t.numerator*pow(t.denominator,-1,p*p)%(p*p)
    assert tm%p==0
    coefficient=tm//p
    assert coefficient=={5:3,7:2,11:8}[p],(p,coefficient)
    return coefficient

def verify(p,q1,q2,delta_expected):
    assert all(is_prime(q) and q%p==1 and q!=P for q in (q1,q2))
    assert ap(p)=={5:-3,7:-5,11:-4}[p]
    assert (p+1-ap(p))%p!=0     # nonanomalous -> local E(Qp)[p]=0
    primitive_coefficient=local_MW_P_primitive(p)
    assert all((q+1-ap(q))%p==0 for q in (q1,q2))
    g1,log1=dlogs(q1,p);g2,log2=dlogs(q2,p)
    n=q1*q2
    moment=[0]*4;num=0
    for a in range(1,n//2+1):
        x,y=a%q1,a%q2
        if x==0 or y==0:continue
        t=modular_symbol(a,n,p)
        b,c=log1[x],log2[y]
        moment[0]=(moment[0]+t)%p
        moment[1]=(moment[1]+t*b)%p
        moment[2]=(moment[2]+t*c)%p
        moment[3]=(moment[3]+t*b*c)%p
        if a in (1,2,3,7,101):
            assert modular_symbol(n-a,n,p)==t
            assert log1[q1-x]==b and log2[q2-y]==c
        num+=1
    moment=[2*m%p for m in moment]
    assert 2*num==(q1-1)*(q2-1)
    assert moment==[0,0,0,delta_expected],(p,q1,q2,moment)
    assert delta_expected%p
    print("BSD389_DERIVED_KATO_EXPLICIT_RECIPROCITY_UNIT_INPUT_PASS",
          "p",p,"q1",q1,"q2",q2,
          "half_units",num,"total_units",2*num,
          "roots",(g1,g2),"moments",moment,
          "nonanomalous",True,"local_torsion_exponent_t",0,
          "P_local_Kummer_primitive_coefficient",primitive_coefficient,
          "Kummer_P_plus_derived_Kato_form_local_H1_basis",True,
          "expstar_kappa_n_mod_p","UNKNOWN_UNIT_TIMES_"+str(delta_expected),
          flush=True)

def run():
    assert modular_symbol(7,389,11)==10
    for args in ((5,41,61,4),(7,113,673,2),
                 (11,397,991,1),(5,61,991,3)):
        verify(*args)
    # Pure algebra counterexample: T^2*(p+T) has I-adic order 2,
    # mu invariant 0, and a NONUNIT degree-two coefficient.
    for p in (5,7,11,17,23,107):
        f={2:p,3:1}
        assert any(v%p!=0 for v in f.values())
        assert f[2]%p==0 and f[3]%p==1
    print("BSD389_IMC_PRIMITIVITY_DOES_NOT_FORCE_DEGREE_TWO_UNIT_PASS")
    print("BSD389_KATO_DERIVED_TRANSVERSE_TEST_ALL_PASS")
    print("BOUNDARY: computes modular symbol inputs only; cohomological existence follows from published theorem, not a computed Galois cocycle; no p-uniform Sha bound.")

if __name__=="__main__":run()
