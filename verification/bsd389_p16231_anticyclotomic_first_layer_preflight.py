#!/usr/bin/env python3
"""Exact arithmetic preflight for Castella–Hsieh's *trivial-character* theta.

K=Q(sqrt(-3)), E=389a1, p=16231, N-=389. This code computes the
first p-primary ring-class layer and a local split coordinate mod p^2.

This is NOT a computation of Gross points P_n^a, the quaternionic
local embedding into M_2(Z_p), or the actual theta coefficient.

Optional --moments-json PATH accepts 16231 aggregated rows:
{"p":16231,"rows":[{"i":0,"sum_phi_P1":integer,"sum_phi_P2":integer},...]}
where each sum is over a in mu_(p-1) in the exact Castella–Hsieh
Appendix n=1 formula. It checks lengths, indices, and extracts
c_0,c_1,c_2 mod p from those input rows. Their arithmetic correctness
is NOT certified by this extractor; even c0=c1=0 modp does not prove
these coefficients vanish integrally.
"""
import argparse
import hashlib
import json
from math import gcd
from pathlib import Path

P = 16231
N = 389

def roots_mod_p2():
    assert P % 4 == 3 and P % 3 == 1
    d = (-3) % P
    z = pow(d, (P+1)//4, P)
    assert z*z % P == d
    inv2 = pow(2, -1, P)
    roots = sorted({((-1+z)*inv2) % P, ((-1-z)*inv2) % P})
    assert len(roots) == 2
    lifted = []
    for r in roots:
        assert (r*r+r+1) % P == 0
        deriv = (2*r+1) % P
        assert deriv != 0
        k = (-((r*r+r+1)//P) * pow(deriv,-1,P)) % P
        s = r+k*P
        assert (s*s+s+1) % (P*P) == 0
        lifted.append(s)
    a,b = lifted
    assert (a+b+1)%(P*P)==0
    assert a*b%(P*P)==1
    return roots,lifted

def extract_moments(path):
    raw=Path(path).read_bytes()
    data=json.loads(raw)
    assert data["p"]==P
    rows=data["rows"]
    assert len(rows)==P
    u0=u1=u2=0
    for i,row in enumerate(rows):
        assert row["i"] == i
        s1=row["sum_phi_P1"]
        s2=row["sum_phi_P2"]
        assert type(s1) is int and type(s2) is int
        w=(128*s1-s2)%P
        u0=(u0+w)%P
        u1=(u1+w*i)%P
        u2=(u2+w*(i*(i-1)//2))%P
    scale=pow(128,-2,P)
    result=[scale*v%P for v in (u0,u1,u2)]
    print("THETA_N1_AGGREGATE_SHA256",hashlib.sha256(raw).hexdigest(),flush=True)
    print("THETA_N1_FIRST_THREE_MOMENTS_FROM_SUPPLIED_ROWS",result,flush=True)
    print("BOUNDARY_ROWS_THEMSELVES_NOT_AUTHENTICATED_AS_GROSS_POINTS",flush=True)
    print("BOUNDARY_MODP_LOWER_TERMS_ZERO_NOT_PROOF_OF_EXACT_VANISHING",flush=True)
    print("BOUNDARY_THETA_ORDER_TWO_NOT_CERTIFIED_BY_THIS_EXTRACTOR",flush=True)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--moments-json",type=Path)
    args=parser.parse_args()
    assert P!=N
    assert N%3==2 and P%3==1
    roots,lifted=roots_mod_p2()
    print("K_MINUS3_P16231_SPLIT_ROOTS_MODP_PASS",roots,flush=True)
    print("K_MINUS3_P16231_HENSEL_ROOTS_MODP2_PASS",lifted,flush=True)
    # Ring class number formula for nonmaximal order of conductor p^n:
    # h(O_f)=f/[O_K^x:O_f^x] prod_l|f (1-chi_K(l)/l).
    # h(K)=1, unit index 3 for f>1, chi_K(p)=1.
    h_p=(P-1)//3
    h_p2=P*(P-1)//3
    assert h_p==5410 and h_p2==87809710
    assert h_p%P!=0 and h_p2%P==0
    assert h_p2//h_p==P
    print("K_MINUS3_RINGCLASS_CONDUCTOR_P_ORDER_PASS",h_p,flush=True)
    print("K_MINUS3_RINGCLASS_CONDUCTOR_P2_ORDER_PASS",h_p2,flush=True)
    print("K_MINUS3_FIRST_P_PRIMARY_QUOTIENT_AT_P2_PASS",P,flush=True)
    # For p split, (O_K / p^2)^x / (Z/p^2)^x has a cyclic order-p
    # principal-unit factor. This is local algebra, not a quaternion embedding.
    assert pow(1+P,P,P*P)==1 and (1+P)%(P*P)!=1
    print("LOCAL_PRINCIPAL_UNIT_CYCLIC_ORDER_P_PASS",flush=True)
    alpha_inv2=pow(128,-2,P)
    assert alpha_inv2==4986
    print("E389A1_ALPHA_INVERSE_SQUARED_MODP_PASS",alpha_inv2,flush=True)
    assert P*(P-1)==263429130
    print("CH_THETA_N1_RAW_TWO_INDEX_EVALUATION_COUNT",P*(P-1),flush=True)
    if args.moments_json:
        extract_moments(args.moments_json)
    else:
        print("THETA_GROSS_POINT_AGGREGATES_NOT_PROVIDED",flush=True)
    print("BOUNDARY_CH_THETA_CHARACTERS_TRIVIAL_NOT_CHI53",flush=True)
    print("BOUNDARY_ORD_T_THETA_EQUALS_2_NOT_PROVED",flush=True)
    print("ANTICYCLOTOMIC_FIRST_LAYER_PREFLIGHT_PASS",flush=True)

if __name__=="__main__":
    main()
