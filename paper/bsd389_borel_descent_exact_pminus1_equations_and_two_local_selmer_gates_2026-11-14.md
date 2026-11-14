# E389a1: explicit descent equations for the degree-(p+1) dual-isogeny Selmer, with ONLY TWO remaining rational local gates

**2026-11-14. Mathematical status:** a fully proved, exact primewise cohomological descent criterion; genuine \(\mathrm{GL}_2(\mathbf F_p)\)-equivariant linear equations, a class-field interpretation, and a separate localization criterion for membership in the *rational* p-Selmer. New verification uses authentic full GL2 action, but **does not calculate any ray class group, any p-isogeny Selmer dimension, an all-large-p bound on Sha, or the exact complex BSD leading term.**

## 1. Geometry imported from the genuine degree-(p+1) Borel descent

E/Q is the optimal conductor-389 elliptic curve
$$
E:y^2+y=x^3+x^2-2x,\qquad E(\mathbf Q)\simeq\mathbf Z P\oplus\mathbf Z Q,
\quad P=(-1,1),\ Q=(0,-1).
$$
Fix a prime \(p\ge5\), \(p\ne389\), with **surjective** residual image on \(V=E[p]\):
$$
\Gamma=\operatorname{Gal}(F/\mathbf Q)=\mathrm{GL}_2(\mathbf F_p),
\qquad F=\mathbf Q(E[p]).
$$
Let \(C\subset V\) be one torsion line, \(B=\mathrm{Stab}_{\Gamma}(C)\), \(K=F^B\). Then \([K:\mathbf Q]=p+1\). The line is stable over \(K\), defining a bona fide degree-p isogeny \(\phi:E_K\to E'=E_K/C\), and its dual \(\widehat\phi:E'\to E_K\) has kernel
$$
W=E'[\widehat\phi]=V/C
$$
as a \(G_K\)-module, with the quotient Borel character.

