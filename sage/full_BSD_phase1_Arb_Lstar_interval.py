#!/usr/bin/env python3
"""BSD 389a1 / Phase I: rigorous analytic leading coefficient enclosure.

SageMath 10.9, execute with the activated Miniforge Sage `python -u`.
Does not use PARI/Dokchitser, real periods, regulators or conjectural Sha.

Mathematical premise: L(E,1)=0, certified separately via exact modular symbols;
root number +1 implies L'(E,1)=0. Therefore
    L''(E,1)/2 = c * integral_0^infinity exp(t) t^2
                    sum_{n>=1} a_n exp(-c n exp(t)) dt,
    c = 2*pi/sqrt(389).

Uses FLINT/Arb CBF.integral for mathematically validated quadrature;
explicit globally valid Fourier and integral-tail bounds are added to the ball.
"""
from sage.all import EllipticCurve, RealBallField, ComplexBallField, ZZ, proof

proof.all(True)
E = EllipticCurve('389a1')
assert E.conductor() == ZZ(389) and E.root_number() == 1
assert E.rank(proof=True) == 2
M, T, PREC = 160, 7, 160
an = [int(a) for a in E.anlist(M)[1:]]
assert len(an) == M
assert an[:20] == [1, -2, -2, 2, -3, 4, -5, 0, 1, 6, -4, -4,
                   -3, 10, 6, -4, -6, -2, 5, -6]
print('BSD389_PHASE1_ARITHMETIC_AND_Q_EXPANSION_PASS', M, flush=True)

R = RealBallField(PREC)
C = ComplexBallField(PREC)
c = R(2) * R.pi() / R(389).sqrt()
cc = C(c)

def integrand(z, analytic):
    # Entire function. The analytic flag does not change the function.
    y = z.exp()
    q = (-cc * y).exp()
    f = C(0)
    for a in reversed(an):
        f = (f + a) * q
    return cc * y * z * z * f

# Splitting improves adaptive ball integration convergence.
# acb_calc_integrate encloses both rounding and quadrature errors.
segments = [(0, 1), (1, 2), (2, 4), (4, T)]
finite = C(0)
for left, right in segments:
    part = C.integral(integrand, left, right,
                      rel_tol=2.0**-55, abs_tol=2.0**-55,
                      eval_limit=40000)
    finite += part
    print('BSD389_ARB_RIGOROUS_SEGMENT', left, right, part, flush=True)

# All n: Deligne/Hasse + multiplicativity gives
# |a_n| <= d(n)*sqrt(n) <= 2*n.
# Fourier remainder after n=M, integrated on y>=1:
# log(y)^2 <= (y-1)^2, and
# int_1^inf (y-1)^2 exp(-c*n*y) dy = 2 exp(-c*n)/(c*n)^3.
# Summing n>=M+1 bounds it by
# 4 exp(-c*(M+1)) / (c^2*(M+1)^2*(1-exp(-c))).
q = (-c).exp()
n0 = M + 1
fourier_bound = (R(4) * (-c*n0).exp() /
                (c*c*R(n0*n0)*(1-q))).above_abs()

# Integral remainder for t>=T, y>=Y=exp(T):
# log(y)^2 <= y^2, sum_n 2*n exp(-c*n*y) = 2*r/(1-r)^2,
# r = exp(-c*y) <= exp(-c*Y).
Y = R(T).exp()
rY = (-c*Y).exp()
integral_bound = (R(2)*rY/(1-rY)**2 *
                  (Y**2 + 2*Y/c + 2/c**2)).above_abs()

print('BSD389_ARB_RIGOROUS_FOURIER_TAIL_UPPER', fourier_bound, flush=True)
print('BSD389_ARB_RIGOROUS_INTEGRAL_TAIL_UPPER', integral_bound, flush=True)
assert fourier_bound < R('1e-22')
assert integral_bound < R('1e-130')

# The real part of a CBF integral is a rigorous real enclosure.
# Since the omitted tails have arbitrary signs, widen symmetrically.
full = finite.real().add_error(fourier_bound + integral_bound)
assert full > R(0)
assert full < R(1)
print('BSD389_ARB_RIGOROUS_ANALYTIC_LSTAR_ENCLOSURE', full, flush=True)
print('BSD389_ARB_RIGOROUS_ANALYTIC_LSTAR_RADIUS', full.rad(), flush=True)
reference = R('0.7593165002884267702301926078947220190781')
assert (full - reference).contains_zero(), 'Interval misses independent numerical reference'
print('BSD389_PHASE1_ANALYTIC_ENCLOSURE_PASS', flush=True)
print('BOUNDARY: L(E,1)=0 must be separately exact-certified (not inferred from numeric Lstar)', flush=True)
print('BOUNDARY: period/regulator are NOT enclosed here; no equality of transcendental factors proved', flush=True)
print('BOUNDARY: global Sha finiteness and #Sha=1 remain unproved', flush=True)
