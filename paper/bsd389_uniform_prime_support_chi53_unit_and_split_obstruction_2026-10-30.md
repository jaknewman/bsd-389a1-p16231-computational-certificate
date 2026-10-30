# Toward a uniform prime-support bound for Sha(389a1/Q) — exact finite-factor result and remaining bridge

**Date:** 2026-10-30. **Status:** two **rigorous uniform algebraic statements** and one **separate explicitly unproved Selmer-control objective**. This document does NOT claim a global exceptional-prime bound for Sha, Sha finiteness or complete BSD. The progress is in isolating a nonzero fixed algebraic factor, removing its prime-support uncertainty, and demonstrating why split-prime-only techniques cannot provide an all-prime bound from finitely many fixed imaginary quadratic fields.

## 1. The precise uniform target (all p at once)

Let E/Q: y²+y=x³+x²−2x = 389a1, of proven rank two and trivial rational torsion, with a full certified Mordell–Weil basis. For EVERY prime p, its Kummer sequence gives
\[
0\longrightarrow E(\mathbf Q)/pE(\mathbf Q)
\longrightarrow \operatorname{Sel}_p(E/\mathbf Q)
\longrightarrow \Sha(E/\mathbf Q)[p]\longrightarrow0.
\]
Since E(Q)/pE(Q) is F_p²,
\[
\dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)
 =2+\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p].
\]

**Uniform-support criterion (elementary implication):** If one constructs an integer C ≠ 0, a finite set S of primes, and a valid proof for **every** p outside S that
\[
\dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)>2
\quad\Longrightarrow\quad p\mid C,
\]
then
\[
\operatorname{Supp}\Sha(E/\mathbf Q)\subseteq
S\cup\{\text{prime divisors of }C\}.
\]
Every nonzero p-primary torsion group has an element of order p, hence ruling out Sha[p] rules out ALL Sha[p∞]. However **finite prime support does not by itself prove Sha finite**: one must also bound/exclude each remaining p-primary component (for example, Q_p/Z_p is an infinite group supported only at p).

The outstanding mathematical task is the *uniform Selmer implication*, NOT the integer factoring step. Uniform residual Galois surjectivity outside an explicit exceptional set does NOT supply it.

## 2. A fixed factor from the archived K=Q(sqrt(-3)) character of conductor 53

The project archived an ordered 18-class Brandt/Gross orbit with coefficients
\[
(c_0,\ldots,c_{17})=
(0,0,-1,0,0,-1,-1,2,2,-1,-1,2,2,-1,-1,0,0,-1).
\]
Define \(F(X)=\sum_{j=0}^{17}c_jX^j\) and \(\zeta=\zeta_9\). Modulo the monic cyclotomic polynomial \(\Phi_9(X)=X^6+X^3+1\) one has the **exact integral identity**
\[
F(X)\equiv -3X^5-3X^4+3X^3-3X
        \equiv -3X(X^4+X^3-X^2+1)\pmod{\Phi_9(X)}.
\]
Put \(U=X^4+X^3-X^2+1\), \(V=X^4-X^3-1\). Direct polynomial multiplication and reduction prove \(UV\equiv1\pmod{\Phi_9(X)}\). Thus \(u=U(\zeta)\in\mathbf Z[\zeta]^\times\) with inverse \(V(\zeta)\), and
\[
F(\zeta)=-3\zeta u,\qquad
N_{\mathbf Q(\zeta)/\mathbf Q}(F(\zeta))
=(-3)^6 N(\zeta)N(u)=3^6=729.
\]
The same norm is obtained independently by the *exact Bareiss determinant* of the 6×6 integer matrix for multiplication by \(F(\zeta)\) in the basis \(1,\zeta,\ldots,\zeta^5\).

**Uniform algebraic conclusion (PROVED from the archived coefficient vector):** For EVERY rational prime \(p\ne3\), \(F(\zeta)\) is a unit in
\(\mathbf Z[\zeta]\otimes\mathbf Z_p\). Its ideal has no prime factors over any p other than 3. The only rational prime divisor of its norm is 3.

