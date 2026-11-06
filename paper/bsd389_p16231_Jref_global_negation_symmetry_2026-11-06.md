# Exact negation symmetry of the cyclotomic \(J_{\mathrm{ref}}\) summand

Date: 2026-11-06. Curve E=389a1, p=16231, good ordinary. A **symbolic identity**, not a new large numerical computation, in the same normalized setting as \`paper/c01_to_sage_quadratic_coefficient_identity_2026-10-24.md\`.

## Setup

Write \(x=a+pb\in(\mathbf Z/p^2\mathbf Z)^\times\) with \(1\leq a<p\), \(0\leq b<p\), and \(\gamma=1+p\). Let
\[
 \omega(a)\gamma^{u(x)}=x+p^2\kappa(x)\pmod{p^3},\qquad
 w(x)=(2u(x)-1)a^{-1}\pmod p.
\]
Let \(m(r)\) denote the normalized even modular symbol, so \(m(-r)=m(r)\) and \(m(r+n)=m(r)\) for integers \(n\). For \(D_x=\begin{psmallmatrix}1&x\\0&p^2\end{psmallmatrix}\) put
\[
 F(D) = m(D\infty)-m(D0),\quad
 M_0(D)=F(D)-\alpha^{-1}F(\operatorname{diag}(p,1)D),
\]
\[
 M_1(D)=\alpha^{-1}\sum_{c=0}^{p-1}c F(\beta_c D),\quad
 \beta_c=\begin{psmallmatrix}1&c\\0&p\end{psmallmatrix},
 \quad \alpha\equiv a_p\not\equiv0\bmod p.
\]
The per-pair summand is
\[
 j(x)=-w(x)\bigl(M_1(D_x)-\kappa(x)M_0(D_x)\bigr)\pmod p.
\]

## Theorem (all units \(x\), no spot-check assumption)

Let \(x^\star=p^2-x\), with its canonical representative in \(1,\ldots,p^2-1\). Then
\[
 \boxed{j(x^\star)=j(x)\pmod p}.
\]

### Proof

1. Because \(\omega(p-a)=-\omega(a)\) and \(x^\star=-x+p^2\),
\[
 u^\star=u,\quad \kappa^\star=-\kappa-1,\quad w^\star=-w\pmod p.
\]
The coordinate map is \((a,b)\mapsto(p-a,p-1-b)\).

2. Evenness and integer-periodicity of \(m\) give
\[
 F(D_{x^\star})=F(D_x),\qquad
 F(\operatorname{diag}(p,1)D_{x^\star})
 =F(\operatorname{diag}(p,1)D_x).
\]
Therefore \(M_0(D_{x^\star})=M_0(D_x)\pmod p\).

3. In the weighted sum, the exact cusp arguments satisfy
\[
 {x^\star+p^2c\over p^3}={c+1\over p}-{x\over p^3}.
\]
Replace \(c\) with \(t=p-1-c\) and use evenness plus period 1 to obtain
\(F(\beta_c D_{x^\star})=F(\beta_t D_x)\).
Consequently,
\[
 M_1(D_{x^\star})
 =-\alpha^{-1}\sum_t(t+1)F(\beta_t D_x)
 =-M_1(D_x)-M_0(D_x)\pmod p.
\]
The last equality uses the Hecke relation
\(\sum_t F(\beta_t D)=a_p F(D)-F(\operatorname{diag}(p,1)D)
\equiv\alpha M_0(D)\pmod p\).

4. Combining,
\[
 M_1^\star-\kappa^\star M_0^\star
 =-\bigl(M_1-\kappa M_0\bigr),\qquad w^\star=-w.
\]
Thus \(j(x^\star)=j(x)\).

## Consequences and relation to real user logs

There are no fixed units for the involution since \(p\) is odd. Hence
\[
 J_{\mathrm{ref}}\equiv 2\sum_{a=1}^{(p-1)/2}\sum_{b=0}^{p-1}
 j(a+pb)\pmod p.
\]
For p=16231 this is \(131\,714\,565\) orbit representatives out of \(263\,429\,130\) units. The already archived global result \(J=4486\) **predicts** an orbit-half sum \(2243\bmod p\), but that half-sum is *not independently recomputed here*.

The user's actual direct source logs give

- \((a,b)=(1,0)\): \(M_0=11031,M_1=2316,\kappa=0,w=-1,j=2316\).
- \((a,b)=(16230,16230)\): \(M_0=11031,M_1=2884,\kappa=-1,w=1,j=2316\).

Indeed \(2884\equiv-2316-11031\bmod16231\). This latter 'new pair' is *symmetry-related* to the earlier \((1,0)\) oracle and is **not independent evidence of a new orbit**. The genuinely new orbit in the 2026-11-06 C++ crosschecks was \((1,1)\) with \(j=14896\), whereas \((2,3)\) had already been tested as a direct expected-value oracle. See:

- \`results/bsd389_p16231_Jref_direct_sage_pair_USER_PASS_2026-11-06.md\`
- \`results/bsd389_p16231_Jref_direct_sage_vs_frozen_CPP_NEW_PAIRS_USER_PASS_2026-11-06.md\`

**Critical boundary:** even a universal symmetry proof cannot by itself certify the numerical \(J_{\mathrm{ref}}=4486\) or the full source-to-C++ global identity, let alone Sha[p∞]. Future work should audit the *structural* Manin/Shapiro/Hecke transport once, not accumulate symmetry-redundant test cases.
