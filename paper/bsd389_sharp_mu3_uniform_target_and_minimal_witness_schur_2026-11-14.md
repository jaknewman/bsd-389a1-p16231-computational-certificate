# E389a1: the sharp uniform degree bound is μ_p≤3, and minimal-witness Schur coordinates identify every Sha[p] direction

**Date:** 2026-11-14.
**Proof status:** algebraic consequences of the *published* results of Kim and Castella–Sano; finite-field Schur sanity model executed in pure Python. **Not** an unconditional all-prime bound, proof of global Sha finiteness, or complex BSD identity.

## 1. The sharp uniform target

E=389a1: y²+y=x³+x²−2x, MW group Z², conductor 389, root number +1, optimal Manin constant 1 and Tamagawa product 1.

For every good prime p≥5 with residual image GL2(Fp), define μ_p to be the smallest number of auxiliary prime factors among **mod-p unit** Kurihara numbers (not among finite-level coefficients merely nonzero modulo higher p-powers). Castella–Sano Theorem B guarantees that the collection of units is nonempty at *some* auxiliary degree. The Mazur–Tate functional-equation parity gives μ_p even; Kim Theorem 1.8 and the rational rank 2 exclude degrees 0 and 1. Thus

$$
\mu_p\in\{2,4,6,\ldots\}.
\tag{1}
$$

**Theorem 1 — a hypothetical strict upper bound of 4 suffices.** If there is an integer B such that

$$
\mu_p\le3\quad\text{for every prime }p>B,\ p\ne389,
\tag{2}
$$

then for each such p,

$$
\boxed{\mu_p=2,\qquad \Sha(E/\mathbf Q)[p^\infty]=0.}
\tag{3}
$$

**Proof:** (1) and (2) give μ_p=2. A mod-p unit two-factor coefficient gives Selmer corank exactly 2 by Kim 1.8, and the finite quotient has zero length by Kim 1.8 together with Castella–Sano B (indeed the unit itself forces ∂^(2)=∂^(∞)=0). Kummer with MW rank2 implies Sha[p∞]=0. QED.

The implication does **not** require E(Q_p)[p]=0, because we apply Kim **Theorem 1.8** rather than the semilocal **Theorem 1.10**. Thus anomalous primes are not silently omitted in the target (2). The finite exceptional set p≤B and the bad p=389 still require individual finiteness/vanishing certificates before one can conclude full global Sha finiteness.

**Sharpness:** A bound μ_p≤4 would imply at most dim_Fp Sha[p]≤2 at non-anomalous primes with Kim 1.10, but it would *not* imply Sha[p]=0. A hypothetical family of finite paired groups Sha[p∞]≅(Z/p)^2 for infinitely many p would have μ_p=4 at those p, respect Cassels–Tate parity and yield globally infinite support. This is a formal consistency example, **not** a statement that such a family occurs for 389a1. Thus among integer upper bounds on μ, **3 is the largest universally decisive threshold** via the parity gap.

Primary literature:
- Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, Theorems 1.8 and 1.10, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf .
- Castella–Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem B, https://arxiv.org/html/2601.14504 .

**Important limitation:** Showing (2) remains equivalent, within this Kurihara route, to the all-large-p vanishing we want. This note does not manufacture (2) from Hecke Smith data or local Chebotarev information.

## 1 bis. NEW 2026 theorem sharpening: an ODD first-nonzero-degree dichotomy for Kato's genuine Kolyvagin CLASSES and a TWO-auxiliary finiteness certificate

**2026-11-15 (actual theorem, not a synthetic model).** This is a rigorously deduced arithmetic corollary of the **published** Burungale–Castella–Grossi–Skinner, *Non-vanishing of Kolyvagin systems and Iwasawa theory*, Cambridge J. Math. 14 (2026), no.2, Corollary C and Theorem C, together with Dokchitser p-parity and the genuine rank-two MW group of E389a1.

Primary 2026 source: https://arxiv.org/pdf/2312.09301 (revision v2 dated 2026-01-18), **PDF p.4, Theorem C and Corollary C**. The authors' **Kato Kolyvagin class** κ_n^Kato∈H¹(Q,T_pE/I_n T_pE) is **not** the scalar Kurihara number δ_n and is **not** the unit witness μ_p of §1. The two notions must NEVER be interchanged.

