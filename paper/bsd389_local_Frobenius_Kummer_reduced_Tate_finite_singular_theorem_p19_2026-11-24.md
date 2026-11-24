# 389a1 — Frobenius–Kummer–Tate local quadratic-form theorem, and a new independent p=19 test of ILTR

**Date: 24 November 2026.** **PROVED**: a precise local cohomological identity identifying the rank-one symmetric form built from the reduced finite-field Tate pairing with the nilpotent Frobenius finite–singular map, including a direct formula for the p-torsion point. **NEW FINITE TEST**: a genuine authentic modular-symbol Kurihara sum on 4,344,996 half-units at p=19 agrees with the independently computed reduced Tate prediction 4 mod19. **NOT PROVED**: the global Kato/Mazur–Tate mixed-coefficient reciprocity ILTR, all-p vanishing of Sha, or exact complex rank-two BSD.

## 1. The exact local result

Let \(E/\mathbf F_q\) be any elliptic curve, \(p\ge5\) an odd prime different from the characteristic q, with
\[
q\equiv1\bmod p,\qquad \#E(\mathbf F_q)=pM,\quad p\nmid M.
\]
Let \(\pi\) be arithmetic q-power Frobenius and \(V=E[p](\overline{\mathbf F}_q)\), with Weil pairing \(e_p:V\times V\to\mu_p\).

