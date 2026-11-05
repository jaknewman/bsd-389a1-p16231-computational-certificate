#!/usr/bin/env python3
"""Construct a conductor-ONE CM embedding for K=Q(sqrt(-3)) in Brandt(389).

Unlike the existing conductor-53 Stage14 embedding, this finds omega in an
actual integral maximal left order with omega^2+omega+1=0, and constructs
its split local M2(Z/p^2) chart for p=16231. This corrects the otherwise
fatal conductor-53 contamination of a trivial-character p-tower.

Exact Sage and PARI qfminim enumeration, norm/trace, 16 multiplication
identities, and unimodular basis determinant; outputs a small JSON file.

This DOES NOT construct p-power Gross points or evaluate the theta series.
"""
import json
from pathlib import Path
from sage.all import BrandtModule, QQ, ZZ, Zmod, QuadraticForm, matrix, vector

P = 16231
MOD = P * P
R0, R1 = 49689135, 213756225
assert (R0 * R0 + R0 + 1) % MOD == 0
assert (R1 * R1 + R1 + 1) % MOD == 0
assert (R0 + R1 + 1) % MOD == 0
assert (R0 - R1) % P != 0

BM = BrandtModule(389, base_ring=QQ)
ideals = list(BM.right_ideals())
assert len(ideals) == 33
B = BM.quaternion_algebra()
weights = list(BM.monodromy_weights())
assert len(weights) == 33

def quadratic_norm_form(basis):
    # Sage's QuadraticForm(ZZ, 4, coeff) takes upper-triangular
    # coefficients, with off-diagonal coefficients of z_i*z_j.
    c = []
    norms = [ZZ(z.reduced_norm()) for z in basis]
    for i in range(4):
        for j in range(i, 4):
            c.append(norms[i] if i == j
                     else ZZ((basis[i] + basis[j]).reduced_norm()
                             - norms[i] - norms[j]))
    Q = QuadraticForm(ZZ, 4, c)
    for z in [(1, 0, 0, 0), (0, 1, 1, 0),
              (2, -3, 0, 1), (-1, 2, 3, 4)]:
        x = sum((ZZ(z[k]) * basis[k] for k in range(4)), B(0))
        assert Q(z) == x.reduced_norm()
    return Q

def cm_roots_for_order(order):
    basis = tuple(order.basis())
    assert len(basis) == 4
    Q = quadratic_norm_form(basis)
    assert Q.is_positive_definite()
    # Exhaustive by PARI Fincke-Pohst: all integral norm-one units.
    short = Q.short_vector_list_up_to_length(2, True)
    assert len(short) == 2
    roots = {}
    units = set()
    for vec in short[1]:
        z = tuple(int(v) for v in vec)
        for sg in (-1, 1):
            coord = tuple(sg * t for t in z)
            x = sum((ZZ(coord[k]) * basis[k] for k in range(4)), B(0))
            assert x in order and x.reduced_norm() == 1
            units.add(coord)
            if x.reduced_trace() == -1:
                assert x * x + x + B(1) == 0
                roots[coord] = x
    return basis, roots, len(units)

# The exact Brandt weight is half the number of order units. An
# integral omega root has six units mu_6, hence only weights divisible
# by three can contain O_K. This prefilter avoids 33 PARI enumerations.
from collections import Counter
hist = dict(sorted(Counter(int(w) for w in weights).items()))
print("CONDUCTOR1_CM_BRANDT_WEIGHT_HISTOGRAM", hist, flush=True)
candidate_indices = [idx for idx,w in enumerate(weights) if int(w) % 3 == 0]
assert candidate_indices, "NO_WEIGHT_DIVISIBLE_BY_THREE"
matches = []
for idx in candidate_indices:
    order = ideals[idx].left_order()
    basis, roots, n_units = cm_roots_for_order(order)
    assert n_units == 2 * int(weights[idx])
    for coord in roots:
        matches.append((idx,coord))
    print("CONDUCTOR1_CM_ORDER_FOUND", idx,
          "ROOTS",len(roots),"UNITS",n_units,
          "BRANDT_WEIGHT",int(weights[idx]),flush=True)

assert matches, "NO_MAXIMAL_CM_EMBEDDING: unexpected at discriminant 389"
print("CONDUCTOR1_CM_GLOBAL_EMBEDDINGS_PASS",
      len(matches), "ORDERS",len(set(i for i,_ in matches)),flush=True)
idx, coord = matches[0]
order = ideals[idx].left_order()
basis = tuple(order.basis())
omega = sum((ZZ(coord[k]) * basis[k] for k in range(4)), B(0))
assert omega in order
assert omega.reduced_trace() == -1 and omega.reduced_norm() == 1
assert omega * omega + omega + 1 == 0
print("CONDUCTOR1_CM_SELECTED_OPTIMAL_EMBEDDING_PASS",
      idx, list(coord), flush=True)

