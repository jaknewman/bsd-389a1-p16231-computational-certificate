# 389a1: integral Selmer-complex descent criterion, Hecke-component orthogonality, and a Galois representation obstruction

**14 November 2026. Result status: three rigorous formal/geometric theorems.** This note directly attacks the demand for a single p-independent integer matrix controlling the unknown E389a1 Sha. It proves the exact necessary and sufficient algebraic criterion for a *uniform* finite-free integral complex and proves that two natural direct constructions cannot furnish the missing map. **It does not construct the arithmetic comparison map**, and proves neither all-large-p Sha vanishing nor strong BSD.

## 0. Exact geometric inputs

Let E/Q: y²+y=x³+x²−2x, conductor 389, Mordell–Weil group Z², discriminant +389, modular degree 40. The Atkin–Lehner minus Jacobian J^-=J_0(389)^− has dimension 21 and is Q-isogenous to E×A20. Stein (1999) proves L(A20,1)≠0 and hence rank A20(Q)=0. Classical Kolyvagin–Logachev gives finite Sha(A20/Q). Sources:
- https://wstein.org/Tables/389/389/node1.html ;
- https://www.lmfdb.org/EllipticCurve/Q/389a1/ .

Let α:J^-→E be the optimal quotient restriction, β:E→J^- its dual. Then αβ=[40], and the genuine, p-independent idempotent e=βα/40 lies in End(J^-)⊗Z[1/10]. For p≥7 it acts integrally on Tate modules, Selmer, and Sha. The complement B^-=ker(α)^0 is isogenous to A20, and E×B^-→J^- has degree dividing 1600. So, at any p≥7,

X_p(J^-)=X_p(E)⊕X_p(B^-)

up to canonical identification via the p-prime isogeny, where X_p(A)=Sel_{p∞}(A/Q)^∨; the e-summand is E and the (1−e)-summand B^-.

## 1. Theorem A — no e-compatible map from E-Sha into the complementary finite Sha

Let R be any commutative ring in which 40 is invertible, V an R-module with an idempotent e, and V_E=eV, V_B=(1−e)V.

**Proposition.** If f:V_E→V_B is R-linear and **intertwines the action of e**, then f=0. Indeed for every x∈V_E, f(x)=f(ex)=ef(x)=0 because e acts as 0 on V_B.

For E389a1 apply this to the corresponding Selmer and Sha summands for every p≥7. No Hecke/projector-compatible map from Sha(E)[p∞] to Sha(B^-)[p∞] can inject a NONZERO Sha(E) class. The finite rank-zero complement therefore supplies no prime-independent bound on E-Sha through a Hecke-equivariant cross-component embedding. This does NOT exclude a genuinely derived cohomological map to an *E-isotypic* finite module, or a correspondence that does not intertwine this projector.

For full Hecke equivariance: the E-factor idempotent is the central primitive idempotent in the semisimple rational Hecke algebra, and at primes away from the modular congruence number 40 it is integral. A Hecke-linear map therefore intertwines e at those primes. The elementary idempotent argument itself needs only e-compatibility, not any stronger assertion on arbitrary correspondences.

## 2. Theorem B — a fixed *trivial-Galois* modular-symbol lattice cannot receive E[p]

Let p≥5 be a prime such that ρ_{E,p}:G_Q→GL_2(F_p) is surjective. Let W be any F_p-vector space on which G_Q acts trivially (e.g. a **bare** integer 390-Manin-symbol coefficient lattice modulo p, given an artificially trivial Galois action).

Then

$$
\boxed{\operatorname{Hom}_{G_{\mathbf Q}}(E[p],W)=0.}
\tag{B}
$$

**Proof.** The image of ρ contains −I. If f:E[p]→W is Galois-equivariant and σ acts as −I on E[p], then for every v, f(−v)=σf(v)=f(v), but linearity gives f(−v)=−f(v). Since p is odd, 2f(v)=0 forces f=0.

Therefore the **naïve** identification of the integral Hecke-symbol lattice (which is topological, with no such natural Tate-module Galois action) with a direct quotient of E[p] is impossible. Actual regulator/Galois-cohomology maps might still connect the objects by much subtler mechanisms; Theorem B does not exclude those.

## 3. Theorem C — exact arithmetic equivalence of a fixed finite ℤ-complex comparison with finite Sha support

Fix a finite set of rational primes S. Put R=Z[S^{−1}] and for p∉S define
$$
X_p=\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee.
$$
We already know a saturated rank-two Mordell–Weil group, so Kummer/Pontryagin gives
$$
X_p\simeq \mathbf Z_p^2\oplus\Sha(E/\mathbf Q)[p^\infty]^\vee,
$$
without assuming Sha finite.

**Theorem C (an iff, but not a construction).** The following are equivalent:

(i) The prime-to-S direct sum \(\bigoplus_{p\notin S}\Sha(E/\mathbf Q)[p^\infty]\) is finite.

(ii) There exists a bounded complex \(C^\bullet\) of finite free R-modules and an index i such that **for every p∉S** an R-completed arithmetic isomorphism
$$
\boxed{H^i(C^\bullet)\otimes_R\mathbf Z_p\simeq X_p}
\tag{C1}
$$
holds (as Z_p-modules, without requiring canonical choice). It is enough to require the same for a single finitely generated R-module H instead of a perfect complex.

