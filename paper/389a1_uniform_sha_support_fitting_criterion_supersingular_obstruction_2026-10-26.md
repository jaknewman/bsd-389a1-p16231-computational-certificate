# Uniform prime support for Sha(389a1): a precise Fitting ideal theorem and two no-go results

**Date:** 2026-10-26. **Status:** two unconditional algebraic propositions and a rigorous correction to the global strategy; **NO** new proof of uniform Sha vanishing, finite Sha or all-prime BSD.

## 1. An exact uniform Fitting criterion, stronger than the fixed-matrix presentation hypothesis

Write E: y²+y=x³+x²−2x over Q, and for each rational prime ell put

`X_ell = Hom_cont(Sha(E/Q)[ell^infinity], Q_ell/Z_ell)`.

This compact Pontryagin dual is a finitely generated Z_ell-module because the elliptic-curve ell-power Selmer group has finite ell-Selmer quotient and finite corank. Let `Fitt_0(X_ell)` denote its zeroth Fitting ideal in `Z_ell`.

**Uniform-support theorem (conditional premise, unconditional implication).** Suppose there exist a nonzero integer `D_E` and a finite set S of rational primes such that

`D_E ∈ Fitt_{0,Z_ell}(X_ell)` for **every** ell outside S.

Then

`Sha(E/Q)[ell^infinity]=0` for every ell outside S with `ell ∤ D_E`.

**Proof.** For ell not dividing D_E, the image of D_E in Z_ell is a unit. Since `D_E` belongs to the zeroth Fitting ideal, that ideal equals all of Z_ell. For a finitely generated module M over a local ring, `Fitt_0(M)=R` if and only if `M=0` (derive from a presentation matrix: a unit maximal minor implies all generators vanish; equivalently use Nakayama). Therefore X_ell=0, and hence the dual torsion group Sha[ell^infinity]=0. QED.

**Strength:** This does NOT require that the sizes of the varying p-Selmer presentations or their matrices are uniform in ell, and does NOT assume beforehand that Sha[ell^infinity] is finite. For a finite p-primary Sha group X_p of length e_p, `Fitt_0(X_p)=(p^e_p)`; therefore `D_E∈Fitt_0(X_p)` is the exact concrete uniform exponent bound `e_p≤v_p(D_E)`.

**What is missing:** No theorem in the currently verified source and project evidence produces such a single D_E or proves the Fitting containment for every ell. Taking D_E=1 would *already* amount to proving Sha is zero for every prime outside S, so it cannot be inferred merely from the conjectural complex BSD order 1.

## 2. Exact self-dual toy Selmer complex: rational derivatives are blind to finite Sha

Let R=Z_p and, for each integer k≥0, take the perfect two-term complex

`C_k: R^4 -> R^2`, with differential `d_k(x1,x2,x3,x4)=(p^k*x3,p^k*x4)`.

Then, for **every** k:

`H^0(C_k)=R*e1⊕R*e2` (rank 2, same primitive exterior generator `e1∧e2`) and

`H^1(C_k)=(R/p^k R)^2` (the convention for k=0 gives 0).

Over Q_p all complexes C_k are quasi-isomorphic to the same two-dimensional rational vector space concentrated in degree zero, and their rational derived leading term can be nonzero on the same primitive rank-two line. Nevertheless the finite defect groups have sizes `p^(2k)` and zeroth Fitting ideal

`Fitt_0(H^1(C_k))=(p^(2k))`.

Reducing the differential modulo p gives a rank 2 kernel for k=0, but a rank 4 kernel for every k≥1, which exactly models the parity gap `dim Sel_p=2` versus `>=4` for an odd-p self-dual elliptic curve.

**No-go theorem:** Nonvanishing of a rationalized second-derived Euler/Kato class, and even primitivity of a rank-two generator of compact integral Selmer, can be identical in these examples while finite p-Sha varies arbitrarily. It therefore cannot entail an inequality `dim Sel_p<=3` without an additional theorem controlling the integral *cokernel/Fitting ideal*.

