#!/usr/bin/env python3
"""Finite-level cyclotomic Mazur–Tate probe at conductor p^2, p=5,7,599.

Calculates three tame-trivial Gamma moments C_j, j=0,1,2, from authentic
Neron-normalized plus modular symbols and audits EVERY Hecke p^2 -> p
fibre. This is NOT the q1*q2 Kurihara number and gives NO Sha bound.

Run in SageMath:
 python -u verification/bsd389_p599_cyclotomic_p2_moment_probe.py --p 599 --table ~/bsd389_p599_manin_table.txt
 python -u verification/bsd389_p599_cyclotomic_p2_moment_probe.py --p 5
"""
import argparse
import hashlib
import time
from pathlib import Path
from sage.all import EllipticCurve, QQ
from sage.libs.eclib.newforms import ECModularSymbol
from kurihara_manin_390_fast import table_390, symbol_by_manin

def coordinates(a,p):
    pp=p*p
    assert 1<=a<pp and a%p
    q=pow(a,p-1,pp)
    assert q%p==1
    k=(-(q-1)//p)%p
    assert (1+p*k)%pp==pow(a,1-p,pp)
    return k

def load_table(p,file):
    if file is None:
        E=EllipticCurve(QQ,[0,1,1,-2,0])
        return table_390(ECModularSymbol(E,sign=1),p)
    raw=file.read_bytes()
    a=list(map(int,raw.split()))
    assert len(a)==393 and a[0]==p
    assert all(0<=v<p for v in a[3:])
    if p==599:
        assert a[:3]==[599,6912461,13963889]
        assert hashlib.sha256(raw).hexdigest()=='fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8'
    print('CYCLOTOMIC_MANIN_TABLE_SHA256',hashlib.sha256(raw).hexdigest(),flush=True)
    return a[3:392],a[392]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--p',type=int,choices=(5,7,599),default=599)
    ap.add_argument('--table',type=Path,default=None)
    ap.add_argument('--progress',type=int,default=0)
    a=ap.parse_args()
    p=a.p; n=p*p
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    ap_E=int(E.ap(p))
    vals,infty=load_table(p,a.table)
    assert len(vals)==389
    s0=int(infty)
    if p==599:
        assert ap_E==0 and s0==0,('supersingular/rank-two normalization',ap_E,s0)
    print('CYCLOTOMIC_P2_CONFIG','p',p,'n',n,'a_p',ap_E,'S0_modp',s0,flush=True)
    s_at_p=[0]*p
    for b in range(1,p):
        s_at_p[b]=int(symbol_by_manin(b,p,p,(vals,infty)))
    buckets=[0]*p
    moments=[0,0,0]
    seen=0
    start=time.monotonic()
    # All nonzero units are paired a <-> -a by the plus-symbol.
    for aa in range(1,(n-1)//2+1):
        if aa%p==0:
            continue
        b=aa%p
        s=int(symbol_by_manin(aa,n,p,(vals,infty)))
        k=coordinates(aa,p)
        assert coordinates(n-aa,p)==k
        for bb in (b,p-b):
            buckets[bb]=(buckets[bb]+s)%p
        moments[0]=(moments[0]+2*s)%p
        moments[1]=(moments[1]+2*s*k)%p
        moments[2]=(moments[2]+2*s*(k*(k-1)//2))%p
        seen+=1
        if a.progress and seen%a.progress==0:
            print('CYCLOTOMIC_P2_PROGRESS',seen,'of',p*(p-1)//2,flush=True)
    assert seen==p*(p-1)//2
    # Weight-two Hecke relation:
    # a_p S(b/p) = S(b) + sum_{j=0}^{p-1} S((b+j*p)/p^2).
    for b in range(1,p):
        expected=(ap_E*s_at_p[b]-s0)%p
        assert buckets[b]==expected,('HECKE_P2_FIBRE_MISMATCH',p,b,buckets[b],expected)
    print('CYCLOTOMIC_P2_ALL_HECKE_FIBRES_PASS',p-1,flush=True)
    for aa in (1,2,3,p-1,p+1,n//2):
        if aa%p==0:continue
        assert symbol_by_manin(aa,n,p,(vals,infty))==symbol_by_manin(n-aa,n,p,(vals,infty))
        k=coordinates(aa,p)
        assert (pow(aa,p,n)*(1+p*k))%n==aa%n
    assert sum(buckets)%p==moments[0]
    print('CYCLOTOMIC_P2_PARITY_GAMMA_PASS','pairs',seen,flush=True)
    if ap_E%p==0 and s0==0:
        assert all(buckets[b]==0 for b in range(1,p))
        assert moments[0]==0
        print('CYCLOTOMIC_P2_SUPERSINGULAR_ZERO_AUGMENTATIONS_PASS',p-1,flush=True)
    print('CYCLOTOMIC_P2_TAME_TRIVIAL_MOMENTS',p,
          'C0',moments[0],'C1',moments[1],'C2',moments[2],
          'seconds',round(time.monotonic()-start,3),flush=True)
    print('BOUNDARY: finite cyclotomic theta moments, NOT Kurihara delta, Selmer or Sha.',flush=True)

if __name__=='__main__':
    main()
