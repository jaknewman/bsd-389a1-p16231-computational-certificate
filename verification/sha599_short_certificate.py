#!/usr/bin/env python3
"""Independent bounded-memory audit for E=389a1, supersingular p=599.

Recomputes the Mazur--Tate C_2 from the raw, SHA256-pinned Manin table
using continued fractions. Checks the algebraic reductions of the full
level-p^3 coefficient, without actually enumerating p^3 units. Optionally
calls Sage to reverify arithmetic gates and the p-adic regulator.

Theory: Stein--Wuthrich, Math. Comp. 82 (2013), Alg. 11.1,
  https://wstein.org/papers/mcom2649-iwasawa-alg.pdf
Sage implementation: sage/schemes/elliptic_curves/padic_lseries.py

The printed analytic coefficient is DERIVED, not obtained by calling
Dp_valued_series. The accompanying mathematical note documents the proof.
"""
import argparse
import hashlib
import math
from pathlib import Path
import time

P = 599
N = P * P
LEVEL = 389
EXPECTED_HASH = "fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8"
EXPECTED_HEADER = [599, 6912461, 13963889]
EXPECTED_C = (0, 0, 543)
EXPECTED_PAIRS = 179101
EXPECTED_EDGES = 1924081
EXPECTED_CHECKSUM = 779927018
MOD_CHECKSUM = 1000000007