Independent standard-library-only code:
[verification/bsd389_uniform_chi53_toric_unit.py](../verification/bsd389_uniform_chi53_toric_unit.py). Executed locally and produced:
```text
UNIFORM_CHI53_EXACT_CYCLOTOMIC_FACTOR_PASS F=-3*zeta9*U
UNIFORM_CHI53_EXPLICIT_INVERSE_PASS U*UINV=1
UNIFORM_CHI53_NORM_DETERMINANT_PASS 729
UNIFORM_CHI53_P_UNIT_ALL_PRIMES_EXCEPT_3_MATHEMATICAL_PASS
SPLITTING_SCOPE chi53_K_minus3 only applies to p congruent 1 modulo 3
BOUNDARY_NO_SHA_UNIFORM_FINITE_SUPPORT_PROOF; theta_order2_and_integral_primitivity_not_proved
```

**Precise nonclaim:** F(ζ) is an *archived finite Gross-orbit algebraic factor*, not a proven universal index of Sha or Selmer. Its identification with a normalized adelic toric period still uses the separate optimal-embedding, Jacquet–Langlands and test-vector conventions, as noted in [the source chi53 script](../verification/bsd389_chi53_order9_from_archive.py). More importantly, neither nonvanishing of the formal toric period nor even nonvanishing of a generalized Kato class automatically forces **integral p-primitivity** or Sha[p]=0. Therefore we **CANNOT put C=729 in the preceding uniform Selmer criterion** without a new integral comparison theorem. The derived ideal bound concerns only this toric factor.

## 3. Exact no-go lemma: finitely many fixed imaginary quadratic fields cannot cover every p in split-only methods

Take ANY finite family of imaginary quadratic fields \(K_i\) with negative fundamental discriminants \(D_i\), and let \(M=\mathrm{lcm}(|D_1|,\ldots,|D_m|)\). For every prime p ≡ −1 mod M, prime to M, the associated primitive quadratic character satisfies
\[
\chi_{D_i}(p)=\chi_{D_i}(-1)=-1
\]
because \(D_i<0\). Hence **p is inert in every K_i**. By Dirichlet's theorem, the class \(-1\bmod M\) contains infinitely many primes. Consequently NO FINITE SET of fixed imaginary quadratic fields can cover all but finitely many rational primes using the requirement “p splits in one of these fields”.

This is a strict mathematical obstruction for strategies that apply only a split-p anticyclotomic theorem (such as Castella–Hsieh’s setup at the fixed K). It does NOT rule out:
- allowing K to vary with p;
- an inert/supersingular theorem that works without the splitting hypothesis;
- a wholly different global integral Euler system or Selmer-comparison method.

For the current fixed K=Q(sqrt(-3)), p>3 splits iff p≡1 mod 3. Thus 16231 is split, while 107 and 599 are inert. The proven chi53 unit-factor statement is algebraic for all p≠3 but the **selected split-p anticyclotomic theorem** only applies in its split cases; do not mix these two ranges.

Primary source for the splitting hypothesis: Castella–Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, [Cambridge, §2.2 / Theorem 2.3](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864).

## 3 bis. A second uniform obstruction: no fixed list of Kurihara auxiliary conductors covers all primes

Our existing rank-two Kurihara certificates rely on **p-admissible auxiliary primes** \(q_1,q_2\), which satisfy at least \(q_i\equiv1\pmod p\), as well as \(a_{q_i}(E)\equiv q_i+1\pmod p\).

**Elementary exact lemma.** Fix a squarefree auxiliary conductor \(n=q_1\cdots q_r\), with \(r\ge1\). If n is admissible for a prime p under these conditions then
\[
 p\mid q_i-1\quad\text{for every }i,\qquad
 p\mid d_n:=\gcd(q_1-1,\ldots,q_r-1).
\]
Since \(d_n\) is a fixed nonzero integer, a **single fixed n** can serve only **finitely many** p. Any **finite list of fixed n** can serve only a finite union of such prime divisors. This is independent of the curve's Fourier coefficients: the \(q\equiv1\pmod p\) prerequisite alone suffices.

Our exact previously used examples illustrate this stronger obstruction:

