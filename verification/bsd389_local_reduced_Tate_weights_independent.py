#!/usr/bin/env python3
"""Local Tate-weight auditor for E=389a1. No modular symbols are evaluated.

This exact finite-field calculation uses the elliptic group law and Miller
functions only. It verifies q-local weights against previously frozen
two-prime empirical fits. The 137-pair *universal* identity is NOT proved.
"""
from random import Random

SAMPLES={
  5:([41,61,131,211,251,271,571,641,751,991,1031,1181,1321,1381,1811],
     [3,1,1,2,3,3,2,2,2,4,4,1,3,4,3],
     [1,2,2,4,1,1,4,4,4,3,3,2,1,3,1],3),
  7:([113,673,1429,2423,3389],
     [1,4,4,3,4],[1,4,4,3,4],2),
 11:([397,991,1321,3389,3433,4643],
     [8,1,9,9,8,4],[1,7,8,8,1,6],7),
 13:([131,911,1249,2237],[11,7,11,10],None,None),
 17:([1667,5237],[16,16],None,None)
}

def add(A,B,q):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if x==u and (y+v+1)%q==0:return None
    slope=((3*x*x+2*x-2)*pow(2*y+1,-1,q)
            if x==u else (v-y)*pow(u-x,-1,q))%q
    nu=(y-slope*x)%q
    X=(slope*slope-1-x-u)%q
    return X,(-slope*X-nu-1)%q

def mul(A,n,q):
    result=None
    while n:
        if n&1:result=add(result,A,q)
        A=add(A,A,q);n>>=1
    return result

def count_points(q):
    n=1
    for x in range(q):
        D=(1+4*(x*x*x+x*x-2*x))%q
        n+=1 if D==0 else (2 if pow(D,(q-1)//2,q)==1 else 0)
    return n

def primitive(q):
    n=q-1;divisors=[];d=2
    while d*d<=n:
        if n%d==0:
            divisors.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:divisors.append(n)
    return next(g for g in range(2,q)
                if all(pow(g,(q-1)//v,q)!=1 for v in divisors))

def line_add(A,B,q):
    if A is None:return B,lambda T:1
    if B is None:return A,lambda T:1
    x,y=A;u,v=B
    if x==u and (y+v+1)%q==0:
        return None,lambda T:(T[0]-x)%q
    slope=((3*x*x+2*x-2)*pow(2*y+1,-1,q)
            if x==u else (v-y)*pow(u-x,-1,q))%q
    nu=(y-slope*x)%q
    X=(slope*slope-1-x-u)%q
    Y=(-slope*X-nu-1)%q
    def value(T):
        xx,yy=T
        den=(xx-X)%q
        if den==0:raise ZeroDivisionError("vertical pole")
        return ((yy-slope*xx-nu)*pow(den,-1,q))%q
    return (X,Y),value

def miller(G,p,T,q):
    R=G;f=1
    for bit in bin(p)[3:]:
        R,line=line_add(R,R,q)
        z=line(T)
        if not z:raise ZeroDivisionError("Miller zero")
        f=f*f*z%q
        if bit=="1":
            R,line=line_add(R,G,q)
            z=line(T)
            if not z:raise ZeroDivisionError("Miller zero")
            f=f*z%q
    assert R is None
    return f

def auxiliary(q,seed):
    rng=Random(seed)
    for _ in range(100):
        x=rng.randrange(q)
        D=(1+4*(x*x*x+x*x-2*x))%q
        if D and pow(D,(q-1)//2,q)!=1:continue
        for y in range(q):
            if (y*y+y-x*x*x-x*x+2*x)%q==0:return x,y
    raise RuntimeError("cannot find auxiliary point")

def reduced_tate(G,e,p,q,shift_checks=1):
    vals=[]
    for seed in range(17,100):
        R=auxiliary(q,seed);Q=add(e,R,q)
        if Q is None:continue
        try:
            numerator=miller(G,p,Q,q)
            denominator=miller(G,p,R,q)
            val=pow(numerator*pow(denominator,-1,q)%q,(q-1)//p,q)
            assert pow(val,p,q)==1
            vals.append(val)
            if len(vals)>=shift_checks:break
        except (ValueError,ZeroDivisionError):continue
    assert len(vals)>=shift_checks and len(set(vals))==1,(p,q,vals)
    return vals[0]

def weight(q,p,checks=False):
    n=count_points(q)
    assert n%p==0 and n%(p*p)!=0 and (q-1)%p==0
    P=(q-1,1);Q=(0,q-1)
    e=P if mul(P,n//p,q) is not None else Q
    G=mul(e,n//p,q)
    assert G is not None and mul(G,p,q) is None
    v=reduced_tate(G,e,p,q,8 if checks else 1)
    assert v!=1,("degenerate Tate weight",q,p)
    if checks:assert reduced_tate(G,mul(e,2,q),p,q)==pow(v,2,q)
    z=pow(primitive(q),(q-1)//p,q)
    return next(j for j in range(1,p) if pow(z,j,q)==v)

def main():
    count=0
    for p,(qs,expected,u,old_C) in SAMPLES.items():
        weights=[weight(q,p,i<2) for i,q in enumerate(qs)]
        assert weights==expected,(p,weights,expected)
        count+=len(qs)
        if u:
            alpha=u[0]*pow(weights[0],-1,p)%p
            assert all(alpha*w%p==v for w,v in zip(weights,u))
            assert old_C*alpha*alpha%p==2
        print("INDEPENDENT_TATE_WEIGHT_PASS",p,len(qs),weights)
    print("INDEPENDENT_TATE_WEIGHTS_PASS",count,
          "weights across p=5,7,11,13,17")
    print("BORDER: exact finite arithmetic, NOT universal rank2 BSD")

if __name__=="__main__":main()
