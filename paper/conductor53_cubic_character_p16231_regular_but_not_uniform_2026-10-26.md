# Conducteur 53 : regularite cubique exacte a p=16231, et obstacle a l'uniformite

Date: 2026-10-26. Type: **new elementary theoretical lemma with exact finite-field computation**, not a full Sha/BSD theorem and not a certification of the central Rankin L-values.

## Fixed data

Let `K=Q(sqrt(-3))`, `omega=(-1+sqrt(-3))/2`, with `omega^2+omega+1=0`; set f=53. The prime 53 is inert in K because 53=2 mod 3. The ring class number is

`h(O_53)=53*(1+1/53)/[O_K^*:O_53^*]=54/3=18`;

its class group is cyclic C18, as independently computed in the existing conductor53 quaternionic pipeline. Let psi be a cubic ring-class character, psi^tau=psi^-1. Then `chi=psi/psi^tau=psi^2` is also cubic and nontrivial.

## Explicit finite-field cubic character

Take `F=(O_K/(53))=F_53[omega]` of order 53². The quotient by scalar units from `F_53^*` and the image of the global `O_K^*` has order 18. The homomorphism

`C(u)=u^((53^2-1)/3)=u^936 in mu_3(F)`

kills scalar units because 52 divides 936, and kills the global units because 6 divides 936. Hence it descends to a cubic character of `Pic(O_53)`. Since `C(5+3omega)=omega != 1`, this is a nontrivial cubic character (up to conjugating the primitive cubic root of unity).

Now 16231 is prime and `16231=51²-51*(-94)+(-94)²`, so the algebraic integer `lambda=51-94omega` has norm 16231, giving one of the two primes above 16231 in K; 16231=1 mod 3 and thus splits. Direct exponentiation in the finite field shows

`C(lambda)=(51-94omega)^936=omega != 1`.

Therefore the associated cubic class character is nontrivial at both primes above 16231 (their values are opposite primitive cube roots), and

`chi(bar(p_16231)) != 1`.

This proves **the exact p-regularity gate** for the cubic auxiliary theta form in Castella–Hsieh Theorem A, without appealing to the incomplete quaternionic toric-period pipeline. It does **not** prove nonvanishing of `L(E^(-3),1)` or `L(E/K,chi,1)`; those remain separate analytic gates. Nor does the character nontriviality construct the generalized Kato class or prove its integrality.

## A negative uniformity theorem for a fixed cubic character

Let H_53/K be the ring-class field; `Gal(H_53/K)=C18`. The cubic character chi has kernel of size 6. By Chebotarev, among prime ideals of K with degree one away from its ramified finite set, **one third** have Frobenius in the kernel. Equivalently, among rational primes splitting in K, conditional density 1/3 have `chi(bar(p))=1`, and conditional density 2/3 are regular for this fixed chi (apart from finitely many ramified primes).

Since rational primes split in K with density 1/2, the splitting-and-cubic-regularity conditions hold for density 1/3 of all rational primes, and fail on an infinite set of split primes. This is a statement about the auxiliary character, **not** the additional good-ordinary condition on E and not about Sha.

**Corollary:** The fixed pair `(K=-3, conductor f=53, cubic chi)` cannot satisfy the `chi(bar p)!=1` auxiliary regularity hypothesis for every prime p. Therefore it cannot, by itself, furnish a uniform all-p application of the Castella–Hsieh theorem. Varying the character, order or quadratic field is mathematically necessary to obtain unrestricted coverage. Even a finite collection of nontrivial characters of the same Pic(O_53) leaves the split primes whose class is identity untreated; inert primes in K are outside this construction.

## A second, deeper obstruction: rational nonvanishing vs integral Sha

Castella–Hsieh (Forum of Mathematics Sigma 10, 2022, e12), Theorem A, gives (under its global central-L, residual ramification, inert-level and p-regularity hypotheses) `kappa_p != 0 => dim_Qp Sel(Q,V_pE)=2`. This only eliminates the Qp-corank of Sha[p^infinity], not its finite p-primary torsion. Any *uniform prime-support* theorem requires a compatible **integral** class/primitivity statement controlling Sel_p over Fp, not merely existence of nonzero kappa_p over Qp.

