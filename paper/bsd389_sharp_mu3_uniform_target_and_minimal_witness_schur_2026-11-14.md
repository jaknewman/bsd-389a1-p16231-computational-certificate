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
