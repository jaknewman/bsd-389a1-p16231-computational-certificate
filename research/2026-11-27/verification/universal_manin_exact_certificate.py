#!/usr/bin/env python3
"""Exact, p-independent 390-Manin-edge certificate for E=389a1.

This is a finite proof of the UNIQUE rational symbol in the subspace cut out
by the Manin S/R/plus relations and sampled T2=-2 Hecke identities, after
normalization m(7/389)=-1. Relies on the standard Manin and Hecke identities
and independently established Neron cusp normalization. Never assumes BSD.

Usage: python3 bsd389_universal_manin_exact_certificate.py \
    --table manin_390.txt
"""
import argparse, hashlib
from fractions import Fraction
from math import gcd
from pathlib import Path

N=389
DIM=N+1

def idx(c,d):
    c%=N;d%=N
    return N if c==0 else d*pow(c,-1,N)%N

def rep(t): return (0,1) if t==N else (1,t)

def accumulate(terms):
    o={}
    for j,c in terms:
        o[j]=o.get(j,0)+c
        if o[j]==0:del o[j]
    return o

def manin_rows():
    for t in range(DIM):
        c,d=rep(t)
        yield accumulate([(idx(c,d),1),(idx(d,-c),1)])
        yield accumulate([(idx(c,d),1),(idx(d,-c-d),1),(idx(-c-d,c),1)])
        yield accumulate([(idx(c,d),1),(idx(-c,d),-1)])

def path(r):
    f=Fraction(r); f-=f.numerator//f.denominator
    a,n=f.numerator,f.denominator
    o={N:1}
    if a==0:return o
    pn,pd,ln,ld=1,0,0,1
    x,y=a,n
    q0,x,y=x//y,y,x%y
    assert q0==0
    while y:
        q,x,y=x//y,y,x%y
        nn,nd=q*ln+pn,q*ld+pd
        det=ln*nd-nn*ld
        assert abs(det)==1
        j=idx(ld,nd) if det==1 else idx(nd,ld)
        o[j]=o.get(j,0)+det
        if o[j]==0:del o[j]
        pn,pd,ln,ld=ln,ld,nn,nd
    assert (ln,ld)==(a,n)
    return o

def hecke_row(r,q,aq):
    terms=[]
    for val,co in [(r,aq),(q*r,-1)]+[(Fraction(r+t,q),-1) for t in range(q)]:
        terms.extend((j,co*c) for j,c in path(val).items())
    return accumulate(terms)

def evalrow(row,vec):return sum(a*vec[i] for i,a in row.items())

def mod_rank(rows,p):
    piv={}
    for row in rows:
        v={j:a%p for j,a in row.items() if a%p}
        while v:
            k=min(v)
            if k not in piv:
                inv=pow(v[k],-1,p)
                piv[k]={i:a*inv%p for i,a in v.items()}
                break
            a=v[k]
            for j,b in piv[k].items():
                x=(v.get(j,0)-a*b)%p
                if x:v[j]=x
                elif j in v:del v[j]
    return len(piv)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--table',type=Path,default=Path(__file__).with_name('bsd389_universal_manin_390.txt'))
    args=ap.parse_args()
    raw=args.table.read_text().strip()
    v=list(map(int,raw.split()))
    assert len(v)==DIM and all(-2<=x<=2 for x in v)
    sha=hashlib.sha256((' '.join(map(str,v))+'\n').encode()).hexdigest()
    counts={x:v.count(x) for x in sorted(set(v))}
    print('UNIVERSAL_TABLE_SHA256',sha,flush=True)
    print('UNIVERSAL_TABLE_COUNTS',counts,flush=True)
    rel=list(manin_rows())
    assert len(rel)==1170
    assert all(evalrow(r,v)==0 for r in rel)
    print('EXACT_INTEGRAL_MANIN_S_R_PLUS_PASS',len(rel),flush=True)
    r2=[hecke_row(Fraction(a,n),2,-2) for n in range(2,66) for a in range(1,n) if gcd(a,n)==1]
    assert len(r2)==1307
    assert all(evalrow(r,v)==0 for r in r2)
    print('EXACT_INTEGRAL_T2_HECKE_PASS',len(r2),flush=True)
    mr=mod_rank(rel+r2,7)
    assert mr==389
    print('RATIONAL_UNIQUENESS_VIA_MOD7_RANK_PASS',mr,'over_390',flush=True)
    # Another independent set of eigenrelations, NOT used to solve uniqueness.
    for q,aq in ((3,-2),(5,-3),(7,-5)):
        tested=0
        for n in range(2,54):
            for a in range(1,n):
                if gcd(a,n)!=1:continue
                assert evalrow(hecke_row(Fraction(a,n),q,aq),v)==0,(q,a,n)
                tested+=1
        print('INDEPENDENT_EXACT_INTEGRAL_HECKE_PASS','q',q,'ap',aq,'tested',tested,flush=True)
    s7=evalrow(path(Fraction(7,N)),v)
    s5=evalrow(path(Fraction(5,N)),v)
    s0=evalrow(path(Fraction(0)),v)
    assert (s7,s5,s0)==(-1,-2,0)
    print('EXACT_NERON_CUSP_ANCHORS_PASS',s7,s5,s0,flush=True)
    assert gcd(*v)==1
    print('PRIMITIVE_MANIN_VECTOR_PASS','gcd',gcd(*v),flush=True)
    for p in (5,7,11,13,17,19,23,29,31,37,41):
        print('PRIME_REDUCTION_AVAILABLE','p',p,'table_sha',sha[:16],flush=True)
    print('BOUNDARY: exact rational modular symbol; NOT automatic nonzero two-prime Kurihara for all p, NOT full BSD.')

if __name__=='__main__':main()
