#!/usr/bin/env python3
"""Local mod-p reduction counterexample to a naive permanent bridge on 389a1.
Uses the transformed curve Y^2=X^3+4X^2-32X+16.
P=(-4,12), Q=(0,-4). Kurihara values are inherited from earlier certificates.
"""
P=(-4,12); Q=(0,-4)
def add(A,B,q):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if (x-u)%q==0 and (y+v)%q==0:return None
    if A==B:
        if y%q==0:return None
        s=((3*x*x+8*x-32)*pow((2*y)%q,-1,q))%q
    else:s=((v-y)*pow((u-x)%q,-1,q))%q
    X=(s*s-4-x-u)%q
    return (X,(s*(x-X)-y)%q)
def mul(R,n,q):
    A=None
    while n:
        if n&1:A=add(A,R,q)
        R=add(R,R,q)
        n>>=1
    return A
def count(q):
    total=q+1
    for x in range(q):
        rhs=(x*x*x+4*x*x-32*x+16)%q
        if rhs: total+= 1 if pow(rhs,(q-1)//2,q)==1 else -1
    return total
def local_line(p,q):
    n=count(q); assert n%p==0,(p,q,n)
    R=mul(P,n//p,q); S=mul(Q,n//p,q)
    if R is not None:
        for i in range(p):
            if mul(R,i,q)==S:return n,(1,i)
    if S is not None:
        for i in range(p):
            if mul(S,i,q)==R:return n,(i,1)
    raise AssertionError((p,q,'noncyclic local line'))
for p,qs in [(5,[41,61,131,251]),(7,[113,673,1429,2423])]:
    lines=[]
    for q in qs:
        n,v=local_line(p,q)
        print('LOCAL',p,q,'COUNT',n,'REDUCTION',v)
        lines.append(v)
    v=lines[0];w=lines[2]
    naive=(v[0]*w[1]+v[1]*w[0])%p
    actual=1 # both old pair certificates have delta_13=1
    print('PAIR13',p,'NAIVE_PERMANENT',naive,'CERTIFIED_KURIHARA',actual)
    if p==7:
        assert naive==0 and actual==1
        print('NAIVE_LOCAL_PERMANENT_FACTORIZATION_REFUTED_PASS')
print('BOUNDARY: does NOT refute a genuine cohomological Bockstein comparison')
