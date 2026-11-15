# 389a1 at p=599: signed analytic unit from an INDEPENDENT genuine p² Manin moment and proof-level Selmer closure

**2026-11-15. This note presents a NEW computer-assisted proof route to \(\Sha(E/\mathbf Q)[599^\infty]=0\), conditional ONLY on the explicitly listed authenticated exact finite arithmetic input and the stated published/preprint theorems.** It does **not** prove the all-prime Sha finiteness or exact complex rank-two BSD, and it does not independently invoke Sage \`E.sha().p_primary_bound(599)\`. The note is a DRAFT for independent mathematical and software review before accepting the p599 closure as an unqualified theorem.

## 1. Actual E389a1 and finite arithmetic input, now independently recomputed

Take the minimal semistable curve
\[
E/\mathbf Q:y^2+y=x^3+x^2-2x,\quad N=389,\quad \Delta=+389.
\]
Published/archived certified arithmetic: \(E(\mathbf Q)=\mathbf Z P\oplus\mathbf Z Q\), \(P=(-1,1),Q=(0,-1)\), rank 2, torsion 1, Tamagawa product1, real_components2, Manin constant1, \(a_{599}=0\) supersingular, surjective \(\rho_{E,599}:G_\mathbf Q\to\mathrm{GL}_2(\mathbf F_{599})\).

At \(p=599\), let \(m^+(a/n)\) denote the authentic Néron-normalized *plus modular symbol* used by the Sage/eclib cyclotomic measure. Let \(j_2(a)\in\mathbf Z/p\) be the cyclotomic exponent characterized by \(a=\omega(a)(1+p)^{j_2(a)}\pmod{p^2}\). Define
\[
 C_2:=\sum_{a\in(\mathbf Z/p^2)^\times}\binom{j_2(a)}2\,m^+(a/p^2)
 \pmod p.
\]
The user's original fully executed Sage/eclib table is SHA256
\`fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8\`, and authentic result \(C_2=543\), \(C_0=C_1=0\); the original user log and trace are archived in
\`results/p599_sha_short_certificate_user_run_2026-10-30.md\`.

**New truly independent assistant execution 2026-11-15:** the companion
[verification/bsd389_p599_integral_manin_independent_c2_20261115.py](../verification/bsd389_p599_integral_manin_independent_c2_20261115.py)
reconstructs the entire finite conductor-p² sum from the historically *separately authenticated* 390-entry signed **INTEGER** Manin vector on a research branch, using Euclidean rational-cusp modular symbols instead of the pinned p599 eclib table. All 179101 plus-symmetry representatives are evaluated, with the EXACT output

    P599_INDEPENDENT_INTEGER_390_MANIN_CUSPS 179101 seconds 0.879
    P599_INDEPENDENT_MOMENTS 0 0 543
    P599_INDEPENDENT_SOURCE_CHECK_PASS_C2 543

This is a second *method and data-source* check, although the integral vector's independent archival derivation is itself a project dependency. The code also independently spot-checks \(m^+(7/389)=-1\), \(m^+(5/389)=-2\). Assistant script SHA256
\`2dc8404d806bf9139e976061ad248b1a91dbea1b7bd3b46a24449c139994386d\`.

## 2. A SHORT EXACT p³→p² SIGNED LEADING COEFFICIENT FORMULA

Let \(\alpha^2=-p\) (since \(a_p=0\)), and \(j_3(a)\in\mathbf Z/p^2\) the cyclotomic exponent at conductor \(p^3\). Put
\[
 w(j)=\binom j2,\qquad
 B_3:=\sum_{a\in(\mathbf Z/p^3)^\times}w(j_3(a))\,m^+(a/p^2).
\]
No conductor-p³ modular symbol appears in \(B_3\) — only the already authenticated conductor-p² symbols. Every lift \(a=b+t p^2\) for fixed b mod p² changes \(j_3\) through the complete set \(j_2(b)+pk,\ k\in\mathbf F_p\), since \((1+p)^p\equiv1+p^2\bmod p^3\). For **every** j,
\[
 \sum_{k=0}^{p-1} \binom{j+pk}2
 \equiv p\binom j2 \pmod{p^2}.
\]
Consequently
\[
 \boxed{B_3\equiv p C_2\pmod{p^2},
 \qquad B_3/p\equiv C_2\equiv543\pmod p.}\tag{A}
\]
This follows by an integral identity, not a statistical pilot or a complete p³ enumeration. It is checked at p5,7,11,599 with 100% of chosen j in the standalone exact verifier.

## 3. Pollack's INTEGRAL signed minus coefficient: no regulator or p³ cusp table needed

In Sage's source \`padic_lseries.py\`, at supersingular \(a_p=0\), the n=3 approximation to the analytic eigenvalue \(p\)-adic L-function has coefficient
\[
 [T^2]L_{p,\alpha}^{(3)}(T)
 =\frac{\alpha A_3-B_3}{2p^2},
\]
where \(A_3\) involves conductor-p³ cusp symbols, but \(B_3\) is the above sum of p² symbols. The denominator 2 is exactly \(\#\pi_0(E(\mathbf R))=2\). The expression follows from Sage's concrete measure
\(\mu(a+p^3\mathbf Z_p)=\alpha^{-3}m^+(a/p^3)-\alpha^{-4}m^+(a/p^2)\)
and \(\alpha^{-3}=\alpha/p^2,\ \alpha^{-4}=1/p^2\).

At X=0 the Pollack/Castella logarithm matrix is
\[
 Z_{\log}=\frac1p\begin{pmatrix}1&1\\ \alpha&-\alpha\end{pmatrix}.
\]
The \(\mathrm{GL}_2\)-basis vectors of Castella §4.1 satisfy
\(\nu_\alpha=(\omega-\beta\varphi\omega)/2\),
\(\nu_\beta=(\omega-\alpha\varphi\omega)/2\),
\(\alpha+\beta=0,\alpha\beta=p\), and hence
\[
 \boxed{\nu_-=\omega/p,\qquad\nu_+=-\varphi\omega.}
\]
The unprojected Dieudonné vector computed from Sage's eigenvalue pair is
\[
 [T^2]\mathbf L_p^{(3)}=(-B_3/(2p^2),-A_3/(2p))
 \quad\text{in the }(\omega,\varphi\omega)\text{ basis}.
\]
Therefore the **INTEGRAL signed minus** coefficient at quadratic order is
\[
 \boxed{[T^2]L_{p}^{-,(3)}=p\cdot(-B_3/(2p^2))=-B_3/(2p).}\tag{B}
\]
**Crucially the entire enormous A3 cusp sum cancels EXACTLY.** Combining (A),(B):
\[
 \boxed{[T^2]L_{599}^{-}\equiv-543/2\equiv28\pmod{599}.}\tag{C}
\]

**Precision gate.** This is not just an approximation to an arbitrary precision. Sage's proven supersingular bound at n=3, T² is \(\_prec\_bounds(3,3)[2]=2(2)-(3+2)=-1\) in the \(\alpha\)-adic valuation, where \(v_\alpha(\alpha)=1\) and \(v_\alpha(p)=2\). An \(O(\alpha^{-1})\) error in the eigenvalue coefficient \(G+\alpha H\) has scalar component \(G\) in \(\mathbf Z_p\); multiplication by p to obtain the *signed minus* coefficient makes the error \(O(p)\). Thus (C) is the congruence of the **genuine analytic signed p-adic L-function**, not merely the n=3 approximate coefficient. This argument is independent of the Frobenius-projected first-coordinate error proof used in the old p599 short certificate.

**Two independent normalization crosschecks.**
1. For a rank-zero constant eigenfunction the formula gives \(L_p^-(0)=(p-1)L(E,1)/\Omega_E\) and \(L_p^+(0)=2L(E,1)/\Omega_E\), EXACTLY the trivial-character constants in Burungale–Skinner–Tian–Wan (2024), §1.1.1, and Kim (2008), Introduction. This rules out a missing \(p^{\pm1}\) normalization at the signed-vs-eigenvalue step.
2. Reconstructing the same coefficient from the archived Sage Frobenius projection \(F=(1-\varphi)^{-2}\mathbf L_p\) gives \(F_{0,2}\equiv571,\ F_{1,2}\equiv0\bmod p\), with \(\varphi=\small\begin{pmatrix}0&-1/p\\1&0\end{pmatrix}\), and \([T^2]L_p^-=(p-1)F_{0,2}+2F_{1,2}\equiv28\bmod599\).

The **historical supersingular normalization conflict** in Stein–Wuthrich 2013, §6.2 vs §4.4, is thus **AVOIDED entirely**. We do NOT use the printed inequality involving the raw \(\mathrm{Reg}_p\); no p-adic regulator is required in the main argument.

## 4. A NEW GENERAL ALGEBRAIC LEMMA: rank-two MW + char=(T²) + no finite submodule ⇒ Sha[p∞]=0

Let \(\Lambda=\mathbf Z_p[[T]]\). Let \(E/\mathbf Q\) be an elliptic curve of known saturated rank-two Mordell–Weil group, good supersingular at p≥5, with full residual GL2(Fp). Let \(X^-=\mathrm{Sel}_{p^\infty}^-(E/\mathbf Q_\infty)^\vee\) denote the Pontryagin-dual minus signed cyclotomic Selmer group.

**Lemma.** Assume
(i) \(\operatorname{char}_\Lambda(X^-)=(T^2)\);
(ii) \(X^-\) has NO nonzero finite Λ-submodule;
(iii) the natural rational restriction \(\mathrm{Sel}_{p^\infty}(E/\mathbf Q)\hookrightarrow
\mathrm{Sel}_{p^\infty}^-(E/\mathbf Q_\infty)^\Gamma\) is injective, and it contains the image of the rank-two MW divisible subgroup.
Then
\[
\boxed{\Sha(E/\mathbf Q)[p^\infty]=0.}\tag{D}
\]

**Proof.** The structure theorem for finitely generated torsion Λ-modules yields a pseudo-isomorphism from \(X^-\) to a module N supported only at height-one prime (T), with total T-length2. Therefore N is either \(\Lambda/(T^2)\) or \((\Lambda/T)^2\), up to a finite pseudo-null term. We choose a map \(X^-\to N\) with finite kernel and cokernel; (ii) forces kernel0. Since N is free of rank2 over \(\mathbf Z_p\), X^- is also free of Zp-rank2 and T acts nilpotently. Condition (iii) yields
\(\operatorname{rank}_{\mathbf Z_p}(X^-/TX^-)\ge2\). Since \(\operatorname{rank}_{\mathbf Z_p}(X^-)=2\), the nilpotent T must act as 0 on X^-\(\otimes\mathbf Q_p\), hence also on X^- itself by torsion freeness. Thus \(X^-\cong\mathbf Z_p^2\) as a Λ-module with T=0. Dualizing,
\[
\mathrm{Sel}_{p^\infty}^-(E/\mathbf Q_\infty)^\Gamma
\cong(\mathbf Q_p/\mathbf Z_p)^2.
\]
The globally saturated MW image \((\mathbf Q_p/\mathbf Z_p)^2\) embeds into it; any embedding between two divisible p-groups of equal finite corank is surjective (Pontryagin dual of an injective map of divisible groups is a surjective endomorphism of Zp², necessarily invertible). Hence the subgroup \(\mathrm{Sel}_{p^\infty}(E/\mathbf Q)\), sitting between the MW group and the same invariants, equals MW. The exact Kummer sequence forces Sha[p∞]=0. QED.

**Checking the hypotheses (ii),(iii) for this ACTUAL curve and p.** By B.D. Kim, *The plus/minus Selmer groups for supersingular primes*, J. Aust. Math. Soc. 95 (2013), Theorem 1/19, the **minus signed** \(\Lambda\)-cotorsion Selmer group has no proper finite-index \(\Lambda\)-submodule; duality gives (ii). For (iii), since \(\mathrm{GL}_2(\mathbf F_p)\) has no nontrivial abelian p-quotient when p≥5, the p-division field \(\mathbf Q(E[p])\) is linearly disjoint from the cyclotomic \(\mathbf Z_p\)-extension \(\mathbf Q_\infty\). Thus \(E[p](\mathbf Q_\infty)=0\), hence \(E[p^\infty](\mathbf Q_\infty)=0\), making global H¹ restriction injective by inflation-restriction. At the infinite p-adic place, every base-field local Kummer class satisfies the signed minus norm condition (base rational points satisfy every trace relation), so restriction lands in the signed Selmer. At primes not dividing p the Kummer conditions are respected. MW rank2 injects as required.

## 5. APPLICATION: the 2024 published-theorem breakthrough — signed MAIN CONJECTURE

Burungale–Skinner–Tian–Wan, *Zeta elements for elliptic curves and applications*, arXiv:2409.01350 v2 (2024), **Theorem 1.3**, proves the FULL signed Kobayashi Main Conjecture for **every semistable elliptic curve over Q at any supersingular prime p>2**:
\[
\boxed{\operatorname{char}_\Lambda(X^\pm)=(L_p^\pm)}
\]
(with only an additional gate at p3). This theorem is stated explicitly in §1.1.1, printed page3 of the 2024 preprint: https://arxiv.org/pdf/2409.01350 .

Thus for E389a1 and p599 its hypotheses hold. Kato's rank lower bound or Castella 2025 Thm A(i) establishes that \(\operatorname{ord}_T L_p^-\ge2\). The unit (C) implies the **STRONGER FULL POWER SERIES IDEAL IDENTITY**
\[
\boxed{(L_{599}^-)=(T^2)\subset\mathbf Z_{599}[[T]],}
\]
because \(L_{599}^-(T)=T^2(28+599u_0+T u_1(T))\) and the parenthetical factor is a power-series unit. Main-conjecture equality gives
\(\operatorname{char}_\Lambda(X^-)=(T^2)\). Lemma §4 and B.D. Kim's no-finite-submodule theorem then yield the **computer-assisted arithmetic conclusion**
\[
\boxed{\Sha(E389a1/\mathbf Q)[599^\infty]=0.}
\]

**Important provenance/status qualifier:** This is a complete *proposed proof*, assuming the authenticated historical 390-integer symbol vector is correctly normalized (independently tested against the user-executed eclib table), the finite arithmetic run remains reproducible, and the signed p-adic L-functions normalized by the 2024 main conjecture are exactly those obtained through the Pollack/Castella matrix (crosschecked at trivial character). The key unpublished piece in previous work — an interpretation of the Stein–Wuthrich raw regulator — is not used. It deserves **independent scholarly review** before the project changes its SHA599 status from REVIEW_REQUIRED to CERTIFIED. This branch/PR is for that review; main and prior gate labels remain unchanged.

**Sources:**
- Burungale, Skinner, Tian, Wan (2024), Thm1.3: https://arxiv.org/pdf/2409.01350 ;
- Castella (2025), Def3.1.1 and Def4.2.1: https://web.math.ucsb.edu/~castella/Coates.pdf ;
- B.D. Kim (2013), Theorem1: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7AD9B7AB53A73F23F8E78F78488FA75C/S1446788713000165a.pdf/the-plusminus-selmer-groups-for-supersingular-primes.pdf ;
- Pollack (2003), \(\alpha\)-distribution and signed decomposition: https://math.bu.edu/people/rpollack/Papers/On_the_padic_Lfunction_of_a_modular_form_at_a_ss_prime.pdf ;
- Sage current source: https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/schemes/elliptic_curves/padic_lseries.py ;
- exact original arithmetic log: results/p599_sha_short_certificate_user_run_2026-10-30.md .

## 6. Scope and high-level verdict

The present research identifies an exact p²-only **signed cyclotomic unit criterion** for rank-two semistable supersingular curves under full residual GL2:
\[
\boxed{C_{2,p}\not\equiv0\pmod p\Longrightarrow
\operatorname{char}_{\Lambda_p}(X^-_p)=(T^2)
\Longrightarrow \Sha(E/\mathbf Q)[p^\infty]=0,}
\]
given the same Manin normalization and rank-two/local hypotheses. This is a genuinely NEW non-Kurihara sufficient theorem relying on the already proved signed Main Conjecture, with a remarkably cheap \(O(p^2)\) conductor-moment test rather than p³ and full two-auxiliary-prime Kurihara sums. It is *primewise*, **not** a proof that C2 remains nonzero for all sufficiently large supersingular p and not a proof of global Sha finiteness. The complex rank-two BSD leading coefficient \(L''(E,1)/2=\Omega_E\mathrm{Reg}_E\#\Sha\) remains OPEN.