Let p≥5 be a prime of good **ORDINARY** reduction, p≠389, with E(Qp)[p]=0, and assume E[p] is irreducible (in particular all surjective residual GL2 primes). No assumption of finite Sha. Burungale et al. Theorem C applies **unconditionally** in the irreducible case (by the "in particular" clause of that theorem), and their Corollary C gives

    d_Kato(p) := min{ν(n) : κ_n^Kato != 0} = corank_Zp H¹_str(Q,E[p∞]).

Here ν(n) counts DISTINCT auxiliary prime factors and n=1 (ν=0) is allowed in the definition. The system is not everywhere zero by Theorem C, so d_Kato(p) is finite.

Define s_p=corank_Zp Sha(E/Q)[p∞]. The standard exact p∞ Kummer sequence reads

    0 → E(Q)⊗Qp/Zp → Sel_{p∞}(E/Q) → Sha(E/Q)[p∞] → 0,

where the first term is (Qp/Zp)^2 (saturated proven MW rank2). At good p, the finite local Kummer target is E(Qp)⊗Qp/Zp ≅ Qp/Zp, and the localization of MW to it is ONTO: a non-torsion rational P maps to a nonzero p-adic logarithm and hence induces multiplication by a nonzero element a∈Zp on Qp/Zp, which is surjective even when v_p(a)>0. This does NOT require that the mod-p MW localization be primitive. Lifting any class of Sha through Sel_{p∞}, one can use a global MW class to kill its p-local Kummer image. Thus one obtains the exact strict localization Kummer sequence

    0 → ker[(Qp/Zp)^2→Qp/Zp] → H¹_str(Q,E[p∞])
      → Sha(E/Q)[p∞] → 0,

up to possible finite changes of local conditions at the bad place 389, which have NO effect on Zp coranks (and for p not dividing 388 the ℓ=389 finite local cohomology gate vanishes altogether). As the source of the local map has corank2 and its image has corank1, the kernel has corank1. Hence

    **corank H¹_str(Q,E[p∞]) = 1+s_p.**

Combining with BCGS Corollary C:

    **d_Kato(p) = 1+s_p.**

By the p-parity theorem, since E has global sign +1 and MW rank2,
    corank_Zp Sel_{p∞}(E/Q) = 2+s_p ≡0 mod2,
so s_p is even. Consequently

    **d_Kato(p)∈{1,3,5,...}.**

In particular, a SINGLE **Genuine cohomology class** κ_n^Kato≠0 with ν(n)≤2 forces d_Kato(p)≤2, hence by the odd gap d_Kato(p)=1, s_p=0, and

    **Sha(E/Q)[p∞] is FINITE.**

Conversely, if Sha(E/Q)[p∞] is finite, s_p=0 and BCGS gives d_Kato(p)=1, so there EXISTS a nonzero genuine Kato Kolyvagin class at **one** auxiliary prime. This yields the exact arithmetic equivalence:

    **Sha(E/Q)[p∞] finite ⇔ ∃ q∈L_Kato(p) with κ_q^Kato≠0
    ⇔ ∃ n with ν(n)≤2 and κ_n^Kato≠0.**

The middle equivalence uses BCGS Theorem C (for the existence and exact order) and the parity gap. The \(\kappa_q^{\mathrm{Kato}}\) may be nonzero *at higher p-power precision* and need NOT have nonzero reduction modulo p. Thus this theorem certifies **finiteness**, NOT the stronger vanishing Sha[p∞]=0. Full vanishing still requires an actual mod-p **unit Kurihara witness at auxiliary degree2**, or an equivalent integral Fitting/Selmer result.

