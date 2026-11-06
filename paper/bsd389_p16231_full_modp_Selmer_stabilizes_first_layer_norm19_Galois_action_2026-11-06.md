# Exact first-layer stabilization of the entire anticyclotomic mod-16231 Selmer group

Date: 2026-11-06. **New theorem from already certified theta, the original Chida–Hsieh control theorem, and Pollack–Weston's no-finite-submodule theorem**. No frozen Gross/Manin/level-2 computation is repeated. This **does not** prove nontrivial first-layer Galois action, Sha=0 or full BSD.

## Arithmetic framework

Let \(E=389a1\), \(p=16231\), \(K=\mathbf Q(\sqrt{-3})\), and \(K_\infty/K\) its anticyclotomic \(\mathbf Z_p\)-extension. Let \(K_m\subset K_\infty\) be the unique subextension of degree \(p^m\); put \(\Gamma=\operatorname{Gal}(K_\infty/K)\), and \(\Lambda=\mathbf Z_p[[T]]\) with \(T=\gamma-1\). Let \(S_\Delta(K_m,E[p])\) and \(S_\Delta(K_\infty,E[p])\) be the precise N^-=389 ordinary residual Selmer groups in Chida–Hsieh 2013/15 Proposition 1.9 (no ramified Nplus places, because Nplus=1). Put \(S_\infty=\operatorname{Sel}_\Delta(K_\infty,E[p^\infty])\), \(X=S_\infty^\vee\).

Earlier in this PR and in the accepted source/data archive:
1. \(\Theta(T)=T^2u(T)\) with \(u\in\Lambda^\times\); Chida–Hsieh main-conjecture divisibility gives \((T^4)\subseteq\operatorname{char}_\Lambda(X)\).
2. The original Pollack–Weston 2011 Proposition 3.6, with Nplus1, identifies the Nminus-ordinary and minimal Selmer over K∞, and their anticyclotomic extension of Greenberg's nofinite theorem applies, since E(K)[p]=0 and the Selmer is cotorsion. Thus X has NO finite Λ-submodule.
3. The exact commutative algebra theorem then yields \(X\simeq\mathbf Z_p^a\), \(2\le a\le4\), with \(T^a X=0\). In particular, on the residual \(\mathbf F_p\)-module \(X/pX\), \(\bar T^4=0\).
4. Chida–Hsieh Proposition 1.9(1)-(2) guarantees exact control at **every** finite level for E[p], plus \(S_\Delta(K_\infty,E[p])=S_\infty[p]\). Residual irreducibility ensures \(E(K_\infty)[p]=0\), so there is no extraneous global H0 kernel.

## Theorem A: a full infinite mod-p Selmer module already lives at first layer

Since \(p=16231>4\), the freshman's-dream identity in characteristic p gives, on \(X/pX\),
\[
\gamma^p=(1+\bar T)^p=1+\bar T^p=1.
\]
Thus \(\Gamma^p\) acts trivially on \(X/pX\). Dualizing, it also acts trivially on
\[
S_\infty[p]\cong(X/pX)^\vee=S_\Delta(K_\infty,E[p]).
\]
By Chida–Hsieh finite-level control,
\[
S_\Delta(K_1,E[p])
\xrightarrow{\sim}
S_\Delta(K_\infty,E[p])^{\Gamma^p}
=S_\Delta(K_\infty,E[p]).
\]
For **every m≥1** the same applies to the subgroup \(\Gamma^{p^m}\subseteq\Gamma^p\). Hence:

\[
\boxed{
S_\Delta(K_1,E[p])\xrightarrow{\sim}
S_\Delta(K_m,E[p])\xrightarrow{\sim}
S_\Delta(K_\infty,E[p])
\quad\text{for EVERY }m\ge1.
}\tag{1}
\]

All arrows are **genuine restrictions** and are equivariant for the natural finite cyclic Galois action through \(G_1=\operatorname{Gal}(K_1/K)\). No assertion is made about p^n-torsion for n≥2; the theorem concerns the **entire mod-p** Selmer at all tower levels.

In particular
\[
\boxed{
\dim_{\mathbf F_p}S_\Delta(K_1,E[p])=a\in\{2,3,4\}.
}\tag{2}
\]
This is **bounded in first-layer field degree p**, rather than an abstract infinite \(\Lambda\)-module.

## Theorem B: a sharp finite-level test for both Sha[p∞] components

Let \(\sigma\) generate \(G_1\), and write \(D_\sigma=\sigma-1\) on the finite \(\mathbf F_p\)-vector space \(S_\Delta(K_1,E[p])\).

The exact base-field control and Kummer/quadratic descent give
\[
\dim_{\mathbf F_p}\ker D_\sigma
=
2+\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]
+\dim_{\mathbf F_p}\Sha(E^{(-3)}/\mathbf Q)[p].
\]
By Dokchitser–Dokchitser p-parity and Cassels–Tate, both Sha[p] dimensions are even, hence the dimension of \(\ker D_\sigma\) is even and at least two.