## 3. Supersingular primes are an infinite missing branch, not finitely many exceptional primes

For the specific E, the standard c4 invariant is 112 and the minimal discriminant is +389, so

`j(E)=112^3/389=1404928/389`,

which is not an algebraic integer, hence E is non-CM. More generally, Elkies's 1987 theorem states **every** elliptic curve over Q has infinitely many supersingular primes, so in particular E=389a1 has infinitely many good supersingular primes.

Consequently a hypothetical theorem `Sha[ell^infinity]=0 for all sufficiently large good-ordinary ell` leaves infinitely many supersingular ell untreated. This corrects any impression that proving ordinary vanishing leaves merely finitely many exceptional primes globally. Even a uniform ordinary criterion from Kato or Skinner–Urban must be supplemented with a supersingular/control-of-signed-Selmer criterion, or replaced by the all-ell Fitting target of Section 1.

Elkies's original: *The existence of infinitely many supersingular primes for every elliptic curve over Q*, Invent. Math. 89 (1987), 561–568. Confirmed on author's bibliography: https://people.math.harvard.edu/~elkies/math_pubs.html

## 4. Precisely how this interfaces with Burns–Kurihara–Sano (2024)

Burns, Kurihara and Sano, *On derivatives of Kato's Euler system for elliptic curves* (J. Math. Soc. Japan 76 (2024) 855–919), prove an **order-of-vanishing** divisibility for derived zeta elements in arbitrary analytic rank under hypotheses. Their *Generalized Perrin–Riou Conjecture* predicts the exact integral **leading-term** congruence in rank ≥2. They also establish a connection to the p-part of classical BSD via Iwasawa main conjectures.

The distinction matters: the proved vanishing-order statement means a derivative enters a filtration of a predicted order; it does **not** prove that the normalized top nonzero coefficient is a *unit*, or that it bounds `Fitt_0(X_ell)` uniformly across primes. An integral leading-term and finite-dual-Selmer/Fitting comparison theorem would still be required. The toy complex of Section 2 shows logically why this distinction cannot be ignored.

Publication: https://doi.org/10.2969/jmsj/90699069

## 5. Consolidated actual target and proof boundary

**Target:** Derive a single nonzero integer `D_E` and an all-ell outside finite S source-backed integral comparison `D_E∈Fitt_0(X_ell)` using derived Kato/Euler-system determinants, or prove an equivalent all-ell upper bound. This would establish global finiteness outside S immediately, including infinitely many supersingular primes. Nothing in the existing exact Manin/Shapiro p=16231 data, conductor53 Gross period, published finite-range Stein–Wuthrich theorem, or current BKS order-of-vanishing theorem constructs that integer.

The p=16231 prime-primary Sha result remains a separately claimed **conditional computer-assisted** computation based on a bona fide p-primary Kato/Iwasawa upper-bound theorem; it does not depend on the false implication that rational Kato primitivity controls finite Sha.

**STATUS: UNIFORM FITTING CRITERION PROVED AS A LOGICAL LEMMA; ARITHMETIC PREMISE OPEN.**

## Addendum: complete odd-prime parity despite infinite supersingular set

Although the infinite supersingular set blocks an ordinary-only proof, **parity itself applies to all odd primes**. Dokchitser–Dokchitser, Annals of Mathematics 172 (2010), prove the p-parity conjecture over Q for all p. Combining the even p^infinity-Selmer corank of 389a1 (root number +1) with the finite alternating Cassels–Tate pairing yields `dim_Fp Sel_p(E/Q)∈{2,4,6,...}` for *every odd p*, including supersingular p and bad p=389. Therefore a hypothetical **reduction-independent uniform** Selmer bound `dim Sel_p≤3` for all sufficiently large odd p would settle all sufficiently large prime-primary Sha groups. The parity theorem is complete; this **upper bound remains open**. See [all odd-prime parity theorem addendum](389a1_uniform_sha_parity_core_rank_one_correct_target_2026-10-26.md).
