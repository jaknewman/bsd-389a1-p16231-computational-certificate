# E389a1 — exact obstruction to prime-factor pruning; unconditional Chebotarev slope densities; a new modular-symbol spectral sieve proof target

**2026-11-25. Research statuses:** THEOREM A is a *rigorously deduced specialization of published Kim + Castella–Sano*, not an original proof of Sha=0. THEOREM B is a PROVED exact, quantitative Kummer–Chebotarev calculation valid uniformly for all p in the full-image range. THEOREM C is a PROVED finite Fourier/character inequality spelling out a stronger, independently testable sufficient route to two-factor nonvanishing. The required THIN-PRIME MODULAR-SYMBOL cancellation in Theorem C is NOT PROVED by existing equidistribution papers. No uniform p-tail Sha or exact complex BSD result is claimed.

## A. Exact prime-factor pruning obstruction — NO naive Chebotarev shortcut

Fix E/Q=389a1, with r=rank E(Q)=2, Tamagawa product 1, no E(Q)[p], and conductor 389. For every sufficiently large good p, Mazur's full image and the Manin unit hypotheses hold, so Chan-Ho Kim, *Structure of Selmer groups and the Iwasawa main conjecture*, Theorem 1.8, applies. Castella–Sano 2026 Theorem B establishes the refined Kurihara minimum valuation \(\partial^{(\infty)}(\widetilde\delta)=v_p(\operatorname{Tam}_E)=0\); in particular the mod-p unit witnesses exist at SOME number of prime factors.

Define
\[
m_p:=\min\{\nu(n):\widetilde\delta_n\not\equiv0\bmod p,\ n\ \text{squarefree product of p-admissible Kolyvagin primes}\}.
\]
All derivatives in this minimum are true *complete* Hecke-normalised modular-symbol weighted sums, not truncated computations.

**THEOREM A (deduced from Kim+Castella–Sano):**
\[
\boxed{m_p=\dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)
=2+\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p].}
\tag{A1}
\]
It holds with NO initial finiteness assumption for Sha and explicitly allows an infinite divisible p-part. The p-primary Sha is cofinitely generated and its finite reduced quotient has even p-rank (Cassels–Tate), while its divisible corank is even by p-parity. Hence \(m_p\in\{2,4,6,\ldots\}\).

**Proof.** Set \(X=\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee\), a finitely generated Zp-module, and \(d=\dim_{\mathbf F_p}X/pX=\dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)\) by the base p-Kummer exact sequence (both dimensions equal \(2+\dim\Sha[p]\)). By Kim Theorem 1.8, let \(c=\operatorname{rk}_{\mathbf Z_p}X=\operatorname{ord}(\widetilde\delta)\), and for i≥c of the correct parity,
\[
\operatorname{Fitt}_{i,\mathbf Z_p}(X)
=p^{\partial^{(i)}(\widetilde\delta)-\partial^{(\infty)}(\widetilde\delta)}\mathbf Z_p.
\]
By Castella–Sano \(\partial^{(\infty)}=0\). Over the PID Zp, the smallest i for which \(\operatorname{Fitt}_i(X)=\mathbf Z_p\) is precisely the minimal number \(d\) of Zp-generators of X, i.e. \(d=\dim X/pX\). Since \(d\equiv c\pmod 2\), Kim's formula applies to i=d. Thus the smallest i where \(\partial^{(i)}=0\), equivalently there exists a p-unit δ with exactly i factors, is \(m_p=d\). Values i<c have zero Fitting ideal, while all indices of wrong parity have zero derivatives by functional equation, so there are no smaller witnesses. This proves (A1). QED.

**CRITICAL CONSEQUENCE:** A universal rule allowing one to start with the Castella–Sano witness of arbitrary factor count and DELETE 2 factors without losing p-unit nonvanishing would force \(m_p=2\), hence precisely Sha(E/Q)[p]=0. Such a pruning rule requires a NEW arithmetic theorem and is not supplied by Chebotarev, the all-factor nonvanishing theorem, Hecke recursions, or the local MW determinant.

## B. The actual number of MW-independent two-prime choices: EXACT positive-density theorem

