# 389a1: core vertices exist at every p-power level for all sufficiently large p, and the CORRECT uniform Kato I1 criterion includes the p-local index

**Date:** 24 November 2026. **Proved:** core-vertex existence by applying published Mazur–Rubin theorems to the canonical elliptic Selmer structure under full residual image, and an exact, noncircular ideal-quotient lemma. **Not proved:** the corrected Kato I1 primitivity needed to conclude global Sha vanishing, or the exact complex rank-two BSD leading coefficient. No new calculation is proposed.

## A. Published theorem solves the core-vertex existence hypothesis, subject to canonical setup

Let E=389a1 and p>3 sufficiently large that \(\rho_{E,p}(G_{\mathbf Q})=\mathrm{GL}_2(\mathbf Z_p)\). Such a tail exists by non-CM and Serre open image (no effective cutoff claimed). Take \(T=T_p(E)\), \(A_m=E[p^m]\), \(\mathcal F_{\rm can}\) the canonical Selmer structure (full at p on T and ordinary unramified away from p, with induced finite-level conditions).

1. **Full image implies the standard Mazur–Rubin Galois hypotheses.** Mazur–Rubin, *Kolyvagin Systems*, Chapter 6.2, assumptions (30),(31) and Lemma 6.2.3, explicitly verify hypotheses (H.0)–(H.4) and local cartesian hypothesis (H.6) for \(E[p^m]\) and \(\mathcal F_{\rm can}\). Their choice of Kato/Kolyvagin auxiliary primes also supplies (H.5); see same section following the lemma. Their usual Chebotarev construction supplies a cofinal auxiliary set with arbitrarily deep level \(m\).

2. **Core Selmer rank is one, independently of MW rank.** Mazur–Rubin Proposition 6.2.2 explicitly says
\[
\chi(A_m,\mathcal F_{\rm can})=1
\]
for every m. This is not a claim that rank E(Q)=1: the ordinary self-dual Kummer structure has core Selmer rank zero, while the canonical structure is relaxed at p.

3. **Core vertices exist arbitrarily deep.** Mazur–Rubin Corollary 4.1.9(ii),(iii) shows the existence of core vertices with appropriately chosen p^m-admissible auxiliary primes, even divisible by any prescribed finite square-free set of admissible primes. Their Theorem 4.1.10 asserts that the modified primal and dual Selmer modules at such a core vertex are finite-level FREE over \(R_m=\mathbf Z/p^m\) and one side vanishes. Since canonical core rank equals one, the primal Selmer module is free of rank \(1+\nu(n)\), and the dual module is zero. These are precisely the two conclusions in Burns–Sakamoto–Sano II, Hypothesis 4.2 (for \(R_m\), rank r=1).

Therefore, **for all sufficiently large p and every m≥1**, BSS Hypothesis 4.2 for the ordinary canonical \(E[p^m]\)-structure follows from the published Mazur–Rubin theory. It does NOT need a computational Sha witness or an assumption that Sha(E/Q) is finite.

References:
- Mazur–Rubin, *Kolyvagin Systems* (AMS 2004), Corollary 4.1.9, Theorem 4.1.10, Proposition 6.2.2, Lemma 6.2.3, and the discussion following it.
- BSS II arXiv:1805.08448v1, Hypothesis 4.2 on page 20 (PDF page index 19), Corollary 6.15(ii) on page 42 (PDF page index 41). **Numbering alert:** the arXiv v1 is numbered 6.15(ii), while an archived version of our previous notes says Corollary 6.21(ii). Use the actual edition citation when quoting; the mathematical containment is the same.

**BSS Hypothesis 6.1(i) (torsion-free global H¹) for the pro-p abelian tower.** For any finite abelian p-extension F/Q, the image of \(G_F\) on E[p] is all GL₂(F_p): its quotient by this normal image is an abelian p-group, but the abelianization of GL₂(F_p) has order p−1 for p≥5. Thus E[p](F)=0. From \(0\to T\xrightarrow{p}T\to E[p]\to0\), global H¹(O_{F,S},T)[p] injects into H⁰(F,E[p])=0. This f.g. Z_p-module is consequently torsionfree, hence reflexive as required in the base-order case R=Z_p. Hypothesis 6.1(ii) follows from H⁰(F,T)=0. BSS's 6.7 and 6.11 are handled by the standard ray-class pro-p auxiliary tower and Frobenius eigenvalues of absolute value √q≠1. Formal application must use one consistent tower, finite local structures and Kato's chosen auxiliary integers c,d, and is not itself a proof that the resulting Kato system is primitive.