The earlier proof and the explicit p=5 sextic/K5 Vélu isogeny are in
[the prior Borel-descent PR #29](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/pull/29).

Put \(\Sigma=\{p,389,\infty\}\). The isogeny Selmer \(\operatorname{Sel}_{\widehat\phi}(E'/K)\) is a finite \(\mathbf F_p\)-space inside \(H^1(G_{K,\Sigma_K},W)\): all ramification of V and K/Q is supported on \(\Sigma\).

## 2. An EXACT nonsplit short exact sequence of actual Galois modules

Consider **all p+1 Galois conjugate lines** \(C_i\in\mathbf P(V)\), and put
$$
M=\bigoplus_{C_i\in\mathbf P(V)}V/C_i.
$$
The Galois action transports and permutes each quotient by its authentic twisted action (never the trivial action). It is canonically isomorphic, as a \(\Gamma\)-representation, to
$$
M=\operatorname{Ind}_{B}^{\Gamma}(W).
$$
Let
$$
\iota:V\to M,\quad v\mapsto(v\bmod C_i)_{C_i},\qquad
\mathcal R_p:=\operatorname{coker}\iota.
$$
Since the intersection of all p+1 lines is 0, \(\iota\) is injective. Thus
$$
\boxed{0\to V\xrightarrow{\iota}M\to\mathcal R_p\to0,
\quad\dim_{\mathbf F_p}M=p+1,\quad\dim\mathcal R_p=p-1.}\tag{SE}
$$
This sequence is Galois equivariant, but **does not split as G-module**: by Frobenius reciprocity
$$
\operatorname{Hom}_\Gamma(M,V)\simeq\operatorname{Hom}_B(W,V)=0.
$$
Indeed an image of 1 under a B-map W→V must be fixed under \(\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\), so lies in the e1-line; \(\begin{psmallmatrix}2&0\\0&1\end{psmallmatrix}\), which acts trivially on W, then forces the image to vanish. The genuine isogeny Selmer may therefore have classes not descending from the rational Selmer.

## 3. Exact p−1 *linear* descent constraints (not merely a dimension count)

Identify \(V=\mathbf F_p^2\) with coordinates \(v=(x,y)\), and index lines by
$$
C_t=\langle(1,t)\rangle \ (t\in\mathbf F_p),\qquad
C_\infty=\langle(0,1)\rangle.
$$
The quotient functional for C_t is \(\ell_t(x,y)=y-tx\), and for C∞ is \(\ell_\infty(x,y)=x\).
A coordinate \(m=(m_0,m_1,\ldots,m_{p-1},m_\infty)\in M\) lies in \(\iota(V)\) **iff**
$$
\boxed{D_t(m)=m_t-m_0+t\,m_\infty=0
\quad\forall t=1,\ldots,p-1.}\tag{D}
$$
There are precisely p−1 independent equations. Equivalently \(D:M\to\mathbf F_p^{p-1}\) is surjective with kernel \(\iota(V)\). The quotient coordinates have their **induced nontrivial Γ-action**, not a trivial one.

For p=5, in coordinates \((m_0,m_1,m_2,m_3,m_4,m_\infty)\), the matrix of D is
$$
\boxed{
\begin{pmatrix}
-1&1&0&0&0&1\\
-1&0&1&0&0&2\\
-1&0&0&1&0&3\\
-1&0&0&0&1&4
\end{pmatrix}\quad(\bmod 5).}
$$

## 4. The cohomological descent obstruction is exactly these equations on EVERY class-field generator

The central element \(z=-I\in\Gamma\) fixes every line, and acts as \(-1\) on **each** quotient \(V/C_i\). Hence it acts as \(-1\) on V, M **and** \(\mathcal R_p\). Since \(p\ne2\), Sah's lemma gives
$$
\boxed{H^j(\Gamma,V)=H^j(\Gamma,M)=H^j(\Gamma,\mathcal R_p)=0
\quad(j\ge0).}\tag{Sah}
$$
(Reference: Jan Nekovář, §5.5.2, https://www.ahmedmatar.net/matar_nekovar.pdf ; the theorem is also standard in Serre group cohomology.)

Global Galois cohomology of (SE), and Shapiro's lemma, now give **an exact sequence**
$$
\boxed{
0\to H^1(G_{\mathbf Q,\Sigma},V)
\longrightarrow H^1(G_{K,\Sigma_K},W)
\xrightarrow{\mathfrak o_p}
H^1(G_{\mathbf Q,\Sigma},\mathcal R_p).
}\tag{G}
$$
The initial zero comes from \(H^0(G_{\mathbf Q,\Sigma},\mathcal R_p)=0\), and the arrow to \(H^1(K,W)\) is the *previously constructed* restriction/dual-isogeny coefficient quotient. No omitted surjectivity is claimed at the right.

Let \(A_{F,\Sigma}\) be the maximal elementary p quotient of the S-ramified abelian class-field Galois group of F:
$$
A_{F,\Sigma}=
\operatorname{Gal}(F_\Sigma^{ab}/F)/p.
$$
It is finite by global class-field theory. For each of the three \(\Gamma\)-modules \(T=V,M,\mathcal R_p\) the same Sah inflation–restriction gives
$$
H^1(G_{\mathbf Q,\Sigma},T)
\overset{\sim}{\longrightarrow}
\operatorname{Hom}_\Gamma(A_{F,\Sigma},T).
$$

Given \(\xi\in H^1(G_{K,\Sigma_K},W)\), transport it by Shapiro and then restrict to F. It becomes a \(\Gamma\)-equivariant homomorphism
$$
h_\xi:A_{F,\Sigma}\to M.
$$
By (G), the class descends to H¹(Q,V) **if and only if** its obstruction vanishes, equivalently
$$
\boxed{
D_t(h_\xi(\sigma))=0\quad
\forall\,\sigma\in A_{F,\Sigma},\quad
\forall\,t=1,\ldots,p-1.}\tag{TEST}
$$
Because A_{F,Σ} is a **finite** Fp vector space, it is sufficient to test a set of Fp-generators of its S-ramified class-field group. Thus (TEST) really gives a finite linear-algebra procedure, once this genuine class-field module is computed.

The nontrivial \(\Gamma\)-action on \(\mathcal R_p\) and all local isogeny conditions must be retained. The p−1 equations are pointwise constraints on the **entire finite class-field homomorphism**, not p−1 scalar evaluations of one E-torsor.

## 5. Exactly TWO remaining rational local Selmer gates: p and 389

Let
$$
\mathscr D_p
=\ker\bigl(\mathfrak o_p:
\operatorname{Sel}_{\widehat\phi}(E'/K)
\to H^1(G_{\mathbf Q,\Sigma},\mathcal R_p)\bigr).
$$
By (G) every \(c\in\mathscr D_p\) admits a **unique**
lift \(\widetilde c\in H^1(G_{\mathbf Q,\Sigma},V)\).

For each \(\ell\in\{p,389\}\), let \(H^1_f(\mathbf Q_\ell,V)\) denote the *true local Kummer finite subgroup* \(E(\mathbf Q_\ell)/p\). Define the restriction-to-two-places map
$$
\lambda_{p,389}:\mathscr D_p\longrightarrow
\frac{H^1(\mathbf Q_p,V)}{H^1_f(\mathbf Q_p,V)}
\oplus
\frac{H^1(\mathbf Q_{389},V)}{H^1_f(\mathbf Q_{389},V)},
\quad
c\mapsto
(\operatorname{res}_p\widetilde c,\operatorname{res}_{389}\widetilde c)
\bmod H^1_f.
$$

**Theorem (exact rational Selmer sieve).**
$$
\boxed{\operatorname{Sel}_p(E/\mathbf Q)
\simeq\ker\lambda_{p,389}\subseteq\mathscr D_p.}\tag{SEL}
$$

**Proof:** The rational p-Selmer always injects into the K-isogeny Selmer by the Kummer naturality already proved in PR #29, and the ambient injection (G) says it lies in \(\mathscr D_p\). Its local images lie in \(H^1_f\) at p and 389, so it lies in the kernel.

Conversely a c in the kernel has a unique global cohomology lift \(\widetilde c\) unramified outside \(\Sigma\). At every good prime \(\ell\notin\{p,389\}\) the local Kummer subgroup \(H^1_f(\mathbf Q_\ell,V)\) **equals the unramified subgroup** for \(\ell\ne p\) and good reduction (standard Néron reduction/Kummer theorem). Thus \(\widetilde c\) automatically satisfies the rational local Selmer condition there. At the two remaining finite primes the condition is imposed by \(\lambda_{p,389}=0\). For the real place, H¹(R,E[p])=0 because complex conjugation has order 2 prime to p. Hence the class is in the rational p-Selmer. QED.

**Consequently, using the certified MW basis P,Q**, the arithmetic obstruction has the exact dimension formula
$$
\boxed{
\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]
=
\dim_{\mathbf F_p}\ker\lambda_{p,389}-2.
}\tag{SHA}
$$

This is an exact **computable-in-principle, noncircular** class-field/isogeny descent criterion. Computing \(\ker\lambda\) requires **genuine number-field class groups and S-units together with p- and 389-adic local isogeny/Kummer conditions**, neither of which is done by the finite-group script.

**Sharp sufficient criterion.** For a fixed p, a true arithmetic computation yielding
\(\dim_{\mathbf F_p}\ker\lambda_{p,389}=2\)
proves \(\Sha[p^\infty]=0\), without a prior Sha input. But this criterion is equivalent to the fixed-p goal and *its uniform all-large-p satisfaction remains unproved*.

## 6. Exact finite-field arithmetic audit, actual execution

The independent [Python verifier](../verification/bsd389_borel_descent_compatibility_audit.py), run in the assistant's container on November 14, 2026, checks:

- D has exact kernel equal to \(\iota(V)\), with p−1 independent relations, for p=5,7,11,13,107,16231.
- The authentic \(\Gamma\)-action on each quotient V/C, including its scalar factor and nontrivial permutation of the projective lines, preserves the diagonal V. It is **not** a trivial-action model.
- The \(-I\) central element acts exactly as \(-1\) on V, M and thus \(\mathcal R_p\); this is the hypothesis for Sah.
- Hom_B(V/C,V)=0 and the induced sequence has no Γ-linear retraction.
- **EXHAUSTIVE** \(\Gamma\)-equivariance tests at every invertible 2×2 matrix over F5 (480 elements) and over F7 (2016 elements), plus randomized exact tests for p11,13,107,16231.

Local genuine assistant-side SHA-256 of the exact standalone executable:
\`1450eaf026cf9a176a46741669b55f1b0e94c29f3c099e78e520cbc7a07c57bf\`.

The program does **not** calculate \(\dim\mathscr D_p\), the arithmetic class-field group \(A_{F,\Sigma}\), any p-adic local Selmer quotient, actual Sha, or a bound independent of p.

## 7. Honest relevance to the global BSD question

This provides an actually constructed, precise map and *finite arithmetic linear equations* to separate rational classes from the extra Selmer classes over K_p. It is stronger than merely injecting Sel_p into the full K-isogeny Selmer; it avoids falsely requiring the total K-isogeny Selmer to have dimension only 2.

However, the number of projective lines, the dimension p−1 of the obstruction representation, the class-field group of \(F=\mathbf Q(E[p])\), and the local conditions **all vary with p**. The suite of exact comparisons (G), (TEST), (SEL) is **NOT** a p-independent perfect \(\mathbf Z\)-complex, a fixed nonzero annihilator D, or the desired all-large-p bound \(\mu_p\le3\).

The next genuine arithmetic task is to **compute** \(A_{F,\Sigma}\)'s relevant equivariant ray-class/S-unit eigenspaces, or the equivalent K-isogeny Selmer plus \(\mathfrak o_p\) and the two local gates, at a *new unproved prime* (e.g. supersingular 599 or ordinary 16231 if the archived 2026-11-09 independent Kato certificate is not accepted). To finish globally, a separately proven prime-independent bound for these descent-compatible dimensions would still be necessary. No previous Sha-p certificates should be rerun merely for regression unless needed to validate the new method.

**Verdict: new exact cohomological descent equations and two-local Selmer characterization; no new Sha vanishing and no complete rank-two BSD.**