Fix p≥11 of good reduction with full mod p² image \(\rho_{E,p^2}(G_{\mathbf Q})=\mathrm{GL}_2(\mathbf Z/p^2)\), and let P=(-1,1), Q=(0,-1) be a saturated MW basis. Write \(F_2=\mathbf Q(E[p^2])\), \(V=E[p]\).

**Lemma (joint Kummer Galois surjectivity over F2).** The Galois extension \(F_2(p^{-1}P,p^{-1}Q)/F_2\) has group \(V^2\).

**Proof.** The image H⊂V² is GL2(Fp)-stable. Because V is absolutely irreducible and End_GL2(V)=Fp, any proper G-stable submodule of the semisimple module V² is annihilated by a nonzero equivariant combination (a,b):V²→V. Hence the Kummer class of aP+bQ restricts to zero on G_F2. But \(H^1(\mathrm{GL}_2(\mathbf Z/p^2),V)=0\) by Sah's lemma: the central scalar −I acts by −1 on V, and (−I−1)=−2 is invertible modp. Inflation–restriction therefore injects H¹(Q,V) into H¹(F2,V) for classes killed by the restriction, so the global Kummer class of aP+bQ vanishes. This contradicts the p-saturation of P,Q. Hence H=V². QED.

Consider an unramified good q, with Frobenius A in GL2(Z/p²). A modp is **nonidentity unipotent** precisely when E(Fq)/p is a 1-dimensional Fp-line and q≡1 modp (under our specified determinant-one unipotent conjugacy class). In GL2(Fp), this is ONE conjugacy class of cardinality p²−1, i.e. density
\[
\frac{p^2-1}{|\mathrm{GL}_2(\mathbf F_p)|}
=\frac1{p(p-1)}.
\]
For each such mod-p matrix, write a p² lift \(A=U+pB\) in a suitable basis, with \(U=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)\). The condition
\[
p\parallel \#E(\mathbf F_q)=\det(1-A)
\]
is exactly that the lower-left entry B21 be NONZERO modulo p, a fraction \((p-1)/p\) of the p⁴ possible lifts. Therefore the **exact Chebotarev density of good Frobenius q satisfying q≡1 modp, local p-quotient 1-dimensional, and p||#E(Fq)** is
\[
\boxed{d_{\mathrm{Frob},p}=\frac1{p^2}.}
\tag{B1}
\]
Proof uses full modp² Galois image.

For fixed such A, the independent Kummer translation pair \((t_P,t_Q)\in V²\) is UNIFORM. Passing to the 1-dimensional quotient \(V/(A-1)V\) yields a UNIFORM ordered pair of local MW coordinates \((a,b)\in\mathbf F_p²\). In particular, the local projective direction \([a:b]\in\mathbf P^1(\mathbf F_p)\) is uniform, conditional on the pair not being zero. Let \(\mathcal Q_{p,s}\) be q of the specified type with nonzero local MW vector of intrinsic projective slope s∈P¹(Fp). Then
\[
\boxed{\operatorname{dens}(\mathcal Q_{p,s})=\frac{p-1}{p^4}\quad\text{for EACH of the p+1 projective slopes s}.}
\tag{B2}
\]
Summing gives density \((p²-1)/p⁴\) for any nonzero row.

**THEOREM B (two independent local directions: exact positive density).** Among ORDERED distinct rational prime pairs (q1,q2) satisfying the above conditions and with invertible MW localization determinant, their two-variable natural Chebotarev density is
\[
\boxed{
D_p=\sum_{s\ne t}\operatorname{dens}(\mathcal Q_{p,s})
          \operatorname{dens}(\mathcal Q_{p,t})
=\frac{(p+1)(p-1)^2}{p^7}>0.
}
\tag{B3}
\]
Equivalently, for every FIXED p in the full-image tail, their count for q1,q2≤X is asymptotic to
\[
\boxed{D_p\operatorname{Li}(X)^2},
\]
as X→∞, with repeated q excluded (negligible). Conditional on each local vector being nonzero, two prime directions are independent with probability exactly p/(p+1). The density follows from the finite Galois group and Chebotarev; NO assumption of Sha triviality or global modular-symbol nonvanishing is used.

