# E389a1: minimal unit Kurihara degree = full mod-p Selmer dimension, even at anomalous primes

Date 2026-11-21; target E: y^2+y=x^3+x^2-2x, N=389, Delta=389,
MW rank2, E(Q)_tors=0, Manin constant1, Tamagawa product1.

**NEW strengthening of the preexisting 2026-11-14 research-branch theorem**:
the exact degree/dimension equality needs NO local hypothesis
E(Q_p)[p]=0. In particular it applies at all good ordinary and
supersingular p>=5, including anomalous primes p|#E(F_p). This
eliminates a condition from the older argument using Kim Thm 1.10.
It does not prove degree two always occurs, nor global Sha finiteness.

Primary sources independently read against the theorem statements:

- C.-H. Kim, *The structure of Selmer groups and the Iwasawa main
  conjecture for elliptic curves*, Thm 1.8(1),(2), displayed structure
  formula, printed page 7:
  https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
- F. Castella, T. Sano, *On refined nonvanishing conjectures by
  Kurihara and Kolyvagin*, Theorem B, printed page 3:
  https://web.math.ucsb.edu/~castella/Kurihara.pdf
- W. Stein, C. Wuthrich, *Algorithms for the arithmetic of elliptic
  curves using Iwasawa theory*, Thm 12.3, printed page 1788:
  https://wstein.org/papers/mcom2649-iwasawa-alg.pdf
- LMFDB full E389a1 data:
  https://www.lmfdb.org/EllipticCurve/Q/389a1/

## 1. Theorem and proof

For p>=5 with p!=389 let
  S_p=Sel(Q,E[p^infty]),  X_p=S_p^vee,
  A_p=Sha(E/Q)[p^infty],
and let \tilde\delta_{p,n} be the genuine integral
Neron-period normalized Kurihara coefficients in Z_p/I_n.
Let
  mu_p=min { nu(n): \tilde\delta_{p,n} NOT IN p(Z_p/I_n) },
where nu(n) is the number of auxiliary prime factors and
the minimum of empty set is +infinity.

**Theorem (all good p):**

  mu_p = dim_{F_p} Sel(Q,E[p])
       = 2 + dim_{F_p} Sha(E/Q)[p].

In particular:
  mu_p=2 iff Sha(E/Q)[p^infty]=0.
  mu_p=4 iff dim_Fp Sha(E/Q)[p]=2.
  mu_p=6 iff dim_Fp Sha(E/Q)[p]=4.
More generally mu_p is finite and even for all p>=5 good.

**Proof.** By the LMFDB full-image result and the project's
earlier all-prime Sage certification, E[p] has surjective
GL_2(F_p) image for every p>=5. Since the optimal Manin
constant and Tamagawa product equal 1, Castella--Sano
Theorem B applies at every good p: ordinary p automatically,
supersingular p by N=389 squarefree. Thus
  partial^(infty)(\tilde\delta_p)=0,
so at least one unit coefficient exists and mu_p<infinity.

Put rho=ord(\tilde\delta_p), defined by the first NONZERO
coefficient in its finite ring (which may be divisible by p).
By Kim Theorem 1.8, rho=cork_Zp(S_p).
The same theorem's structure formula gives:
  S_p = (Q_p/Z_p)^rho (+)
    (+)_{i>=1} (Z/p^{e_i}Z)^{(+2)}, e_i>=0,
where only finitely many e_i are positive.
This is the precise published theorem, independent of
E(Q_p)[p]=0; that local torsion assumption is instead
required for the separate semilocal isomorphism in Kim
Theorem 1.10.

Let d=d_{Z_p}(X_p)=dim_{F_p}(X_p/pX_p), the MINIMUM number of
generators over the local ring Z_p. The displayed
structure shows d=rho+2s, where s counts the positive
paired exponents, so d and rho have the same parity.

For every finitely generated module M over a local ring R,
  Fitt_i(M)=R  iff  i>=d_R(M).
