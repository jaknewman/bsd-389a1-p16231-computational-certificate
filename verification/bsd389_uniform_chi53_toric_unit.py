#!/usr/bin/env python3
"""Pure-Python exact integral uniform factor for the ARCHIVED chi53 orbit.

Verifies only the algebraic polynomial consequences of the frozen 18
coefficients, NOT the origin of the Gross orbit, theta derivative,
Kato primitivity or the Tate-Shafarevich group.
"""

COEFFS = (0, 0, -1, 0, 0, -1, -1, 2, 2, -1, -1, 2, 2, -1, -1, 0, 0, -1)
PHI9 = (1, 0, 0, 1, 0, 0, 1)   # 1 + X^3 + X^6
PHI3 = (1, 1, 1)
U = (1, 0, -1, 1, 1)           # 1-X^2+X^3+X^4
U_INV = (-1, 0, 0, -1, 1)     # -1-X^3+X^4


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            z[i+j] += v*w
    return trim(z)


def mod(a, phi):
    a = trim(a)
    deg = len(phi) - 1
    assert phi[-1] == 1
    while len(a) > deg:
        q = a[-1]
        off = len(a) - len(phi)
        for j, coefficient in enumerate(phi):
            a[off+j] -= q*coefficient
        a = trim(a)
    return a


def determinant_bareiss(rows):
    a = [list(r) for r in rows]
    n = len(a)
    assert all(len(r) == n for r in a)
    sign = 1
    previous = 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k+1, n) if a[r][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value = a[i][j]*pivot - a[i][k]*a[k][j]
                assert value % previous == 0
                a[i][j] = value // previous
        for i in range(k+1,n):
            a[i][k] = 0
        previous = pivot
    return sign*a[n-1][n-1]


def main():
    assert mod(COEFFS, PHI9) == [0, -3, 0, 3, -3, -3]
    assert mod(COEFFS, PHI3) == [0]
    assert mod(mul(U, U_INV), PHI9) == [1]
    assert mod(COEFFS, PHI9) == mod(mul((0, -3), U), PHI9)
    print('UNIFORM_CHI53_EXACT_CYCLOTOMIC_FACTOR_PASS F=-3*zeta9*U')
    print('UNIFORM_CHI53_EXPLICIT_INVERSE_PASS U*UINV=1')
    # Multiplication by F(zeta9) on Z[zeta9] has determinant the norm.
    deg = len(PHI9)-1
    basis_cols = [mod(mul(COEFFS, [0]*j+[1]), PHI9) for j in range(deg)]
    matrix = [[(col[i] if i < len(col) else 0) for col in basis_cols]
              for i in range(deg)]
    norm = determinant_bareiss(matrix)
    assert norm == 729 == 3**6
    print('UNIFORM_CHI53_NORM_DETERMINANT_PASS', norm)
    print('UNIFORM_CHI53_P_UNIT_ALL_PRIMES_EXCEPT_3_MATHEMATICAL_PASS')
    print('SPLITTING_SCOPE chi53_K_minus3 only applies to p congruent 1 modulo 3')
    print('BOUNDARY_NO_SHA_UNIFORM_FINITE_SUPPORT_PROOF; theta_order2_and_integral_primitivity_not_proved')


if __name__ == '__main__':
    main()