**Certified finite matrix counts:** For p=5,7,11, an entirely independent stdlib Python script enumerates all p⁴ lifts of U, checks exactly (p−1)p³ have p||det(1-A), and verifies (B1)-(B3) using exact rational arithmetic. Outputs:
- p=5: Frobenius 1/25, per-slope 4/625, independent ordered pair 96/78125.
- p=7: Frobenius 1/49, per-slope 6/2401, independent ordered pair 288/823543.
- p=11: Frobenius 1/121, per-slope 10/14641, independent ordered pair 1200/19487171.
The script tests finite algebraic counts; the group-theoretic/Kummer proof and Chebotarev justify the theorem.

## C. Concrete NEW analytic proof target: weighted modular-symbol mixing over THIN Chebotarev prime pairs

Kim+Castella–Sano give a unit at m_p factors but do NOT imply m_p=2. Theorem B proves abundance of excellent pairs locally; the **only remaining missing input for such pairs is nonvanishing of the GENUINE globally computed δ_{q1q2}**.

There is an existing dynamic method potentially relevant: Jungwon Lee & Hae-Sang Sun, *Dynamics of continued fractions and distribution of modular symbols*, JEMS 27 (2025), 3527–3582, Theorems A/B, establishes residual equidistribution of modular symbols when averaging over ALL rational numbers with denominators ≤X. It does NOT cover:
(i) products of TWO primes q1q2 in Chebotarev conjugacy classes,
(ii) TWO multiplicative primitive-root logs modulo the primes,
(iii) q-local reductions of two fixed rational MW points, nor
(iv) a variance estimate UNIFORM in the prime p varying through all sufficiently large primes.
Therefore no published equidistribution theorem is being misapplied here.

For p fixed and s≠t in P¹(Fp), let A_{p,s,t}(X) be ordered pairs of distinct primes q1,q2≤X, q1∈Q_{p,s},q2∈Q_{p,t}. Its size is asymptotic to
\[
N_{p,s,t}(X)=\left(\frac{p-1}{p^4}\right)^2\mathrm{Li}(X)^2.
\]
Freeze the SMALLEST positive primitive root at every q, and define the genuine complete modular-symbol mixed derivative δ_{q1q2}∈Fp with this convention. For h∈Fp×, define its additive Fourier correlation
\[
C_{p,s,t,h}(X)=\sum_{(q_1,q_2)\in A_{p,s,t}(X)}
 e^{2\pi i h\,\widetilde\delta_{q_1q_2}/p}.
\]

**THEOREM C (exact Fourier sieve inequality, elementary).** Suppose for some p and s≠t there exist an X with N=|A_{p,s,t}(X)|>0 and \(\eta<1\) such that for every h∈Fp×
\[
\boxed{|C_{p,s,t,h}(X)|\le\eta N.}
\tag{C1}
\]
Then
\[
\boxed{\#\{(q_1,q_2)\in A_{p,s,t}(X):
    \widetilde\delta_{q_1q_2}\ne0\bmod p\}
\ge\frac{p-1}{p}(1-\eta)N>0.}
\tag{C2}
\]
Proof: additive character orthogonality says
\[
\#\{\delta=0\}=\frac{N+\sum_{h=1}^{p-1}C_{p,s,t,h}}p
\le \frac{1+(p-1)\eta}{p}N.
\]
Subtract from N. QED.

**New research HYPOTHESIS (nontrivial beyond existence):** For E389a1, every sufficiently large p admits some s≠t with \(\sup_{h\ne0}|C_{p,s,t,h}(X)|/N\to0\) as X→∞. This would prove **positive density of true two-factor p-unit Kurihara witnesses** and hence Sha(E/Q)[p∞]=0 in the p-tail. It is substantially stronger than just one witness and is falsifiable by computing finite conditional histograms or by finding a p with nonzero Sha[p] (which by Theorem A would force EVERY δ_{qr}=0). Its proof would require a NEW arithmetic transfer-operator/large-sieve estimate capable of handling the thin Chebotarev and discrete-log conditions; Lee–Sun alone does not supply it.

**Archived independent finite observations, not proof of hypothesis:** At p=5, the 105 genuine two-factor Kurihara residues from 15 auxiliary primes have values 0:12,1:19,2:25,3:23,4:26. Thus conditional on the 93 nonzero-determinant pairs, the four nonzero residues occur 19,25,23,26 times, nearly evenly. The chosen 15 primes are NOT random prime samples at X→∞, so this has no asymptotic force.

## D. Why this is real forward work and not BSD-by-assumption

