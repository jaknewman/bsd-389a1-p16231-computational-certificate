# 389a1 — A rank-r, arbitrary-depth jet-to-Sha theorem; rigorous proof + falsification of a tempting local-only hypothesis

**24 November 2026.** This note answers the methodological question "Can we formulate a new mathematical proposition, test it against genuine arithmetic, and certify or reject it?" The answer is **YES** at the finite-prime level. The rank-r lemma below is proved algebraically; its application to 389a1 at p=5 uses true independently computed theta coefficients and the published Bullach–Honnor Fitting theorem. The theorem does **not** establish uniform existence of such theta jets for every sufficiently large p, global Sha finiteness, or the exact complex BSD leading term. We do not claim literature-level originality without a priority search.

## I. Hypothesis to FALSIFY: local independence alone forces a unit Kurihara derivative

A tempting "rank-two reciprocity" guess was
\[
(H_{\rm local})\quad
\operatorname{rank}_{\mathbf F_p}
\operatorname{im}\!\left(E(\mathbf Q)/p\to
 E(\mathbf F_{q_1})/p\oplus E(\mathbf F_{q_2})/p\right)=2
\Longrightarrow \widetilde\delta_{q_1q_2}\not\equiv0\bmod p.
\]

**COUNTEREXAMPLE FROM AUTHENTIC DATA**: E=389a1, p=5, q1=5351, q2=13001, both good primes with q_i≡1 mod25 and a_{q_i}≡2 mod25. The previously independently audited finite-field arithmetic gives
- E(F5351)/5 is one-dimensional and \(\bar Q=-\bar P\);
- E(F13001)/5 is two-dimensional and \(\bar Q=2\bar P\);
- choosing a nonzero projection of E(F13001)/5 on the line occupied by \(\bar P\), the two MW localization rows are (1,-1) and (1,2), whose determinant is 3 mod5, a unit; the full two-prime local MW image has dimension 2;
- the **genuine weighted 34,775,000-class modular-symbol computation** gives \(\widetilde\delta_{5351\cdot13001}\equiv15\bmod25\), and so \(\delta\bmod5=0\).

Therefore (H_local) is **FALSE**. Caveat: at 13001 the local F5 dimension is 2. This example does NOT falsify the narrower hypothesis that *both individual finite local quotients have dimension exactly one*. It emphatically falsifies the general local-rank-only assertion as stated here.

This concrete failed test tells us any valid bridge must incorporate a *global Kato/Mazur–Tate coefficient*; Chebotarev and the MW local determinant alone are insufficient.

## II. New rank-r jet-to-Sha bound — precise conditional THEOREM

Fix p odd, integer k≥1, and rank r with \(1\le r<p\). Let E/Q be an elliptic curve with E(Q)[p]=0 and MW rank r. Let K/Q be a cyclic Galois extension of degree m=p^k such that E[p](K)=0. Let
\[
R=\mathbf Z_p[G]\simeq\mathbf Z_p[T]/((1+T)^{p^k}-1),\quad
\mathfrak m=(p,T),\quad
X=\operatorname{Sel}_{p^\infty}(E/K)^\vee.
\]
Suppose there exists a **genuine arithmetic** element \(\Theta\in R\), represented by an integral polynomial \(\Theta(T)=\sum_{j\ge0}c_jT^j\), for which:
1. **Fitting hypothesis**: \(\Theta\in\operatorname{Fitt}_{0,R}(X)\), e.g. by an independently applicable published Mazur–Tate/Selmer theorem, not by numerical agreement;
2. **rank-r low jets**: \(c_j\in p^k\mathbf Z_p\) for \(0\le j<r\);
3. **first visible jet**: \(v_p(c_r)=s<k\).

**THEOREM (rank-r quantitative jet criterion).** Under (1)–(3), without any Sha-finiteness hypothesis,
\[
\boxed{\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]\le s.}
\]
For E/Q, if the established p-parity theorem and the Cassels–Tate alternating pairing apply at odd p, the dimension is even; consequently
\[
\boxed{\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]\le 2\lfloor s/2\rfloor.}
\]
In particular **s=0 or 1 implies \(\Sha(E/\mathbf Q)[p^\infty]=0\)**.

