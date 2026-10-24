#!/usr/bin/env python3
"""BSD389 V61: [T^2] of eclib ordinary L-series, level n=2, mod p^2.

Reuses V54 mod-p checkpoints to audit every new block. Does *not* compute
level n=3: the optional level-3 output is conditional on the proposed
C01-to-measure-increment comparison, not an independent verification.

Run in Sage's Python:
  python -u v61_a2_mod_p2.py pilot
  python -u v61_a2_mod_p2.py all
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
BINOM_SUM = P * (P - 1) * (P - 2) // 6
HOME = Path.home() / 'bsd389-c01-v14-production'
OLD = HOME / 'v54_a2_checkpoints'
ROOT = HOME / 'v61_a2_p2_checkpoints'
C01_J = 4486
V56_B_OVER_P = 9534


def source_path(lo, hi):
    return OLD / f'a_{lo:05d}_{hi-1:05d}.json'


def out_path(lo, hi):
    return ROOT / f'p2_a_{lo:05d}_{hi-1:05d}.json'


def sha_record(record):
    body = {k: v for k, v in record.items() if k != 'sha256'}
    blob = json.dumps(body, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(blob).hexdigest()


def read_v54(lo, hi):
    data = json.loads(source_path(lo, hi).read_text())
    v = data['sum_mod_p']
    count = (hi - lo) * P
    expected = hashlib.sha256(
        f'389a1|{P}|{lo}|{hi}|{v}|{count}|v54'.encode()
    ).hexdigest()
    assert data['sha256'] == expected
    assert data['lo'] == lo and data['hi'] == hi
    assert data['count'] == count and 0 <= v < P
    return v


def read_chunk(lo, hi):
    data = json.loads(out_path(lo, hi).read_text())
    assert data['sha256'] == sha_record(data)
    assert data['version'] == 'V61-A2-N2-P2'
    assert data['lo'] == lo and data['hi'] == hi
    assert data['pair_count'] == (hi - lo) * P
    assert data['f2_raw_mod_p2'] % P == read_v54(lo, hi)
    for k in ('f2_raw_mod_p2', 'f1_sum_mod_p2'):
        assert 0 <= data[k] < P2
    return data


def setup():
    from sage.all import EllipticCurve, QQ, ZZ
    E = EllipticCurve('389a1')
    L = E.padic_lseries(ZZ(P), implementation='eclib')
    assert E.real_components() == 2
    assert L._quotient_of_periods_to_twist(1) == 1
    assert L._prec_bounds(2, 3)[2] >= 1
    assert L._prec_bounds(3, 3)[2] >= 2
    alpha = int(L.alpha(4).lift()) % P2
    assert alpha % P == 128
    return L.modular_symbol, QQ, alpha


def residue(q, modulus):
    num = int(q.numerator())
    den = int(q.denominator())
    assert den % P != 0, 'p-divisible denominator: cannot reduce modulo p^2'
    return num * pow(den, -1, modulus) % modulus


def compute(lo, hi):
    f, QQ, alpha = setup()
    raw_f2 = 0
    sum_f1 = 0
    evaluations = 0
    start = time.monotonic()
    for a in range(lo, hi):
        sum_f1 = (sum_f1 + residue(QQ(f(QQ(a) / P)), P2)) % P2
        q = ((pow(a, P - 1, P2) - 1) // P) % P
        ia = pow(a, -1, P)
        for b in range(P):
            u = (b * ia - q) % P
            if u < 2:
                continue
            w = (u * (u - 1) // 2) % P2
            x = a + P * b
            fv = residue(QQ(f(QQ(x) / P2)), P2)
            raw_f2 = (raw_f2 + w * fv) % P2
            evaluations += 1
    old = read_v54(lo, hi)
    if raw_f2 % P != old:
        raise ArithmeticError(
            f'V54 mismatch for [{lo},{hi}): {raw_f2 % P} != {old}'
        )
    result = dict(version='V61-A2-N2-P2', lo=lo, hi=hi,
                  pair_count=(hi-lo)*P, evaluations=evaluations,
                  f2_raw_mod_p2=raw_f2, f1_sum_mod_p2=sum_f1,
                  v54_raw_mod_p=old, alpha_mod_p2=alpha)
    result['sha256'] = sha_record(result)
    print(f'CHUNK [{lo},{hi}) raw_f2_mod_p2={raw_f2} '
          f'v54_mod_p={old} f1_sum_mod_p2={sum_f1} '
          f'evaluations={evaluations} '
          f'sec={time.monotonic()-start:.2f}', flush=True)
    return result


def write_chunk(lo, hi):
    ROOT.mkdir(parents=True, exist_ok=True)
    dest = out_path(lo, hi)
    if dest.exists():
        print('EXISTING', lo, hi, read_chunk(lo, hi)['f2_raw_mod_p2'], flush=True)
        return
    result = compute(lo, hi)
    tmp = dest.with_suffix(f'.{os.getpid()}.tmp')
    with tmp.open('w') as fp:
        json.dump(result, fp, sort_keys=True)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, dest)
    assert read_chunk(lo, hi)['f2_raw_mod_p2'] == result['f2_raw_mod_p2']


def run(pilot=False):
    ROOT.mkdir(parents=True, exist_ok=True)
    stop = min(HALF + 1, 1 + BATCH) if pilot else HALF + 1
    t0 = time.monotonic()
    raw_f2 = 0
    sum_f1 = 0
    done = 0
    alpha_value = None
    for lo in range(1, stop, BATCH):
        hi = min(lo + BATCH, stop)
        if not out_path(lo, hi).exists():
            subprocess.run([sys.executable, '-u', str(Path(__file__).resolve()),
                            'chunk', str(lo), str(hi)], check=True)
        data = read_chunk(lo, hi)
        if alpha_value is None:
            alpha_value = data['alpha_mod_p2']
        assert alpha_value == data['alpha_mod_p2']
        raw_f2 = (raw_f2 + data['f2_raw_mod_p2']) % P2
        sum_f1 = (sum_f1 + data['f1_sum_mod_p2']) % P2
        done += hi-lo
        print(f'PROGRESS a={done}/{HALF} f2_mod_p2={raw_f2} '
              f'elapsed_min={(time.monotonic()-t0)/60:.1f}', flush=True)
    if pilot:
        print('V61_PILOT_PASS', flush=True)
        return
    assert done == HALF
    assert raw_f2 % P == 0, 'V54 full raw sum was 0 mod p'
    inv_alpha = pow(alpha_value, -1, P2)
    lower_term = inv_alpha * (BINOM_SUM % P2) * sum_f1 % P2
    a2_n2 = pow(inv_alpha, 2, P2) * (raw_f2-lower_term) % P2
    assert a2_n2 % P == 0, 'V54 computed A2(n2) == 0 modulo p'

    # CONDITIONAL bridge: NOT an independently computed A2(n=3).
    delta_over_p = C01_J * pow(2 * 2 * 128**2, -1, P) % P
    a2_n3_conditional = (a2_n2 + P * delta_over_p) % P2
    quotient_conditional = a2_n3_conditional // P
    ratio_conditional = quotient_conditional * pow(V56_B_OVER_P, -1, P) % P
    summary = dict(algorithm='eclib n=2 plus optional C01 bridge',
                   a_covered=done, pair_count=done*P,
                   precision_modulus=P2, alpha_mod_p2=alpha_value,
                   raw_f2_mod_p2=raw_f2, sum_f1_mod_p2=sum_f1,
                   lower_term_mod_p2=lower_term,
                   a2_n2_mod_p2=a2_n2,
                   c01_j_mod_p=C01_J,
                   c01_delta_over_p_mod_p_CONDITIONAL=delta_over_p,
                   a2_n3_mod_p2_CONDITIONAL=a2_n3_conditional,
                   a2_n3_over_p_mod_p_CONDITIONAL=quotient_conditional,
                   ratio_to_v56_leading_CONDITIONAL=ratio_conditional,
                   WARNING='Level-3 value is conditional on the global C01 bridge; not an independent level-3 computation.')
    summary['sha256'] = sha_record(summary)
    dest = ROOT / 'v61_a2_p2_result.json'
    tmp = dest.with_suffix('.tmp')
    with tmp.open('w') as fp:
        json.dump(summary, fp, indent=2, sort_keys=True)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, dest)
    print('V61_A2_N2_MOD_P2', a2_n2, flush=True)
    print('V61_C01_INCREMENT_OVER_P_CONDITIONAL', delta_over_p, flush=True)
    print('V61_A2_N3_OVER_P_CONDITIONAL', quotient_conditional, flush=True)
    print('V61_RATIO_TO_V56_CONDITIONAL', ratio_conditional, flush=True)
    print('V61_LEVEL2_COMPLETE_LEVEL3_CONDITIONAL', flush=True)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] in ('pilot', 'all'):
        run(pilot=(sys.argv[1] == 'pilot'))
    elif len(sys.argv) == 4 and sys.argv[1] == 'chunk':
        lo, hi = int(sys.argv[2]), int(sys.argv[3])
        assert 1 <= lo < hi <= HALF+1
        write_chunk(lo, hi)
    else:
        raise SystemExit('usage: python -u v61_a2_mod_p2.py pilot|all')