THEOREM A pinpoints EXACTLY what a rank-two witness would eliminate; it proves that Castella–Sano high-factor nonvanishing cannot be pruned by a formal local argument. THEOREM B gives the exact positive-density local supply, with no Sha assumption and an explicit formula for every large p. THEOREM C isolates a **genuinely new analytical estimate** on complete modular symbols over prime products, stronger than and quantitatively independent in formulation from the one-pair unit conjecture. Its proof is not in hand.

No artificial operator toy, local MW determinant, randomly fitted Tate weight, or finite p sample is advertised as proof of (C1). The unresolved challenge is global modular-symbol Fourier cancellation, with its precise thin prime and discrete-log constraints.

### References
- Castella–Sano, arXiv:2601.14504, Theorem B: https://web.math.ucsb.edu/~castella/Kurihara.pdf
- Chan-Ho Kim, *The structure of Selmer groups...*, Theorem 1.8: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
- Lee–Sun, JEMS (2025), Theorems A/B: https://ems.press/journals/jems/articles/14298906
- Mazur, surjectivity of the p-adic Galois representation for semistable curves at p≥11 as quoted by Bullach–Honnor 2025, Remark 1.3: https://dominikbullach.github.io/MazurTate.pdf
- Existing project full independent local Kummer proof: paper/bsd389_uniform_deep_Kummer_Chebotarev_MW_local_basis_theorem_2026-11-24.md

**FINAL VERDICT 25 Nov 2026:** New quantified Chebotarev theorem and exact pruning/Selmer equality rigorous; finite matrix tests PASS. Global two-prime analytic Fourier cancellation remains UNPROVED, therefore no uniform Sha finiteness or exact complex BSD claimed.


## E. Exact self-dual group-ring countermodel: functional equation alone CANNOT force a quadratic jet

This is an **abstract finite group-ring model**, not a genuine elliptic-curve theta nor a counterexample to BSD.

Let p≥5 and \(\bar R=\mathbf F_p[C_p]\cong\mathbf F_p[T]/T^p\), \(\sigma=1+T\). Define
\[
\boxed{\Theta_{\mathrm{toy}}=(\sigma+\sigma^{-1}-2)^2.}
\]
The involution # sends σ to σ⁻¹, so \(\Theta_{\mathrm{toy}}^\#=\Theta_{\mathrm{toy}}\) exactly. Yet
\[
\sigma+\sigma^{-1}-2=\frac{T^2}{1+T}
\quad\Longrightarrow\quad
\boxed{\Theta_{\mathrm{toy}}=\frac{T^4}{(1+T)^2}\ne0
\ \text{with first nonzero term }T^4.}
\]
Thus the **exact same inversion/self-dual functional-equation symmetry**, nonzero augmentation element and even parity allow order 4 rather than 2. The p5 genuine valuation-one K25 theta had first unit term T⁴ (with extra p-adic depth), demonstrating that such higher-order behavior is not mathematically artificial.

**Scope:** This elementary countermodel shows that inversion symmetry, even parity, and abstract nonvanishing do not logically force a rank-two first jet. It DOES NOT implement the actual Kato Euler-system norm relations or claim the existence of a rank-two E with such a theta. Theorem A explains the genuine arithmetic obstruction: extra Selmer mod-p generators.

## F. Quantifier and frozen-generator precautions

- The exact Chebotarev density B3 is for **each fixed p** as X→∞. No error term uniform in growing p is proved; the explicit rational density formula holds for all p in the full-image tail.
- A projective local MW slope [a:b] is intrinsic under change of the local generator. In contrast, an individual Kurihara residue \(\tilde\delta_{qr}\) changes by a p-UNIT when primitive roots change; the Fourier-distribution hypothesis must freeze a deterministic primitive-root convention (the minimal positive primitive root is one possible choice).
- The unit/nonunit condition on \(\tilde\delta_{qr}\) is independent of primitive-root choices. A proof of a density theorem conditional on the smallest-primitive-root convention must avoid averaging over artificially randomized primitive roots, which would create a **spurious uniform distribution of nonzero residue values** without producing any new arithmetic witness.
- The existing Lee–Sun transfer operator averages rational fractions with **all** eligible denominators up to a bound. The prime-product and discrete-log restriction is genuinely new; there is no shortcut by citing its already published spectral gap.
