#!/usr/bin/env python3
"""Exact finite-field audit of three MW local matrices at p=5,7,107.

This does NOT compute Sha, prove global duality or certify an Euler system.
The cohomological proof is in the companion paper note.
"""
DATA = [
    (5, (41, 61), ((1, 3), (1, 0)), ((0, 1), (2, 3))),
    (7, (113, 673), ((1, 3), (1, 6)), ((2, 6), (2, 5))),
    (107, (369793, 383917), ((1, 15), (1, 53)), ((38, 70), (76, 31))),
]

def mul(A, B, p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) % p
                       for j in range(2)) for i in range(2))

def trans(A):
    return tuple(tuple(A[j][i] for j in range(2)) for i in range(2))

ID = ((1, 0), (0, 1))
for p, qs, A, inv_expected in DATA:
    det = (A[0][0]*A[1][1]-A[0][1]*A[1][0]) % p
    assert det != 0
    dinv = pow(det, -1, p)
    inv = tuple(tuple(v*dinv % p for v in row) for row in
                ((A[1][1], -A[0][1]), (-A[1][0], A[0][0])))
    assert inv == inv_expected
    assert mul(A, inv, p) == ID == mul(inv, A, p)
    assert mul(trans(A), trans(inv), p) == ID
    singular_kernel = [(u, v) for u in range(p) for v in range(p)
        if (A[0][0]*u + A[1][0]*v) % p == 0
        and (A[0][1]*u + A[1][1]*v) % p == 0]
    assert singular_kernel == [(0, 0)]
    print("PT_LOCAL_DUALITY_MATRIX_AUDIT_PASS", "p", p, "q", qs,
          "det", det, "inverse", inv, "orthogonal_singular_kernel", 0)
print("SCOPE_LOCAL_LINEAR_ALGEBRA_ONLY_PTI_FROM_STANDARD_GLOBAL_DUALITY")
