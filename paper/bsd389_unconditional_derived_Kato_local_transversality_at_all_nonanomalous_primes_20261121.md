# E389a1 — unconditional genuine derived Kato classes give a complementary p-local line at every nonanomalous good prime

**2026-11-21.** A positive uniform cohomological theorem by applying the
published Castella--Sano + Kim reciprocity theorems to E389a1.
This NOTE does NOT prove that a witness of AUXILIARY DEGREE TWO exists
at every p, that the global Sha is finite, or that exact complex BSD holds.

E/Q: y^2+y=x^3+x^2-2x, N=389, rank E(Q)=2, trivial rational
torsion, minimal discriminant 389, Tamagawa product=1,
optimal modular parametrization with Manin constant 1.
Full residual image GL2(Fp) at all p>=5 follows from the
semistable image theorem for p>=11 and explicit p5,p7 gates.

Primary-source inputs checked against actual statements:

(A) F. Castella & T. Sano, *On refined nonvanishing conjectures
by Kurihara and Kolyvagin*, 20 January 2026 preprint,
Theorem B and Corollary A, printed page 3:
https://web.math.ucsb.edu/~castella/Kurihara.pdf
For p>3 with surjective residual image, p-unit Manin
constant, good ordinary reduction OR good supersingular
reduction with N squarefree, M_infty(delta)=v_p(Tam_E)=0.
Thus there exists a p-admissible squarefree auxiliary
conductor n with a p-UNIT normalized Kurihara coefficient
delta_n; the number nu(n) of prime factors is NOT bounded.

(B) Same preprint, Theorem 2.1.3, printed page 7,
citing C.-H. Kim, *The structure of Selmer groups and
the Iwasawa main conjecture for elliptic curves*,
Theorem 3.11:
https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
For each such n>1, a GENUINE Kato-derived cohomology class
kappa_n^Kato in H^1(Q,T_p(E)/I_n T_p(E)) satisfies
    expbar_omega^*(res_p(kappa_n^Kato))
       = u_n * p^t * delta_n    in Z_p/I_n,
where u_n is a unit and p^t=#E(Q_p)[p^infty].

This is an integral derived cohomological class CONSTRUCTED
by the Euler/Kolyvagin machinery, NOT the nonexistent
corestriction lifts yP,yQ postulated in the older
rank-two exterior-product norm repair.

## Theorem 1 — uniform local Kummer complement, without Sha finiteness

Fix ANY good prime p>=5 with p not dividing #E(F_p).
Let V=E[p]. Then there exists an admissible auxiliary
conductor n(p) and a nonzero residual global derived
Kato class kappa_n bar in H^1(Q,V) such that
    expbar_omega^*(loc_p(kappa_n bar)) != 0 (mod p).

Moreover, with H_f^1(Q_p,V) denoting the local Kummer
subspace, one has the DIRECT SUM decomposition
    **H^1(Q_p,V)
      = H_f^1(Q_p,V) (+) F_p*loc_p(kappa_n bar).**

PROOF.
1. Since E has good reduction and p>=5, the reduction
   kernel E_1(Q_p) has no p-torsion. Nonanomaly implies
   E(F_p)[p]=0, whence E(Q_p)[p]=0.
   Consequently E(Q_p)/p is 1-dimensional F_p.
2. The local Euler characteristic and Weil self-duality
   yield dim_Fp H^1(Q_p,E[p])=2 because H^0(Q_p,E[p])=0.
   The Kummer subgroup H_f has dimension one.
3. The local dual exponential vanishes on the Bloch--Kato
   finite local condition, hence its integral mod-p
   reduction expbar^* vanishes on H_f^1(Q_p,V).
4. Castella--Sano Theorem B gives n with delta_n a
   p-unit. Nonanomaly makes t=0. Kim's derived explicit
   reciprocity then proves expbar^*(loc_p(kappa_n bar))
   =u_n delta_n !=0 mod p. The Kato class has
   NONZERO localization in the complementary
   1-dimensional quotient H^1/H_f.
5. Therefore expbar^* is a nonzero functional on the
   2-dimensional H^1 with 1-dimensional H_f in its
   kernel. Its kernel is exactly H_f, and the
   Kato localization spans a complement. QED.

**NO assumption on Sha[p^infty] was used.**
The theorem works whether or not Sha[p] is nonzero:
the number of auxiliary prime factors in n can
increase when the p-Selmer dimension is larger.
The local complement is a genuine positive
p-uniform Kato-cohomological construction, not
a global Selmer-rank bound.

## Theorem 2 — one can identify the EXACT missing auxiliary degree

For p as above, let mu_p be the smallest number of
factors in an auxiliary conductor n with delta_n
a p-unit. Kim Theorem 1.8 plus the Kummer sequence
and the Castella--Sano nonvanishing theorem give:
   mu_p = dim_Fp Sel(Q,E[p])
        = 2 + dim_Fp Sha(E/Q)[p].