Indeed a presentation with d minimal generators has an
identity-size zero minor at i=d, and the lower Fitting
ideals are contained in the maximal ideal; equivalently
Nakayama identifies d with dimension of M/mM.

For i>=rho with i congruent to rho modulo 2, Kim 1.8(2)
gives
  Fitt_{i,Z_p}(X_p) = p^{partial^(i)-partial^(infty)} Z_p
                     = p^{partial^(i)} Z_p.
Therefore among indices of the correct parity,
  partial^(i)=0 iff i>=d.
A coefficient is a p-unit in Z_p/I_n precisely when its
divisibility index is zero; hence the smallest auxiliary
degree of a unit coefficient is mu_p=d.

Finally the rank-two Mordell--Weil Kummer sequence gives
  0 -> (Q_p/Z_p)^2 -> S_p -> A_p -> 0.
Pontryagin duality splits this (Z_p^2 projective):
  X_p = Z_p^2 (+) A_p^vee.
Hence
  d=2+dim_Fp(A_p^vee/p A_p^vee)
   =2+dim_Fp A_p[p].
The finite-level Kummer sequence
  0 -> E(Q)/p -> Sel(Q,E[p]) -> Sha(E/Q)[p] -> 0
also shows its dimension is exactly d, without needing
a natural identification with S_p[p] at the local torsion
primes. This completes the proof.

**Scope warning.** This counts minimal auxiliary *unit*
coefficients modulo p, not the first coefficient that is
merely nonzero modulo a higher p-power. The latter, ord(delta)
and m2(p), distinguish an infinite p-primary Sha corank
from finite Sha with nonzero p-primary torsion. The equality
does not imply mu_p<=3 and thus does not prove global BSD.

## 2. Concrete anomalous-prime consequence beyond old local gate

For p in {859,1213,1493,1951}, a direct exact Legendre-sum
point count on E gives
  a_p(E)=1,  #E(F_p)=p.
These are good ordinary *anomalous* primes. Regardless of
whether local E(Q_p)[p] itself is nonzero, the above theorem
requires no local torsion hypothesis.

All four p are <48859 and are covered by Stein--Wuthrich
Theorem 12.3, which establishes Sha(E/Q)[p]=0 for the
listed good ordinary primes apart from p16231. Thus

  mu_859=mu_1213=mu_1493=mu_1951=2.

In particular, for each of these four p, there EXIST
p-admissible q1(p),q2(p) with a Neron-normalized unit
two-prime Kurihara number. The primes q_i are not
explicitly constructed by this nonconstructive deduction.

This genuinely removes the 'nonanomalous' restriction
of the 2026-11-14 branch's mu=mod-p-Selmer proof.
It is not a first proof of the existence of those
pairwise witnesses: the 2026-11-14 finite-range work
already derived existence using Kim 1.8/Fitting and
Stein--Wuthrich by another method.

## 3. Published finite-range boundary, and what is still needed

Stein--Wuthrich Thm 12.3 covers p=2 and all 5005
good ordinary primes p<48859 except p=16231.
Among p>=5 in the range, this is 5003 good ordinary
primes with proved Sha[p]=0. The already user-run
separate Sage proof-mode p=107 supersingular
p_primary_bound(107)=0 adds a single good prime.
Thus 5004 good p>=5 below48859 have mu_p=2,
in the sense above.

There remain 17 good primes in the range not covered
by this combination (16 supersingular, and 16231
ordinary), plus the bad prime 389 and the small p=2,3.
The 17 good ones are:
  599,1049,2957,6661,8263,9397,9551,14633,15101,
  16231,28591,30671,30869,31799,34781,36263,45161.
A separate archived p599 supersingular p-adic regulator
argument has a *normalization caveat*, so do not silently
move 599 into the fully proved list without resolving it.

**The finite count is NOT an all-large-p theorem.**
The two new explicit complete Kurihara certificates
at p=17,23 from 2026-11-21 are new EXPLICIT witnesses,
not first-ever proofs that those Sha components vanish:
they were already within the Stein--Wuthrich published
ordinary-prime range.

