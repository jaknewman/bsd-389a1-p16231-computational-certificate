# BSD 389a1 — global proof targets after the p=16231 certificates (2026-11-06)

**No prime-local certificates are to be rerun as part of this note.** Curve \(E=389a1\), rank \(2\), torsion \(1\), Tamagawa product \(1\). This note distinguishes two mathematically separate global proof problems: (A) the support of \(\Sha\); (B) the *exact* archimedean leading coefficient. It records a new-to-this-project link with the *original* Birch–Swinnerton-Dyer prime-product conjecture and GRH for this individual Hasse–Weil \(L\)-function.

## 1. A real theorem behind the user's GRH observation

Let \(N_\ell=\#E_{\mathrm{ns}}(\mathbf F_\ell)\), non-singular points on a minimal reduction at each prime (including \(\ell=389\)), and put
\[
P_E(x)=\prod_{\ell\le x}\frac{N_\ell}{\ell}.
\]
The original Birch–Swinnerton-Dyer prime-product assertion is
\[
P_E(x)\sim C_E(\log x)^{\mathrm{rank}E(\mathbf Q)}
=C_E(\log x)^2.
\]
Goldfeld's theorem (1982) says that this *strong original asymptotic for all x* implies **both**
\[
\operatorname{ord}_{s=1}L(E,s)=2
\quad\text{and}\quad
\mathrm{RH}(L(E,s)):\ \Re \rho=1
\text{ for every nontrivial zero }\rho.
\]
It determines
\[
C_E=\frac{2!\sqrt 2\,e^{2\gamma}}{L''(E,1)}
=\frac{\sqrt2\,e^{2\gamma}}{L''(E,1)/2}.
\]
**This is RH for the one GL(2) function \(L(E,s)\), not the full generalized RH for every Dirichlet/automorphic \(L\)-function.** The *modern* claim \(\operatorname{ord}_{s=1}L(E,s)=2\) and the BSD leading coefficient at one point do **not** imply the locations of other zeros.

Primary published source: Arshay Sheth, *Euler Product Asymptotics for L-functions of Elliptic Curves*, IMRN 2025, Theorem 1.3, https://doi.org/10.1093/imrn/rnaf214.

## 2. Equivalent prime-sum target and its difficulty

At good primes let \(\alpha_\ell,\beta_\ell\) be Frobenius roots of
\(X^2-a_\ell X+\ell\). Define the explicit prime-power sum
\[
\psi_E(x)=\sum_{\substack{\ell^k\le x\\\ell\nmid389}}
 (\alpha_\ell^k+\beta_\ell^k)\log\ell.
\]
Conrad (2005) and Kuo–Murty (2005) establish the analytic link between the unrestricted prime-product asymptotic and the strong error estimate
\[
\boxed{\psi_E(x)=o(x\log x).}
\]
Precisely, the exponent/constant of the product are fixed by the actual
order of vanishing and \(L^{(r)}(E,1)/r!\); to get the claimed *rank-two*
exponent one must know that the analytic order is two.

The standard RH consequence \(\psi_E(x)=O(x(\log x)^2)\) is *not*
enough to obtain that unrestricted little-o estimate by itself.
Sheth (2025), Theorem B, proves under RH that
\[
P_E(x)\sim C_E(\log x)^r
\]
**only outside a set of finite logarithmic measure** (not all \(x\));
the full asymptotic of Goldfeld is stronger than RH alone.

Thus the prime-product route is mathematically valid and may furnish an
analytic proof of rank two and a formula for \(L''(E,1)\), but is not an
easy shortcut through GRH. None of this controls the global \(\Sha\).

## 3. The exact Selmer criterion for \(\Sha=0\) (ALL primes)

The Kummer exact sequence, for every prime \(p\), gives
\[
0\longrightarrow E(\mathbf Q)/p E(\mathbf Q)
\longrightarrow\operatorname{Sel}_p(E/\mathbf Q)
\longrightarrow\Sha(E/\mathbf Q)[p]\longrightarrow0.
\]
Because the certified Mordell–Weil group is \(\mathbf Z^2\) with
trivial torsion,
\[
E(\mathbf Q)/pE(\mathbf Q)\simeq\mathbf F_p^2.
\]
Since \(\Sha\) is a torsion abelian group,
\[
\boxed{\Sha(E/\mathbf Q)=0
\iff\forall p\text{ prime},\
       \dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)=2.}
\]
This is a **proved reformulation**; it is not a proof that every Selmer
dimension equals two.