**Why this is an actual new dichotomy, not circular use of finiteness:** BCGS Corollary C applies to nonzero Kato Kolyvagin classes without assuming Sha finite, and our MW localization surjectivity follows from an already proved rank-two non-torsion point. We prove only an equivalence; the low-degree Kato witness needed to use it has **not been produced for all large p**. BCGS Theorem C guarantees some κ_n≠0 but allows ν(n)≥3. Their refined theorem that the minimum p-divisibility index M∞ equals the sum of Tamagawa valuations (=0 for our curve) guarantees a primitive derivative at *some*, potentially arbitrarily large auxiliary degree, NOT that d_Kato(p)=1. The distinction between these two quantifiers is essential.

**Density-one range.** By Serre's open-image theorem, residual GL2 holds for all but finitely many p. For the non-CM curve, p with a_p=0 (supersingular) have density0 and p with a_p=1 (anomalous, for p≥7) have density0: for any auxiliary ℓ with full GL2(Fℓ), Chebotarev bounds the density of primes with a_p=a by #GL2 matrices of fixed trace a / #GL2 ≪1/ℓ; let ℓ→∞. Hence the exact ODD Kato degree / strict Sha corank formula above applies on a NATURAL DENSITY-ONE set of p. This is a true global theorem on a density-one family, but density-one eligibility does **not** imply that Sha is finite there, because low-degree nonvanishing is still unknown.

**Research significance.** For global finiteness one need only a two-auxiliary **nonzero genuine Kato cohomology class**, not necessarily a scalar Kurihara p-unit; parity upgrades this to a one-auxiliary nonzero class. For full Sha triviality, the stricter mod-p degree-two unit certificate from §1 remains necessary in this approach. The two-prime MW-localization density theorem from PR#20 and the transverse Selmer identification from PR#16 do NOT by themselves make the genuine Kato classes nonzero; this is the actual remaining global obstruction. No all-large-p low-degree nonvanishing or complex BSD equality is claimed.

## 2. Minimal-witness Selmer decomposition — fully proved

Fix a good p for which, in addition, E(Q_p)[p]=0 and Kim's semilocal theorem 1.10 applies. Let n=q1⋯qr be any **minimal mod-p unit** Kurihara witness with r=μ_p.

Kim gives a genuine isomorphism

$$
\lambda_n:S_p:=\operatorname{Sel}(E[p]/\mathbf Q)
\xrightarrow{\sim}\bigoplus_{i=1}^{r}L_i,
\qquad L_i:=E(\mathbf F_{q_i})/p.
\tag{4}
$$

By admissibility, dim L_i≥1, and the proof of Kim 1.10 gives r=dim S_p. Therefore each L_i has dimension 1. Let
$$
M_p:=E(\mathbf Q)/pE(\mathbf Q)\simeq\mathbf F_p^2
\hookrightarrow S_p.
$$
Since λ_n is an isomorphism, the r×2 matrix A_M of the restrictions of λ_n to the two full MW generators has rank 2. Choose **two row indices I={i,j}** for which the 2×2 minor \(A_I\) is invertible. Let R be the remaining r−2 indices.

Define the Selmer group **strict only at these two indices**:
$$
S_I^{\rm strict}:=\ker(S_p\longrightarrow L_i\oplus L_j).
$$

**Theorem 2 (minimal-witness Schur decomposition):**
$$
\boxed{S_p=M_p\oplus S_I^{\rm strict},\qquad
S_I^{\rm strict}\xrightarrow{\sim}\Sha(E/\mathbf Q)[p],\qquad
S_I^{\rm strict}\xrightarrow[\lambda_R]{\sim}
\bigoplus_{k\in R}L_k.}\tag{5}
$$

**Proof.** Restriction of λ_I to M_p is an isomorphism by the invertible minor A_I. Hence the projection
r:S_p→L_I→M_p obtained using (λ_I|_M)^{-1} splits the injection M_p→S_p, and its kernel is S_I^strict. The Kummer exact quotient S_p/M_p is Sha[p]; this identifies S_I^strict with Sha[p]. Since full λ_n is an isomorphism and λ_I=0 on S_I^strict, its restriction λ_R identifies the strict kernel with the full product of the remaining r−2 local lines. QED.

