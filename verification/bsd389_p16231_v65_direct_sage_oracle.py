#!/usr/bin/env python3
"""Independent V65 source/normalization and Shapiro-coset oracle for p=16231.

Reads only the SHA256-pinned original 390-Manin relation export and the
2,175,242-byte V65 binary reference table used by BOTH full scalar J engines.

Checks ALL 67 complete Hecke fibres (67*16231 = 1,087,477 entries) and
directly compares F(G), F(PG), sampled F(beta_t G), and sampled
F(P r_j G) INCLUDING j=infinity to Sage's independently implemented
'L_ratio' modular symbols. Uses neither the original V11 C01 sparse
producer nor the independently computed 263-million-pair J scalar.

This is a verification of the shared modular-symbol oracle, NOT a fresh
global J sum or a direct level-p^3 p-adic L-function calculation.

Usage in Sage Python:
  python -u verification/bsd389_p16231_v65_direct_sage_oracle.py
  python -u verification/bsd389_p16231_v65_direct_sage_oracle.py --oracle eclib

The Sage implementation is the default, intentionally independent of
the eclib implementation used to build the binary table.
"""
import argparse
import hashlib
import json
import struct
from pathlib import Path

from sage.all import EllipticCurve, QQ

P = 16231
LEVEL = 389
AP = 128
GENERATORS = 67
EXPECTED_REL_SHA = "9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8"
EXPECTED_TABLE_SHA = "aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REL = ROOT / "historical/originals/bsd389_tame_relation_export_p16231.json"
DEFAULT_TABLE = (
    Path.home()
    / "bsd389-c01-v14-production"
    / "v65_independent_terminal"
    / "eclib_beta_table.bin"
)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def mul(x, y):
    a, b, c, d = x
    A, B, C, D = y
    return (a*A+b*C, a*B+b*D, c*A+d*C, c*B+d*D)


def det(x):
    return x[0]*x[3]-x[1]*x[2]


def residue(value):
    value = QQ(value)
    num, den = int(value.numerator()), int(value.denominator())
    assert den % P != 0, ("NON_INTEGRAL_SYMBOL", value)
    return num * pow(den, -1, P) % P


def modular_edge(m, mat):
    """F(mat) = m(mat.infinity) - m(mat.0); m(infinity)=0."""
    a, b, c, d = mat
    return ((m(QQ(a)/c) if c else QQ(0))
            - (m(QQ(b)/d) if d else QQ(0)))


def source_inputs(relpath, tablepath):
    raw_rel = relpath.read_bytes()
    raw_table = tablepath.read_bytes()
    assert digest(raw_rel) == EXPECTED_REL_SHA, (
        "WRONG_ORIGINAL_SHAPIRO_RELATIONS", digest(raw_rel))
    assert digest(raw_table) == EXPECTED_TABLE_SHA, (
        "WRONG_V65_ECLIB_BINARY_TABLE", digest(raw_table))
    obj = json.loads(raw_rel)
    assert (obj["N"], obj["p"]) == (LEVEL, P)
    assert len(obj["reps"]) == LEVEL+1
    assert len(obj["generators"]) == GENERATORS
    gen = [tuple(map(int, row)) for row in obj["generators"]]
    assert all(det(x) == 1 for x in gen)
    rinf = tuple(map(int, obj["rinf"]))
    assert det(rinf) == 1 and rinf[2] % LEVEL == 0 and rinf[3] % P == 0
    assert len(raw_table) == 20 + GENERATORS*(P+2)*2
    assert raw_table[:8] == b"BSD65F01"
    assert struct.unpack_from("<III", raw_table, 8) == (P, LEVEL, GENERATORS)
    print("P16231_V65_ORIGINAL_SHAPIRO_SHA256_PASS", EXPECTED_REL_SHA, flush=True)
    print("P16231_V65_BINARY_TABLE_SHA256_PASS", EXPECTED_TABLE_SHA, flush=True)
    return gen, rinf, raw_table


