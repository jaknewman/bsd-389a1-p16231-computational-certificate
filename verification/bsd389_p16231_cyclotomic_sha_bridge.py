#!/usr/bin/env python3
"""389a1 p=16231: quick, source-aware archival arithmetic bridge.

This does NOT sum level-3 Sage measures, does NOT recompute C01 and does
NOT call p_primary_bound. It checks committed inputs and reconstructs the
proved conditional implication to Sha[p^infinity]=0. Run under normal Python.

Usage:
  python -u verification/bsd389_p16231_cyclotomic_sha_bridge.py
"""
from __future__ import annotations
from pathlib import Path
import hashlib
import json

P = 16231
P2 = P * P
ROOT = Path(__file__).resolve().parents[1]

def require(cond, message):
    if not cond:
        raise RuntimeError(message)

def load_json(relative):
    path = ROOT / relative
    require(path.is_file(), f"MISSING_INPUT {path}")
    return json.loads(path.read_text(encoding='utf-8'))

def main():
    level2 = load_json('historical/level2/v61_a2_p2_result.json')
    moment = load_json('historical/v65/v65_terminal_certificate.json')
    source_bridge = ROOT / 'paper/c01_sage_n3_minus_n2_universal_lemma_auditable_2026-10-26.md'
    source_gate = ROOT / 'results/kato389_sage10_9_terminal_pass_2026-10-19.md'
    provenance = ROOT / 'results/independent_scalar_J_global_263429130_pairs_PASS_2026-10-26.md'
    for f in [source_bridge, source_gate, provenance]:
        require(f.is_file(), f'MISSING_THEOREM_OR_EVIDENCE {f}')

    # Verify checksum of the original n=2 archive before relying on its values.
    body = {k: v for k, v in level2.items() if k != 'sha256'}
    canonical = json.dumps(body, sort_keys=True, separators=(',', ':')).encode()
    require(hashlib.sha256(canonical).hexdigest() == level2.get('sha256'),
            'LEVEL2_ARCHIVE_SHA256_MISMATCH')
    require(level2['precision_modulus'] == P2, 'WRONG_MODULUS')
    require(level2['a_covered'] == (P-1)//2, 'INCOMPLETE_LEVEL2_HALF_DOMAIN')
    require(level2['pair_count'] == ((P-1)//2)*P, 'BAD_PAIR_COUNT')
    require(level2['raw_f2_mod_p2'] == 79629286, 'LEVEL2_RAW_SUM_CHANGED')
    require(level2['sum_f1_mod_p2'] == 0, 'LEVEL2_LOWER_SUM_CHANGED')
    require(level2['alpha_mod_p2'] == 179060520, 'FROBENIUS_UNIT_ROOT_CHANGED')
    alpha = int(level2['alpha_mod_p2'])
    require((alpha*alpha - 128*alpha + P) % P2 == 0, 'UNIT_ROOT_NOT_A_ROOT')
    require(alpha % P == 128, 'WRONG_UNIT_ROOT_BRANCH')
    a2_n2 = int(level2['a2_n2_mod_p2'])
    require(a2_n2 == 1199*P, 'N2_QUADRATIC_COEFFICIENT_CHANGED')
    require(level2['lower_term_mod_p2'] == 0, 'LOWER_TERM_CHANGED')
    print('ARCHIVED_LEVEL2_COEFFICIENT_AUTHENTICATED_PASS', a2_n2, flush=True)

    # Terminal C01 value; its mathematical identity with the source-level
    # reference scalar is a separate theorem/provenance requirement.
    require(moment['status'] == 'V65_INDEPENDENT_TERMINAL_PASS', 'BAD_TERMINAL_STATUS')
    require(moment['generators'] == 67, 'WRONG_MANIN_DIMENSION')
    require((moment['J0'], moment['J1'], moment['J']) == (16014, 4703, 4486),
            'C01_SCALAR_CHANGED')
    require((moment['J0'] + moment['J1']) % P == moment['J'], 'BAD_SUM_OF_MOMENTS')
    original_report = provenance.read_text(encoding='utf-8')
    require('INDEPENDENT_SCALAR_GLOBAL_J_4486_PASS pairs=263429130' in original_report,
            'INDEPENDENT_GLOBAL_C01_REPORT_NOT_FOUND')
    print('ARCHIVED_GLOBAL_C01_REPORTED_PASS J', moment['J'], flush=True)

    # Universal n3 - n2 correction from published project lemma, using the
    # Frobenius alpha only modulo p because the correction is multiplied by p.
    bridge_text = source_bridge.read_text(encoding='utf-8')
    require('p*J_ref/(4*alpha²)' in bridge_text,
            'UNIVERSAL_BRIDGE_STATEMENT_MISSING')
    factor = pow(4*128*128, -1, P)
    correction_over_p = int(moment['J']) * factor % P
    a2_n3 = (a2_n2 + P * correction_over_p) % P2
    require(factor == 9362 and correction_over_p == 8335, 'CORRECTION_CHANGED')
    require(a2_n3 == 154746354 and a2_n3 % P == 0, 'N3_VALUE_CHANGED')
    a2_leading = (a2_n3 // P) % P
    require(a2_leading == 9534, 'ANALYTIC_LEADING_DIGIT_CHANGED')
    print('CYCLOTOMIC_L2_OVER_P_MOD_P_CONDITIONAL', a2_leading, flush=True)

    gate = source_gate.read_text(encoding='utf-8')
    for phrase in ['KATO389_LOCAL_RANK2_SURJECTIVE_ORDINARY_PASS',
                   "KATO389_NORMALIZATION_LEVEL3_PRECISION_PASS ['+Infinity', '2', '2']",
                   'KATO389_ARITHMETIC_GATE_PASS']:
        require(phrase in gate, 'MISSING_KATO_SAGE_SOURCE_GATE '+phrase)
    b_leading = (1930 * pow(1-pow(128, -1, P), 2, P)) % P
    require(b_leading == a2_leading != 0, 'BSD_REGULATOR_LEADING_DIGIT_MISMATCH')
    q = a2_leading * pow(b_leading, -1, P) % P
    require(q == 1, 'LEADING_QUOTIENT_CHANGED')
    print('CYCLOTOMIC_L2_BSD_FACTOR_UNIT_RATIO_CONDITIONAL_PASS',
          'v_p=0', 'ratio_mod_p=1', flush=True)
    print('PROVED_KATO_UPPER_EXPONENT_CONDITIONAL_ON_SOURCE_BRIDGE', 0, flush=True)
    print('SHA_16231_PRIMARY_ZERO_CONDITIONAL_ON_ARCHIVED_SOURCE_AND_INPUTS',flush=True)
    print('BOUNDARY: no direct Sage n3 or p_primary_bound run; '+
          'J_ref identification and finite-input correctness must be accepted.',flush=True)
    print('BOUNDARY: this is p-primary only, not global BSD, and '+
          'ratio=1 mod p is not exact p-adic BSD equality.',flush=True)

if __name__ == '__main__':
    main()