**Proof (ii⇒i).** The R-cohomology H=H^i(C) is finitely generated, since the complex consists of finite free R-modules. As R is a PID, H≅R^r⊕T with finite torsion T, whose prime divisors all lie outside S. Choose any p∉S for which the already-known Sha[p∞]=0, e.g. p=7 if p∉S, or choose an ordinary covered p outside the finite S by Stein–Wuthrich's finite range when possible; **more directly**, for any p∉S, the rank of H⊗Zp equals r, and the source X_p has rank \(2+\operatorname{corank}\Sha[p^\infty]\). To conclude r=2 without assuming a certified p outside S, add the natural requirement \(\operatorname{rank}_R H=2\), which is the rank-two version of (ii). Under this requirement, comparing torsion gives \(\Sha[p^\infty]^\vee\simeq T\otimes\mathbf Z_p\). Hence every p∉S outside the finitely many primes dividing #T has Sha[p∞]=0, and all remaining p-parts are finite. Their direct sum is finite; indeed its exact order equals #T.

**Proof (i⇒ii).** If the prime-to-S Sha group is finite, put \(T=\bigoplus_{p\notin S}\Sha(E/\mathbf Q)[p^\infty]^\vee\) as a finite R-module. Take H=R²⊕T. A finite presentation of T over the PID R resolves H by a bounded complex of finite free R-modules with H^i(C)=H; completing at every p∉S gives \(H\otimes_R\mathbf Z_p\simeq X_p\). The isomorphisms are abstract, not canonical or arithmetic constructions; this proof uses the desired finiteness as input. QED.

Thus the correct exact formulation of (ii) is:
**there exists a finite free R-complex C with rank_R H^i(C)=2 and comparison (C1) for all p∉S**.

**Consequences if an independent C and these comparisons were ever actually constructed:**
- Smith normal form of an R-presentation of H yields a fixed finite torsion module T; its order D=#T is a **single p-independent** annihilator of all Sha[p∞] for p∉S.
- The genuine arithmetic comparison (C1), not the algebraic existence of some perfect C or the Smith calculation alone, is precisely the missing step.
- At primes in S, independent finiteness proofs are still required for global Sha finiteness.
- The exact complex L''(E,1)/2 leading-term BSD identity is independent and remains unproved.

**Important logic:** (ii) is fully equivalent to the finiteness goal *if* one is free to choose C abstractly. Merely **postulating** an unspecified finite free C satisfying (C1) is circular. Actual progress would demand **constructing C independently from a specific modular/Euler/motivic arithmetic object**, then building the comparison (C1) unconditionally. For this E, the 390 integral modular symbols and the Hecke Smith constant2 give a finite module H of the right abstract rank but lack the arithmetic comparison, and the Theorem B direct Galois map would be zero.

## 4. A sharp infinite prime-support countermodel

For each p≥7 set the *synthetic* modules
$$
X_p^{\rm toy}=\mathbf Z_p^2\oplus(\mathbf Z/p)^2,\qquad
Y_p^{\rm toy}=0.
$$
Let e_p act as identity on X_p^toy and zero on Y_p^toy. It is an integral idempotent at every p; E-compatible maps to Y vanish identically. Each X_p is finitely presented, its torsion is finite and has a perfect alternating pairing, and the free MW wedge is primitive. Yet the direct sum of the toy p-torsion over all p≥7 is infinite and no nonzero integer kills it. Thus **global projectors and all-prime local presentations do not imply the cross-p rational descent (C1)**.

This model is not an actual Sha(E389a1) construction. The companion Python script verifies all matrix identities on finite samples p5,7,11,107,16231 and gives the elementary general proof of the infinite-prime obstruction.

## 5. The scientifically viable remaining construction

The desired object is a Selmer-complex **motivic** determinant with a comparison arising from a *global Euler/Kato zeta element* and a **proved p-independent rational/integral normalization**, not an ordinary matrix of fixed Hecke eigenvalues. Castella–Sano 2026 §2.2 establish determinant versions of the Iwasawa Main Conjecture prime by prime; Burns–Sakamoto–Sano's general higher Kolyvagin derivatives supply machinery for cohomological derivatives, not the required fixed E389a1 **global** integral comparison.

Sources:
- https://arxiv.org/html/2601.14504 , §2.2;
- https://kclpure.kcl.ac.uk/portal/en/publications/on-the-theory-of-higher-rank-euler-kolyvagin-and-stark-systems-ii/ ;
- https://wstein.org/Tables/389/389/node1.html ;
- project prior no-go on global Fitting intersection and rank-two cyclotomic Bockstein: paper/bsd389_global_diagonal_Fitt_intersection_exact_criterion_2026-11-01.md, research-branch paper/bsd389_GLOBAL_exact_Bockstein_leading_coefficient_adeliac_gluing_obstruction_2026-11-09.md .

**Verdict:** an explicit unconditional **no-go** for complement-transfer and bare-Galois-trivial Hecke comparison, plus an exact iff for the *genuine* uniform perfect-complex specialization needed. No nonzero global annihilator, all-large-p μ≤3 bound, Sha finiteness or complete BSD is claimed.
