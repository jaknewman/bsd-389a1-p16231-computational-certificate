#!/usr/bin/env python3
"""Independent coefficient [T^2] of ordinary eclib p-adic L-series, mod 16231.

Execute with Sage's Python: python -u v54_independent_a2.py pilot|all
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

P = 16231
P2 = P * P
HALF = (P - 1) // 2
BATCH = 32
ROOT = Path.home() / "bsd389-c01-v14-production" / "v54_a2_checkpoints"


def path_for(lo, hi):
    return ROOT / f"a_{lo:05d}_{hi-1:05d}.json"


def digest(lo, hi, value, count):
    return hashlib.sha256(f"389a1|{P}|{lo}|{hi}|{value}|{count}|v54".encode()).hexdigest()


def read_chunk(lo, hi):
    d = json.loads(path_for(lo, hi).read_text())
    count = (hi - lo) * P
    assert d['lo'] == lo and d['hi'] == hi
    assert d['count'] == count and 0 <= d['sum_mod_p'] < P
    assert d['sha256'] == digest(lo, hi, d['sum_mod_p'], count)
    return d['sum_mod_p']


def sage_setup():
    from sage.all import EllipticCurve, QQ, ZZ
    E = EllipticCurve('389a1')
    L = E.padic_lseries(ZZ(P), implementation='eclib')
    assert E.real_components() == 2
    assert L._quotient_of_periods_to_twist(1) == 1
    assert L.alpha(4).lift() % P == 128  # ordinary branch
    assert L._prec_bounds(2, 3)[2] >= 1
    return L, QQ, ZZ


def calc(lo, hi):
    L, QQ, ZZ = sage_setup()
    f = L.modular_symbol
    acc = 0
    evaluations = 0
    start = time.monotonic()
    for a in range(lo, hi):
        q = ((pow(a, P-1, P2)-1)//P) % P
        ia = pow(a, -1, P)
        for b in range(P):
            u = (b*ia - q) % P
            if u < 2:
                continue
            weight = (u*(u-1)//2) % P
            x = a + P*b
            z = QQ(f(QQ(x)/P2))
            den = int(z.denominator())
            if den % P == 0:
                raise ArithmeticError(f'p-divisible denominator at a={a} b={b}')
            value = (int(z.numerator()) * pow(den, -1, P)) % P
            acc = (acc + weight * value) % P
            evaluations += 1
    elapsed = time.monotonic()-start
    print(f'CHUNK [{lo},{hi}) sum={acc} evaluations={evaluations} sec={elapsed:.2f}', flush=True)
    return acc


def write_chunk(lo, hi):
    ROOT.mkdir(parents=True, exist_ok=True)
    dest = path_for(lo, hi)
    if dest.exists():
        print('EXISTING', lo, hi, read_chunk(lo, hi), flush=True)
        return
    result = calc(lo, hi)
    count = (hi - lo)*P
    data = dict(lo=lo, hi=hi, count=count, sum_mod_p=result,
                sha256=digest(lo, hi, result, count))
    tmp = dest.with_suffix(f'.{os.getpid()}.tmp')
    with tmp.open('w') as fd:
        json.dump(data, fd, sort_keys=True)
        fd.flush()
        os.fsync(fd.fileno())
    os.replace(tmp, dest)
    assert read_chunk(lo, hi) == result


def run_all(pilot):
    ROOT.mkdir(parents=True, exist_ok=True)
    stop = min(HALF+1, 1+BATCH) if pilot else HALF+1
    t0 = time.monotonic()
    total = 0
    done = 0
    for lo in range(1, stop, BATCH):
        hi = min(stop, lo+BATCH)
        if not path_for(lo, hi).exists():
            subprocess.run([sys.executable, '-u', __file__, 'chunk', str(lo), str(hi)], check=True)
        total = (total+read_chunk(lo, hi))%P
        done += hi-lo
        print(f'PROGRESS a={done}/{HALF} raw_half_sum={total} elapsed_min={(time.monotonic()-t0)/60:.1f}', flush=True)
    if pilot:
        print('V54_PILOT_PASS', flush=True)
    else:
        answer = total * pow(128, -2, P) % P
        summary = dict(a_covered=done, terms=done*P, raw_half_sum_mod_p=total,
                       a2_mod_p=answer, precision_at_least=1,
                       normalization='eclib eta=0, n=2, periods quotient=1, real components=2')
        dest = ROOT / 'v54_a2_result.json'
        tmp = dest.with_suffix('.tmp')
        with tmp.open('w') as fd:
            json.dump(summary, fd, indent=2, sort_keys=True)
            fd.flush()
            os.fsync(fd.fileno())
        os.replace(tmp, dest)
        print('V54_A2_MOD_P', answer, flush=True)
        print('V54_INDEPENDENT_A2_COMPLETE', flush=True)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] in ('pilot', 'all'):
        run_all(sys.argv[1] == 'pilot')
    elif len(sys.argv) == 4 and sys.argv[1] == 'chunk':
        lo, hi = int(sys.argv[2]), int(sys.argv[3])
        assert 1 <= lo < hi <= HALF+1
        write_chunk(lo, hi)
    else:
        raise SystemExit('usage: python -u v54_independent_a2.py pilot|all')
