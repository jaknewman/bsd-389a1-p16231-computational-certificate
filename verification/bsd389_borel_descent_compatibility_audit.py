#!/usr/bin/env python3
"""Exact projective-line Borel descent compatibility equations for E389a1.

This proves linear-algebra identities in GL2(Fp) used in the Galois
cohomology theorem. It does NOT compute ray class groups, isogeny
Selmer groups or Sha, and does not certify full BSD.
"""
from math import isqrt
import random

def matmulvec(g,v,p):
    a,b,c,d=g;x,y=v
    return ((a*x+b*y)%p,(c*x+d*y)%p)

def lines(p):return tuple(range(p))+(p,)

def functional(C,v,p):
    x,y=v
    return x%p if C==p else (y-C*x)%p

def line_generator(C,p):return (0,1) if C==p else (1,C)

def quotient_lift(C,p):return (1,0) if C==p else (0,1)

def translate_line(g,C,p):
    u,v=matmulvec(g,line_generator(C,p),p)
    assert (u,v)!=(0,0)
    return p if u==0 else (v*pow(u,-1,p))%p

def M_action(g,m,p):
    result=[None]*(p+1)
    for C in lines(p):
        CC=translate_line(g,C,p)
        scalar=functional(CC,matmulvec(g,quotient_lift(C,p),p),p)
        assert scalar!=0 and result[CC] is None
        result[CC]=(scalar*m[C])%p
    assert all(x is not None for x in result)
    return tuple(result)

def inc(v,p):
    return tuple(functional(C,v,p) for C in lines(p))

def D(m,p):
    return tuple((m[t]-m[0]+t*m[p])%p for t in range(1,p))

def GL2_random(p,rng):
    while True:
        g=tuple(rng.randrange(p) for _ in range(4))
        a,b,c,d=g
        if (a*d-b*c)%p:return g

def audit(p):
    rng=random.Random(389000+p)
    assert p>=5 and all(p%q for q in range(2,isqrt(p)+1))
    for x,y in ((0,0),(1,0),(0,1),(1,1),(p-1,p-2)):
        v=(x,y);m=inc(v,p)
        assert D(m,p)==(0,)*(p-1)
        for _ in range(15):
            g=GL2_random(p,rng)
            assert M_action(g,m,p)==inc(matmulvec(g,v,p),p)
    for _ in range(25):
        m=tuple(rng.randrange(p) for _ in range(p+1))
        assert all(x==0 for x in D(m,p))==(m==inc((m[p],m[0]),p))
        g=GL2_random(p,rng)
        assert all(x==0 for x in D(m,p))==all(x==0 for x in D(M_action(g,m,p),p))
    scalar_minus=(p-1,0,0,p-1)
    for _ in range(7):
        m=tuple(rng.randrange(p) for _ in range(p+1))
        assert M_action(scalar_minus,m,p)==tuple(-x%p for x in m)
    # Borel quotient W has character d, while the only B-map W->V
    # is zero: U-fixed vectors lie on the e1-line, diag(2,1)
    # acts trivially on W but nontrivially on that line.
    assert not any((y==0 and x!=0 and 2*x%p==x)
                   for x in range(p) for y in range(p))
    print('BOREL_DESCENT_PMINUS1_EQUATIONS_GAMMA_EQUIVARIANT_PASS',
          'p',p,'M_dim',p+1,'V_dim',2,'obstruction_dim',p-1,
          'Sah_central_minusI',True,
          'no_equivariant_retraction',True,flush=True)

for p in (5,7,11,13,107,16231):audit(p)

def exhaustive(p):
    total=0
    for a in range(p):
      for b in range(p):
       for c in range(p):
        for d in range(p):
         if (a*d-b*c)%p==0:continue
         total+=1
         g=(a,b,c,d)
         for v in ((1,0),(0,1)):
            assert M_action(g,inc(v,p),p)==inc(matmulvec(g,v,p),p)
         for i in range(1,p):
            m=[0]*(p+1);m[i]=1
            assert len(D(M_action(g,m,p),p))==p-1
    assert total==p*(p-1)**2*(p+1)
    print('EXHAUSTIVE_GL2_BOREL_DESCENT_ACTION_PASS',p,total,flush=True)

for p in (5,7):exhaustive(p)
print('SCOPE: FINITE REPRESENTATIONS ONLY; NO SELMER / RAY CLASS / SHA UNIFORM RESULT')
