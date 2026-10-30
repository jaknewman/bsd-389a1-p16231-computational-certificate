#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""389a1 at p=16231: (i) a rigorous Sage bound for Sha[p^infinity];
(ii) an exact modulo-p aggregator for the anticyclotomic theta coefficients.

Reference for theta: Castella--Hsieh, Forum Math. Sigma 10 (2022),
Appendix section 6, formula for Theta_(f/K,n).

This program DOES NOT manufacture level-p^2 Gross point evaluations.
For --a2, you must supply p authentic, exhaustive sums s_i =
    sum_{a in mu_{p-1}} phi_f(P_2^{a(1+p)^i}),  0 <= i < p,
in newline-delimited JSON, with records of form
    {"i": 0, "sum_p2": 12345678, "count": 16230}
(each sum contains precisely p-1 genuine CM evaluations). The program
certifies the combinatorial reduction and accumulated residues, not
provenance/adelic identification of the externally computed values.

The order of vanishing of Theta is NOT certified merely by a2 mod p:
its constant and linear terms must separately vanish EXACTLY in Z_p.

Modes:
  python -u bsd389_a2_sha_16231.py --selftest
  python -u bsd389_a2_sha_16231.py --sha
  python -u bsd389_a2_sha_16231.py --sha --order
  python -u bsd389_a2_sha_16231.py --a2 /path/to/p2_sums.jsonl