This is a **true primewise arithmetic consequence** of Kim, not a synthetic construction; it is conditional on the actual minimal unit witness. For r=2 the strict kernel vanishes. For r=4 (if such a prime exists for this E) the strict kernel is exactly 2-dimensional and is detected by the remaining two local Kummer lines. This does not establish existence of r=4 for 389a1.

## 3. Exact matrix formula (Schur complement)

Choose a basis of S_p extending the MW basis by arbitrary lifts s_1,...,s_d of a basis of Sha[p], d=r−2. Order rows by I,R and columns by MW,Sha-lifts. The true semilocal localization is an invertible r×r matrix

$$
\mathcal L=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\qquad A\in\mathrm{GL}_2(\mathbf F_p).
$$

Subtracting suitable MW combinations from the Sha lifts gives strict classes with first two local coordinates zero. The **remaining coordinates** are governed by

$$
\boxed{S=D-CA^{-1}B,\qquad
\det\mathcal L=\det A\cdot\det S.}\tag{6}
$$

Since λ_n is an isomorphism, S is an invertible d×d matrix. For d=0 its determinant is defined to be 1. This is an explicit formula for how the extra Sha[p] directions occupy the remaining auxiliary places.

**Caution:** A unit *full* determinant det(L) does not force d=0; when d=2, both det A and det S can be units. Thus a determinant of a high-degree semilocal map cannot replace the unavailable *degree-two Kurihara unit* or the actual Selmer-Fitting comparison.

## 4. Sharp formal countermodel — exact test but NOT the elliptic curve

The dependency-free script
[verification/bsd389_sharp_uniform_degree_and_schur_model.py](../verification/bsd389_sharp_uniform_degree_and_schur_model.py)
builds genuine finite-field *toy* linear algebra:
$$
S_p^{\rm toy}=\mathbf F_p^{\,2+2s},\quad
M_p^{\rm toy}=\mathbf F_p^2,\quad
W_p^{\rm toy}=\mathbf F_p^{2s}
$$
for s=0,1,2 and p=5,7,11,107, using our *actual previously certified* 2×2 MW local A matrices at each of those p. It extends A to a larger full invertible local matrix whose Schur complement is identity and gives W a standard alternating pairing.

The program replays **all 12** block determinants and every strict lift, including the synthetic case s=1 (degree 4), and prints PASS. Execution was by the assistant in local Python on 2026-11-14; SHA-256 of the exact script:
92f9298b10f5c72f058fa770a97cc94d5dd9222e65fb3d39bfac3434c3f6f0fb.

This is **not** a construction of actual Tate–Shafarevich elements, actual Kurihara numbers or a realization of a Kato system for E389a1. It proves only that independent MW local invertibility, arbitrarily many unit semilocal coordinates and symplectic parity are formally compatible with nonzero extra p-Selmer directions.

## 5. Exact remaining uniform theorem — no recycling of earlier certifications

To obtain a **real** value B in (2) we need new arithmetic information excluding any degree-4 (or greater) first Kurihara unit at all good p>B, i.e. an independent degree-two derived Kato primitivity theorem or a genuinely integral Selmer-complex comparison outside a finite integer exceptional set.

- The fixed universal MW wedge P∧Q is primitive everywhere but its image in the *full* Selmer dual may have torsion cokernel.
- The genuine modular-symbol Hecke Smith minor 2 belongs to a Hecke lattice, not Fitt₂(Sel^∨), and does not produce (2).
- Chebotarev supplies many invertible 2×2 local MW matrices for every covered p, but Theorem 2 shows why this is compatible with nonzero strict Selmer classes.
- The p²-level two-factor nonvanishing criterion (PR #22) remains **equivalent in consequence** to degree-two unit existence, by Cassels–Tate evenness; deeper precision without nonvanishing does not bypass the strict-kernel obstruction.
- Numerical positive L''(E,1)/2 proves analytic rank2, but has no proved integral p-independent comparison to the strict Selmer torsion.

**Verdict:** sharp uniform threshold and a fully proved Schur-complement local description of all extra Selmer directions under a minimal witness; verified formal countermodels show which existing data cannot force the bound. The actual p-uniform bound (2) is still OPEN; so are global Sha finiteness and the exact complex BSD leading coefficient.
