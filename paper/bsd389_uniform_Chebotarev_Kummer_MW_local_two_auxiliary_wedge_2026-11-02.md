# A true prime-uniform theorem for rank-two **Mordell–Weil localizations** via Kummer + Chebotarev

**2026-11-02. Mathematical status:** a fully reasoned **unconditional theorem subject only to the explicitly stated residual-surjectivity and Mordell–Weil primitivity hypotheses**, with no hypothesis on \(\Sha\), no BSD input, no Kato main conjecture and no modular symbols. For E=389a1, prior independently certified MW generators and semistable residual surjectivity make it apply to **every prime p≥11** (with separately verified residual surjectivity it extends to p=5,7). Its conclusion is an infinity of **p-admissible Kolyvagin auxiliary pairs at which the MW localization wedge is a unit**. It **does NOT** assert any of the corresponding two-prime Kurihara numbers is nonzero; these are distinct arithmetic objects.

Primary background: [Davide Lombardo–Sebastiano Tronto, Kummer theory of elliptic curves and mod-p Galois representations](https://link.springer.com/article/10.1007/s40574-024-00427-6); [Sah's lemma central-scalar mechanism](https://arxiv.org/abs/2012.06263) (the specific H¹=0 is proved directly below); [Chebotarev density theorem]; and [Kim, Theorems 1.8 and 1.10, for the separate Selmer/Kurihara implications](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf).

## I. Theorem: uniform existence of rank-two auxiliary local bases

Let \(E/\mathbf Q\) be an elliptic curve and let \(P,Q\in E(\mathbf Q)\) have **linearly independent reductions in \(E(\mathbf Q)/pE(\mathbf Q)\)**, with p an odd prime \(p\ge5\). Assume
\[
\bar\rho_{E,p}:G_{\mathbf Q}\twoheadrightarrow \operatorname{GL}_2(\mathbf F_p).
\]
Then **there exist infinitely many ordered pairs of distinct good auxiliary primes \(q_1,q_2\) away from p and the conductor**, with:

1. \(q_i\equiv1\bmod p\) and \(a_{q_i}(E)\equiv q_i+1\equiv2\bmod p\).
2. Each \(E(\mathbf F_{q_i})/pE(\mathbf F_{q_i})\) has **dimension exactly one** over \(\mathbf F_p\).
3. The reduction/local Kummer map
   \[
   \operatorname{span}_{\mathbf F_p}\{\bar P,\bar Q\}
   \longrightarrow E(\mathbf F_{q_1})/p\oplus E(\mathbf F_{q_2})/p
   \]
   is an **isomorphism**, equivalently its 2×2 localization determinant is a unit mod p.

More strongly, both q's can be selected from separately prescribed positive-density Chebotarev sets, so there are infinitely many disjoint pairs.

### Step 1. The Kummer classes remain independent over Q(E[p])

Put \(V=E[p]\cong\mathbf F_p^2\) and \(K=\mathbf Q(E[p])\). The extension \(K/\mathbf Q\) has Galois group \(\mathrm{GL}_2(\mathbf F_p)\) by assumption. The Kummer sequence yields
\[
E(\mathbf Q)/pE(\mathbf Q)\hookrightarrow H^1(G_{\mathbf Q},V).
\]
The restriction map
\[
H^1(G_{\mathbf Q},V)\to H^1(G_K,V)
\]
is injective, because by inflation–restriction its kernel is \(H^1(\mathrm{GL}_2(\mathbf F_p),V)\).

**Direct proof that this H¹ is zero:** let \(z=2I\) be the **central scalar** in \(\mathrm{GL}_2(\mathbf F_p)\), with \(z-1=I\) invertible. For a 1-cocycle \(c\), centrality yields
\[
(z-1)c(g)=(g-1)c(z)
\]
for every \(g\in\mathrm{GL}_2(\mathbf F_p)\). Thus \(c(g)=(g-1)(z-1)^{-1}c(z)\) is a coboundary. Therefore \(H^1=0\), *for every p≥3*, and restriction is injective.

Because \(\bar P,\bar Q\) were independent in \(E(\mathbf Q)/p\), the restricted Kummer classes remain independent in \(H^1(G_K,V)\). As \(G_K\) acts trivially on V, they are honest continuous homomorphisms
\[
c_P,c_Q:G_K\longrightarrow V.
\]

### Step 2. **Full two-point Kummer image** over K

Let
\[
U=\operatorname{im}\left(c_P,c_Q:G_K\to V\oplus V\right).
\]
Since P and Q are rational, \(U\) is stable under the **diagonal** natural action of \(\mathrm{GL}_2(\mathbf F_p)=\operatorname{Gal}(K/\mathbf Q)\).

The standard representation V is absolutely irreducible and has scalar endomorphism ring \(\operatorname{End}_{\mathrm{GL}_2}(V)=\mathbf F_p\). Each coordinate projection of U is a nonzero stable subspace (since \(c_P,c_Q\) are nonzero) and therefore equals V.

Suppose U were proper. The intersection \(U\cap(0\oplus V)\) is a stable subspace of the simple module V; hence either 0 or V. If it were V, surjectivity of the first projection implies U=V², contradicting properness. So the intersection is 0, and the first projection identifies \(U\simeq V\); the second projection defines an equivariant map \(V\to V\), necessarily scalar \(tI\). Then \(c_Q=t\,c_P\), contradicting independence of their two restricted Kummer classes. Hence
\[
\boxed{U=V\oplus V.}
\]

Equivalently, in the finite Galois extension
\[
L=\mathbf Q(E[p],p^{-1}P,p^{-1}Q),
\]
the kernel of \(\operatorname{Gal}(L/\mathbf Q)\to\mathrm{GL}_2(\mathbf F_p)\) is **exactly V²**. This is *full two-point Kummer surjectivity*, deduced from saturated MW independence and residual GL2 surjectivity, not assumed.

### Step 3. Prescribe a unipotent Frobenius and two independent local Kummer rows

Fix a nonidentity unipotent matrix
\[
A=\begin{pmatrix}1&1\\0&1\end{pmatrix}\in\mathrm{GL}_2(\mathbf F_p).
\]
It has \(\det A=1\), \(\operatorname{tr}A=2\), and \(\dim_{\mathbf F_p}V/(A-I)V=1\). Choose \(w\in V\setminus(A-I)V\). Because the kernel above is **all V²**, there exist two Galois elements \(\sigma_P,\sigma_Q\in\operatorname{Gal}(L/\mathbf Q)\) both projecting to A, whose Kummer components \((c_P,c_Q)\) are respectively
\[
(c_P,c_Q)(\sigma_P)=(w,0),\qquad
(c_P,c_Q)(\sigma_Q)=(0,w)
\]
after choosing an initial lift and multiplying by suitable kernel elements. Here the Kummer cocycles are evaluated at lifts; adjusting the lift by the full kernel gives arbitrary prescribed components at fixed A. The local classes are their images in \(V/(A-I)V\).

By **Chebotarev**, infinitely many good rational primes \(q_P,q_Q\) have Frobenius conjugate to \(\sigma_P,\sigma_Q\), respectively; exclude the finite ramified set and choose them distinct. Frobenius characteristic polynomials give
\[
q_i\bmod p=\det A=1,\qquad a_{q_i}(E)\bmod p=\operatorname{tr}A=2,
\]
which are precisely the **p-admissible auxiliary prime congruences** used for Kurihara. Moreover
\[
E(\mathbf F_{q_i})/p
\simeq H^1(\mathbf F_{q_i},E[p])
\simeq V/(A-I)V
\]
using the local good-reduction Kummer sequence, Lang's theorem, and the fact the finite-field absolute Galois group is procyclic. Both local targets are 1-dimensional. The chosen Frobenius translations mean that under suitable choices of their Fp bases the localization of P,Q has matrix
\[
\boxed{\begin{pmatrix}1&0\\0&1\end{pmatrix},}
\]
hence determinant 1. Frobenius conjugation changes bases and representatives, but preserves the invariant property of independent local rows. This proves all three assertions and the infinitude of ordered pairs. QED.

## II. Application **uniform in p** to E=389a1

The curve
\[
E:y^2+y=x^3+x^2-2x
\]
has conductor N=389, discriminant +389, and semistable reduction (unique multiplicative bad place 389). Our research project previously independently certified its full Mordell–Weil basis
\[
P=(-1,1),\quad Q=(0,-1)
\]
with no torsion; hence their reductions are independent in \(E(\mathbf Q)/pE(\mathbf Q)\) for **all rational primes p**. Mazur's semistable residual-surjectivity theorem gives \(\bar\rho_{E,p}\cong \mathrm{GL}_2(\mathbf F_p)\) for **every p≥11** (including p=389, though the elliptic curve has bad reduction at that p). The p5 and p7 residual-surjectivity gates were also independently certified in the project.

**Consequently**:
\[
\boxed{\begin{gathered}
\text{For every prime }p\ge11,\quad
\exists^\infty\text{ p-admissible distinct pairs }(q_1,q_2)\\
\text{such that }\
P\wedge Q\ \text{maps to an Fp-unit in }\
(E(\mathbf F_{q_1})/p)\wedge(E(\mathbf F_{q_2})/p).
\end{gathered}}
\]
The same follows for p5,7 assuming the previously independently certified residual-surjectivity checks. No numerical search over infinitely many p was performed or needed: this is an exact Galois/Chebotarev theorem.

This **generalizes** the separately assistant-computed explicit local determinants p5=2, p7=3 and p107=38 on the historically used auxiliary pairs; it does **not** assert Chebotarev automatically chooses the very same primes as previously used.

### Subtle point: p-divisibility of the finite group order

The theorem requires \(\dim E(\mathbf F_q)/p=1\), and the nonidentity unipotent Frobenius guarantees exactly this. It does **not** demand \(p^2\nmid\#E(\mathbf F_q)\); it may happen that p² divides the group order while its p-rank remains 1. The **finite** p5/p7/p107 explicit checks enjoy the stronger p||#E(Fq), which allows the shortcut \([\,\#E(\mathbf F_q)/p\,]\) projection. Do NOT conflate these conditions in implementations for newly chosen Chebotarev auxiliary primes.

## III. Why this is a genuine advance yet NOT the uniform Sha bound

The above theorem establishes a **prime-uniform supply of good local test primes** which detect the saturated rank-two Mordell–Weil wedge, and eliminates any need to *assume* the existence of nondegenerate local pairs for each large p.

But it does NOT prove that the **same** pair of auxiliaries has
\[
\widetilde\delta_{q_1q_2}(E)\ne0\bmod p.
\]
Even nonzero mod-p Kurihara numbers at *some number of auxiliary primes*, as proved under the hypotheses of [Castella–Sano Theorem B](https://web.math.ucsb.edu/~castella/Kurihara.pdf), do **not** bound that number by two. The actual two-prime Kurihara value comes from a global Kato Euler/Kolyvagin-derived class and a weighted modular-symbol functional, not simply from localizing P and Q. The previous [eight-term full-Hecke-marginal kernel construction](bsd389_kurihara_full_marginal_kernel_and_free_mixed_coefficient_2026-11-02.md) explicitly demonstrated why local/eigensymbol primitivity alone cannot force its nonvanishing.

**Exact missing arithmetic bridge:** prove a **uniform** compatibility/nonvanishing theorem comparing the global Kato-derived degree-2 class (or an independently constructed determinant class in Selmer cohomology) with the local MW wedge for at least one admissible Chebotarev pair at each p, with an integral unit comparison modulo p. Merely knowing the MW wedge is detected by some local pair does not provide such a global comparison; a proof must not assume that desired implication.

The two independent remaining strong-BSD obligations remain (1) an actual global finite-support/finiteness result for Sha and (2) the exact complex leading-term equality \(L''(E,1)/2=\Omega_E\operatorname{Reg}(E)\#\Sha(E/\mathbf Q)\).

**Operational conclusion:** the local Kummer-prime existence branch is now **proved for all large p**; continuing to search numerically for local matrices at ever larger p is redundant. The frontier is genuinely global **Euler/Kolyvagin-to-local-MW comparison**, rather than Hecke eigenline uniqueness or availability of adequate auxiliary primes.