**Proof.**

(A) Form the finite quotient algebra
\[
B_s=(\mathbf Z/p^{s+1}\mathbf Z)[T]/(T^{r+1}).
\]
Because r<p, the binomial coefficients \(\binom{p^k}{j}\) are divisible by p^k for every 1≤j≤r. Hence the relation \((1+T)^{p^k}-1\) maps to zero in B_s: there is a **well-defined surjective local-ring homomorphism** \(R\twoheadrightarrow B_s\).

(B) Conditions (2),(3) give \(\Theta\mapsto (p^s u)T^r\ne0\) in B_s for a p-unit u. Every monomial \(p^aT^b\) of total degree at least r+s+1 vanishes in B_s: either a≥s+1 or b≥r+1. Thus \(\mathfrak m^{r+s+1}B_s=0\), and
\[
\boxed{\Theta\notin\mathfrak m^{r+s+1}.}
\]

(C) Let d be the minimal number of R-generators of X. Since R is complete local Noetherian, a minimal finite presentation \(R^N\to R^d\to X\to0\) has all its matrix entries in \(\mathfrak m\). Therefore its d×d minors lie in \(\mathfrak m^d\); i.e.
\[
\operatorname{Fitt}_{0,R}(X)\subseteq\mathfrak m^d.
\]
If \(d\ge r+s+1\), hypothesis (1) would imply \(\Theta\in\mathfrak m^{r+s+1}\), contradiction. Hence \(d\le r+s\).

(D) Since E[p](K)=0, inflation–restriction injects \(H^1(\mathbf Q,E[p])\hookrightarrow H^1(K,E[p])\). Restriction preserves Kummer local conditions, and E[p](K)=0 ensures \(\mathrm{Sel}_p(E/K)\simeq\mathrm{Sel}_{p^\infty}(E/K)[p]\). Therefore
\[
\mathrm{Sel}_p(E/\mathbf Q)\hookrightarrow
\mathrm{Sel}_{p^\infty}(E/K)[p]^G.
\]
Pontryagin duality and Nakayama give
\[
\dim_{\mathbf F_p}\mathrm{Sel}_{p^\infty}(E/K)[p]^G
=\dim_{\mathbf F_p}(X/\mathfrak m X)=d.
\]
The base Kummer sequence, E(Q)[p]=0 and rank r give
\[
\dim_{\mathbf F_p}\mathrm{Sel}_p(E/\mathbf Q)
=r+\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p].
\]
Combining yields \(r+\dim\Sha[p]\le d\le r+s\), proving the bound. Neither global nor K-primary Sha finiteness has been assumed. QED.

(E) The parity refinement uses the p-parity theorem and perfect alternating Cassels–Tate pairing on the finite reduced p-primary quotient. For an odd prime over Q, the p-primary Sha's corank is even when analytic rank and MW rank have the same parity; for E389a1 both are 2. The p-rank of its finite reduced part is even by the alternating pairing. Thus dim Sha[p] is even for our application, giving the displayed parity sharpened inequality. (In the general-r theorem, assert the parity refinement only when the stated parity input is independently verified.)

This theorem GENERALIZES the earlier project-specific r=2 depth-p² gate to **arbitrary rank r<p and depth p^k**. It is a general algebraic criterion with explicitly testable hypotheses, not an unconditional theorem of full BSD or a new proof that suitable q1,q2 always exist.

## III. Run the theorem on the genuine existing rank-two p=5 example — PASS

