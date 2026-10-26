# 389a1, p=16231: Theorem A of Castella–Hsieh and the precise integral obstruction

**Date:** 2026-10-26. **Status:** a rigorous conditional application of an external published theorem to the previously audited, source-conditional p-primary Sha and Gross–Waldspurger evidence. It is NOT a new unconditional full BSD or uniform prime-support theorem.

## 1. Exact input and coefficient field

Let E: y²+y=x³+x²−2x (Cremona 389a1), N=389, p=16231, K=Q(sqrt(-3)), O=O53=Z+53 O_K and chi9 a character of Pic(O) of exact order 9. Choose psi=chi9^5. As complex conjugation acts on ring classes by inversion, psi/psi^tau=psi²=chi9^(10)=chi9. Define f=f_E, g=theta_psi, g*=theta_{psi^-1}. The finite-order eigenvalues alpha=psi(bar(p)) and beta=psi(p) lie in the p-adic coefficient field L=Q_p(zeta9), not necessarily Q_p.

**Important coefficient-field correction:** p=16231 is congruent 4 modulo 9. As ord_9(4)=3 and p is coprime to 9, L/Q_p is the unramified **cubic** extension (valuation ring O_L, uniformizer p). The generalized Kato classes are viewed in Sel(Q,V_p E) tensor_Qp L. Hence a claimed scalar relation between classes and Mordell–Weil generators must allow coefficients in L.

## 2. Verifying the published theorem's exact gates

Castella–Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum of Mathematics, Sigma 10 (2022), Theorem A (implication (1.10)), assumes:

1. E has good ordinary reduction at p>3, analytic root number +1 and L(E,1)=0. For 389a1: p=16231, a_p=128, N=389 and analytic rank exactly 2 by its previous certified modular-symbol/interior bound.
2. p splits in K, and psi has conductor coprime to p*N. Here p=1 mod3, p splits; conductor divides 53, coprime to 16231*389.
3. `L(E^(-3),1)*L(E/K,chi9,1) != 0`. The former has an explicit pure-rational cutoff-and-tail positivity proof in this project (`9/2 < L(E^(-3),1) < 23/5`); the latter is **conditional** on the genuine Gross-point/Brandt-automorphic period identification and faithful user-run Stage 14/22/23/29/30 data, using Waldspurger's implication from nonzero toric period.
4. `chi9(bar(p)) != 1`: direct exact F_53² cubic/ninth root test gave `(51−94omega)^312=((5+3omega)^312)^4`, a primitive ninth root, hence chi9 nontrivial on pbar.
5. residual E[p] irreducible; previous uniform surjectivity certificate at p=16231 supports it under its own recorded finite-input gates.
6. `N^-=389` is the squarefree product of exactly one inert bad prime, and E[p] ramifies there. Indeed v_389(Delta_min)=1 with Delta_min **+389**, so for p!=389 the mod-p Tate inertia is nontrivial because p does not divide 1.

**Sufficiency:** the paper's theorem is not just Theorem B's theta-series order-of-vanishing implication; its Theorem A has a converse that requires only two Selmer/localization conditions beyond these global hypotheses.

## 3. Deduction using the already existing conditional p-primary certificate

Under the previously recorded **computer-assisted conditional** theorem `Sha(E/Q)[p^infinity]=0`, the exact Selmer sequence over Q_p gives

`0 -> E(Q)⊗Q_p -> Sel(Q,V_pE) -> V_p(Sha(E/Q)) -> 0`.

Since rank E(Q)=2 and p-primary Sha is zero under this hypothesis, `dim_Qp Sel(Q,V_pE)=2`. Moreover a non-torsion rational point P remains non-torsion in E(Q_p). The p-adic elliptic formal logarithm has finite (torsion) kernel, so its image is nonzero in `E(Q_p)⊗Q_p`. Therefore the Selmer localization map is nonzero.

By Castella–Hsieh Theorem A, implication (1.10),

`kappa_(alpha,alpha^-1)(f,theta_psi,theta_(psi^-1)) != 0`

and similarly the beta branch. By their Remark 1.6 the two surviving classes span the **one-dimensional** line `ker(log_p)` inside the rank-two Selmer group after tensoring to L. The other two mixed alpha/beta classes vanish.

