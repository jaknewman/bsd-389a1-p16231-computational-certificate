#!/usr/bin/env python3
"""Finite-depth theta coefficient arithmetic gate for 389a1.

Input CSV: precisely p**n rows "i,weight" with consecutive indices
0<=i<p**n, where weight is the AUTHENTIC aggregated Gross weight
W_i from Castella--Hsieh Appendix section 6.

The script verifies the finite weighted sum only. It does NOT certify
Gross-point provenance, adelic reciprocity, or BSD.
"""
from __future__ import annotations
import argparse
import csv
from math import comb
from pathlib import Path


def ordinary_unit_root(p: int, n: int, ap: int) -> int:
    if p < 3 or n < 1 or ap % p == 0:
        raise ValueError("Require odd ordinary p and n>=1")
    a = ap % p
    m = p
    for _ in range(1, n):
        assert (a*a-ap*a+p) % m == 0
        d = (2*a-ap) % p
        t = (-(a*a-ap*a+p)//m * pow(d, -1, p)) % p
        a += m*t
        m *= p
    assert (a*a-ap*a+p) % m == 0 and a % p
    return a


def compute(p: int, n: int, ap: int, rows):
    mod = p**n
    a = ordinary_unit_root(p, n, ap)
    moments = [0, 0, 0]
    count = 0
    for i, w in rows:
        if i != count:
            raise ValueError(f"Expected index {count}, got {i}")
        if i >= mod:
            raise ValueError("More than p**n rows")
        w = int(w) % mod
        moments[0] = (moments[0]+w) % mod
        moments[1] = (moments[1]+i*w) % mod
        moments[2] = (moments[2]+(i*(i-1)//2)*w) % mod
        count += 1
    if count != mod:
        raise ValueError(f"Incomplete vector: {count} of {mod}")
    gauge = pow(a, -(n+1), mod)
    coeff = tuple((x*gauge) % mod for x in moments)
    return {"p":p,"n":n,"modulus":mod,"alpha":a,
            "raw_moments":tuple(moments),"coefficients":coeff,
            "conditional_gate":coeff[1]==0 and coeff[2]!=0}


def read_csv(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            if not row or row[0].strip().startswith("#"):
                continue
            if len(row) != 2:
                raise ValueError("Require CSV index,weight")
            yield int(row[0]), int(row[1])


def vp(x, p):
    if x == 0:
        return float("inf")
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v


def self_test():
    for p in (5, 7, 11, 13):
        for n in (1, 2, 3):
            for j in (1, 2, 3, 4):
                assert vp(comb(p**n, j), p) == n
    print("PASS finite-to-infinite p-adic coefficient precision")
    for n in (1, 2, 3):
        p, ap, mod = 5, -3, 5**n
        a = ordinary_unit_root(p, n, ap)
        w = (100 * pow(a, n+1, mod)) % mod
        def rows():
            for i in range(mod):
                yield i, (w if i in (0,2) else -2*w if i==1 else 0)
        result = compute(p, n, ap, rows())
        assert result["coefficients"] == (0, 0, 100%mod)
        assert result["conditional_gate"] == (n==3)
        print(f"PASS SYNTHETIC p5 n={n} coefficients={result['coefficients']}")
    for p,n,c1,c2 in ((5,3,0,100),(11,2,0,10),(7,2,49,7)):
        mod=p**n
        for k in (2,3,4,5,6):
            if k%p and c1%mod==0:
                transformed=(k*k*c2+k*(k-1)//2*c1)%mod
                assert (transformed!=0)==(c2%mod!=0)
    print("PASS generator orientation invariance")
    print("SELF_TEST_PASS synthetic weights only; NO_GROSS_PROVENANCE_ASSERTED")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test",action="store_true")
    parser.add_argument("--p",type=int)
    parser.add_argument("--n",type=int)
    parser.add_argument("--ap",type=int)
    parser.add_argument("--weights-csv",type=Path)
    args=parser.parse_args()
    if args.self_test:
        self_test()
        return
    if any(x is None for x in (args.p,args.n,args.ap,args.weights_csv)):
        parser.error("Provide --p --n --ap --weights-csv or --self-test")
    result=compute(args.p,args.n,args.ap,read_csv(args.weights_csv))
    print("FINITE_GROSS_WEIGHT_ARITHMETIC",result)
    if result["conditional_gate"]:
        print("CONDITIONAL_THETA2_GATE_PASS: requires genuine authenticated Gross weights, c0=0 and the functional equation")
    else:
        print("NO_THETA_ORDER_CONCLUSION")


if __name__=="__main__":
    main()