"""
import argparse
import hashlib
import json
from pathlib import Path

P = 16231
A_P = 128


def moment_coeff(j, i, p=P):
    if j == 0:
        return 1
    if j == 1:
        return i
    if j == 2:
        return (i * (i-1) // 2) % p
    raise ValueError("only degrees 0,1,2 are supported")


def selftest():
    assert P > 3 and pow(A_P, 2, P) != 0
    inv = pow(A_P, -2, P)
    assert inv == 4986
    # sum_{i=0}^{p-1} binom(i,j) = binom(p,j+1) == 0 mod p,
    # for j=0,1,2 and every p>3. Thus the P_1 term cancels mod p.
    for j in range(3):
        coeff_sum = sum(moment_coeff(j,i,P) for i in range(P)) % P
        assert coeff_sum == 0, ("P1_NONCANCELLATION", j, coeff_sum)
    # an exact sanity check for the factor -alpha^{-2} mod p
    assert (-inv) % P == 11245
    print("A2_P1_TERM_CANCELLATION_ALL_DEGREES_0_TO_2_PASS",flush=True)
    print("A2_ALPHA_UNIT_ROOT_MOD_P", A_P,flush=True)
    print("A2_NEG_ALPHA_INVERSE_SQUARED_MOD_P", (-inv)%P,flush=True)
    print("A2_REQUIRED_P2_GROSS_EVALUATIONS", P*(P-1),flush=True)
    print("A2_NUMBER_OF_AGGREGATED_ROWS",P,flush=True)


def aggregate_a2(inputfile, output):
    selftest()
    sums = [None]*P
    counts = [None]*P
    digest = hashlib.sha256()
    with inputfile.open('rb') as f:
        for k, raw in enumerate(f,1):
            digest.update(raw)
            if not raw.strip():
                continue
            row = json.loads(raw)
            i = int(row['i'])
            assert 0 <= i < P, ("ROW_INDEX_OUT_OF_RANGE", k, i)
            assert sums[i] is None, ("ROW_DUPLICATE", k, i)
            count = int(row['count'])
            assert count == P-1, ("INCOMPLETE_A_SUM", k, count)
            sums[i] = int(row['sum_p2']) % P
            counts[i] = count
    missing = [i for i,x in enumerate(sums) if x is None]
    print("A2_INPUT_SHA256",digest.hexdigest(),flush=True)
    print("A2_AGGREGATED_ROWS",P-len(missing),"OF",P,flush=True)
    if missing:
        print("A2_STATUS INCOMPLETE_NO_CERTIFICATE",flush=True)
        print("A2_FIRST_MISSING_INDEX",missing[0],flush=True)
        return 2
    total = P*(P-1)
    moments = [sum(moment_coeff(j,i)*sums[i] for i in range(P))%P for j in range(3)]
    scale = (-pow(A_P, -2, P))%P
    coefficients = [scale*m%P for m in moments]
    print("A2_AUTHENTIC_P2_GROSS_VALUES_CLAIMED",total,flush=True)
    for j,val in enumerate(coefficients):
        print("THETA_COEFF_DEGREE_%d_MOD_%d"%(j,P),val,flush=True)
    print("A2_MOD_P_NONZERO",bool(coefficients[2]),flush=True)
    print("BOUNDARY: a_0=a_1 EXACTLY ZERO not certified by residue checks",flush=True)
    print("BOUNDARY: Gross point value origin and i_p convention are external",flush=True)
    rep={"curve":"389a1","p":P,"a_p":A_P,
         "sha256":digest.hexdigest(),"rows":P,"values_claimed":total,
         "coeff_mod_p":coefficients,
         "status":"THETA_MOD_P_DEGREES_0_1_2_AGGREGATED",
         "boundary":"Only mod-p coefficients; exact vanishing lower terms and Gross provenance are external"}
    output.write_text(json.dumps(rep,indent=2)+"\n",encoding='utf-8')
    print("A2_REPORT",output,flush=True)
    return 0


def bound_sha(also_order=False):
    try:
        from sage.all import EllipticCurve, ZZ
    except ImportError as e:
        raise SystemExit("Run this mode under the activated Sage Python environment") from e
    E=EllipticCurve('389a1')
    assert int(E.conductor()) == 389
    ap = int(E.ap(ZZ(P)))
    print("SHA_P",P,"A_P",ap,"ORDINARY",ap%P !=0,flush=True)
    assert ap == A_P
    assert int(E.discriminant()) % P != 0
    print("SHA_KATO_STEIN_WUTHRICH_BOUND_START",flush=True)
    try:
        e=int(E.sha().p_primary_bound(ZZ(P)))
    except Exception as exc:
        print("SHA_BOUND_NOT_OBTAINED",type(exc).__name__,str(exc),flush=True)
        return 3
    assert e>=0
    print("SHA_P_PRIMARY_PROVEN_UPPER_EXPONENT",e,flush=True)
    print("SHA_P_PRIMARY_FINITE_CERTIFIED_PASS",flush=True)
    if e==0:
        print("SHA_P_PRIMARY_ZERO_CERTIFIED_PASS",flush=True)
    else:
        print("SHA_P_PRIMARY_ORDER_UPPER_BOUND",f"{P}^{e}",flush=True)
        print("BOUNDARY: exponent > 0 alone does not prove Sha[p^infinity]=0",flush=True)
    if also_order:
        print("SHA_SKINNER_URBAN_ORDER_START",flush=True)
        try:
            order_exp=int(E.sha().p_primary_order(ZZ(P)))
            print("SHA_P_PRIMARY_PROVEN_EXACT_EXPONENT",order_exp,flush=True)
            if order_exp==0:
                print("SHA_P_PRIMARY_ZERO_CERTIFIED_PASS",flush=True)
        except Exception as exc:
            print("SHA_EXACT_ORDER_NOT_OBTAINED",type(exc).__name__,str(exc),flush=True)
    return 0


def main():
    p=argparse.ArgumentParser()
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--selftest',action='store_true')
    g.add_argument('--sha',action='store_true')
    g.add_argument('--a2',type=Path,metavar='SUMS_JSONL')
    p.add_argument('--order',action='store_true',help='also ask Skinner--Urban exact order (may be expensive)')
    p.add_argument('--output',type=Path,default=Path.home()/"bsd389_a2_mod16231.json")
    a=p.parse_args()
    if a.selftest:
        selftest(); return 0
    if a.sha:
        return bound_sha(a.order)
    return aggregate_a2(a.a2,a.output)

if __name__=='__main__':
    raise SystemExit(main())