## B. The exact p-local index: saturation is NOT the issue, but its valuation can be >0

Define \(X_p=\mathrm{Sel}_{p^\infty}(E/\mathbf Q)^\vee\) and \(X_p^0\) the dual of the strict-at-p p-infinity Selmer. Rank E(Q)=2 and E(Q) torsionfree give
\[
X_p\simeq\mathbf Z_p^2\oplus Y_p,\qquad
Y_p=\Sha(E/\mathbf Q)[p^\infty]^\vee
\]
with Y_p finitely generated and not assumed finite.

The p-adic localisation of the rational MW subgroup into \(H_f^1(\mathbf Q_p,E[p^\infty])\simeq\mathbf Q_p/\mathbf Z_p\) is nonzero because a non-torsion rational point cannot have zero p-adic local elliptic logarithm (the local logarithm's kernel is torsion). It is thus surjective on divisible p-primary groups. Dualizing gives an exact sequence
\[
0\to\mathbf Z_p\xrightarrow{j_p}X_p\to X_p^0\to0.
\]
The image of j_p in the canonical MW dual quotient \(X_p\to\mathbf Z_p^2\) has coordinates \(a_p,b_p\), not both zero. Set
\[
\mathfrak l_p=(a_p,b_p)=p^{t_p}\mathbf Z_p,\quad t_p\ge0.
\]
This ideal depends **only on localisations of the known saturated MW basis P,Q**, not on Sha or a choice of splitting of X_p.

The rank-shift theorem proved in paper/bsd389_exact_local_Fitting_rank_shift_and_Kato_I1_route_2026-11-24.md yields
\[
\boxed{
\mathrm{Fitt}_{1,\mathbf Z_p}(X_p^0)=
\mathfrak l_p\,\mathrm{Fitt}_{2,\mathbf Z_p}(X_p).
}
\]
This remains valid if Sha[p∞] has infinite corank: both Fitting ideals then vanish.

## C. NEW uniform arithmetic criterion: divide the I1 ideal by its mandatory local factor

Suppose the published BSS containment is applicable to the *genuine* Kato-derived system \(\kappa_p\) with the appropriate canonical Selmer structure. The preceding source audit and local comparison then give
\[
I_1(\kappa_p)\subseteq
\mathrm{Fitt}_1(X_p^0)=\mathfrak l_p\mathrm{Fitt}_2(X_p).
\]
Define the **corrected ideal** by the ordinary ideal quotient in the DVR \(\mathbf Z_p\):
\[
\boxed{J_p:=(I_1(\kappa_p):\mathfrak l_p)
=\{x\in\mathbf Z_p:x\mathfrak l_p\subseteq I_1(\kappa_p)\}.}
\]
Because ideal quotients are monotone and
\[
(\mathfrak l_p\,\mathrm{Fitt}_2(X_p):\mathfrak l_p)
=\mathrm{Fitt}_2(X_p)
\]
for the nonzero principal ideal \(\mathfrak l_p\), we get a genuine **p-adic Selmer bound**
\[
\boxed{J_p\subseteq\mathrm{Fitt}_{2,\mathbf Z_p}(X_p)
=\mathrm{Fitt}_0(Y_p).}
\]
This is noncircular and does not assume global Sha finiteness.

A **unit in J_p** is equivalent to \(\mathfrak l_p\subseteq I_1(\kappa_p)\), or \(p^{t_p}\in I_1(\kappa_p)\). It forces \(\mathrm{Fitt}_2(X_p)=\mathbf Z_p\) and hence Sha[p∞]=0. This is **strictly weaker in general** than demanding \(I_1(\kappa_p)=\mathbf Z_p\).

More generally, if for all sufficiently large p one shows
\[
\boxed{p^{t_p}D\in I_1(\kappa_p)}
\]
for a **single nonzero integer D independent of p**, then \(D\in J_p\) for every such p, and \((D)\subseteq\mathrm{Fitt}_2(X_p)\). Once the finitely many remaining primes are handled and all prime divisors of D lie in a certified Sha-zero set, the established global integer proof cut implies **Sha(E/Q)=0**.

**The difficult unproved uniform assertion is the corrected nonvanishing/primitivity of I1(Kato)**. The published existence of an abstract primitive Kolyvagin system cannot establish the primitivity of the **specific Kato-derived** system.

## D. Why an uncorrected p-unit target would be unnecessarily restrictive

Take an idealized but exact possible Selmer algebra with
\[
X_p=\mathbf Z_p^2,\quad Y_p=0,\quad
j_p(1)=(p,0).
\]
Then \(\Sha[p^\infty]=0\) but \(X_p^0\simeq\mathbf Z_p\oplus\mathbf Z/p\), and
\[
\mathrm{Fitt}_1(X_p^0)=(p).
\]
Hence **every** Kato-derived \(I_1\subseteq\mathrm{Fitt}_1(X_p^0)\) is divisible by p and can never be a unit, even though Sha vanishes! The *corrected* ideal J_p may still be a unit. This algebraic observation explains why insisting on \(I_1=\mathbf Z_p\) for every large p can be much stronger than BSD: it additionally excludes every prime with nonprimitive MW localisation.

## E. Decision gate

The source-theoretic core-vertex obstacle is now settled for the sufficiently-large-p GL₂ tail; the local Fitting rank shift and ideal quotient correction are proved; no more finite-field or Mazur–Tate Smith experiments are justified.

**Only serious remaining uniform arithmetic task** for the global Sha-part: show \(J_p=\mathbf Z_p\) for every large p, or construct a fixed D with \(D\in J_p\) for each p, **for the genuinely normalized Kato-derived system**, with complete hypotheses and genuine local-condition transfer. Even doing this would **not** prove the separate exact complex rank-two BSD leading term.

The actual uniform corrected primitivity result is NOT present in BSS, Mazur–Rubin, Kato, or our repository. Do not label it PASS.


## CORRECTION DATED 2026-11-24 — Castella–Sano and Kim close the primitive-index step, not rank-two Sha

The earlier research suggestion to prove nonvanishing of the *entire Kato Kolyvagin system* or to construct a brand-new explicit reciprocity bridge is outdated. See the independent full statement and source audit in [bsd389_2026_Castella_Sano_Kim_uniform_Kato_index_and_exact_two_prime_Sha_criterion.md](bsd389_2026_Castella_Sano_Kim_uniform_Kato_index_and_exact_two_prime_Sha_criterion.md).

**What is now THEOREM for all sufficiently large p of E=389a1:**
- Castella–Sano 2026 Theorem B: the actual global Kurihara family has minimum p-valuation zero, \(\partial_p^{(\infty)}=v_p(\mathrm{Tam}_E)=0\), as N=389 squarefree and p has good ordinary or supersingular reduction. This supplies a Kurihara unit at **some** even number of prime factors.
- Their Theorem 2.1.3 is the **existing genuine explicit reciprocity bridge** between Kato's actual derived Galois classes and the numerical Kurihara coefficients (with the local torsion factor). The earlier statement that such a bridge needed to be invented is too strong and must not be used.
- Their equations (2.16),(2.17) give \(\mathcal M_\infty(\kappa^{\rm Kato})=v_p(\#E(\mathbf Q_p)[p^\infty])\), at most 1 for good p≥7. Conversion from their classical Kolyvagin-system divisibility to the BSS generator scalar \(a_p\) needs normalization comparison, so **do not assert \(v_p(a_p)\) from the source without that check**.
- Chan-Ho Kim Theorem 1.8 gives Selmer corank exactly \(\rho_p=\min\{\nu(n):\delta_n\neq0\}\) and the Fitting ideals from the minimum valuations at each number of prime factors. For E(Q) rank2 and Tamagawa product1, this proves the exact equivalence
\[
\boxed{\Sha(E/\mathbf Q)[p^\infty]=0
\iff\exists\,n=q_1q_2\text{ with }\delta_n\ne0\bmod p.}
\]
This is a theorem **equivalence**, not a proof the right-hand side holds for all p.

**Scope correction:** the full-Kato index and global some-factor nonvanishing are settled (for p in the large good tail); the **first nonzero factor count \(\rho_p=2\)** is the genuine remaining Sha obstruction. An arbitrary-factor Kato primitive system does not force I1(strict) to have the specific index required to kill Sha, and the two-factor problem is as hard as the rank-two Sha assertion itself. These theorems say nothing about the separate exact complex BSD leading-term equality.