def audit(args):
    gens, rinf, raw = source_inputs(args.relations, args.table)
    E = EllipticCurve(QQ, [0, 1, 1, -2, 0])
    assert int(E.conductor()) == LEVEL and int(E.ap(P)) == AP
    assert int(E.real_components()) == 2
    symbol = E.modular_symbol(
        sign=+1, implementation=args.oracle, normalize="L_ratio")
    alpha_inv = pow(AP, -1, P)
    assert alpha_inv == 5199
    Pmat = (P, 0, 0, 1)
    # Include the exceptional representative for EVERY generator.
    cosets = (0, 1, 71, P-1, P)
    hecke = direct_fg = direct_beta = direct_shapiro = 0
    for g, G in enumerate(gens):
        base = 20 + g*(P+2)*2
        fG, fP = struct.unpack_from("<HH", raw, base)
        fs = struct.unpack_from(f"<{P}H", raw, base+4)
        assert fG < P and fP < P and all(v < P for v in fs)
        assert (fP + sum(fs) - AP*fG) % P == 0, (
            "V65_FULL_FIBRE_HECKE_FAIL", g)
        hecke += P
        true_fG = residue(modular_edge(symbol, G))
        true_fP = residue(modular_edge(symbol, mul(Pmat, G)))
        assert (fG, fP) == (true_fG, true_fP), (
            "SAGE_V65_FG_FP_MISMATCH", g, (fG, fP), (true_fG, true_fP))
        direct_fg += 2
        # Deterministic independent samples spanning the whole tame fibre.
        ts = sorted({0, 1, 2, 53, P//2, P-2, P-1, (g*241+71) % P})
        for t in ts:
            beta = (1, t, 0, P)
            expected = residue(modular_edge(symbol, mul(beta, G)))
            assert fs[t] == expected, (
                "SAGE_V65_BETA_T_MISMATCH", g, t, fs[t], expected)
            direct_beta += 1
        # Direct cusp evaluation for P*r_j*G (including infinity) is
        # independent of all cached basis-moment and dual-transport code.
        for j in cosets:
            rj = (1, 0, LEVEL*j, 1) if j != P else rinf
            assert det(rj) == 1 and rj[2] % LEVEL == 0
            f_rj = residue(modular_edge(symbol, mul(rj, G)))
            assert f_rj == fG, ("GAMMA0_INVARIANCE_MISMATCH", g, j)
            f_P_rj = residue(modular_edge(symbol, mul(Pmat, mul(rj, G))))
            if j == 0:
                source = fP
            elif j == P:
                source = fs[0]
            else:
                source = fs[pow(LEVEL*j, -1, P)]
            assert f_P_rj == source, (
                "SHAPIRO_PTRANSPORT_MISMATCH", g, j, f_P_rj, source)
            # Explicitly verify the M0 coordinate fed into C01's dual.
            observed_m0 = (f_rj - alpha_inv*f_P_rj) % P
            expected_m0 = (fG - alpha_inv*source) % P
            assert observed_m0 == expected_m0
            direct_shapiro += 1
        if (g+1) % 10 == 0 or g+1 == GENERATORS:
            print("P16231_V65_ORACLE_PROGRESS", g+1, "/", GENERATORS,
                  flush=True)
    assert hecke == 1087477 and direct_fg == 134
    assert direct_shapiro == GENERATORS*len(cosets)
    print("P16231_V65_ALL_67_COMPLETE_HECKE_FIBRES_PASS",
          "entries", hecke, flush=True)
    print("P16231_V65_INDEPENDENT_SAGE_FG_FP_PASS",
          "checks", direct_fg, "oracle", args.oracle, flush=True)
    print("P16231_V65_INDEPENDENT_SAGE_BETA_SAMPLES_PASS",
          "checks", direct_beta, flush=True)
    print("P16231_V65_INDEPENDENT_SAGE_SHAPIRO_M0_PASS",
          "checks", direct_shapiro, "infinity_representatives",
          GENERATORS, flush=True)
    print("P16231_V65_SHARED_MANIN_ORACLE_AUDIT_PASS", flush=True)
    print("BOUNDARY This independently checks shared V65 table provenance, "
          "all Hecke sums and sampled true Sage cusps; it does not "
          "recompute J=4486 or the full n3 analytic series.", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--relations", type=Path, default=DEFAULT_REL)
    ap.add_argument("--table", type=Path, default=DEFAULT_TABLE)
    ap.add_argument("--oracle", choices=("sage", "eclib"), default="sage")
    args = ap.parse_args()
    audit(args)


if __name__ == "__main__":
    main()
