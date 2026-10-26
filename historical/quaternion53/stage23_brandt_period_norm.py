#!/usr/bin/env python3
"""Stage 23: exact Brandt-coordinate/CM-period normalization audit.
This does NOT certify the remaining adelic test-vector identification.
Run inside Sage environment: python -u bsd389_chi53_stage23_normalization_audit.py
"""
import json
from pathlib import Path
from collections import Counter
from sage.all import ZZ, QQ, vector, BrandtModule, PolynomialRing, cyclotomic_polynomial

H = Path.home()
s14 = json.loads((H/'bsd389_chi53_stage14_orbit19.json').read_text())
s7 = json.loads((H/'bsd389_quaternion_53_stage7_pair_audit.json').read_text())
steps = s14['steps']
assert len(steps) == len(s14['values']) == 18

# Certified integer eigenvector; see independent Stage 3 Hecke audit.
v = vector(ZZ, [0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0])
assert len(v) == 33
B = BrandtModule(ZZ(389))
assert B.dimension() == 33
W = tuple(ZZ(w) for w in B.monodromy_weights())
print('BRANDT_WEIGHT_VECTOR', list(W), flush=True)
print('BRANDT_EIGENVECTOR', list(v), flush=True)

# Do not silently assume Sage's right-ideal indexing coincides with Stage 14:
# this equality is necessary but by itself not sufficient to establish the identification.
ids = [int(s['index']) for s in steps]
vals = [ZZ(x) for x in s14['values']]
assert all(0 <= i < 33 for i in ids)
assert [v[i] for i in ids] == vals, 'BRANDT_VECTOR_INDEXING_DISAGREES_WITH_STAGE14'
print('STAGE23_VECTOR_INDEX_MATCH_PASS')

pairs = {(int(p['order_index']), tuple(int(z) for z in p['theta_coordinates'])): int(p['pair_id']) for p in s7['pairs']}
pairs.update({(int(p['order_index']), tuple(int(z) for z in p['conjugate_coordinates'])): int(p['pair_id']) for p in s7['pairs']})
ids_pair = [pairs[(int(s['index']), tuple(int(z) for z in s['coefficients']))] for s in steps]
assert sorted(ids_pair) == list(range(18))
print('STAGE23_EMBEDDING_BIJECTION_PASS')

for k,i in enumerate(ids):
    print('CM_VALUE', k, 'BRANDT_INDEX', i, 'PAIR', ids_pair[k], 'VALUE', vals[k], 'WEIGHT', W[i], flush=True)

orb_w = [W[i] for i in ids]
if all(w == 1 for w in orb_w):
    print('STAGE23_ORBIT_MASS_WEIGHTS_ONE_PASS')
else:
    print('STAGE23_ORBIT_MASS_WEIGHTS_NOT_ALL_ONE', orb_w)
    raise AssertionError('Stage6 unit counts or Sage indexing require reconciliation')

T2 = B.hecke_matrix(2)
right = T2*v
left = v*T2
print('T2_RIGHT_EIGEN', bool(right == -2*v), 'T2_LEFT_EIGEN', bool(left == -2*v), flush=True)
assert right == -2*v or left == -2*v, 'STAGE23_EIGENLINE_T2_FAIL'
print('STAGE23_T2_EIGENLINE_PASS')

R = PolynomialRing(QQ, 'X'); X = R.gen()
P = sum(QQ(vals[k])*X**k for k in range(18))
phi9 = R(cyclotomic_polynomial(9))
rem = P % phi9
assert rem != 0
assert phi9.resultant(P) == 729
assert P % R(cyclotomic_polynomial(3)) == 0
print('STAGE23_ORDER9_REMAINDER', rem)
print('STAGE23_ORDER9_NORM', phi9.resultant(P))
print('STAGE23_BRANDT_FUNCTION_VALUES_AND_PERIOD_PASS')
print('STAGE23_REFERENCE_CM_POINT_AT_CONDUCTOR1_OPEN')
print('STAGE23_ADELIC_LIFT_AND_ORIENTATION_OPEN')
print('STAGE23_WALDSPURGER_TEST_VECTOR_IDENTIFICATION_OPEN')
print('L_CENTRAL_NONVANISHING_NOT_CERTIFIED')