**This nonvanishing conclusion is CONDITIONAL** on both the previously computer-assisted p-primary Sha proof and the computer-assisted Gross/Waldspurger Rankin-L nonvanishing. In particular, Theorem A does not turn any assumed numerical value into an unconditional theorem automatically.

## 4. An explicit candidate generator of the Kato line

Let P,Q be a Z-basis of E(Q)/tors (the two rational generators supplied by the previous Sage basis stage). Put `lambda_P=log_E(P), lambda_Q=log_E(Q)` in Q_p. Since at p=16231 the good reduction count is `#E(F_p)=p+1-a_p=16104`, which is prime to p, multiplication by 16104 sends any local point to the formal group, proving `lambda_P,lambda_Q in p*Z_p`. They are not both zero.

Set `m=min(v_p(lambda_P),v_p(lambda_Q))`, which is a finite positive integer. The Mordell–Weil lattice vector

`R_p=(lambda_Q/p^m)*P - (lambda_P/p^m)*Q`

is **primitive** in `E(Q)⊗Z_p`, and spans the kernel of the local logarithm. Consequently there exists `c_p in L^×` with

`kappa_(alpha,alpha^-1)=c_p*R_p`

after rationalizing the lattice and choosing one coherent comparison of the generalized-Kato class with the Mordell–Weil space. **Theorem A proves `c_p != 0`; it provides no valuation or integrality theorem for `c_p`.** This is an exact concrete description of what is controlled by the nonvanishing theorem.

## 5. Crucial correction: mere integral Kato primitivity cannot eliminate finite Sha

Even strengthening `c_p!=0` to `c_p∈O_L^×` would **NOT automatically imply** `Sha(E/Q)[p]=0`: the rationalized Selmer group and even the integral inverse-limit Selmer module `Sel(Q,T_pE)` are insensitive to finite p-power Sha torsion.

Indeed, inverse limiting the p^n-Kummer sequences gives

`0 -> E(Q)⊗Z_p -> Sel(Q,T_pE) -> T_p(Sha(E/Q)[p^infinity]) -> 0`.

For a finite p-primary abelian group A, `T_p(A)=lim_n A[p^n]` under multiplication by p is zero. So, when Sha[p^infinity] is finite, `Sel(Q,T_pE)` can equal `E(Q)⊗Z_p` even if `Sha(E/Q)[p]` is nonzero. Primitivity inside this rank-two Z_p lattice, alone, does not detect those missing finite Sha classes.

The **correct additional theorem** needed for uniform prime support is an integral rank-two Euler/Kolyvagin-system **Fitting-ideal or Selmer presentation comparison** proving that a canonical derived class (or a fixed algebraic determinant of a compatible system) bounds the *finite* group `Sha[p^infinity]`. A standalone nonzero generalized-Kato class, or a primitive one-dimensional line in the rational Selmer group, supplies no such bound.

This is a sharper obstacle than previously advertised: it removes the unsound implication `integral primitiveness => Sha[p]=0` unless supplemented with a published or proved arithmetic control theorem. The already separate p=16231 Sage/Kato upper-bound argument is a different valid route, because it directly supplies a proved Sha upper exponent rather than just Selmer dimension.

## 6. Uniformity cannot follow from a fixed chi9

A single order-nine auxiliary ring-class character is nonregular at infinitely many splitting primes by Chebotarev, and its chosen coefficient field/p-stabilization varies with p. Thus the single p=16231 nonzero class does not create a global integer controlling all other primes.

## Definitive status

- Conditional generalised Kato nonvanishing for E at p=16231: **mathematical implication established** from Castella–Hsieh Theorem A and the project's previously recorded computer-assisted gates.
- Explicit rank-two local-logarithm Kato line: **algebraically established**, with nonzero scalar c_p of *unknown valuation*.
- Integral Fitting-ideal / higher-rank Euler-system comparison controlling finite Sha: **OPEN**.
- Uniform prime-support bound and full BSD: **OPEN**.

Primary reference: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864, Theorem A (1.9),(1.10), Remarks 1.5–1.6.

Project-specific Gröss/Waldspurger: [Genuine toric-orbit period bridge](389a1_chi53_waldspurger_gross_orbit_exact_identification_2026-10-26.md); [previous p-primary Sha conditional certificate](p16231_minimal_prime_primary_sha_certificate_2026-10-26.md).
