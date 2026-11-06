> **2026-11-06 NEW EXACT CONTROL AT THE FIXED P=16231 (not all p):** the assumption (C) in this paper is now discharged **for the Chida–Hsieh (N^-=389)-ordinary anticyclotomic module**, which is not automatically the same as the classical Selmer at the entire infinite tower. Chida–Hsieh Proposition 1.9 (2014/15) applies to (K=\mathbf Q(\sqrt{-3})) with p=16231 (surjective E[p], ordinary, a_p=128 with (a_p^2\not\equiv1\mod p)), and gives (X_{\Delta}/TX_{\Delta}\cong S_{\Delta}(K,E[p^\infty])^\vee). At the base K, Proposition 1.7 (residual ramification at 389) plus nonanomalous ordinary local Kummer comparison at p identify (S_{\Delta}(K,E[p^\infty])) with the **classical** Selmer. Therefore the exact rank-two Fitting augmentation formula is a proven theorem at this p **with (X_{\Delta})**. This does **not** extend Kim's 2026 initial-Fitting theorem to discriminant -3, prove (\mathrm{Fitt}_{2,\Lambda}(X_\Delta)=\Lambda), or settle Sha. [Complete proof](bsd389_p16231_CH_original_exact_control_Kminus3_classical_aug_Fitt2_2026-11-06.md).

# A genuine augmentation bridge: higher anticyclotomic Fitting2 to BOTH quadratic Sha eigenspaces

Date: 2026-11-06. **Formal integral theorem under an explicitly stated ARITHMETIC CONTROL ISOMORPHISM.** This is not a proof of global BSD or that the control theorem extends unchanged to K=Q(sqrt(-3)). No previously certified computation is rerun.

## 1. Exact published Selmer control in the standard field range

C.-H. Kim, *On the Fitting ideals of anticyclotomic Selmer groups of elliptic curves with good ordinary reduction*, Canadian Math. Bull. 69 (2026), Proposition 4.3, proves for E,p,K under his hypotheses (Im),(Na),(Def),(Ram):
\[
\mathrm{Sel}(K_n,E[p^\infty])
\longrightarrow \mathrm{Sel}(K_\infty,E[p^\infty])[\omega_n]
\]
is an **isomorphism**, where
\(\omega_n=(1+T)^{p^n}-1\), so \(\omega_0=T\).
Its Theorem 1.1 and field setup additionally impose **odd discriminant <-4**, hence this published proposition cannot simply be cited for the project's fixed K=Q(sqrt(-3)), whose discriminant is -3. One would need to check the underlying control proof for exceptional units or use a different quadratic field satisfying the published hypotheses. This note treats the exact control isomorphism as a transparent assumption, not an achieved result for K=-3.

## 2. Theorem: exact specialized higher Fitting identity