The genuine Mazur–Tate histogram for the r_character=1 diagonal cyclic degree-25 field K at conductor n=5351×13001 was computed independently in two implementations:
\[
(a_0,\ldots,a_{24})=(-424,9536,-424,3388,5172,-8022,-2658,-1240,-9294,-1588,-1580,-1512,9782,3208,3208,9782,-1512,-1580,-1588,-9294,-1240,-2658,-8022,5172,3388).
\]
Set F(X)=Σa_j X^j, \(\Theta(T)=F(1+T)\). Direct exact integer arithmetic yields
\[
c_0=\sum a_j=0,\quad
c_1=\sum ja_j=-108600\equiv0\bmod25,\quad
c_2=\sum\binom j2a_j=-993960\equiv15\bmod25.
\]
Therefore k=2, r=2, s=1, and in the exact quotient
\[
R\to(\mathbf Z/25)[T]/(T^3),\qquad
\Theta\longmapsto15T^2\ne0.
\]
The curve is semistable, p=5 has independently recorded full residual image, K is abelian of degree25 so E[5](K)=0, and \(\mu_5\not\subset K\) since [K:Q] is odd. Hence the main published Bullach–Honnor Theorem 1.4(b) is applicable to this genuine K and the correctly normalized Mazur–Tate \(\Theta\) (note the # involution is harmless for semistable E by their Remark 1.5(a)).

Our theorem gives
\[
\dim_{\mathbf F_5}\Sha(E/\mathbf Q)[5]\le1.
\]
The established p-parity gives an even dimension; therefore
\[
\boxed{\Sha(E/\mathbf Q)[5^\infty]=0.}
\]
The result is a **mathematical consequence of the actual historical arithmetic certificate**, not a new global p-tail bound. A quick independent computation verifying the three integer coefficients is included in the companion lightweight script. It is NOT a replacement for the authenticated 34,775,000-class source run or proof of the published Selmer-Fitting theorem.

For the separate genuine p5 conductor 5351×10651, the archived two-prime derivative is 22 mod25, a p-unit: this is the s=0 case; at p=11 the archived q397×991 Kurihara number is 1 mod11, also s=0 at depth k=1, subject in each case to verification of the exact low-jet/Fitting prerequisites.

## IV. The genuine NEW research hypothesis to test, without tautology

**Hypothesis H2 (all-large-p rank-two quadratic jet existence).** For E389a1 there is a bound B such that for every prime p>B there exists a cyclic real degree-p² extension K/Q generated by a two-factor deep Mazur–Tate conductor, satisfying the *independently checkable* low-jet/Fitting conditions of Theorem II with
\[
\boxed{v_p(c_2(\Theta_K))\le1.}
\]
The proven theorem and parity would imply Sha(E/Q)[p^\infty]=0 for all p>B.

Tests with genuinely archived data:
- p=5, q=(5351,13001), k=2, c2 mod25=15 (v=1): **H2 instance PASS**.
- p=5, q=(5351,10651), k=2, \(\delta=22\bmod25\) (v=0): **second H2 instance PASS**, conditional on correct theta coefficient normalization.
- p=11, q=(397,991), k=1, δ≡1 mod11: **rank-two depth-one criterion PASS**, but this does **NOT** test H2 at p² depth.
- Unbounded large-p claim: **UNTESTED AND UNPROVED**. It must not be announced merely because Chebotarev supplies the auxiliary primes.

**Critical limitation:** With Kim/CS structural theorems, H2 is at least as strong as the unresolved all-large-p Sha-vanishing conclusion; it is a concrete *testable route*, not yet an independently proved simplification of difficulty. The mathematically valid new contribution here is the general rank-r jet-to-Sha inequality plus its authenticated rank-two example and falsification of an overstrong local-only hypothesis.

## V. What would count as progress next (and what would not)

A potentially independent route is a theorem about p²-depth quadratic coefficients derived from an actual *global* rank-two Kato/Bockstein regulator map, valid uniformly for p and *not* assuming Sha finiteness or the BSD leading-term formula. It must imply a bound on the first nonzero jet, not just the existence of auxiliary primes. Such a comparison has **not** yet been proved and is not implied by the local MW determinant (counterexample I).

No further 34M-class scan, twenty-field Smith audit, or extrapolation from the two current p=5 examples can prove H2. A serious attempt must derive the global coefficient bound theoretically, and validate every normalization at the level of genuine arithmetic classes.

Sources: Bullach–Honnor, *On the refined 'Birch–Swinnerton-Dyer type' conjectures of Mazur and Tate*, Theorem 1.4(b), Remark 1.5(a), https://arxiv.org/pdf/2511.07203; Mazur–Rubin/Kummer restriction and p-parity; the archived authentic project modular-symbol arithmetic cited in prior notes.