| Fixed auxiliary pair \((q_1,q_2)\) | Exact gcd \(d_n\) | Eligible \(p\ge5\) from congruences alone |
|---|---:|---|
| (41,61) | \(20=2^2\cdot5\) | \(5\) |
| (113,673) | \(112=2^4\cdot7\) | \(7\) |
| (369793,383917) | \(1284=2^2\cdot3\cdot107\) | \(107\) |

**Result:** Keeping a finite suite of previously computed Kurihara conductors cannot by itself replace all remaining p-specific calculations by a uniform argument. To use Kurihara–Kim uniformly, the auxiliary conductor \(n(p)\) must **vary with p**, and one must obtain an effective *uniform nonvanishing/primitivity theorem* that applies to those varying conductors. The existence of a nonzero witness at selected p=5,7,107 is not such a theorem.

**Interaction with the previous section:** both the split-p anticyclotomic approach (requiring varying imaginary K or a new inert-prime theorem) and the Kurihara auxiliary-prime approach (requiring varying n) have an explicit reason why finitely many frozen local tests cannot settle infinitely many p. This does **not** make all-prime support impossible: it identifies the exact quantifier switch our next proof must supply.

### Independent execution record

The script for the preceding exact chi53 norm theorem has now also been run **successfully by the user on Ubuntu**, in addition to the original local independent run; see [verbatim PASS transcript](../results/chi53_uniform_toric_norm729_USER_SAGE_PASS_2026-10-30.md). This strengthens its computational provenance but changes none of the separate Selmer implications still to be proved.

---

## 3 ter. Positive uniform theorem: infinitely many admissible auxiliary primes at every surjective p

The previous lemma rules out a **fixed** finite set of auxiliary conductors. It does not say we cannot find auxiliary primes for an arbitrary p. In fact we can **prove their existence uniformly**, using only mod-p surjectivity and Chebotarev:

**Theorem (exact, conditional only on residual surjectivity at the chosen p).** Let \(p\ge5\) be a rational prime such that
\[
\bar\rho_{E,p}:G_{\mathbf Q}\twoheadrightarrow \operatorname{GL}_2(\mathbf F_p)
\]
is surjective. Then the set of good primes \(q\ne p\) with
\[
q\equiv1\pmod p,\quad a_q(E)\equiv q+1\pmod p,\quad
\dim_{\mathbf F_p}E(\mathbf F_q)[p]=1
\]
has natural density **at least** \(1/(p(p-1))\), and the subset with **nontrivial unipotent Frobenius** has density **exactly** \(1/(p(p-1))\). In particular it contains infinitely many primes, and it is always possible to choose two or more distinct such q for this p.

**Proof.** Choose the conjugacy class \(C\) of
\[
U=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\in\mathrm{GL}_2(\mathbf F_p).
\]
Its centralizer consists exactly of invertible matrices
\(\begin{psmallmatrix}a&b\\0&a\end{psmallmatrix}\), with \(a\in\mathbf F_p^\times\) and \(b\in\mathbf F_p\); it has \(p(p-1)\) elements. Since
\(|\mathrm{GL}_2(\mathbf F_p)|=(p^2-1)(p^2-p)\), the class C has \(p^2-1\) elements. Chebotarev applied to \(\mathbf Q(E[p])/\mathbf Q\) gives primes q whose Frobenius class equals C with natural density
\[
\frac{|C|}{|\mathrm{GL}_2(\mathbf F_p)|}
=\frac1{p(p-1)}>0.
\]
For every such q, the Weil pairing/determinant identity yields
\(\det\bar\rho(\operatorname{Frob}_q)\equiv q\equiv1\bmod p\);
the trace identity yields \(a_q(E)\equiv\operatorname{tr}(U)=2\equiv q+1\bmod p\).
Finally, the reduction's p-torsion is the fixed subspace
\(\ker(U-I)\), of dimension exactly one because \(U\) is nontrivial unipotent. QED.

**Precise scope:** This proves basic **mod-p auxiliary-prime admissibility**, including cyclic p-torsion. More stringent p^n-level congruences or additional local conditions in a particular version of Kim/Kolyvagin's theorem would need separate checking in a higher torsion field. The historical uniform residual-surjectivity claim for 389a1 must be accepted with its own validated finite-exception list; the Chebotarev theorem does **not** certify that claim itself.