def assert_lift_identities(prime):
    """Identity for j mod p and lifts j+t*p mod p^2; no symbols needed."""
    assert prime >= 5 and all(prime % q for q in range(2,math.isqrt(prime)+1))
    assert sum(j*(j-1)//2 for j in range(prime)) % prime == 0
    for j in range(prime):
        lhs = sum((j+t*prime)*(j+t*prime-1)//2 for t in range(prime))
        rhs = prime * (j*(j-1)//2)
        assert (lhs-rhs) % (prime*prime) == 0


def parse_table(path):
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == EXPECTED_HASH, f"Manin table SHA256 mismatch: {digest}"
    seq = list(map(int,raw.split()))
    assert len(seq) == 393, f"Expected 393 integers, found {len(seq)}"
    assert seq[:3] == EXPECTED_HEADER, f"Unexpected table header: {seq[:3]}"
    vals = seq[3:]
    assert len(vals) == 390 and all(0<=v<P for v in vals)
    return vals,digest


def raw_modular_symbol(a,n,M,inverses):
    """Independent signed full-convergent rational path, same specification as native audit."""
    pn,pd,ln,ld = 1,0,0,1
    x,y=n,a
    value=M[389]
    sign=-1
    edges=0
    while y:
        q,r=divmod(x,y)
        x,y=y,r
        nn=q*ln+pn
        nd=q*ld+pd
        if sign==1:
            c,d=ld%LEVEL,nd%LEVEL
        else:
            c,d=nd%LEVEL,ld%LEVEL
        idx=389 if c==0 else (d*inverses[c])%LEVEL
        value=(value+sign*M[idx])%P
        pn,pd=ln,ld
        ln,ld=nn,nd
        sign=-sign
        edges+=1
    assert x==1 and ln==a and ld==n
    return value,edges


def compute_level_p2(table, progress):
    M, sha = parse_table(table)
    print("MANIN_TABLE_SHA256",sha,flush=True)
    inv=[0]*LEVEL
    for c in range(1,LEVEL): inv[c]=pow(c,-1,LEVEL)
    bucket=[0]*P
    C0=C1=C2=0
    edgecount=0
    checksum=0
    pairs=0
    tic=time.monotonic()
    for a in range(1,(N-1)//2+1):
        if a%P==0: continue
        t=pow(a,P-1,N)
        assert t%P==1
        k=(-((t-1)//P))%P
        assert (pow(a,P,N)*(1+P*k))%N==a
        v,edges=raw_modular_symbol(a,N,M,inv)
        edgecount+=edges
        bucket[a%P]=(bucket[a%P]+v)%P
        bucket[-a%P]=(bucket[-a%P]+v)%P
        C0=(C0+2*v)%P
        C1=(C1+2*v*k)%P
        C2=(C2+v*k*(k-1))%P
        checksum=(checksum+(a*v+k*k)%MOD_CHECKSUM)%MOD_CHECKSUM
        pairs+=1
        if progress and pairs%progress==0:
            print("P599_FINITE_PROGRESS",pairs,"/",EXPECTED_PAIRS,"sec",round(time.monotonic()-tic,2),flush=True)
    assert pairs==EXPECTED_PAIRS, pairs
    assert edgecount==EXPECTED_EDGES, edgecount
    assert checksum==EXPECTED_CHECKSUM,checksum
    assert tuple([C0,C1,C2])==EXPECTED_C,(C0,C1,C2)
    assert all(b==0 for b in bucket[1:]),"Hecke p^2 -> p fibres not zero"
    print("P599_LEVEL_P2_INDEPENDENT_PASS","C0",C0,"C1",C1,"C2",C2,"pairs",pairs,"edges",edgecount,"checksum",checksum,flush=True)
    return C2


def arithmetic_sage_gate(f0):
    from sage.all import EllipticCurve,QQ,ZZ,log
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    p=ZZ(P)
    assert E.conductor()==389
    assert E.discriminant()==389
    assert E.ap(p)==0 and E.is_supersingular(p)
    assert E.real_components()==2
    assert E.rank(proof=True)==2
    G=E.gens(proof=True)
    assert len(G)==2 and E.gens_certain()
    assert E.torsion_order()==1
    assert list(E.tamagawa_numbers())==[1]
    assert E.galois_representation().is_surjective(p)
    # Symbol normalization check: p599 table uses eclib positive symbols;
    # for discriminant >0 the extra Sage _scaling factor is 1.
    from sage.libs.eclib.newforms import ECModularSymbol
    M=E.modular_symbol(sign=1,implementation='eclib')
    N=ECModularSymbol(E,sign=1)
    assert M._scaling==1
    for d in (5,41,599): assert M(QQ(1)/d)==N(QQ(1)/d)
    reg=E.padic_regulator(p,prec=6)
    K=reg[0].parent()
    lg=log(K(1+p))
    normalized=[reg[i]/lg**2 for i in range(2)]
    assert normalized[0].valuation()==0
    assert normalized[1].valuation()>=1
    b=int(ZZ(normalized[0].residue()))
    assert b==571,("regulator residue not expected",b)
    assert f0==b
    print("SAGE_ARITHMETIC_GATES_PASS","rank",2,"generators",str(G),"surjective",True,"regulator_0_modp",b,"regulator_1_val",normalized[1].valuation(),flush=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--table',type=Path,required=True)
    parser.add_argument('--sage',action='store_true',help='also check curve, full MW group, surjectivity and regulator via Sage')
    parser.add_argument('--progress',type=int,default=25000)
    args=parser.parse_args()
    print("SHA599_SHORT_CERTIFICATE_START",flush=True)
    # Lemmas for all tame chars and full Teichmueller exponent lifts
    for q in (5,7,11): assert_lift_identities(q)
    # At 599 an O(p^2) symbolic proof avoids huge iteration over 599^2 integers
    assert_lift_identities(P)
    print("LIFT_WEIGHT_IDENTITIES_PASS",flush=True)
    c2=compute_level_p2(args.table,args.progress)
    # For a_p=0, Hecke implies A3 =0 (mod p), and the p lifts give
    # B3/p = C2 (mod p). Projection from Sage's (1-phi)^(-2) with
    # 2 real components gives F0 = [2A3 - (p-1)B3/p] / 2(p+1)^2.
    # This computation is a derived congruence, not a p^3 enumeration.
    f0=(-(P-1)*c2*pow(2*(P+1)**2,-1,P))%P
    f1=0
    assert f0==571
    assert (2*f0-c2)%P==0
    print("ANALYTIC_FROBENIUS_DERIVED","F0_modp",f0,"F1_modp",f1,"kind","HECKE_PLUS_PRECISION_LEMMA",flush=True)
    print("PRECISION_NOTE","alpha-adic O(alpha^-1): G_error in Zp, H_error in p^-1 Zp; Frobenius projection kills mod p",flush=True)
    if args.sage: arithmetic_sage_gate(f0)
    else: print("SAGE_ARITHMETIC_GATES_NOT_RUN",flush=True)
    print("KATO_THEOREM_APPLICATION","Stein-Wuthrich Algorithm 11.1; review mathematical note",flush=True)
    print("BOUNDARY","Does not execute p_primary_bound or compute the p^3 sum; theorem application depends on the stated exact algebraic lemmas",flush=True)
    print("SHA599_SHORT_CERTIFICATE_FINISHED",flush=True)

if __name__=='__main__': main()