# O_K=Z[omega], so R_i intersect K=O_K automatically.
basis_coords = matrix(QQ, 4, 4,
   lambda i, j: QQ(basis[j].coefficient_tuple()[i]))
def coords(x):
    return basis_coords.solve_right(vector(QQ, list(x.coefficient_tuple())))
def red(x):
    x = QQ(x)
    n = int(x.numerator()) % MOD
    d = int(x.denominator()) % MOD
    assert d % P, ("NON_P_INTEGRAL", x)
    return (n * pow(d, -1, MOD)) % MOD
def zero(x):
    return all(red(t)==0 for t in coords(x))
def equal(x,y):
    return zero(x-y)

# Peirce matrix units in R_i tensor Z/p².
e = (omega-B(R1))/(R0-R1)
f = B(1)-e
assert equal(e*e,e) and equal(f*f,f)
assert zero(e*f) and zero(f*e) and equal(e+f,B(1))
print("CONDUCTOR1_CM_LOCAL_IDEMPOTENTS_PASS",flush=True)

selected = None
for j,bj in enumerate(basis):
    x=e*bj*f
    for k,bk in enumerate(basis):
        y0=f*bk*e
        c=red((x*y0).reduced_trace())
        if not c%P:
            continue
        y=pow(c,-1,MOD)*y0
        if (equal(x*y,e) and equal(y*x,f)
            and equal(e*x,x) and equal(x*f,x)
            and equal(f*y,y) and equal(y*e,y)
            and zero(x*x) and zero(y*y)):
            selected=(j,k,c,x,y)
            break
    if selected:
        break
assert selected is not None
j,k,c,x,y=selected
print("CONDUCTOR1_CM_LOCAL_MATRIX_UNITS_PASS",j,k,c,flush=True)

ring=Zmod(MOD)
def tr(z):
    return red(z.reduced_trace())
def image(z):
    return matrix(ring,2,2,[
        tr(e*z*e),tr(e*z*y),tr(x*z*e),tr(f*z*f)
    ])

assert image(B(1)) == matrix(ring,2,2,[1,0,0,1])
assert image(omega) == matrix(ring,2,2,[R0,0,0,R1])
maps=[image(t) for t in basis]
for a in range(4):
    assert int(maps[a].trace()) == red(basis[a].reduced_trace())
    assert int(maps[a].det()) == red(basis[a].reduced_norm())
    for b in range(4):
        assert image(basis[a]*basis[b]) == maps[a]*maps[b]
print("CONDUCTOR1_CM_LOCAL_16_PRODUCT_IDENTITIES_PASS",flush=True)

flat=[[int(M[0,0]),int(M[0,1]),int(M[1,0]),int(M[1,1])]
      for M in maps]
basis_map=matrix(ring,4,4,lambda a,b:flat[b][a])
det=int(basis_map.det())%MOD
assert det%P != 0
print("CONDUCTOR1_CM_LOCAL_M2_ISOMORPHISM_PASS",det,flush=True)

dest=Path.home()/"bsd389_p16231_conductor1_CM_base_and_local_split.json"
report={
    "status":"CONDUCTOR1_CM_GLOBAL_AND_P_LOCAL_SPLIT_PASS",
    "source":"Independent Sage BrandtModule(389), exhaustive norm-one qfminim",
    "curve":"389a1","K":"Q(sqrt(-3))","p":P,"modulus":MOD,
    "available_cm_root_embeddings":[{"brandt_index":i,"coordinates":list(v)}
                                   for i,v in matches],
    "selected_brandt_index":idx,
    "omega_basis_coordinates":list(coord),
    "omega_quaternion_coefficients":[str(v) for v in omega.coefficient_tuple()],
    "matrix_unit_basis_indices":[j,k],
    "matrix_unit_initial_trace":c,
    "omega_split_roots":[R0,R1],
    "order_basis_images":flat,
    "basis_map_determinant":det,
    "scope":"Conductor-1 optimal embedding and p^2 local splitting; Gross class assignments and theta derivative NOT computed"
}
dest.write_text(json.dumps(report,indent=2)+"\n")
print("CONDUCTOR1_CM_JSON_REPORT",dest,flush=True)
print("CONDUCTOR1_CM_GLOBAL_AND_P_LOCAL_SPLIT_PASS",flush=True)
print("BOUNDARY_PPOWER_GROSS_POINT_CLASSES_NOT_YET_COMPUTED",flush=True)
print("BOUNDARY_THETA_DERIVATIVE_AND_SHA_NOT_PROVED",flush=True)
