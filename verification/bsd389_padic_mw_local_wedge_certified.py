#!/usr/bin/env python3
"""E389a1: true normalized p-adic MW log residues at p599 and p16231.

Exact Jacobian-projective operations modulo p^60 with weighted
p-normalization on the isomorphic short curve. No huge rational
multiples, external Sage, class group, Sha or complete BSD claimed.
"""
A=-3024
P=(-24,324,1)
Q=(12,-108,1)
INF=(0,1,0)

def points(p):
    total=1
    for x in range(p):
        D=(4*x*x*x+4*x*x-8*x+1)%p
        if D==0:total+=1
        elif pow(D,(p-1)//2,p)==1:total+=2
    return total

def vp(n,p,cap):
    if n==0:return cap
    i=0
    while n%p==0:
        i+=1;n//=p
    return i

def norm(T,m,p):
    X,Y,Z=[v%m for v in T]
    if Z==0 and Y!=0:return INF
    if X==Y==Z==0:raise ArithmeticError("all Jacobian coordinates zero")
    power=0;n=m
    while n%p==0:
        power+=1;n//=p
    s=min(vp(X,p,power)//2,vp(Y,p,power)//3,vp(Z,p,power))
    return (X//p**(2*s),Y//p**(3*s),Z//p**s) if s else (X,Y,Z)

def neg(T,m):return (T[0],-T[1]%m,T[2])

def double(T,m):
    X,Y,Z=T
    if Z%m==0:return INF
    X%=m;Y%=m;Z%=m
    aa=X*X%m;bb=Y*Y%m;cc=bb*bb%m
    dd=2*((X+bb)**2-aa-cc)%m
    ee=(3*aa+A*Z**4)%m
    ff=ee*ee%m
    return (ff-2*dd)%m,(ee*(dd-(ff-2*dd))-8*cc)%m,2*Y*Z%m

def add(T,U,m):
    X1,Y1,Z1=T;X2,Y2,Z2=U
    if Z1%m==0:return tuple(z%m for z in U)
    if Z2%m==0:return tuple(z%m for z in T)
    Z1%=m;Z2%=m;X1%=m;X2%=m;Y1%=m;Y2%=m
    z1=Z1*Z1%m;z2=Z2*Z2%m
    u1=X1*z2%m;u2=X2*z1%m
    s1=Y1*z2*Z2%m;s2=Y2*z1*Z1%m
    if u1==u2:
        return INF if s1!=s2 else double(T,m)
    h=(u2-u1)%m
    i=(2*h)**2%m
    j=h*i%m
    r=2*(s2-s1)%m
    v=u1*i%m
    return ((r*r-j-2*v)%m,
            (r*(v-(r*r-j-2*v))-2*s1*j)%m,
            ((Z1+Z2)**2-z1-z2)*h%m)

def mul(T,k,m,p):
    if k<0:return mul(neg(T,m),-k,m,p)
    out=INF
    while k:
        if k&1:out=norm(add(out,T,m),m,p)
        T=norm(double(T,m),m,p)
        k>>=1
    return out

def param(T,p):
    m=p*p
    X,Y,Z=T
    assert Z%p==0
    den=(Y-108*Z**3)%m
    assert den%p!=0
    t=(-6*Z*(X-12*Z*Z)*pow(den,-1,m))%m
    assert t%p==0
    return t

def check(p,expected):
    n=points(p)
    assert n%p
    m=p**60
    a=param(mul(P,n,m,p),p)//p*pow(n,-1,p)%p
    b=param(mul(Q,n,m,p),p)//p*pow(n,-1,p)%p
    assert (a,b)==expected and a!=0
    k=b*pow(a,-1,p)%p
    if k>p//2:k-=p
    assert (a*(-k)+b)%p==0
    R=norm(add(mul(P,-k,m,p),Q,m),m,p)
    assert param(mul(R,n,m,p),p)==0
    print("E389A1_MW_LOG_LOCAL_SATURATION_PASS",
          "p",p,"N",n,"logP/p",a,"logQ/p",b,
          "primitive_R",f"Q-({k})P",
          "local_class_p_divisible",True,flush=True)

for p,a in ((5,(2,4)),(7,(5,3)),(11,(6,7)),
            (107,(13,42)),(599,(119,121)),(16231,(6575,12208))):
    check(p,a)
print("SCOPE: LOCAL_P_ADIC_DATA_ONLY; NO_CLASSGROUP_SHA_BSD")
