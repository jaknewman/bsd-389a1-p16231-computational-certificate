# E389a1: regularized 2+1 GMA modulo p^n, local Kummer size, and the missing integral bridge

Date: 2026-11-21. Starting point: d72c386 (nonregularity of V_p(E) + 1).
This is a mathematically limited **finite-level coefficient result**, not full BSD.

## Exact coefficient statement

Let E : y^2+y=x^3+x^2-2x and T=T_p(E), p >= 5. Set
k_n=(p-1)p^(n-1), R_{p,n}=T + Z_p(k_n).
The upper-right trace-zero adjoint block is
Hom(Z_p(k_n),T)/p^n = (T/p^n)(-k_n).
The p-adic cyclotomic character to the power k_n is 1 modulo p^n
(Euler's theorem), so this Galois module is isomorphic to E[p^n].
It follows that H^1 of the two coefficients agrees. When the local
conditions are **defined by transport from the Kummer conditions**
the resulting mod-p^n Selmer group is the elliptic one.
This does not identify natural automorphic local conditions.

In the convention HT(Q_p(1))=-1, the rational diagonal sum
V_p(E) + Q_p(k_n) has weights 0,-1,-k_n, which are distinct.
The rational upper-right block V_p(E)(-k_n) has weights
k_n,k_n-1. It has zero Bloch--Kato H^1_f dimension at p
(p >= 5, p != 389), whereas V_p(E) has H^1_f dimension one.
Consequently the rational finite local condition does not agree
with the elliptic one. This dimensional difference is not a proof
about the size of the intrinsic finite-level torsion local condition.

## Exact local Kummer quotient at six certified primes

For p = 5,7,11,107,599,16231, independently count the points on
the reduction of E. The pairs (a_p,#E(F_p)) are:
( -3,9),(-5,13),(-4,16),(0,108),(0,600),(128,16104).
All six have p not dividing #E(F_p). Since p>=5 and p!=389,
E has good reduction at p and the formal-group kernel
E_1(Q_p) is topologically Z_p. The reduction group has order
prime to p. Therefore E(Q_p)/p^n E(Q_p) is Z/p^n Z.
The local Kummer group has order p^n and Z_p-length n
for every n>=1, not just for the four experimentally sampled levels.

In particular, when a proposed local comparison replaces the
elliptic Kummer subgroup by zero, it loses a subgroup of order
p^n; hence any truly integral local correction for that replacement
must account for this length n. **We have not established that the
intrinsic finite-level Bloch--Kato subgroup of the regularized
twist is zero**, so no general lower bound n on an automorphic
comparison cokernel is claimed.

## The tower issue: no fixed compatible regularization

The weights depend on n: k_n=(p-1)p^(n-1). For p>=5 the LTE lemma
gives v_p((1+p)^k_n -1)=n and even
(1+p)^k_n = 1-p^n (mod p^(n+1)).
Thus the specific diagonal companion at level n is not the same
as the companion at level n+1. Each E[p^n] is seen at its own
regularized weight; the family is **not a single fixed rational
Galois representation whose ordinary reductions yield E[p^n]
for every n**. In the p-adic weight space k_n tends to zero,
but ordinary integer weights tend to infinity.

A continuous compatible integral or derived automorphic
interpolation across these levels, its intrinsic local Selmer
conditions, and a uniform bound on any denominators are entirely
unproved. Even an interpolation would not by itself fix the
direction of the congruence/Fitting inequality from d72c386.

## Criterion for a usable global conclusion

A genuinely nonzero fixed integer D, independent of p and n,
annihilating Sha(E/Q)[p^n] for all primes and levels, would imply
Sha(E/Q) is finite: prime-to-D primary components would vanish;
the finitely many components at p dividing D would have bounded
exponent and, by finite corank/cofinite-generation properties
of elliptic p-Selmer, be finite. No such D is constructed.

Next mathematical target: an actual nonregular/derived integral
automorphic Selmer comparison that preserves the p-local Kummer
condition, plus a reverse-direction Fitting bound independent of
both p and n. The regularized module identity alone cannot do it.

## Machine-checkable regression

- verification/bsd389_regularized_gma_coefficients_20261121.py:
  828 checks across p=5,7,11,107,599,16231; n=1..4; 12 small
  Frobenius primes; independent point counts for trace values.
  Hash (enumerated test inputs):
  4d86c06ecfa7598abb199b6041210f07fbacb7bbaf61bbe224cbea57128344c0.
- verification/bsd389_regularized_gma_local_kummer_20261121.py:
  point-counts (including p=16231 via Legendre sums), plus
  204 sample cyclotomic congruences at n=1..4.
All identities are proven above; the checks are illustrative, not
a substitute for the global number-theoretic arguments.
