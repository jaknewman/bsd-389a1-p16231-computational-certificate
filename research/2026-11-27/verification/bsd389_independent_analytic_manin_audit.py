#!/usr/bin/env python3
"""Independent Fourier/elliptic-period audit of all level-389 plus modular symbols.

No modular-symbol relations or Manin symbols are used to construct the
numerical values: a_n comes from #E(F_l) and Hecke recurrences; Ω from the
real Weierstrass roots and AGM. The Manin table is only read for comparison.
"""
import argparse, math, hashlib
from pathlib import Path
import numpy as np

LEVEL=389

def primes_through(maxn):
    mask=np.ones(maxn+1,dtype=np.bool_);mask[:2]=False
    for i in range(2,math.isqrt(maxn)+1):
        if mask[i]:mask[i*i::i]=False
    return np.flatnonzero(mask)

def coefficients(limit):
    primes=primes_through(limit)
    aps={}
    spf=np.arange(limit+1,dtype=np.int32)
    for p0 in primes:
        p=int(p0)
        if p*p<=limit:
            for k in range(p*p,limit+1,p):
                if spf[k]==k:spf[k]=p
        if p==LEVEL:
            aps[p]=1
            continue
        s=0
        for x in range(p):
            d=(1+4*(x*x*x+x*x-2*x))%p
            if d:s+=(1 if pow(d,(p-1)//2,p)==1 else -1)
        aps[p]=-s
    a=np.zeros(limit+1,dtype=np.int64);a[1]=1
    for n in range(2,limit+1):
        p=int(spf[n]);m=n//p
        a[n]=aps[p]*a[m]-(p*a[m//p] if m%p==0 and p!=LEVEL else 0)
    assert [int(a[i]) for i in range(1,12)]==[1,-2,-2,2,-3,4,-5,0,1,6,-4]
    return a,aps

def cubic_roots_real():
    def f(x):return 4*x*x*x+4*x*x-8*x+1
    intervals=[(-3.,-1.),(0.,.3),(.3,2.)]
    roots=[]
    for lo,hi in intervals:
        flo=f(lo)
        assert flo*f(hi)<0
        for _ in range(64):
            mid=(lo+hi)/2
            if f(mid)*flo>0:lo=mid;flo=flo
            else:hi=mid
        roots.append((lo+hi)/2)
    e3,e2,e1=roots
    q=math.sqrt((e1-e2)/(e1-e3))
    a,b=1.,q
    for _ in range(12):
        a,b=(a+b)/2,math.sqrt(a*b)
    period=math.pi/(a*math.sqrt(e1-e3))
    return period,roots

def symbol_from_table(a, n, tab):
    pn,pd,ln,ld=1,0,0,1
    x,y=n,a
    acc=tab[LEVEL]
    while y:
        q,r=divmod(x,y)
        nn,nd=q*ln+pn,q*ld+pd
        det=ln*nd-nn*ld
        assert abs(det)==1
        c,d=(ld,nd) if det==1 else (nd,ld)
        c%=LEVEL;d%=LEVEL
        idx=LEVEL if c==0 else d*pow(c,-1,LEVEL)%LEVEL
        acc+=det*tab[idx]
        pn,pd,ln,ld=ln,ld,nn,nd
        x,y=y,r
    assert (ln,ld)==(a,n)
    return acc

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--limit',type=int,default=6800)
    ap.add_argument('--table',default=str(Path(__file__).resolve().with_name('manin_390.txt')))
    opts=ap.parse_args()
    assert opts.limit>=3000
    data=open(opts.table,'rb').read()
    print('MANIN_SHA256',hashlib.sha256(data).hexdigest(),flush=True)
    tab=list(map(int,data.split()))
    assert len(tab)==390
    assert hashlib.sha256(data).hexdigest()=='9bce8b66c37b7f257f5a6015c08806c2b80c36d1e47356677e3819fc171e8360'
    a,aps=coefficients(opts.limit)
    period,roots=cubic_roots_real()
    ns=np.arange(1,opts.limit+1,dtype=np.float64)
    weights=a[1:]/ns*np.exp(-2*math.pi*ns/LEVEL)
    worst_err=0
    mismatches=[]
    rchecks={}
    for u in range(1,LEVEL):
        d=pow(u,-1,LEVEL)
        if d>LEVEL//2:d-=LEVEL
        val=np.sum(weights*(np.exp((2j*math.pi/LEVEL)*ns*u)-np.exp((-2j*math.pi/LEVEL)*ns*d)))
        ratio=val.real/period
        target=symbol_from_table(u,LEVEL,tab)
        err=abs(ratio-target)
        worst_err=max(worst_err,err)
        if err>1e-8:mismatches.append((u,ratio,target,err))
        if u in (1,2,3,5,7,11,13,14,21):rchecks[u]=(ratio,target,val.imag)
    # Deligne: |a_n| <= d(n)*sqrt(n) <= 2n (loose but enough); |a_n/n|<=2
    # each symbol is difference of two Fourier series; tail <= 4*q^(M+1)/(1-q)
    q=math.exp(-2*math.pi/LEVEL)
    bound=4*q**(opts.limit+1)/(1-q)
    print('FOURIER_LIMIT',opts.limit,'TAIL_BOUND_ABSOLUTE',bound,flush=True)
    print('AP_CONTROL',{p:aps[p] for p in [2,3,5,7,11,17,89,389]},flush=True)
    print('OMEGA_REAL_AGM',format(period,'.16f'),'ROOTS',roots,flush=True)
    print('ANCHOR_CHECKS',rchecks,flush=True)
    print('ALL_388_PLUS_SYMBOLS', 'PASS' if not mismatches else 'FAIL','WORST_ABS_ERROR',worst_err,'MISMATCHES',mismatches[:10],flush=True)
    if not mismatches: print('FOURIER_AGM_INDEPENDENT_NORMALIZATION_AUDIT_PASS',flush=True)
    if mismatches:raise SystemExit(1)
if __name__=='__main__': main()