Because \(\#E(\mathbf F_q)=\det(1-\pi\mid T_pE)\) has p-adic valuation EXACTLY one, \(\pi-I\) modulo p has rank exactly one. The trace of \(\pi\) is \(q+1-\#E(\mathbf F_q)\equiv2\bmod p\), so
\[
\pi|_V=I+N,\qquad N^2=0,\quad\operatorname{rank}_{\mathbf F_p}N=1.
\tag{1}
\]

Let \(e\in E(\mathbf F_q)\), and pick \(R\in E(\overline{\mathbf F}_q)\) with \(pR=e\). The Kummer cocycle evaluated at Frobenius is
\[
c_e=(\pi-1)R\in V,\qquad [c_e]\in V/NV\simeq E(\mathbf F_q)/pE(\mathbf F_q).
\]
This is the canonical finite-field Kummer isomorphism, using Lang's theorem.

**THEOREM (exact Frobenius/Kummer formula).**
\[
\boxed{[M]e=-N c_e \ \in E(\mathbf F_q)[p]=\ker N.}
\tag{2}
\]

**Proof.** Denote the dual Frobenius (Verschiebung) by \(\hat\pi\). Weil's polynomial gives
\[
\pi+\hat\pi=[a_q],\quad\pi\hat\pi=[q],\quad
(1-\pi)(1-\hat\pi)=[q+1-a_q]=[\#E(\mathbf F_q)].
\]
Therefore
\[
[M]e=[pM]R=(1-\pi)(1-\hat\pi)R
=(1-\hat\pi)(1-\pi)R
=-(1-\hat\pi)c_e.
\]
On V, \(\hat\pi=a_q-\pi\equiv2-(1+N)=1-N\), hence \(1-\hat\pi=N\). This proves (2) exactly. It is independent of the chosen p-division R since replacing R by a p-torsion point changes c_e by N times that point, which N kills. QED.

**COROLLARY (symmetric finite–singular Tate quadratic form).** Identify the degree-one Galois cohomology
\(H^1(\mathbf F_q,V)\simeq V/NV\) and the p-torsion \(E(\mathbf F_q)[p]=\ker N\). The map
\[
\boxed{\Phi_q:V/NV\xrightarrow{\sim}\ker N,\quad [v]\longmapsto -Nv}
\tag{3}
\]
is a canonical isomorphism. The finite-field Tate pairing, viewed through the Kummer cocycle and Weil pairing, defines
\[
\boxed{B_q([v],[w])=e_p(-Nv,w)\in\mu_p.}
\tag{4}
\]
The form is WELL-DEFINED, PERFECT, and SYMMETRIC. It is the canonical rank-one bilinear form from the finite–singular comparison \(\Phi_q\), followed by the Weil pairing.

**Proof.** Both source and target have dimension one, N has rank1, so \(\Phi_q\) is an isomorphism. The expression e_p(-Nv,w) is independent of representatives because N²=0, \(\operatorname{im}N=\ker N\) is an isotropic line for the alternating Weil pairing. Symmetry follows from invariance of the Weil pairing under \(\pi=1+N\):
\[
\langle (1+N)v,(1+N)w\rangle=\langle v,w\rangle.
\]
Expanding, and using that \(\langle Nv,Nw\rangle=0\), gives
\(\langle Nv,w\rangle=-\langle v,Nw\rangle=\langle Nw,v\rangle\).
Hence \(B_q(v,w)=B_q(w,v)\). Perfection follows from \(\Phi_q\) being an isomorphism and Weil duality between \(\ker N\) and \(V/NV\). QED.

**Conventions:** The cohomological definition of the finite-field Tate pairing evaluates \(e_p(g,c_e)\) at Frobenius. Its identification with the Miller **reduced** Tate value may use the inverse depending on convention (Frobenius versus inverse, Weil-pairing argument order). Our numerical weights use one explicitly fixed Miller convention. A sign/orientation comparison is a genuine normalization obligation for the global conjecture; it does not affect symmetry/perfection or the determinant-square structure.

## 2. Exact rank-two determinant consequence — ALL local work is done

For 389a1 (or any rank-two E/Q), fix a prime p and a saturated basis P,Q, and pull the pairing B_q along the reduction
\[
E(\mathbf Q)/p\to E(\mathbf F_q)/p.
\]
In the chosen discrete log of \(\mu_p\) with primitive root \(\gamma_q^{(q-1)/p}\), its matrix is **necessarily**
\[
\mathcal B_q=w_q v_qv_q^\top,
\]
where \(v_q\) is the (P,Q) local image row and \(w_q\) is the independently defined reduced Tate pairing weight. This follows from (4); not an experimental inference. Thus
\[
\boxed{\det(\mathcal B_{q_1}+\mathcal B_{q_2})
=w_{q_1}w_{q_2}\det(v_{q_1},v_{q_2})^2.}
\tag{5}
\]
Proof: the exact rank-two Cauchy–Binet expansion.

**Exactly what is NOT proved** is
\[
\tilde\delta_{q_1q_2}\stackrel{?}=2\det(\mathcal B_{q_1}+\mathcal B_{q_2})\pmod p.
\tag{6}
\]
The left side arises from a **global Kato/Manin zeta element**; the right side from a **local finite–singular Frobenius morphism applied to the rational MW rank-two lattice**. A canonical determinant-line comparison of these sources, including the potential Sha factor, is missing. The theorem above closes the LOCAL part, not the global zeta comparison.

In particular, Burns–Kurihara–Sano, *On derivatives of Kato's Euler system and the Mazur–Tate conjecture*, Conjecture 2.3, predicts precisely a Mazur–Tate leading coefficient involving the **algebraic BSD factor** #Sha(E/Q) (when finite), not just a MW determinant. Their Theorem 1.1 assumes p is prime to #E(Fq) for ramified q and **already assumes BSD over Q**; our auxiliary q have p|#E(Fq), so that theorem is inapplicable. These are critical limitations, not a reason to abandon a new proof.

Reference: https://arxiv.org/pdf/2103.11535, §2.2 Conjecture 2.3, Theorem 1.1; finite-field Tate pairing and Kummer/Frobenius via local class field theory.

## 3. NEW p=19 adversarial test, outside all preceding p=5,7,11,13,17 samples

Select good distinct p-admissible primes
\[
p=19,\quad q_1=2243,\quad q_2=3877
\]
with EXACT finite-field point counts
\[
\#E(\mathbf F_{2243})=2261=19\cdot119,\qquad
\#E(\mathbf F_{3877})=3781=19\cdot199,
\]
traces \(a_{2243}=-17\equiv2\bmod19\), \(a_{3877}=97\equiv2\bmod19\), and both q≡1 mod19. The smallest primitive root at each q is \(\gamma_q=2\).

Independent elliptic finite-field group-law computations of P=(-1,1), Q=(0,-1) give local MW rows:
\[
v_{2243}=(1,1),\quad v_{3877}=(0,1),\quad\Delta=1.
\]
A separate exact reduced Tate/Miller algorithm, not using any modular-symbol value, gives primitive-root-normalized weights
\[
w_{2243}=17,\qquad w_{3877}=18.
\]
This makes the **a priori** ILTR prediction
\[
2\cdot17\cdot18\cdot1^2\equiv\boxed4\bmod19.
\]

After the prediction had been fixed, the genuine full Hecke/Manin two-prime Kurihara weighted sum was computed by an independent optimized C++17 code over precisely
\[
\varphi(2243\cdot3877)/2=(2242\cdot3876)/2=
\boxed{4,344,996}
\]
representatives, using the historically authenticated 390-term integer Manin symbol vector. Both with and without activated C++ assertions the COMPLETE output was
\[
\boxed{\tilde\delta_{2243\cdot3877}=4\bmod19.}
\]
The numerator is not inferred from the p=19 local Tate computation; the global Manin computation was independent.

The number of genuine matched pair values thus increases from **137 at five p** to **138 at six p**, with no refitting of the coefficient 2.

This NEW sample is strong *falsification-oriented* evidence but does not prove the all-p congruence.

## 4. The next proof obligation, now reduced to a single global statement

Let \(C_{\mathrm{Sel}}\) denote the genuinely integral rank-two Selmer complex and \(z_{\mathrm{Kato}}\) its authentic global Kato determinant-line element. The local theorem constructs canonical rank-one symmetric pairings \(B_q\) from the finite–singular morphisms, hence a canonical two-prime rank-two determinant \(D_{q_1q_2}=\det(B_{q_1}+B_{q_2})\), independently of global modular symbols.

**Required new global theorem:** construct the arithmetic determinant-line comparison, without assuming finiteness of Sha or the BSD leading-term formula, that sends the *actual integral* Kato/Mazur–Tate mixed derivative to \(2D_{q_1q_2}\). The comparison must detect the possible torsion/corank of Sha rather than deleting it. If it can be proved with a nonzero global leading scalar (in the Néron integral normalization), the established Bullach–Honnor finite-level jet criterion gives uniform Sha[p∞]=0 for all sufficiently large p. Without this comparison, the 138 matched pairs remain finite evidence.

**Scope:** local comparison PROVED; new p19 finite arithmetic test PASS; uniform global comparison/strong BSD OPEN. No new brute-force families needed.
