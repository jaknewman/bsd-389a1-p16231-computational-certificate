#!/usr/bin/env python3
"""Three AUTHENTIC integer cyclotomic resultants for E=389a1.

Default: recompute from the frozen genuine Manin-390 vector all 1,200 and
196,020 plus-symmetry primitive classes at p5/q41*61 and p11/q397*991,
then compute exact integer resultants of their actual diagonal theta
polynomials. With --depth25-hist PATH, ALSO audit the genuine 28,488,750
class p5-depth25 histogram produced by
verification/bsd389_p5_depth25_full_integer_hist_native.cpp.

This is stronger evidence than the synthetic coefficient/resultant tests,
but it is prime-specific: neither all-large-p Sha finite nor full BSD.
"""
from math import isqrt
from pathlib import Path
import argparse
import hashlib
import sympy as sp

N=389
COMPACT=("22222423212322123232122231233221001122123213121002222221111022224"
"23222221112200001122102211013344223321321111111113232331212112202"
"22323121333422232134222244424332233424333433333443223233222010022"
"22001022233232234433333433342433223342444222243123222433312132322"
"20221121213323231111111112312332244331011220122110000221112222232"
"42222011112222220012131232122110012233213222123232122321232422222")
assert len(COMPACT)==390
V=tuple(int(c)-2 for c in COMPACT)
assert V[389]==0
assert hashlib.sha256(bytes(v+2 for v in V)).hexdigest()=="31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee"
INV=[0]+[pow(j,-1,N) for j in range(1,N)]
x=sp.Symbol("x")
EXPECTED={
    (5,41,61):(4,52128400,2085136,1200),
    (11,397,991):(1,156470779894879023760384,1293146941279991931904,196020),
    (25,5351,10651):(22,23029075931778856293480525074058280758975693396694573028552616039759085259154270453760000,
                      36846521490846170069568840118493249214361109434711316845684185663614536414646832726016,
                      28488750),
}

def symbol(a,n):
    pn,pd,ln,ld=1,0,0,1
    u,v=n,a;acc=V[N]
    while v:
        quo,rem=divmod(u,v)
        u,v=v,rem
        nn=quo*ln+pn
        nd=quo*ld+pd
        det=ln*nd-nn*ld
        assert det in (-1,1)
        c,d=(ld,nd) if det==1 else (nd,ld)
        c%=N;d%=N
        acc+=det*V[(d*INV[c])%N if c else N]
        pn,pd,ln,ld=ln,ld,nn,nd
    assert (ln,ld)==(a,n)
    return acc

def primitive_root(q):
    n=q-1
    factors=sp.factorint(n)
    return next(g for g in range(2,q)
                if all(pow(g,n//r,q)!=1 for r in factors))

def logs(q,m):
    g=primitive_root(q);out=[-1]*q;t=1
    for i in range(q-1):
        assert out[t]<0
        out[t]=i%m
        t=t*g%q
    assert t==1
    return g,out

def authentic_hist(m,q1,q2):
    n=q1*q2
    assert (q1-1)%(2*m)==(q2-1)%(2*m)==0
    g1,L1=logs(q1,m);g2,L2=logs(q2,m)
    hist=[0]*m;count=0
    for a in range(1,(n-1)//2+1):
        a1,a2=a%q1,a%q2
        if not a1 or not a2:continue
        hist[(L1[a1]+L2[a2])%m]+=2*symbol(a,n)
        count+=1
    assert count==(q1-1)*(q2-1)//2
    return hist,count,(g1,g2)

def check(hist,m,q1,q2,count):
    assert len(hist)==m
    delta,B_expected,R_expected,N_expected=EXPECTED[(m,q1,q2)]
    assert count==N_expected
    c0=sum(hist)
    c1=sum(j*z for j,z in enumerate(hist))
    c2=sum(j*(j-1)//2*z for j,z in enumerate(hist))
    assert c0==0 and c1%m==0 and c2%m==delta
    F=sp.Poly(sum(z*x**j for j,z in enumerate(hist)),x)
    S=sp.Poly(sum(x**j for j in range(m)),x)
    B=int(sp.resultant(F,S,x))
    assert B==B_expected and B%m**2==0
    R=B//m**2
    assert R==R_expected
    p=next(iter(sp.factorint(m)))
    assert R%p==1
    print("AUTHENTIC_FULL_MAZUR_TATE_INTEGER_RESULTANT_PASS",
          "p",p,"depth",m,"conductor",q1*q2,"representatives",count,
          "c0",c0,"c1",c1,"c2",c2,"c2_mod_pk",delta,
          "resultant_digits",len(str(abs(B))),
          "resultant",B,"normalized_resultant",R,
          "normalized_modp",R%p,flush=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--depth25-hist",type=Path)
    args=ap.parse_args()
    for m,q1,q2 in ((5,41,61),(11,397,991)):
        hist,count,roots=authentic_hist(m,q1,q2)
        assert roots==((6,2) if m==5 else (5,6))
        check(hist,m,q1,q2,count)
    if args.depth25_hist:
        entries=args.depth25_hist.read_text().splitlines()
        count=int(entries[0].split()[1])
        hist=[int(z) for z in entries[1].split()[1:]]
        assert len(hist)==25 and count==28488750
        check(hist,25,5351,10651,count)
    print("AUTHENTIC_RESULTANT_BOUNDARY_NO_UNIFORM_SHA_ANNIHILATOR")

if __name__=="__main__":
    main()
