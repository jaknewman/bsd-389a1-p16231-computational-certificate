# Beyond the bounded prime search: uniform support via integral rank-two Selmer control

Date: 2026-10-26. **Pure theoretical reduction, not a numerical PASS, not a proof of finite Sha or full BSD.** The goal is to replace endlessly increasing ordinary-prime bounds with a proof that Sha(E/Q)[ell]=0 for all ell outside an explicitly finite exceptional set.

## 1. Exact rank-2 Selmer criterion

Let E=389a1: y²+y=x³+x²-2x, rank E(Q)=2, E(Q)_tors=0. For every prime ell the exact Kummer sequence is

`0 -> E(Q)/ell E(Q) -> Sel_ell(E/Q) -> Sha(E/Q)[ell] -> 0`.

Thus `dim_Fell Sel_ell(E/Q) = 2 + dim_Fell Sha(E/Q)[ell]` and

`Sha(E/Q)[ell^infinity]=0 iff dim_Fell Sel_ell(E/Q)=2`.

The equivalence holds because a nontrivial ell-primary torsion abelian group contains an element of order ell. It requires no BSD conjecture or p-adic normalization.

For the rational p-adic representation V_ell E, the exact analogue is

`0 -> E(Q) tensor Q_ell -> Sel(Q,V_ell E) -> V_ell Sha(E/Q) -> 0`.

Consequently `dim_Qell Sel(Q,V_ell E)=2` eliminates the Q_ell-corank/divisible part of Sha[ell^infinity] and establishes its finiteness (standard finite-cotype property). **It does not prove that the finite ell-primary group is zero**. An integral, mod-ell *primitivity* condition is additionally necessary. This separates the two heights of the remaining theorem.

## 2. A genuine uniform finite-determinant criterion (conditional)

Suppose one can construct **one** fixed integer matrix `A in Mat_{m x n}(Z)` of rational rank `n-2`, and an integer `D0 != 0`, such that for every prime ell not dividing D0 there is a proved isomorphism `Sel_ell(E/Q) ~= ker(A mod ell)` identifying the two Mordell-Weil dimensions. Let `Delta !=0` be the gcd of all `(n-2)x(n-2)` minors of A (or 1 if n=2). Then

`ell not dividing D0*Delta -> rank_Fell(A mod ell)=n-2 -> dim Sel_ell(E/Q)=2 -> Sha(E/Q)[ell^infinity]=0`.

Proof: Smith normal form, or reduction modulo ell of any maximal minor nonzero modulo ell; maximal rational rank prevents larger reduction rank. This argument is exact and unconditional **given the uniform presentation**.

**This is not a claim that such a fixed A already exists.** Its existence with the stated Selmer comparison is the deepest missing theorem. Our existing 390x2012 Manin/Shapiro matrix controls modular-symbol transport at a single prime p=16231; it is NOT a uniform presentation of Selmer groups. Rebranding it as one would be a mathematical error. A finite determinant by itself does not bound Sha without an arithmetic comparison theorem.

### Essential correction on integral primitiveness (2026-10-26)

A rational rank-two generalized Kato nonvanishing theorem—and even **a primitive class in the compact integral Selmer lattice**—does **not** imply that finite Sha[p] vanishes. When Sha[p^infinity] is finite, its p-adic Tate module is zero, so the inverse-limit `Sel(Q,T_pE)` can coincide with `E(Q)⊗Z_p` even with nonzero finite Sha[p]. A global integral Euler/Kolyvagin-system **bound of the finite Sha group**, e.g. via its Fitting ideal or a genuinely uniform mod-p Selmer presentation, is an **independent necessary ingredient**. The fixed-matrix Smith-criterion above remains valid *if its very strong Selmer comparison hypothesis is established*; a Kato class alone is not such a comparison.

See [Castella–Hsieh p16231 implication and precise obstruction](389a1_p16231_generalised_kato_theoremA_and_integral_shasupport_gap_2026-10-26.md).

## 3. Existing higher-rank work relevant to constructing an arithmetic comparison