Since \(\dim S_\Delta(K_1,E[p])\le4\), **either** \(\ker D_\sigma\) has dimension two and both p-Sha vanish, **or** it has dimension four and the total Sha[p] dimension is exactly two. In the latter case \(D_\sigma=0\) on the whole first-layer Selmer space.

Consequently:
\[
\boxed{
D_\sigma\ne0
\quad\Longrightarrow\quad
\Sha(E/\mathbf Q)[p^\infty]=
\Sha(E^{(-3)}/\mathbf Q)[p^\infty]=0.
}\tag{3}
\]

Further, \(\dim S_\Delta(K_1,E[p])\le3\) itself forces the same conclusion by the invariant dimension gap. More precisely, using these two tests together yields a true equivalence:
\[
\boxed{
\Sha(E/\mathbf Q)[p^\infty]=
\Sha(E^{(-3)}/\mathbf Q)[p^\infty]=0
\iff
\left(\dim S_\Delta(K_1,E[p])\le3\right)
\ \mathrm{OR}\
\left(\exists s:\sigma s\ne s\right).
}\tag{4}
\]

Proof of reverse direction when dimension=4: if both Sha p-parts vanish, the invariant dimension is 2; thus \(D_\sigma\) has rank 2, in particular is nonzero. If dimension ≤3, both Sha p-parts vanish by evenness. All directions follow.

**This is an exact finite-level characterization**; it does not construct a moved class \(s\), or prove the dimension≤3 alternative.

## A concrete, already certified generator of G_1 (no new Gross computation)

The repository's previously certified algebraic first-layer ring-class construction identifies
\[
g=5+3\omega,\quad \mathrm{Norm}(g)=19,\quad
G=[g]^{5410}\in\mathrm{Pic}(\mathcal O_{p^2})
\]
whose image in the p-Sylow ring-class quotient of order 16231 has additive coordinate
\[
L_p(G)=14426\bmod 16231\ne0.
\]
This **generates G_1** under class field theory. (The archive also records its equivalent normalized principal-unit coordinate \(G=U^{1805}\).)

Therefore one may take \(\sigma=\mathrm{Art}_K(G)\) or its inverse, depending on Artin reciprocity convention. Since G is a generator, replacing \(\sigma\) by its inverse or any nontrivial p-adic power leaves the condition \(\sigma s\ne s\) invariant.

Theorem B becomes the explicitly labeled **norm-19 first-layer criterion**:
\[
\boxed{
\exists s\in S_\Delta(K_1,E[p])\ \text{with}\ 
\bigl(\mathrm{Art}_K([5+3\omega]^{5410})-1\bigr)s\ne0
\ \Longrightarrow\ 
\Sha(E/\mathbf Q)[p^\infty]=0.
}\tag{5}
\]

The long **full Gross-point orbit does not supply such a cohomological Selmer class** merely by having a nonzero second theta moment; confusing those objects is forbidden by the explicit Fitting codimension-two counterexample in this PR.

## Exact boundary and all-prime disclaimer

What is NOW proven, conditioned only on the already accepted archived CH/theta inputs:
- The anticyclotomic residual Selmer module **stabilizes at the first p-degree layer**, with dimension at most four.
- The norm-19 class gives an explicit generator of that first-layer Galois action (from an old exact certificate, not a new orbit).
- One non-fixed Selmer class, or an upper bound of three dimensions, would imply simultaneous p-primary Sha triviality.

What remains genuinely unproved in this route:
- Either **existence of a non-fixed cohomological Selmer class** at the first layer, or dim≤3 in its actual Selmer. Neither follows from theta-order-two, Iwasawa characteristic ideals or modular Gross moments alone.
- A uniform theorem for all rational primes p; p16231 is only one split ordinary prime and BSD has *infinitely many* possible p-primary obstructions.
- The separate exact complex rank-two BSD leading coefficient.

**Important:** The archived cyclotomic p16231 Kato certificate already supplies a distinct **computer-assisted conditional** route to the Sha(E/Q)[p∞]=0 conclusion; this research note neither repeats nor silently upgrades the archived trust conditions.

## Sources

- Chida–Hsieh, *On the anticyclotomic Iwasawa main conjecture for modular forms*, Proposition 1.9(1)-(2), pp.7–8; https://www.asahi-net.or.jp/~qa4m-cd/AIMC.pdf
- Pollack–Weston (2011), *On anticyclotomic mu-invariants of modular forms*, Proposition 3.6 and its proof (Nplus empty); doi:10.1112/S0010437X11005318
- Greenberg (1999), *Iwasawa theory for elliptic curves*, Proposition 4.14.
- Certified order-p class generator `paper/bsd389_norm19_exact_generator_of_first_pro_p_anticyclotomic_layer_2026-11-05.md`.
- Integral Bockstein higher-Fitting counterexample and nofinite rank4 theorem, in the same research branch.
