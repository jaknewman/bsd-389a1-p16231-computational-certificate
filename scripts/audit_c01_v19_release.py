#!/usr/bin/env python3
"""Read-only inventory for the 389a1/p=16231 C01-V19 release.

Verifies *identity* of archived files against frozen SHA-256 fingerprints,
NOT correctness of their mathematical computations or theorem hypotheses.
No source files or checkpoints are modified; no expensive V19 replay.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path

PINS = {
    'bsd389_c01_v11_aggregated.cpp': '0d8b18696587fc3a0f497c54ebbba99f4d582e69d5a98d0da0e2a4275172b187',
    'bsd389_c01_v11_loader.cpp': 'f398d0f90a36dd3186c5d644a6b3f00f3081ebfc0a18cefd895db60db9b575d9',
    'bsd389_transposed_J_native.cpp': 'e578ae0fac1a112a3a0b135847149c21c546e7099d952c373d25816d3089a545',
    'v19_production.py': '61eef8564236babf1b669c3fdd40db5d201ebc96bb4f1f8a40a04a6b9e5df418',
    'bsd389_c01_v11_aggregated': '31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63',
    'bsd389_tame_relation_export_p16231.json': '9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8',
    'bsd389_tame_scalar_values_p16231.json': '7724c8d730a370e3fdc403293b9fc23f6adad632ca39b53d8439a96f18dd0c7e',
    'state_263429130.bin': '5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e',
}
PRUNE = {'chunks', '.git', '.cache', 'node_modules', 'miniforge3', 'miniconda3',
         'anaconda3', 'envs', '__pycache__', '.local', '.rustup', '.cargo',
         'site-packages', '.venv', 'venv'}


def sha256(path):
    dig = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(2 * 1024 * 1024), b''):
            dig.update(block)
    return dig.hexdigest()


def arithmetic():
    p, ap = 16231, 128
    J = (16014 + 4703) % p
    correction = J * pow(4 * ap * ap, -1, p) % p
    a2_div_p = (1199 + correction) % p
    b_div_p = 1930 * (1 - pow(ap, -1, p))**2 % p
    quotient_digit = a2_div_p * pow(b_div_p, -1, p) % p
    assert (p*p, p**3, J, correction, a2_div_p, b_div_p,
            quotient_digit) == (263445361, 4275981654391, 4486, 8335,
                                9534, 9534, 1)
    return {'p': p, 'a_p': ap, 'J_mod_p': J, 'correction_mod_p': correction,
            'A2_over_p_mod_p': a2_div_p, 'B_over_p_mod_p': b_div_p,
            'quotient_mod_p': quotient_digit,
            'condition': 'J_V19 must be proven equal to J_ref under correct normalization'}


def scan(root, max_depth):
    matches = {key: [] for key in PINS}
    bad = {key: [] for key in PINS}
    counts = 0
    for base, dirs, files in os.walk(root, followlinks=False):
        depth = len(Path(base).relative_to(root).parts)
        if depth >= max_depth:
            dirs[:] = []
        else:
            dirs[:] = sorted(d for d in dirs if d not in PRUNE and not d.startswith('.'))
        for name in files:
            if name not in PINS:
                continue
            path = Path(base) / name
            if not path.is_file() or path.is_symlink():
                continue
            counts += 1
            actual = sha256(path)
            info = {'path': str(path), 'sha256': actual, 'bytes': path.stat().st_size}
            if actual == PINS[name]:
                matches[name].append(info)
            else:
                bad[name].append(info)
    return matches, bad, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.home(),
                        help='archive root (default: home; prunes enormous chunks directory)')
    parser.add_argument('--max-depth', type=int, default=9)
    parser.add_argument('--output', type=Path,
                        default=Path.home() / 'bsd389_c01_v19_release_audit.json')
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir() or args.max_depth < 1:
        parser.error('--root must be a directory and --max-depth >= 1')
    math = arithmetic()
    print('C01_V19_MODULAR_ARITHMETIC_PASS', math['J_mod_p'],
          math['A2_over_p_mod_p'], math['B_over_p_mod_p'], flush=True)
    found, bad, count = scan(root, args.max_depth)
    for name in PINS:
        status = 'PASS' if found[name] else ('MISMATCH' if bad[name] else 'MISSING')
        print('C01_V19_ARCHIVE_PIN', status, name,
              'MATCHES', len(found[name]), 'MISMATCHES', len(bad[name]), flush=True)
    checkpoint = found['state_263429130.bin']
    if checkpoint:
        assert any(item['bytes'] == 4350176 for item in checkpoint), \
            'Final checkpoint hash matched but state byte count differs'
        print('C01_V19_FINAL_STATE_SIZE_PASS', 4350176, flush=True)
    complete = all(found.values())
    result = {
        'scope': 'Frozen SHA-256 identities only; no independent execution proof',
        'root': str(root), 'candidate_files_checked': count,
        'verified': found, 'same_names_wrong_sha': bad, 'modular_arithmetic': math,
        'all_eight_archival_pins_matched': complete,
        'full_chunk_replay_performed': False,
        'C01_source_to_mathematical_functional_proved_by_this_script': False,
        'Sha_16231_unconditionally_proved_by_this_script': False,
        'full_BSD_proved': False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temp = args.output.with_name(args.output.name + '.tmp')
    temp.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    os.replace(temp, args.output)
    print('C01_V19_AUDIT_REPORT', args.output, flush=True)
    print('C01_V19_ARCHIVE_IDENTITY_PASS' if complete else
          'C01_V19_ARCHIVE_IDENTITY_INCOMPLETE', flush=True)
    print('C01_V19_GLOBAL_THEOREM_BRIDGE_STILL_TO_AUDIT', flush=True)
    return 0 if complete else 3


if __name__ == '__main__':
    raise SystemExit(main())