A legitimate global certificate would supply **one explicit nonzero
integer \(C_{\mathrm{Sel}}\)** with a theorem
\[
p\nmid C_{\mathrm{Sel}}\quad\Longrightarrow\quad
\dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)=2,
\]
then resolve each \(p\mid C_{\mathrm{Sel}}\) using the already available
prime-local evidence or separately justified conclusions.
The known integer Smith invariant \(C_{\mathrm{Hecke}}\) proves only
rigidity of one modular-symbol eigenlattice, not this Selmer bound.
No method may silently equate the two. The missing object is a
*prime-independent integral arithmetic map* (e.g., a genuine Euler/
Kolyvagin-to-Selmer Fitting comparison), not more Hecke Smith tests.

## 4. A potentially sharper archimedean goal: prove integrality, not infinite precision

Let \(\Omega_E\) be the correct minimal Néron **real period**,
\(\operatorname{Reg}_E\) the real Néron–Tate regulator, and set
\[
Q_E=\frac{L''(E,1)/2}{\Omega_E\,\operatorname{Reg}_E}.
\]
Given analytic order exactly two and \(\Sha=0\), the remaining BSD
identity is \(Q_E=1\).

**Elementary but decisive conditional lemma:** If one establishes by
an independent *theorem* that \(Q_E\in\mathbf Z\) and has a rigorous
archimedean enclosure \(0<Q_E<2\), then \(Q_E=1\) exactly.
The existing high-precision numerical agreement cannot replace the
integrality theorem. Such an integrality result would itself require
substantial new global motivic/determinant-line arithmetic; no current
certificate establishes it. Ensure that the exact period convention
matches the BSD formula (especially the factor of two for real
connected components).

Thus a serious, *non-numerical* alternative to directly proving
\(Q_E=1\) is to prove the global integral comparison
\(Q_E\in\mathbf Z\). Unlike an approximate equality, this is an
arithmetically rigid proof target.

## 5. Decision and stopping rules

- **Retain** all previously certified local Mordell–Weil, Hecke,
  Kurihara, \(p\)-adic regulator, Brandt, Gross-point, and \(p=16231\)
  source-to-\(J_{\rm ref}\) conclusions as archived; do not rerun.
- **Do not** claim that a GRH hypothesis, the Goldfeld prime product,
  or a low-Selmer-corank BSD theorem (corank \(0,1\)) controls this
  rank-two curve's global \(\Sha\).
- **Global arithmetic target:** construct an integral, prime-uniform
  Selmer comparison forcing
  \(\dim\operatorname{Sel}_p=2\) outside finitely many explicit primes.
- **Exact complex target:** prove \(Q_E\in\mathbf Z\) (or a stronger
  direct identity); a *certified* interval \(0<Q_E<2\) then suffices
  to identify it with \(1\).
- **Optional analytic branch:** study the strong Frobenius sum
  estimate \(\psi_E(x)=o(x\log x)\) as the precise input for the
  original prime-product version, with no claim that this is
  easier than RH/modern rank-two BSD.

The curve's full BSD formula and global finiteness of \(\Sha\)
remain unproved in this dossier. This note establishes only rigorous
*equivalences/reductions* and identifies the inputs they still need.

### Primary references

- Arshay Sheth (2025), *Euler Product Asymptotics for L-functions of Elliptic Curves*, https://doi.org/10.1093/imrn/rnaf214 (Goldfeld theorem; original BSD vs RH; theorem B; Conrad/Kuo–Murty discussion).
- J. S. Milne, *Elliptic Curves*, chapter IV, §10, https://jmilne.org/math/Books/ectext6.pdf.
- F. Castella and M.-L. Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum Math. Sigma (2022), https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864. This is a valuable rank-two source, **not** by itself a full all-\(p\) Selmer Fitting theorem.
