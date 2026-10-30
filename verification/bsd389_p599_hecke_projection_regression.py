#!/usr/bin/env python3
"""Independent exact p599 Manin-normalization and small p5 supersingular checks.

Run with Sage Python:
 python -u verification/bsd389_p599_hecke_projection_regression.py \
     --table ~/bsd389_p599_manin_table.txt

The 599 gate reads the source file and calls 390 independent Sage/eclib
modular symbols. The 5 gate directly evaluates the full level-5^3 Sage
Dp-valued coefficient (only 100 units), and compares against its exact
Hecke-reduced conductor-5^2 coefficient. No 599^3 enumeration is run.

Not a theorem prover; does not itself invoke p_primary_bound(599).
"""
import argparse
import hashlib
from pathlib import Path
from sage.all import EllipticCurve, QQ, ZZ

P=599
LEVEL=389
EXPECTED_HASH="fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8"

def mod_p(r,p):
    r=QQ(r)
    den=int(r.denominator())
    assert den%p, ("NONINTEGRAL_SYMBOL",r,p)
    return int(r.numerator())*pow(den,-1,p)%p

def verify_full_manin(table):
    raw=table.read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest==EXPECTED_HASH, ("TABLE_SHA256_MISMATCH",digest)
    seq=list(map(int,raw.split()))
    assert len(seq)==393 and seq[:3]==[599,6912461,13963889]
    vals=seq[3:392]; infty=seq[392]
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    L=E.padic_lseries(P)
    M=L._modular_symbol
    assert E.ap(P)==0 and E.real_components()==2
    m0=mod_p(M(QQ(0)),P)
    assert infty==m0,("TABLE_INFINITY_MISMATCH",infty,m0)
    for t in range(LEVEL):
        expected=(-m0 if t==0
                  else mod_p(M(QQ(-1)/t),P)-m0)%P
        assert vals[t]==expected,("MANIN_ENTRY_MISMATCH",t,vals[t],expected)
    print("P599_ALL_390_MANIN_ENTRIES_SAGE_MATCH_PASS",
          "p",P,"sha256",digest,flush=True)
    print("P599_ECLIB_NORMALIZATION_PASS","real_components",2,flush=True)

def coords(p,n):
    """Unit -> j via Teich representatives in Z/p^n."""
    mod=p**n
    gamma=1+p
    out={}
    for a0 in range(1,p):
        omega=pow(a0,p**(n-1),mod)
        g=1
        for j in range(p**(n-1)):
            v=(omega*g)%mod
            assert v not in out, ("CYCLOTOMIC_DUPLICATE",v)
            out[v]=j
            g=g*gamma%mod
    assert len(out)==(p-1)*p**(n-1)
    return out

def p5_direct_regression():
    p=5
    E=EllipticCurve("1483a1")
    assert E.ap(p)==0,("NOT_SUPERSINGULAR",E.ap(p))
    L=E.padic_lseries(p)
    M=L._modular_symbol
    factor=ZZ(E.real_components())
    assert factor in (1,2)
    j2=coords(p,2)
    j3=coords(p,3)
    w=lambda k:k*(k-1)//2
    c2=sum(QQ(w(j))*QQ(M(QQ(a)/p**2))
           for a,j in j2.items())
    A3=sum(QQ(w(j))*QQ(M(QQ(a)/p**3))
           for a,j in j3.items())
    B3=sum(QQ(w(j))*QQ(M(QQ(a)/p**2))
           for a,j in j3.items())
    assert mod_p(A3,p)==0, ("HECKE_A3_NONZERO",A3)
    assert mod_p(B3/p-c2,p)==0, ("HECKE_B3_P_MISMATCH",B3,c2)
    for b in range(1,p*p):
        if b%p==0:continue
        lhs=sum(QQ(M(QQ(b+t*p*p)/(p**3))) for t in range(p))
        rhs=E.ap(p)*QQ(M(QQ(b)/(p*p)))-QQ(M(QQ(b)/p))
        assert lhs==rhs,("HECKE_RELATION_EXACT_MISMATCH",b,lhs,rhs)
    predicted=mod_p(c2,p)*pow(int(factor),-1,p)%p
    dp=L.Dp_valued_series(n=3,prec=3)
    analytic0=dp[0][2]
    assert analytic0.valuation()==0, ("LOW_PRECISION_INSUFFICIENT",analytic0)
    actual=int(ZZ(analytic0.residue()))
    assert actual==predicted,("P5_DIRECT_VS_DERIVED_MISMATCH",actual,predicted)
    print("P5_HECKE_EXACT_ALL_FIBRES_PASS",p*(p-1),flush=True)
    print("P5_A3_MODP_ZERO_B3_OVER_P_MATCH_C2_PASS",flush=True)
    print("P5_SUPERSINGULAR_FULL_DP_VS_P2_SHORTCUT_PASS",
          "p",p,"real_components",int(factor),
          "C2",mod_p(c2,p),"derived_F0",predicted,
          "direct_Dp_F0",actual,flush=True)
    print("BOUNDARY: this p5 regression is independent convention testing, "
          "not a direct p599 analytic computation",flush=True)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--table",type=Path,required=True)
    parser.add_argument("--skip-p5",action="store_true")
    args=parser.parse_args()
    print("P599_ANALYTIC_BRIDGE_INDEPENDENT_REGRESSION_START",flush=True)
    verify_full_manin(args.table.expanduser())
    if not args.skip_p5:
        p5_direct_regression()
    print("P599_ANALYTIC_BRIDGE_INDEPENDENT_REGRESSION_FINISHED",flush=True)

if __name__=="__main__":
    main()