Castella–Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum of Mathematics Sigma 10 (2022), e12, Theorems A and B, constructs generalized Kato classes from a triple product involving a CM theta series g. Under explicit auxiliary central-L nonvanishing, residual irreducibility/ramification, inert level and p-regularity hypotheses, the nonvanishing of a generalized Kato class implies

`dim_Qp Sel(Q,V_p E)=2`.

Theorem B gives a possible route: an order-2 zero of a relevant anticyclotomic theta element yields nonvanishing. This is a path to **p-primary finiteness**, not by itself to vanishing; the full integral Sel_p class remains to be controlled. Its hypotheses and order-two theta statement vary with p. There is currently no proved global, single-integer prime-support bound obtained from these theorems for this E.

More generally Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, Journal of the Mathematical Society of Japan 76 (2024), concerns higher-rank derivatives and derived Euler-system relations. Its higher-rank constructions motivate an integral exterior-bidual/Fitting-ideal approach, but do not supply the fixed integer D0*Delta posited above in this example.

## 4. The existing ring-class conductor-53 program naturally feeds this approach

A candidate auxiliary field is K=Q(sqrt(-3)) with omega=(-1+sqrt(-3))/2, satisfying omega²+omega+1=0. The conductor f=53 is inert in K, and the ring-class number formula gives

`h(O_53) = 53*(1+1/53)/[O_K^*:O_53^*] = 54/3 = 18`.

Also `389 = 2 mod 3`, so the only bad prime 389 of E is inert in K, giving `N_f^-=389` (one prime); the conductor 389 is coprime to `3*53²`. The expression `5+3omega` has norm `25-15+9=19`, matching the norm-19 ideal generator in the existing conductor-53 quaternionic calculations. These are algebraic compatibility checks, **not** proof that the previously named χ equals the precise character `psi/psi^tau` in Castella–Hsieh.

An auxiliary weight-one CM theta series `g=theta_psi` from a ring-class character psi of conductor 53 has level dividing `3*53²=8427`, which is coprime to N=389. The crucial complex gate is **not yet proved for these choices**:

`L(E^{(-3)},1) * L(E/K,chi,1) != 0`, with `chi = psi/psi^tau`.

One must also establish the required splitting/regularity of the chosen p and CM theta series; a single fixed psi does **not** automatically cover all primes p. Even if the complex gate is checked and an individual κ_p is nonzero, the proof still needs **integral primitivity modulo p**, uniform enough to remove all but finitely many primes.

Thus the previously OPEN quaternionic gross-class toric-period calculation is mathematically relevant to this theory, not an unrelated exploratory stage. But toric-period nonvanishing alone cannot prove Sha(E/Q)=0 or yield a uniform support integer.

## 5. Priority: one precise missing theorem, not more 16231 checkpoints

Find a *compatible integral rank-two Euler/Kato system with a fixed nonzero rational/algebraic index* whose reduction controls mod-ell Selmer groups for all but a finite set of ell, or an equivalent uniform Fitting-ideal bound. Demonstrate both (i) rational Selmer corank 2 and (ii) integral primitivity. A proof would reduce Sha support to the divisors of a fixed integer and finitely many exceptional primes. No such theorem is deduced in this note.

Current literature check: Banwait, arXiv:2609.08431 (2026-09-08), proves a related cyclotomic unit criterion for **CM elliptic curves of rank two**, with explicitly separate assumptions; our non-CM curve 389a1 is not among those covered. The preprint notes how difficult even an infinitely-many-primes assertion is in rank two. It cannot be imported to E=389a1 wholesale.

Primary research sources:

- https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864
- https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_article/-char/en
- https://arxiv.org/abs/2609.08431
- https://wstein.org/papers/mcom2649-iwasawa-alg.pdf
- [Bounded historic Stein–Wuthrich prime-range corollary, only conditional for p=16231](389a1_stein_wuthrich_2012_exception_16231_conditional_closure_2026-10-26.md).

**Status: THEORETICAL CONDITIONAL REDUCTION, not a new global vanishing theorem.**