Let E=389a1 and fix an odd prime p. Let K be an imaginary quadratic field for which:
- \(\mathrm{rank}\,E(K)=2\), and the quadratic twist \(E^d/\mathbf Q\) has rank 0 and **finite** \Sha (the project's K=-3 twist has these properties);
- \(K_\infty/K\) is an anticyclotomic \(\mathbf Z_p\)-extension and
\[
X_\infty=\mathrm{Sel}(K_\infty,E[p^\infty])^\vee
\]
is a finitely generated \(\Lambda=\mathbf Z_p[[T]]\)-module;
- there is a **proved integral control isomorphism**
\[
\boxed{X_\infty/TX_\infty \simeq
\mathrm{Sel}(K,E[p^\infty])^\vee.}\tag{C}
\]

Define \(I_{+,p}=\mathrm{Fitt}_{0,\mathbf Z_p}
(\Sha(E/\mathbf Q)[p^\infty]^\vee)\) and
\(I_{-,p}=\mathrm{Fitt}_{0,\mathbf Z_p}
(\Sha(E^d/\mathbf Q)[p^\infty]^\vee)\).

**Theorem.** Under (C), there is an EXACT ideal equality:
\[
\boxed{
\frac{\mathrm{Fitt}_{2,\Lambda}(X_\infty)+(T)}{(T)}
=I_{+,p}\cdot I_{-,p}\ \subseteq \mathbf Z_p.
}\tag{*}
\]

**Proof.** Fitting ideals commute with arbitrary base change. Thus the left side is
\(\mathrm{Fitt}_{2,\mathbf Z_p}(X_\infty/TX_\infty)\).
By (C), this equals
\(\mathrm{Fitt}_{2,\mathbf Z_p}(\mathrm{Sel}(K,E[p^\infty])^\vee)\).
Kummer duality and projectivity of \(\mathbf Z_p^2\) give a split
\[
\mathrm{Sel}(K,E[p^\infty])^\vee
 \simeq \mathbf Z_p^2\oplus\Sha(E/K)[p^\infty]^\vee
\]
because \(\mathrm{rank}\,E(K)=2\), **without assuming Sha(E/K) finite**. Hence Fitt2 equals Fitt0 of the Sha dual. For p odd, restriction/corestriction and quadratic descent split
\[
\Sha(E/K)[p^\infty]\simeq
\Sha(E/\mathbf Q)[p^\infty]\oplus
\Sha(E^d/\mathbf Q)[p^\infty].
\]
Fitt0 of a direct sum is the product of Fitt0 of the summands. This is exactly \((*)\). QED.

## 3. Strong corollaries and their exact quantifiers

Let \(\mathfrak m=(p,T)\) be the height-two maximal ideal of \(\Lambda\).

**Corollary A.** Under (C),
\[
\boxed{
\mathrm{Fitt}_{2,\Lambda}(X_\infty)=\Lambda
\iff
\Sha(E/\mathbf Q)[p^\infty]=0
\text{ AND }
\Sha(E^d/\mathbf Q)[p^\infty]=0.
}
\]
Equivalently, the image of \(\mathrm{Fitt}_2\) in
\(\Lambda/\mathfrak m=\mathbf F_p\) is nonzero.
*Proof:* \(\Lambda\) is local, so an ideal is unit iff it is not contained in \(\mathfrak m\). Apply \((*)\) and note \(I_+\cdot I_-=\mathbf Z_p\) iff both factors are units.

**Corollary B (finite exceptional twist set).** Since \Sha(E^d/\mathbf Q) is independently proved **finite** for the rank-zero twist, let the single (not necessarily explicitly evaluated) integer
\(D_-=\#\Sha(E^d/\mathbf Q)\in\mathbf Z_{>0}\).
For **every odd p not dividing \(D_-\)** for which the control isomorphism (C) holds:
\[
\boxed{
\Sha(E/\mathbf Q)[p^\infty]=0
\iff
\mathrm{Fitt}_{2,\Lambda}(X_\infty)=\Lambda.
}
\]
Consequently a theorem establishing the RHS uniformly for all p outside an explicit finite S (plus the known finite support of D_-) would prove the desired all-but-finite-p Sha vanishing; all remaining p-primary components would still need finite bounds, and the complex BSD formula is separate. Merely knowing this equivalence or a pseudo-Fitting statement does not prove uniform vanishing.

**Corollary C (ideal valuation).** If (C) holds and \Sha(E/\mathbf Q)[p^\infty] is finite, then with \(e_{+,p}=v_p(\#\Sha(E/\mathbf Q)[p^\infty])\) and \(e_{-,p}=v_p(D_-)\),
\[
\frac{\mathrm{Fitt}_{2,\Lambda}(X_\infty)+(T)}{(T)}
=p^{e_{+,p}+e_{-,p}}\mathbf Z_p.
\]
At odd p, each finite Sha order is a square (Cassels–Tate). If \Sha(E/\mathbf Q)[p∞] is infinite then \(I_{+,p}=0\), and both sides of \((*)\) are zero.

## 4. Where the 2026 higher-Fitting preprint stops

Da Ronche–Longo–Vigni (March 2026), Theorem 5.9 in the definite case, compares **higher** \(\mathrm{Fitt}_{i,\Lambda}(\mathcal X)\) with Euler-system-generated ideals \(\mathfrak C_i^2\) **only up to pseudo-isomorphism / height-two equivalence** \(\sim\). The genuine obstruction above is precisely the **height-two maximal ideal (p,T)**, which such equivalence can erase. The mathematical proof is our explicit matrix example:
\[
X_{\rm good}=\mathrm{coker}\,\mathrm{diag}(1,1,T^2,T^2),
\quad
X_{\rm bad}=\mathrm{coker}\,\mathrm{diag}\left(
 \begin{pmatrix}p&T\\T&0\end{pmatrix},
 \begin{pmatrix}p&T\\T&0\end{pmatrix}\right).
\]
They have initial Fitt0=(T4), identical finite-layer initial Fitting ideals, and are pseudo-isomorphic, yet the augmented higher ideals are (1) and (p²).

Thus, to use a higher-Fitting Euler-system theorem for global 389a1, one must **strengthen its specialization at \(\mathfrak m=(p,T)\) to an ACTUAL integral unit/minor**, not merely a pseudo-isomorphism of ideals. Even the correct arithmetic equality \((*)\) is conditional on a verified **exact control map** for the chosen auxiliary K.

## 5. Precise new proof target (no new spot checks)

Construct, in the actual canonical anticyclotomic Selmer complex of E over K:
1. An integral exact specialization/control map at augmentation \(T=0\) including all exceptional units, p-adic local conditions, and Tamagawa factors.
2. A rank-two **higher Fitting** generator/minor at the maximal ideal \((p,T)\), with exact p-integral derived Bockstein/height interpretation. Prove a unit (or a uniform rationally descended integer bound), not just a nonzero leading coefficient of \(\theta\) or an ideal equivalence \(\sim\).
3. A uniform all-p argument or p-independent integral numerator controlling the exceptional p support, plus existing certified exceptional components.
4. Independent exact complex leading term \(L''(E,1)/2=\Omega_E\mathrm{Reg}(E)\#\Sha\).

This is a formal theorem and a rigorous quantifier audit; it does NOT construct the rank-two higher Fitting generator, prove control for exceptional K=-3, prove finiteness of Sha, or establish BSD.

### Sources
- Kim (2026) https://doi.org/10.4153/S000843952510088X , Proposition 4.3 (control), Theorem 1.1 (Fitting0), field hypotheses in §1.
- Da Ronche–Longo–Vigni (2026) https://arxiv.org/abs/2603.12357 , Theorem 5.9 and definition of \(\sim\).
- Exact codimension-two counterexample: \`paper/bsd389_integral_Bockstein_height2_counterexample_and_true_Fitting_specialization_2026-11-06.md\`.
- Proven rank-zero twist / quadratic splitting in project: \`paper/389a1_quadratic_base_change_twist_rank0_finite_minus_sha_2026-10-27.md\`.
