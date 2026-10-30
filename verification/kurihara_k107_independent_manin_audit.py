#!/usr/bin/env python3
"""Independent mathematical/implementation audit of the K107 Manin edge kernel.

No import from the production Manin implementation. Uses Sage's independent
continued-fraction convergents, exact rational modular symbols, and randomized
SL(2,Z) representatives. Does not prove every loop iteration was executed
correctly; supplies independent checks of the general Manin edge identity.
"""
import argparse, hashlib, json, math, random
from pathlib import Path
from sage.all import EllipticCurve, QQ, ZZ, continued_fraction

N=389

def residue(x,p):
    x=QQ(x)
    num=int(x.numerator()); den=int(x.denominator())
    if den%p==0: raise AssertionError(('NON_INTEGRAL',x,p))
    return num*pow(den,-1,p)%p

def direct(m,a,n,p):
    return residue(m(QQ(a)/n),p)

def cf_edges(a,n):
    """Return (sign,c,d) for edges including infinity->0; Sage CF only."""
    cf=continued_fraction(QQ(a)/n)
    convergents=[(int(r.numerator()),int(r.denominator())) for r in cf.convergents()]
    # infinity -> 0 = matrix identity, bottom row (0,1)
    yield 1,0,1
    for (u,v),(w,z) in zip(convergents,convergents[1:]):
        determinant=u*z-w*v
        if determinant not in (1,-1): raise AssertionError(('EDGE_DET',u,v,w,z,determinant))
        if determinant==1: yield 1,v,z
        else: yield -1,z,v
    if convergents[-1]!=(a,n): raise AssertionError(('CF_ENDPOINT',a,n,convergents[-1]))

def from_table(a,n,table,p):
    total=0
    for sign,c,d in cf_edges(a,n):
        idx=389 if c%N==0 else (d*pow(c,-1,N))%N
        total=(total+sign*table[idx])%p
    return total

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--table',default='/tmp/k107_table_p107.txt')
    ap.add_argument('--samples',type=int,default=120)
    ap.add_argument('--edges',type=int,default=160)
    ap.add_argument('--seed',type=int,default=389107)
    args=ap.parse_args()
    raw=Path(args.table).read_bytes()
    values=list(map(int,raw.split()))
    if len(values)!=393: raise AssertionError(('TABLE_LENGTH',len(values)))
    p,q1,q2=values[:3]; tab=values[3:]
    assert (p,q1,q2)==(107,369793,383917)
    assert len(tab)==390 and all(0<=v<p for v in tab)
    print('K107_INPUT_TABLE_SHA256',hashlib.sha256(raw).hexdigest(),flush=True)
    E=EllipticCurve(QQ,[0,1,1,-2,0]);n=q1*q2
    m=E.modular_symbol(sign=1,implementation='sage',normalize='L_ratio')
    # Check all entries against their defining rational cusps, using Sage not eclib.
    z=residue(m(QQ(0)),p)
    assert tab[389]==z
    for t in range(N):
        expected=(-z if t==0 else residue(m(QQ(-1)/t),p)-z)%p
        if tab[t]!=expected:raise AssertionError(('TABLE_MISMATCH',t,tab[t],expected))
    print('K107_ALL_390_TABLE_ENTRIES_INDEPENDENT_PASS',flush=True)
    rng=random.Random(args.seed)
    # Test Manin-class invariance directly for arbitrary unimodular matrices,
    # not just matrices from the production continued-fraction path.
    for k in range(args.edges):
        while True:
            c=rng.randint(1,3*N)
            d=rng.randint(1,3*N)
            if math.gcd(c,d)==1:break
        # gcd(d,c) = u*d + v*c =1 -> a=u, b=-v.
        gd,u,v=ZZ(d).xgcd(ZZ(c))
        assert gd==1
        a=int(u);b=-int(v)
        assert a*d-b*c==1
        actual=(residue(m(QQ(b)/d),p)-residue(m(QQ(a)/c),p))%p
        idx=(d*pow(c,-1,N))%N if c%N else 389
        if actual!=tab[idx]:raise AssertionError(('EDGE_INVARIANCE_FAIL',k,a,b,c,d,actual,tab[idx]))
    print('K107_SL2_EDGE_COSET_INVARIANCE_PASS',args.edges,flush=True)
    # Independent CF (Sage convergents) against independent Sage modular symbols.
    targets={1,2,3,1000,2_000_000,100_000_000,100_000_001,
             11_400_000_000,11_400_000_001,n//4,(n-1)//2}
    size=100_000_000
    for _ in range(args.samples):
        block=rng.randint(0,709)
        a=block*size+rng.randint(1,size)
        if a<=(n-1)//2:targets.add(a)
    checked=0
    for a in sorted(targets):
        if a<1 or a>=(n+1)//2 or math.gcd(a,n)!=1:continue
        x=from_table(a,n,tab,p)
        y=direct(m,a,n,p)
        if x!=y:raise AssertionError(('INDEPENDENT_CF_MISMATCH',a,x,y))
        checked+=1
    print('K107_INDEPENDENT_SAGE_CF_CUSP_PASS',checked,flush=True)
    print('K107_INDEPENDENT_MANIN_AUDIT_PASS',json.dumps({'p':p,'n':n,'seed':args.seed,'edges':args.edges,'cusps':checked}),flush=True)
    print('BOUNDARY: finite tests do not substitute for the algebraic Manin coset identity or verify all production operations',flush=True)
if __name__=='__main__':main()
