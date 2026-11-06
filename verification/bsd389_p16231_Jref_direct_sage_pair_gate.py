#!/usr/bin/env python3
"""Direct Sage/eclib reference evaluation of individual p=16231 J_ref pairs.

Computes M0(D_x) and M1(D_x) from genuine rational cusps; it does NOT
use the archived Shapiro transforms, V65 table, or Manin relation exporter.
Optionally compares each result with a fresh *single-pair* evaluation by
the already-frozen independent_c01_scalar_J.cpp binary.

This is a local source-to-reference check, NOT a global J or Sha proof.

Example:
  python -u verification/bsd389_p16231_Jref_direct_sage_pair_gate.py \
      --pair 1:0:2316 --pair 2:3:11725
New cases, with the archived C++ binary already compiled:
  python -u verification/bsd389_p16231_Jref_direct_sage_pair_gate.py \
      --pair 1:1 --pair 16230:16230 \
      --cpp-binary /tmp/bsd389_independent_J \
      --v65-table ~/bsd389-c01-v14-production/v65_independent_terminal/eclib_beta_table.bin
"""
from __future__ import annotations
import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

P = 16231
AP = 128
P2, P3 = P * P, P * P * P
ROOT = Path(__file__).resolve().parents[1]


def parameters(a, b):
    assert 1 <= a < P and 0 <= b < P
    x = a + P*b
    ia = pow(a, -1, P)
    fermat = ((pow(a, P-1, P2)-1)//P) % P
    u = (b*ia-fermat) % P
    omega = pow(a, P2, P3)
    difference = (omega*pow(P+1, u, P3)-x) % P3
    assert difference % P2 == 0
    kappa = difference // P2
    w = ((2*u-1)*ia) % P
    assert pow(omega, P-1, P3) == 1
    return x, u, kappa, w


def selftest():
    assert pow(AP, -1, P) == 5199
    assert (4*AP*AP*9362) % P == 1
    for a, b in ((1,0),(2,3),(1,P-1),(P-1,P-1),(128,137)):
        x,u,kappa,w = parameters(a,b)
        assert (x,u,kappa,w) == (a+P*b,u,kappa,w)
        assert 0 <= u < P and 0 <= kappa < P and 0 <= w < P
    print("JREF_DIRECT_PARAMETER_SELFTEST_PASS", flush=True)


def parse_pair(raw):
    vals = raw.split(":")
    if len(vals) not in (2,3):
        raise argparse.ArgumentTypeError("expected a:b[:expected]")
    try:
        a,b = int(vals[0]),int(vals[1])
        expected = int(vals[2]) if len(vals)==3 else None
    except ValueError as exc:
        raise argparse.ArgumentTypeError("not integers") from exc
    if not (1 <= a < P and 0 <= b < P and
            (expected is None or 0 <= expected < P)):
        raise argparse.ArgumentTypeError("out of range")
    return a,b,expected


def direct_Jref(m,a,b):
    from sage.all import QQ, ZZ
    x,u,kappa,w = parameters(a,b)
    ialpha = pow(AP,-1,P)
    def red(y):
        q = QQ(y)
        numerator,denominator = ZZ(q.numerator()),ZZ(q.denominator())
        if denominator % P == 0:
            raise ArithmeticError("NONINTEGRAL_SOURCE_MODULAR_SYMBOL")
        return (int(numerator%P)*pow(int(denominator%P),-1,P))%P
    # F(D)=m(D.infinity)-m(D.0)=-m(D.0)
    F_D = -red(m(QQ(x)/P2))
    F_PD = -red(m(QQ(x)/P))
    M0 = (F_D-ialpha*F_PD)%P
    total = 0
    for c in range(P):
        F_beta = -red(m(QQ(x+P2*c)/P3))
        total = (total+c*F_beta)%P
        if c and c%4096==0:
            print("JREF_DIRECT_CUSPS_PROGRESS",a,b,c,"OF",P,flush=True)
    M1 = (ialpha*total)%P
    J = (-w*(M1-kappa*M0))%P
    print("JREF_DIRECT_SOURCE_PAIR",a,b,"u",u,"kappa",kappa,"w",w,
          "M0",M0,"M1",M1,"J",J,flush=True)
    return J


def frozen_cpp_pair(binary, table, relations, a, b):
    lo,hi = (a-1)*P+b,(a-1)*P+b+1
    exporter = ROOT/"verification/export_shapiro_transport_stream.py"
    if not (binary.is_file() and table.is_file() and relations.is_file()
            and exporter.is_file()):
        raise FileNotFoundError("MISSING_FROZEN_COMPARATOR_INPUT")
    with tempfile.TemporaryDirectory(prefix="bsd389_Jref_single_") as tmp:
        source = subprocess.Popen(
            [sys.executable,str(exporter),str(relations)],
            stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        try:
            job = subprocess.run(
                [str(binary),str(table),str(lo),str(hi),
                 str(Path(tmp)/"checkpoint.txt")],
                stdin=source.stdout,stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,text=True,check=True)
        finally:
            if source.stdout:
                source.stdout.close()
        err = source.stderr.read() if source.stderr else b""
        status = source.wait()
        if status:
            raise RuntimeError("FROZEN_EXPORTER_FAILED "+repr(err[:500]))
    regex = (r"INDEPENDENT_SCALAR_INTERVAL_PASS start="+str(lo)+
             r" end="+str(hi)+r" J_mod_p=(\d+)")
    matches = re.findall(regex,job.stdout)
    if len(matches)!=1:
        raise RuntimeError("FROZEN_CPP_DID_NOT_RETURN_ONE_PAIR "+job.stdout[-500:])
    return int(matches[0])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest",action="store_true")
    parser.add_argument("--pair",action="append",type=parse_pair)
    parser.add_argument("--cpp-binary",type=Path)
    parser.add_argument("--v65-table",type=Path)
    parser.add_argument("--relations",type=Path,default=(
        ROOT/"historical/originals/bsd389_tame_relation_export_p16231.json"))
    opts=parser.parse_args()
    selftest()
    if opts.selftest:
        return 0
    if bool(opts.cpp_binary)!=bool(opts.v65_table):
        parser.error("--cpp-binary and --v65-table must be provided together")
    pairs=opts.pair or [parse_pair("1:0:2316"),parse_pair("2:3:11725")]
    from sage.all import EllipticCurve,ZZ
    E=EllipticCurve("389a1")
    assert E.conductor()==389 and E.ap(ZZ(P))==AP
    assert E.is_good(P) and E.is_ordinary(P)
    m=E.modular_symbol(sign=+1,implementation="eclib",normalize="L_ratio")
    for a,b,expected in pairs:
        j=direct_Jref(m,a,b)
        if expected is not None:
            assert j==expected,("DIRECT_SOURCE_EXPECTED_MISMATCH",a,b,j,expected)
            print("JREF_DIRECT_ARCHIVED_ORACLE_PASS",a,b,j,flush=True)
        if opts.cpp_binary:
            cpp=frozen_cpp_pair(opts.cpp_binary.expanduser(),
                                opts.v65_table.expanduser(),opts.relations,a,b)
            assert j==cpp,("SOURCE_VS_CPP_MISMATCH",a,b,j,cpp)
            print("JREF_DIRECT_SAGE_VS_FROZEN_CPP_PASS",a,b,j,flush=True)
        elif expected is None:
            print("JREF_DIRECT_VALUE_ONLY_NO_CPP_CROSSCHECK",a,b,j,flush=True)
    print("JREF_LOCAL_PAIR_GATE_PASS",len(pairs),flush=True)
    print("BOUNDARY_NO_GLOBAL_J_OR_SHA_FROM_FINITE_SPOTCHECKS",flush=True)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