Therefore:
- a genuine local-transverse derived Kato class
  exists for SOME (possibly many-factor) conductor
  at EVERY good nonanomalous p (Theorem 1);
- a local-transverse derived Kato class at a
  TWO-factor conductor exists iff Sha[p]=0.
  (This is Kim's algebraic equivalence, NOT
  an independent vanishing proof.)

Thus Theorem 1 solves existence of an ACTUAL
Kato-derived class but does not solve its
two-auxiliary degree restriction.

## Explicit independent arithmetic certificates

The 390-coordinate plus Manin vector from the earlier
real Sage/eclib oracle was frozen with SHA256
   31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee
for its shifted digit encoding.

Exact continued fractions and complete modular-symbol
sums, evaluated by standard-library rational/integer
Python in the current assistant environment:
- p=5, (q1,q2)=(41,61):
  phi(q1*q2)=2400, half reps=1200,
  (M00,M10,M01,M11)=(0,0,0,4) mod 5.
- p=7, (q1,q2)=(113,673):
  phi(q1*q2)=75264, half reps=37632,
  (M00,M10,M01,M11)=(0,0,0,2) mod 7.
- p=11, (q1,q2)=(397,991):
  phi(q1*q2)=392040, half reps=196020,
  (M00,M10,M01,M11)=(0,0,0,1) mod 11.
- an extra p5 pair (61,991):
  phi=59400, half=29700, moments=(0,0,0,3) mod5.

For these p, #E(F_p)=(9,13,16) respectively, so t=0.
Kim Theorem 2.1.3 therefore PROVES that the genuine
corresponding Kato-derived cohomology classes
have p-local dual-exp residues that are NONZERO
modulo p. Their exact residues are u_n times
the displayed numbers; **the unit u_n is NOT
numerically computed and must not be invented**.

This proves that the actual Kato-derived classes
lie outside the ordinary global Mordell--Weil
Kummer image after localization at p.
They supply the non-Kummer local ramification
that the older pure-norm MW wedge constructions lacked.

Verification source:
  verification/bsd389_Kato_derived_local_transverse_three_primes_20261121.py
recomputes the arithmetic coefficients independently
from the FROZEN vector, not from a new Sage/eclib
extraction. The cohomology statement is theorem-level,
not a numerical computation of Galois cocycles.

## Critical source audit — DO NOT reverse BKS hypotheses

D. Burns, M. Kurihara, T. Sano, *On derivatives of Kato's
Euler system for elliptic curves*, J. Math. Soc. Japan
76 (2024), pp. 855-919, primary PDF:
https://kurihara.math.keio.ac.jp/bks4.pdf

- Their Hypothesis 2.2(iii) **ASSUMES Sha[p^infty] finite**.
- The opening of Section 4 (printed p.876) explicitly
  assumes H^1(Z_S,T) is Z_p-free AND Sha[p^infty] finite.
- Thus their Proposition 4.4 and Definition 4.5 of
  the cyclotomic Iwasawa--Darmon derivative, as
  stated in that section, CANNOT be invoked to
  prove Sha finiteness for E389a1: it is an
  assumption of the result in that formulation.
- Their higher Rubin formula Theorem 6.2 also
  assumes Hypothesis 2.2 and cannot eliminate it.
- Their Kato order-of-vanishing inequality for
  the p-adic L-function (Proposition 6.1, citing
  Kato Theorem 18.4) is a distinct necessary
  vanishing statement and does not assert a
  p-UNIT leading coefficient at rank two.
- BKS Proposition 4.14 is an EQUIVALENCE with
  their unproved Conjecture 4.8, not a
  proof of the integral leading coefficient.

This source audit makes the distinction between
(A) actual unconditional Kim/BCS derived classes,
(B) BKS higher-rank Bockstein comparisons with
finite-Sha hypothesis, unambiguous.

## Exact obstruction to inferring a unit second coefficient from IMC

Let p>=5, R=Z_p[[T]], and consider
  f(T)=p*T^2 + T^3.

It has:
  ord_T(f)=2 in Q_p[[T]], and
  mu(f):=min_j v_p([T^j] f)=0,
but the quadratic coefficient is p and is NOT
a p-unit. Likewise g(T)=T^4 has mu=0
and vanishes at every degree <4.

These elementary countermodels prove that
the all-prime Iwasawa primitivity statement
M_infty(delta)=0 and even a rational exact
rank-two leading-order statement do NOT imply
the required integral degree-two unit. A genuine
comparison/regulator controlling that integral
coefficient is needed to bound the true
Fitt_2(X_p) for all large p.

## Exact next goal

Produce an arithmetically independent bound on the
number of auxiliary factors required to obtain
a primitive Kato-derived class, or an integral
derived height/Bockstein comparison that FORCES
the degree-two coefficient to be a p-unit at
every sufficiently large p.

Neither the uniform local complement nor
the Iwasawa main conjecture supplies this
degree-two estimate. The complex BSD leading
term remains independent and unproved.
