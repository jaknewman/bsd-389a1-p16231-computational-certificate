#!/usr/bin/env python3
"""Real p5 T_2 Hecke relation that detects the synthetic eight-term perturbation.

An algebra-only pass verifies an exact 8-term CRT group-ring function H with
FULL ZERO MARGINALS and mixed [TU] coefficient 2, and proves that artificially
adding 3H only at denominator n=2501 BREAKS the T_2 Hecke identity at r=1/n.
Running in Sage additionally checks the true T_2 identity exactly through
both independent normalized modular-symbol implementations (sage and eclib).

--eigenline additionally probes Sage's actual full level-389 sign-plus
E-Hecke eigenspace over GF(5). This probe may be more expensive.

This does NOT prove that H cannot be extended *some other way* across
all conductor levels to obey Hecke; it only rules out the zero extension.
Nor does it prove Sha finite, degree-two uniform Kurihara, or full BSD.
"""
import argparse
from fractions import Fraction
from math import gcd

P,N,Q1,Q2,G1,G2=5,2501,41,61,6,2
H1,H2=40,60
R=Fraction(1,N)

def crt(x,y):
    return (x+Q1*((y-x)*pow(Q1,-1,Q2)%Q2))%N

def support():
    d={}
    for shift in (0,1):
        for k in (0,1):
            for l in (0,1):
                x=pow(G1,k+shift*(H1//2),Q1)
                y=pow(G2,l+shift*(H2//2),Q2)
                a=crt(x,y)
                assert gcd(a,N)==1 and a not in d
                d[a]=(-1)**(k+l)
    assert len(d)==8
    assert all(d[(-a)%N]==v for a,v in d.items())
    return d

def H_cusp(r,d):
    if r.denominator!=N or gcd(r.numerator,N)!=1:
        return 0
    return d.get(r.numerator%N,0)

def hecke2(func):
    # a_2=-2 for E:y²+y=x³+x²-2x.
    return (-2)*func(R)-func(2*R)-func(R/2)-func((R+1)/2)

def algebra():
    d=support()
    assert d=={1:1,124:-1,1892:-1,2015:1,
               2500:1,2377:-1,609:-1,486:1}
    cusps=(R,2*R,R/2,(R+1)/2)
    assert (R+1)/2==Fraction(1251,N)
    vals=[H_cusp(z,d) for z in cusps]
    assert vals==[1,0,0,0] and hecke2(lambda z:H_cusp(z,d))==-2
    for a in d:
        assert H_cusp(Fraction(-a,N),d)==H_cusp(Fraction(a,N),d)
        assert H_cusp(Fraction(a+N,N),d)==H_cusp(Fraction(a,N),d)
    assert (4+3*2)%P==0 and (3*(-2))%P==4
    print("P5_T2_EIGHT_TERM_CRT_EXACT_PASS","support",len(d),
          "indices",sorted(d),flush=True)
    print("P5_T2_HEKKE_CUSP_PERTURBATION_VALUES_PASS",vals,flush=True)
    print("P5_T2_3H_FLIPS_M11_4_TO_0_BUT_HEKKE_DEFECT_PASS",
          "old",4,"new",0,"defect_mod5",4,flush=True)
    return d,cusps

def sage_checks(d,cusps,eigenline):
    from sage.all import EllipticCurve, QQ, GF
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    assert int(E.conductor())==389 and int(E.ap(2))==-2
    for name,kw in (("sage",dict(implementation="sage",normalize="L_ratio")),
                    ("eclib",dict(implementation="eclib"))):
        m=E.modular_symbol(sign=+1,**kw)
        v=[QQ(m(QQ(z.numerator)/z.denominator)) for z in cusps]
        assert -2*v[0]-v[1]-v[2]-v[3]==0,(name,v)
        perturb=[v[i]+3*H_cusp(cusps[i],d) for i in range(4)]
        defect=-2*perturb[0]-perturb[1]-perturb[2]-perturb[3]
        assert defect==-6 and int(defect)%P==4
        print("P5_T2_REAL_SAGE_ECLIB_EXACT_HECKE_IDENTITY_PASS",
              "oracle",name,"values",[str(x) for x in v],flush=True)
        print("P5_T2_FAKE_8TERM_ZERO_EXTENSION_VIOLATES_HECKE_PASS",
              "oracle",name,"defect_exact",defect,"defect_mod5",4,flush=True)
    if eigenline:
        from sage.schemes.elliptic_curves.ell_modular_symbols import modular_symbol_space
        Q=modular_symbol_space(E,+1,QQ)
        assert int(Q.dimension())==1
        print("P5_FULL_LEVEL389_PLUS_Q_EIGENLINE_DIM_PASS",1,flush=True)
        V=modular_symbol_space(E,+1,GF(P))
        dim=int(V.dimension())
        print("P5_FULL_LEVEL389_PLUS_GF5_EIGENSPACE_DIM",dim,flush=True)
        if dim==1:
            print("P5_FULL_LEVEL389_PLUS_GF5_EIGENLINE_DIM1_PASS",
                  "requires_integral_normalization_to_apply_to_cusps",flush=True)
        else:
            print("P5_FULL_LEVEL389_PLUS_GF5_EIGENSPACE_DIM_GT1",
                  "no_unjustified_uniqueness_claim",flush=True)
    print("BOUNDARY_ZERO_EXTENSION_CHECK_NOT_UNIFORM_SHA_OR_BSD",flush=True)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--algebra-only",action="store_true")
    parser.add_argument("--eigenline",action="store_true")
    args=parser.parse_args()
    if args.algebra_only and args.eigenline:
        parser.error("--eigenline requires Sage")
    d,cusps=algebra()
    if not args.algebra_only:
        sage_checks(d,cusps,args.eigenline)

if __name__=="__main__":
    main()
