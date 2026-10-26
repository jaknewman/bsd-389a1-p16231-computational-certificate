#!/usr/bin/env python3
"""Exact Brandt/elliptic-curve Hecke audit for 389a1. Run using python inside Sage."""
from sage.all import *
import json
from pathlib import Path

ROOT = Path.home()
E = EllipticCurve('389a1')
B = BrandtModule(389)
v_list = [0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0]
v = vector(QQ,v_list)
assert B.dimension() == len(v) == 33
assert v != 0

# The agreement of this vector with the serialized orbit is a separate check.
p14 = ROOT / 'bsd389_chi53_stage14_orbit19.json'
if p14.exists():
    orbit = json.loads(p14.read_text())
    steps = orbit['steps']
    assert len(steps) == 18
    vals = [ZZ(v_list[int(s['index'])]) for s in steps]
    assert vals == [ZZ(z) for z in orbit['values']]
    print('STAGE30_ORBIT_COORDINATES_MATCH_PASS', flush=True)
else:
    print('STAGE30_ORBIT_JSON_NOT_FOUND', flush=True)

sturm = (2 * (389 + 1)) // 12
assert sturm == 65
primes = list(prime_range(sturm+1))
print('STAGE30_STURM_BOUND', sturm, 'PRIMES', primes, flush=True)

# The endomorphism convention must be determined before using the eigenline.
# Test the operator on column vectors (M*v), the action naturally associated
# with Sage's Hecke module coordinates. Also report row convention separately.
blocks = []
row_blocks = []
rows = []
for ell in primes:
    a = ZZ(E.ap(ell))
    T = B.hecke_matrix(ell).change_ring(QQ)
    A = T - a*identity_matrix(QQ,len(v))
    right_ok = A*v == 0
    left_ok = v*A == 0
    print('HECKE_PRIME', int(ell), 'A_ELL', int(a),
          'COLUMN', bool(right_ok), 'ROW', bool(left_ok), flush=True)
    if not right_ok:
        raise ArithmeticError('FAIL_COLUMN_HECKE_AT_%s' % ell)
    blocks.append(A)
    row_blocks.append(A.transpose())
    rows.append((int(ell),int(a),bool(right_ok),bool(left_ok)))

stack = block_matrix(QQ, len(blocks), 1, blocks, subdivide=False)
rank = stack.rank()
nullity = len(v) - rank
assert nullity >= 1
print('STAGE30_COMMON_COLUMN_EIGENSPACE_RANK',rank,'NULLITY',nullity,flush=True)
if nullity != 1:
    raise ArithmeticError('JOINT_EIGENSPACE_NOT_ONE_DIMENSIONAL')
print('STAGE30_HECkE_STURM_AND_MULTIPLICITY_ONE_PASS',flush=True)

# Consistency of the Brandt class-function coordinates with the function used
# in the CM sum is certified by comparing the exact source data, not by an
# independent Waldspurger assertion.
report = {
    'curve':'389a1','weight':2,'level':389,'sturm_bound':int(sturm),
    'primes':primes,'hecke_data':rows,'right_column_nullity':int(nullity),
    'brandt_vector':[int(x) for x in v],
    'status':'STAGE30_HECkE_STURM_AND_MULTIPLICITY_ONE_PASS',
    'waldspurger_adelic_period_identification':'NOT_CERTIFIED_BY_THIS_SCRIPT'
}
out = ROOT / 'bsd389_chi53_stage30_hecke_sturm.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print('OUTPUT',out,flush=True)
print('ADELIC_TORIC_PERIOD_IDENTIFICATION_SEPARATE_FROM_HECKE',flush=True)
print('EXIT_STATUS_SUCCESS',flush=True)