## 4. A rigorously sharpened one-bit problem for the uniform tail

For every good p>=5 the exact equality makes the following
equivalent:

(A) Sha(E/Q)[p^infty]=0.
(B) mu_p=2.
(C) dim_Fp Sel(Q,E[p])<=3.
(D) dim_Fp Sel(Q,E[p])=2.
(E) there is a unit two-factor Kurihara coefficient.

Indeed mu_p is always even, and finite. It is enough
to prove ANY of these for all but finitely many p to
obtain finite *prime support* of Sha (not necessarily
finite Sha at the remaining exceptional p). The p-rank
bound is therefore the identical mathematical obstacle,
not a strictly easier source of an a priori upper bound.

The actual missing new theorem must supply a *cohomological
bound independent of these equivalent conclusions*,
for example a genuinely constructed integral derived
Euler-system morphism or a fixed nonzero global
Fitting element. The existing finite Hecke Smith
determinant is NOT one: its natural arithmetic
comparison has not been constructed.

Separately, the exact complex L''(E,1)/2 BSD
leading-term formula remains a distinct proof
obligation even after controlling Sha.

## 5. No artificial p-uniform denominator claim

The proof applies to p<48859 and to all larger p
uniformly, but it is an equivalence. It does not
imply a bound on the auxiliary primes q_i(p), on
their sizes, on mu_p independent of p, or on
the existence of a fixed integer D annihilating
the p-primary Sha groups. In particular it does
not supply a global BSD proof.


## 6. New computational precision floor at the exceptional ordinary p=16231

The strict rank-two Fitting/Kurihara identity,
proved in the other 2026-11-21 note, says
  Fitt_2(X_p) = p^{m_2(p)} Z_p,
where m_2(p) is the least p-adic divisibility index
among **all** two-factor coefficients; m_2=+infinity
when every such coefficient vanishes in its finite
coefficient ring.

If Sha[p^infty] is finite nonzero then
  m_2(p) = v_p(#Sha[p^infty]) in {2,4,6,...}.
In particular, **if no two-factor p-unit exists**,
one can only certify finite but NONTRIVIAL Sha
using an authentic two-factor coefficient with
nonzero residue modulo p^3 or higher. A purported
p-adic valuation exactly one as the *minimum*
would contradict the square-order Cassels--Tate pairing.

The local coefficient of a pair n=q1*q2 lives in Z_p/I_n
with
  I_n = I_{q1}+I_{q2},
  I_q=(q-1, a_q-q-1) Z_p.
To even have a coefficient ring of length >=3, both
q_i must satisfy, for i=1,2,
  q_i == 1 mod p^3,
  a_{q_i} == q_i+1 mod p^3.

Therefore q_i >= p^3+1; the complete naive direct
two-prime modulus n=q1*q2 has the **rigorous**
size lower bound
  n >= (p^3+1)^2.

At p=16231, p^3=4,275,981,654,391 and
  n >= 18,284,019,108,696,945,332,889,664.

This bound concerns this **specific full auxiliary
coefficient modulo p^3 strategy**, NOT the complexity
of all Euler systems, optimized modular-symbol methods,
or the anticyclotomic Gross theta computation.
In particular, if one suspects a finite but nontrivial
Sha[16231^infty], direct exhaustive two-prime
mod-p^3 Kurihara enumeration is a poor method.

This arithmetic observation reinforces the choice of
the already-existing 87,809,710-point p16231
anticyclotomic Gross theta and the integral
Castella--Hsieh leading-order comparison as the
more plausible **prime-specific finiteness route**.
That proof route still needs a precise certification
of the actual global reciprocity/source normalization;
it is NOT settled by this complexity bound.

When a two-prime MOD-p UNIT exists, of course the
cheaper p-level computation already proves Sha[p^infty]=0,
and none of the p^3 lower bound is relevant.
