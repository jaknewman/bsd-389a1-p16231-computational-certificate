#!/usr/bin/env python3
"""p=599: independently confirm W390 chunk additivity and measure the full-range cost.

This is a *bounded* performance / consistency audit, not a computation of
Kurihara delta_n.  It does not extrapolate nonvanishing from sampled chunks.

Usage:
  python -u verification/kurihara_p599_chunk_additivity_benchmark.py \
    --native ~/bsd389_k599_native --table ~/bsd389_p599_manin_table.txt

The native C++ executable must be the uint16_t p599 kernel. It rebuilds the
q1 and q2 discrete-log tables for each invocation, so elapsed wall time
includes that real setup cost rather than only its internal CF loop timer.
"""
import argparse
import hashlib
import re
import subprocess
import time
from pathlib import Path

P, Q1, Q2 = 599, 6912461, 13963889
N = Q1 * Q2
HALF = (N - 1) // 2


def run(native: Path, table: Path, start: int, end: int):
    cmd = [str(native), '--table', str(table), '--start', str(start), '--end', str(end)]
    if end - start + 1 > 1_000_000:
        cmd.append('--allow-large')
    start_time = time.monotonic()
    proc = subprocess.run(cmd, text=True, capture_output=True, check=True)
    wall = time.monotonic() - start_time
    lines = proc.stdout.strip().splitlines()
    assert len(lines) == 2 and lines[0].startswith('KURIHARA_NATIVE_CHUNK '), lines
    assert lines[1].startswith('W390 '), lines
    fields = dict(re.findall(r'(\w+)=([^ ]+)', lines[0]))
    assert fields['STATUS'] == 'PARTIAL_ONLY'
    assert (int(fields['p']), int(fields['q1']), int(fields['q2'])) == (P, Q1, Q2)
    assert (int(fields['start']), int(fields['end'])) == (start, end)
    W = tuple(map(int, lines[1].split()[1:]))
    assert len(W) == 390 and all(0 <= w < P for w in W)
    result = dict(start=start, end=end, span=end - start + 1, wall=wall,
                  loop_seconds=float(fields['seconds']),
                  contraction=int(fields['contraction']),
                  units=int(fields['units']), weighted=int(fields['weights']),
                  edges=int(fields['edges']), W=W)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--native', type=Path, required=True)
    parser.add_argument('--table', type=Path, required=True)
    parser.add_argument('--chunk', type=int, default=200_000,
                        help='length of each additive half-chunk (default 200000)')
    parser.add_argument('--bench', type=int, default=500_000,
                        help='terms in a far-range benchmark chunk (default 500000)')
    args = parser.parse_args()
    assert args.native.is_file() and args.table.is_file()
    assert 20 <= args.chunk <= 500_000 and 20 <= args.bench <= 1_000_000
    raw = args.table.read_bytes()
    vals = [int(x) for x in raw.split()]
    assert len(vals) == 393, f'expected 3 header and 390 Manin residues, got {len(vals)}'
    assert tuple(vals[:3]) == (P, Q1, Q2)
    assert all(0 <= x < P for x in vals[3:])
    print('K599_TABLE_FORMAT_PASS', 'sha256', hashlib.sha256(raw).hexdigest(),
          'len390', 390, flush=True)
    L = args.chunk
    a = run(args.native, args.table, 1, L)
    b = run(args.native, args.table, L + 1, 2 * L)
    full = run(args.native, args.table, 1, 2 * L)
    for key in ('contraction', 'units', 'weighted', 'edges'):
        expect = a[key] + b[key]
        if key == 'contraction':
            expect %= P
        assert expect == full[key], f'chunk-additivity failure for {key}'
    assert all((x + y) % P == z for x, y, z in zip(a['W'], b['W'], full['W']))
    contracted = sum(w * m for w, m in zip(full['W'], vals[3:])) % P
    assert contracted == full['contraction']
    print('K599_W390_CHUNK_ADDITIVITY_PASS',
          'start', 1, 'end', 2 * L, 'contraction', contracted,
          'units', full['units'], 'edges', full['edges'], flush=True)
    first_mid = HALF // 2
    middle = run(args.native, args.table, first_mid, first_mid + args.bench - 1)
    tail = run(args.native, args.table, HALF - args.bench + 1, HALF)
    for label, r in [('EARLY', full), ('MIDDLE', middle), ('TAIL', tail)]:
        rate = r['span'] / max(r['loop_seconds'], 1e-10)
        complete_days = HALF / rate / 86400
        print('K599_BOUNDED_BENCHMARK', label, 'start', r['start'],
              'end', r['end'], 'partial', r['contraction'],
              'loop_seconds', round(r['loop_seconds'], 6),
              'wall_seconds', round(r['wall'], 6),
              'loop_terms_per_sec', round(rate, 1),
              'EXTRAPOLATED_FULL_HALF_DOMAIN_DAYS', round(complete_days, 3),
              flush=True)
    print('K599_GLOBAL_DELTA_STATUS UNCOMPUTED', flush=True)
    print('BOUNDARY: exact finite-range additivity and indicative throughput only;',
          'no nonzero delta and no Sha[599^infinity] conclusion.', flush=True)


if __name__ == '__main__':
    main()
