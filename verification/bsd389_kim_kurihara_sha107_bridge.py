#!/usr/bin/env python3
"""389a1: finite Kurihara witness -> Sha[107^infinity]=0 via Kim's Theorem 1.8.

No Sage or rerun of the 71 billion term Kurihara half-sum.
This checks prime/admissibility data by *fresh* finite-field point counts,
compares the user-completed 2026-10-28 certificate archive to its frozen
SHA-256, and displays the precise theorem argument.

IMPORTANT: an archive SHA only authenticates the previously checked artifact.
It is NOT a proof that the algorithm computing delta was mathematically
correct. The theorem conclusion uses the archived exhaustive δ=34 (mod 107),
the Manin-normalized plus modular symbol, proven MW rank 2, and the known
residual surjectivity/Manin-constant hypotheses. No global BSD claim.

Usage:
  python -u verification/bsd389_kim_kurihara_sha107_bridge.py
  python -u verification/bsd389_kim_kurihara_sha107_bridge.py --archive ~/other/path/certificate.tar.gz
  python -u verification/bsd389_kim_kurihara_sha107_bridge.py --selftest

Reference: Chan-Ho Kim, The structure of Selmer groups and the Iwasawa
main conjecture for elliptic curves, 12 May 2025, Theorem 1.8 (1), (3).
"""
import argparse
import hashlib
import json
from pathlib import Path

P = 107
Q1 = 369793
Q2 = 383917
N = Q1 * Q2
DELTA = 34
EXPECTED_ARCHIVE_SHA256 = (
    "b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754"
)
DEFAULT_ARCHIVE = Path.home() / "bsd389_k107_certificate_COMPLETE_20261028.tar.gz"

# All 64-bit inputs below use a deterministic Miller-Rabin base set.
def isprime_64(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def a_q_from_finite_field(q):
    """a_q = -sum_x (1+4(x^3+x^2-2x) | q) for the given model."""
    assert isprime_64(q) and q != 389 and q % 2
    tot = 0
    for x in range(q):
        d = (((4 * x + 4) * x - 8) * x + 1) % q
        if d:
            chi = pow(d, (q - 1) // 2, q)
            assert chi in (1, q - 1)
            tot += (1 if chi == 1 else -1)
    return -tot


def sha256_file(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for blk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(blk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--archive', type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument('--selftest', action='store_true',
                        help='arithmetical checks only; never a proof of Sha')
    parser.add_argument('--output', type=Path,
                        default=Path.home() / 'bsd389_kim_kurihara_sha107_bridge.json')
    args = parser.parse_args()
    assert isprime_64(P)
    assert isprime_64(Q1) and isprime_64(Q2) and Q1 != Q2
    assert N == 141969819181
    assert Q1 % P == Q2 % P == 1
    assert 0 < DELTA < P
    a1 = a_q_from_finite_field(Q1)
    a2 = a_q_from_finite_field(Q2)
    assert (a1, a2) == (2, -854), (a1, a2)
    assert (a1-Q1-1) % P == 0 and (a2-Q2-1) % P == 0
    print('BSD389_P107_AUXILIARY_PRIMES_INDEPENDENT_POINTCOUNT_PASS',
          Q1, 'A_Q1', a1, Q2, 'A_Q2', a2, flush=True)
    print('BSD389_P107_KURIHARA_ADMISSIBILITY_PASS',
          'p', P, 'n', N, 'nu(n)', 2, flush=True)
    print('BSD389_P107_ARCHIVED_WITNESS_VALUE', DELTA, 'mod', P, flush=True)

    if args.selftest:
        print('SELFTEST_ONLY_NO_ARCHIVE_PROVENANCE_AND_NO_SHA_CLAIM', flush=True)
        return

    path = args.archive.expanduser()
    if not path.is_file():
        raise FileNotFoundError(
            f'Archive absent: {path}. Specify --archive with the correct path. '
            'Do not interpret the hardcoded delta value as an authenticated computation.'
        )
    found = sha256_file(path)
    assert found == EXPECTED_ARCHIVE_SHA256, (
        'FROZEN_ARCHIVE_SHA256_MISMATCH', found, EXPECTED_ARCHIVE_SHA256
    )
    print('BSD389_P107_FULL_710_BLOCK_ARCHIVE_SHA256_MATCH_PASS', found, flush=True)
    print('KIM_THEOREM_1_8_HYPOTHESES_EXTERNAL: rank=2, residual surjectivity, '
          'p-integral/Manin-normalized modular symbols must be the '
          'already audited Sage assertions', flush=True)
    print('KIM_THEOREM_1_8_CORANK_LE_2_FROM_DELTA_NONZERO', flush=True)
    print('KUMMER_MORDELL_WEIL_RANK_GE_2', flush=True)
    print('KIM_THEOREM_1_8_SELMER_CORANK_EQUALS_2', flush=True)
    print('KIM_THEOREM_1_8_PART3_NON_DIVISIBLE_LENGTH_ZERO', flush=True)
    print('SHA_107_PRIMARY_TRIVIAL_CONDITIONAL_ON_CERTIFIED_INPUTS_AND_THEOREM_PASS',
          flush=True)
    record = {
        'status': 'CONDITIONAL_THEOREM_WITH_FROZEN_WITNESS_PASS',
        'curve': '389a1', 'p': P, 'auxiliary_primes': [Q1,Q2],
        'aq': [a1,a2], 'n': N, 'delta_mod_p_from_archived_run': DELTA,
        'witness_archive': str(path), 'archive_sha256': found,
        'source': 'Kim 2025 Theorem 1.8 parts (1) and (3)',
        'algebraic_logic': {
          'MW_rank': 2, 'ord_Kurihara_upper': 2,
          'Selmer_corank': 2,
          'partial_2_of_Kurihara': 0,
          'partial_infinity_of_Kurihara': 0,
          'Selmer_nondivisible_length': 0,
          'Sha_107_primary_order': 1,
        },
        'caveat': ('The SHA match authenticates user-certified completed run. '
                   'Correctness of archived symbol algorithm, compatible '+
                   'Manin normalization, and Galois hypothesis are external '+
                   'proof inputs; this bridge does not rerun the main sum.'),
    }
    args.output.expanduser().write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + '\n',
        encoding='utf-8')
    print('BSD389_P107_KIM_BRIDGE_JSON', args.output, flush=True)

if __name__ == '__main__':
    main()