Their Theorem B uses the **anticyclotomic p-adic theta element** `Theta_(f/K)` at the trivial character. This is not the same as the finite conductor53 toric period or its cubic chi component. Their explicit finite-level formula involves ideals `P_n^a` and `P_{n+1}^a` for p-power ray/ring-class levels and the condition `ord_T Theta_(f/K)=2`. Thus a nonzero conductor53 Gross toric period could certify a **complex Rankin central value** after correct Waldspurger normalization, but does NOT by itself establish Theorem B's `ord_T Theta=2`. Treat these as different mathematical gates.

## Positive published comparison on the very same curve

The 2021 lecture slides by Francesc Castella, *Kato classes*, explicitly use E=389a1 with the different auxiliary field `K=Q(sqrt(-2))` and p=11, and record a finite anticyclotomic theta computation `Theta_p(T)=-T²+58T³+... mod (p²,T^p)` yielding a generalized Kato nonvanishing example. This demonstrates an existing concrete rank-two construction for this exact E; it does not automatically propagate to p=16231 or uniform p. **Indeed K=Q(sqrt(-2)) is unsuitable at p=16231 for this theorem's split-prime branch**: 16231 is 7 mod 8, hence the Kronecker symbol (-2/16231)=-1, so 16231 is inert in Q(sqrt(-2)). In contrast, 16231 is 1 mod 3 and splits in K=Q(sqrt(-3)).

## Remaining mathematically decisive targets

- (A) Prove both `L(E^(-3),1) != 0` and `L(E/K,chi,1) != 0` for the conductor53 cubic chi, with correct quaternionic class transport/Waldspurger identity.
- (B) If aiming for an independently new p16231 Kato-class nonvanishing argument, prove `ord_T Theta_(f/K)=2` from the **anticyclotomic p-power theta family**, not merely from the fixed conductor53 cubic period.
- (C) If aiming for uniform triviality of Sha across all p, establish an **integral** rank-two Euler-system/Fitting-ideal comparison independent of the varying prime; even (A)+(B) at one prime is insufficient.

## Sources

- [Castella–Hsieh, Theorem A, Theorem B and Appendix, 2022](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864)
- [Castella, slides *Kato classes* containing original 389a1, K=-2, p=11 example](https://www.cmat.edu.uy/~tornaria/LATeN/2021/LATeN-2021_04_22-Castella.pdf)
- [Earlier project uniform Selmer support reduction](389a1_uniform_sha_support_rank2_selmer_kato_ringclass53_2026-10-26.md).


## A shorter conditional route to generalized Kato nonvanishing at p=16231

There is an additional strategic simplification for this **specific** p=16231. Under the previously produced computer-assisted p-primary Sha certificate, `Sha(E/Q)[16231^infinity]=0`, hence `dim_Qp Sel(Q,V_p E)=rank(E(Q))=2`. Since the rank is positive, the global Mordell–Weil localization is nonzero (Castella–Hsieh Remark 1.5); therefore the localization hypothesis for the **converse** direction (Theorem A, implication (1.10)) is satisfied.

All auxiliary local hypotheses for the fixed conductor53 theta form can be documented: `p>3` good ordinary with a_p=128, p splits in K, E[p] irreducible/surjective, `N^-=389` squarefree of odd cardinality, E[p] ramified at 389 since v_389(Delta)=1, and the cubic p-regularity proved above. Thus the only **additional complex analytic gate** needed for this theorem is

`L(E^(-3),1) * L(E/K,chi,1) != 0`.

**Conditional corollary.** If this product is proved nonzero and the already-audited computer-assisted p-primary Sha certificate is mathematically faithful, then **the converse implication of Castella–Hsieh Theorem A** directly gives `kappa_(alpha,alpha^-1)(f,theta_psi,theta_psi^-1) != 0` (and its beta analogue) at p=16231. In that direction one does **not** need a new computation of `ord_T Theta_(f/K)=2`; that theta test is an independent analytic path supplied by their Theorem B, useful if the Sha calculation cannot be imported.

This is a new **conditional deduction**, not an unconditional new class: the central L-product has not been certified, and the current p16231 Sha conclusion retains its documented source-precision assumptions. Moreover even this class nonvanishing controls only the Qp-Selmer rank in the forward implication, and does not imply a uniform integral mod-ell Sha primitivity theorem.

Reference: Castella–Hsieh Theorem A (1.9),(1.10) and Remark 1.5, https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864