**Crucial frontier:** Even infinitely many *admissible* q for each p do NOT imply a **nonzero Kurihara number** \(\widetilde\delta_{q_1q_2}\). The precise sought all-p theorem is of the form:
\[
\forall p\notin S,\quad
\exists q_1(p)\ne q_2(p)\text{ satisfying admissibility and }
\widetilde\delta_{q_1(p)q_2(p)}\not\equiv0\bmod p,
\]
or else a genuinely different integral Selmer criterion. Nothing in Chebotarev, by itself, proves this nonvanishing.

Reference for exact conjugacy-class density: [Chebotarev theorem, H. W. Lenstra, Theorem 3.1](https://websites.math.leidenuniv.nl/algebra/Lenstra-Chebotarev.pdf). The finite-group centralizer computation above is self-contained.

---

## 4. New sharp bottleneck and suggested next proof target

We now have a fixed p-adic unit toric factor for **all p ≠ 3**. What we do **not** have is a p-uniform injection or a p-integral identity relating \(\Sha(E)[p]\) to this factor. More precisely:

- A *rank-two rational Selmer corank criterion* (\(\dim_{\mathbf Q_p}\operatorname{Sel}(\mathbf Q,V_pE)=2\)) only proves that the p-primary Sha has no **divisible** part, not that Sha[p] vanishes. Integral primitivity is essential for uniform Sha triviality.
- The remaining anticyclotomic \(\mathrm{ord}_T\Theta_{f/K}=2\) is a p-dependent derivative condition, **not** established by the fixed toric value \(F(\zeta)\ne0\). The two must never be conflated.
- The cyclotomic p-adic regulator and leading p-adic L-series coefficient also depend on p. Individual exact unit computations at 107, 599 and 16231 are valuable local results but do not imply the existence of a common nonzero integer controlling all their exceptional primes.
- A natural sufficient new theorem would construct a single fixed finite integral comparison object (or nonzero determinant C) with a **uniformly valid** arithmetic implication “Sha(E)[p] ≠ 0 ⇒ p | C”, outside a proved finite local-exception set. Only **after** such an implication is established can C be factored and the remaining p cases checked individually.

A September 2026 discussion of rank-two CM curves asks essentially for a fixed algebraic number controlling the bad p for a p-dependent second derivative: [Banwait, arXiv:2609.08431](https://arxiv.org/abs/2609.08431). That paper concerns **CM** curves. Our curve is **non-CM**: \(j(E)=112^3/389=1404928/389\notin\mathbf Z\), whereas a rational CM j-invariant must be an algebraic integer. Its CM-specific theorems cannot simply be applied to E389a1.

**Next mathematical checkpoint:** seek a genuinely *integral, p-uniform* Selmer/derived-theta comparison theorem. Specify a candidate comparison map, its domain, integral normalization, target and independent-of-p determinant; audit it before any further all-prime assertion. A finite collection of p-primary PASS logs, even thousands, does not establish that comparison.

## 5. Results ledger

| Statement | Status |
|---|---|
| Finite Gross-orbit algebra \(F(\zeta)=-3\zeta u\), \(\operatorname{Norm}=729\) | **EXACT PASS** |
| \(F(\zeta)\) is p-adic unit for every p≠3 | **PROVED for this algebraic factor** |
| Every finite family of fixed imaginary K misses infinitely many primes in split-only theories | **PROVED** |
| Genuine adelic toric period identification and integral p-normalization globally | **REQUIRES REVIEW** |
| \(\operatorname{ord}_T\Theta_{f/K}=2\) uniformly in p | **NOT PROVED** |
| Fixed toric factor yields \(\Sha(E)[p]=0\) uniformly | **NO VALID IMPLICATION PRESENTLY** |
| A single global finite exceptional-prime set for Sha | **NOT PROVED** |
| Finiteness of the full Sha group / all-prime BSD | **NOT PROVED** |

This note is deliberately more restrictive than a hopeful conditional theorem: all proven universal assertions concern the fixed algebraic factor and splitting obstruction, not Sha.
