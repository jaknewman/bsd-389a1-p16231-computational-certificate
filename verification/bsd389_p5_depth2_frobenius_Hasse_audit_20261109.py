#!/usr/bin/env python3
"""Independent 389a1 q5351/q13001 point enumeration + general Hasse depth gap.
Does not compute Kurihara or prove global Sha finiteness.
"""
P=(-1,1); Q=(0,-1)
def add(A,B,q):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if (x-u)%q==0 and (y+v+1)%q==0:return None
    if (x-u)%q:
        t=pow((u-x)%q,-1,q)
        l=(v-y)*t%q; z=(y*u-v*x)*t%q
    else:
        d=(2*y+1)%q
        if not d:return None
        t=pow(d,-1,q)
        l=(3*x*x+2*x-2)*t%q;z=(-x*x*x-2*x-y)*t%q
    X=(l*l-1-x-u)%q
    return X,(-l*X-z-1)%q
def mul(n,A,q):
    R=None
    while n:
        if n&1:R=add(R,A,q)
        A=add(A,A,q);n>>=1
    return R
def point_enum(q):
    sq={y*y%q:y for y in range(q)}
    inv2=pow(2,-1,q)
    out=[None]
    for x in range(q):
        d=(1+4*(x*x*x+x*x-2*x))%q
        if d not in sq:continue
        y=((sq[d]-1)*inv2)%q
        out.append((x,y))
        yy=(-y-1)%q
        if yy!=y:out.append((x,yy))
    return out
for q,ap,n,pow5,tors5,ratio in ((5351,-23,5375,125,5,64),
                                 (13001,-73,13075,25,25,2)):
    assert (q-1)%25==0 and ap%25==2
    pts=point_enum(q)
    assert len(pts)==n
    five=[R for R in pts if mul(5,R,q) is None]
    assert len(five)==tors5
    k=n//pow5
    A=mul(k,P,q); B=mul(k,Q,q)
    assert B==mul(ratio,A,q)
    assert mul(pow5,A,q) is None
    if q==5351:assert mul(25,A,q) is not None
    else:
        assert A is not None and mul(5,A,q) is None
        assert all(mul(5,mul(k,R,q),q) is None for R in pts)
    print('P5_DEPTH25_FULL_LOCAL_PROFILE_PASS',q,'a_q',ap,'#E',n,
          'E[5]',tors5,'primary_order',pow5,'Q/P',ratio)
for p in (5,17,107,599,16231):
    d=p*p
    Qmin=((d-2)**2+3)//4
    assert 4*Qmin>=(d-2)**2 and 4*(Qmin-1)<(d-2)**2
    print('HASSE_NONTRACE2_DEPTH2_CONDUCTOR_BOUND',p,Qmin,Qmin*Qmin)
print('BOUNDARY: a_q=2 is an explicit Hasse-gap exception; no uniform Sha result')
