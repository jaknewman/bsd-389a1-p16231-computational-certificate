#!/usr/bin/env python3
"""Standalone exact re-audit of BSD 389a1 cyclotomic raw moments.

Python 3 standard library only. This checks finite modular-symbol sums, not
any Selmer-group theorem. Paths resolve relative to this file, not /mnt/data.

Examples:
  python3 bsd389_standalone_p2_audit.py --primes 5 7 11 89
  python3 bsd389_standalone_p2_audit.py --primes --p389
"""
from __future__ import annotations
import argparse
import csv
import hashlib
from pathlib import Path
from math import gcd

N = 389
TABLE_SHA256 = '9bce8b66c37b7f257f5a6015c08806c2b80c36d1e47356677e3819fc171e8360'

def load_table(path: Path):
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == TABLE_SHA256, 'Manin table checksum mismatch'
    v = list(map(int, raw.split()))
    assert len(v) == N+1
    assert all(-2 <= i <= 2 for i in v)
    return v

def modular_symbol(a: int, n: int, v: list[int]) -> int:
    """Exact Manin continued-fraction path from infinity to a/n."""
    assert 0 < a < n and gcd(a, n) == 1
    pn, pd, ln, ld = 1, 0, 0, 1
    x, y = n, a
    ans = v[N]
    while y:
        q, r = divmod(x, y)
        nn, nd = q*ln + pn, q*ld + pd
        det = ln*nd - nn*ld
        assert det in (-1, 1)
        c, d = (ld, nd) if det == 1 else (nd, ld)
        c %= N
        d %= N
        idx = N if c == 0 else d*pow(c, -1, N) % N
        ans += det * v[idx]
        pn, pd, ln, ld = ln, ld, nn, nd
        x, y = y, r
    assert (ln, ld) == (a, n)
    return ans

def raw_moments(p: int, v: list[int]):
    n = p*p
    c = [0, 0, 0, 0]
    for a in range(1, n):
        if a % p == 0:
            continue
        j = (-(pow(a, p-1, n)-1)//p) % p
        m = modular_symbol(a, n, v)
        b = (1, j, j*(j-1)//2, j*(j-1)*(j-2)//6)
        for k in range(4):
            c[k] = (c[k] + m*b[k]) % p
    return c

def verify_manifest(p, coeffs, path):
    with path.open(newline='') as f:
        records = {int(r['p']): r for r in csv.DictReader(f)}
    if p in records:
        row = records[p]
        expected = [int(row[f'c{i}']) for i in range(4)]
        assert coeffs == expected, (p, coeffs, expected)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--table', type=Path, default=Path(__file__).resolve().parent / 'manin_390.txt')
    ap.add_argument('--manifest', type=Path, default=Path(__file__).resolve().parent.parent / 'data' / 'ordinary_p2_5_to_1999.csv')
    ap.add_argument('--primes', type=int, nargs='*', default=[5, 7, 11, 89])
    ap.add_argument('--p389', action='store_true')
    args = ap.parse_args()
    v = load_table(args.table)
    assert modular_symbol(7, N, v) == -1
    assert modular_symbol(5, N, v) == -2
    print('MANIN_INTEGRAL_TABLE_SHA256_PASS', TABLE_SHA256, flush=True)
    for p in args.primes:
        assert 5 <= p and p != N
        out = raw_moments(p, v)
        if args.manifest.is_file():
            verify_manifest(p, out, args.manifest)
        assert out[0] == out[1] == 0 and out[2] != 0, (p, out)
        print('ORDINARY_RAW_P2_MOMENTS_PASS', p, out, flush=True)
    if args.p389:
        out = raw_moments(389, v)
        assert out == [0, 0, 0, 321], out
        print('MULTIPLICATIVE_P389_RAW_MOMENTS_PASS', out, flush=True)
    print('BOUNDARY: FINITE_MODULAR_SYMBOL_AUDIT_ONLY_NOT_SELMER_OR_FULL_BSD')

if __name__ == '__main__':
    main()
