# p16231: an independent V65 eclib → Sage oracle and the remaining source-chain cut

**Date:** 2026-10-30. **Status:** source-code and exact matrix lemmas written, *new 67-generator Sage script not yet executed by user*. Do not mark it PASS until the authenticated terminal output is provided.

Curve E = 389a1, N=389, p=16231, a_p=128 ordinary, rank 2. We are **not** repeating the historical 263,429,130 pairs, the 131,698,335 nonzero level-2 eclib evaluations, or an expensive full Sage n=3 L-series run.

## 1. Mathematical identity already established, independent of sampled outputs

Set \(\alpha^2-128\alpha+p=0\) with \(\alpha\bmod p=128\), \(\gamma=1+p\), \(D_x=\left(\begin{smallmatrix}1&x\\0&p^2\end{smallmatrix}\right)\) and \(x=a+pb\).

For \(\mu_n(y)=\alpha^{-n}[m(y/p^n)-\alpha^{-1}m(y/p^{n-1})]\), where \(m\) is the Néron-normalized plus modular symbol in the eclib \`L_ratio\` convention, the established binomial/distribution/Hecke computation gives
\[
  A_2^{(3)}-A_2^{(2)}
  \equiv \frac{p J_{\mathrm{ref}}}{4\alpha^2}\pmod{p^2}.
\]
The \(1/4\) is not fitted: one \(1/2\) from \(\binom j2\) and one \(1/2\) from the curve's two real components. See [universal Sage bridge](c01_sage_n3_minus_n2_universal_lemma_auditable_2026-10-26.md).

The **mathematical** reference scalar \(J_{\mathrm{ref}}\) is given independently of any C++ output by
\[
J_{\mathrm{ref}} =
-\sum_{\substack{1\le a<p\\ 0\le b<p}}
w(a,b)\big(M_1(D_x)-\kappa(a,b)M_0(D_x)\big)\pmod p.
\]
The moment transport \(T(h)=\left(\begin{smallmatrix}1&0\\-AB&A^2\end{smallmatrix}\right)\), the adjoint coefficient row \((qW-K,rW)\), the exact Manin cusp-divisor relations, the exception-independent Shapiro split and the continued-fraction telescope show by **source-level algebra** why two different C++ engines implement this same scalar. See [formal duality](c01_shapiro_formal_duality_and_exceptional_audit_2026-10-26.md). This proof is not by extrapolation from six sample pairs.

## 2. New independently checkable V65 source oracle

The 67-generator binary \`eclib_beta_table.bin\` (2,175,242 bytes) is a shared numerical input to the full V19 contraction and the independent new 263m-pair scalar engine. It contains for each generator G:
\[
 f_G=F(G),\quad f_P=F(PG),\quad
 f_t=F(\beta_tG)\ (t=0,\ldots,p-1),
\]
where \(F(H)=m(H\infty)-m(H0)\), \(P=\operatorname{diag}(p,1)\), \(\beta_t=\left(\begin{smallmatrix}1&t\\0&p\end{smallmatrix}\right)\).

New source [\`verification/bsd389_p16231_v65_direct_sage_oracle.py\`](../verification/bsd389_p16231_v65_direct_sage_oracle.py) verifies (when run):

- SHA256 of original all-390-Manin relation JSON \`9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8\`.
- SHA256 of original 67-generator eclib table \`aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c\`.
- All **67** Hecke identities \(\sum_{t=0}^{p-1} f_t+f_P=128 f_G\bmod p\), inspecting exactly **1,087,477** finite-symbol entries.
- **All 67** pairs \(F(G),F(PG)\), sampled \(F(\beta_tG)\), and \(F(P r_j G)\) for \(j=0,1,71,p-1,\infty\). The **independent \`sage\` modular-symbol implementation**, not eclib, evaluates the comparison side.
- For every generator G the exceptional infinity class \(\infty\) is tested directly, not inferred from ordinary finite cosets.

The exact Shapiro identity needed for these checks is elementary: for every \(1\le j<p\) define \(s=(Nj)^{-1}\pmod p\) as its least nonnegative representative and \(r_j=\left(\begin{smallmatrix}1&0\\Nj&1\end{smallmatrix}\right)\). Then
\[
P r_j= H_j\beta_s,\qquad
H_j=\begin{pmatrix}p&-s\\Nj&(1-Njs)/p\end{pmatrix}\in\Gamma_0(N).
\]
The lower right entry is an integer and \(\det H_j=1\), so \(F(P r_j G)=f_s\).
At \(j=0\), \(P r_0=P\) gives \(f_P\).
For the original exceptional representative \(r_\infty=\left(\begin{smallmatrix}-40&-1669\\389&16231\end{smallmatrix}\right)\) with determinant 1,
\[
P r_\infty =
\underbrace{\begin{pmatrix}-649240&-1669\\389&1\end{pmatrix}}_{\in\Gamma_0(389)}
\beta_0,
\]
hence \(F(P r_\infty G)=f_0\), exactly the special branch in \`historical/v65/v65_independent_terminal_ntt.cpp\`. The source's \(M_0(r_j G)=f_G-\alpha^{-1}F(P r_j G)\) follows with no coefficient rescaling.

**Exhaustive extra algebraic gate:** The updated checker now tests the exact factorization `P*r_j=H_j*beta_s` for **every** Shapiro index `j=0,...,p` (16,232 cases, not just five). This branch-independent identity was also executed separately under ordinary Python and passed (`INDEPENDENT_EXACT_SHAPIRO_FACTORIZATIONS_PASS 16232`). The genuine Sage binary-table regression remains *unexecuted* until the user supplies its terminal log.

This test probes a **shared oracle** in a way not supplied by the two full outer-sum computations. The test is still finite/sample-level for direct Sage cusp values, not exhaustive independent regeneration of all 1,087,477 eclib table entries.

## 3. Exact numerical consequences (already historically authenticated)

\`\`\`text
p                       = 16231
a_p                     = 128
alpha^(-1) mod p        = 5199
A2(n=2) / p mod p      = 1199
J_ref mod p             = 4486  [trusted C01 source/global runs]
(4*alpha^2)^(-1) mod p = 9362
J_ref/(4*alpha^2)      = 8335 mod p
A2(n=3) / p            = 9534 mod p  [derived]
reg_p / p^3            = 1930 mod p
BSD_factor / p         = 9534 mod p
analytic / BSD_factor  = 1 mod p    [conditional quotient, a p-adic unit]
\`\`\`

Sage 10.9 for the **good ordinary** case: \`lp._prec_bounds(3,3)[2]=2\`, so the source-derived modulo-\(p^2\) \(T^2\)-coefficient determines the exact leading coefficient's valuation \(1\). Stein–Wuthrich (2013), [Algorithm 11.1 page 1783](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf), writes the ordinary upper-bound formula with \(\operatorname{Reg}_\gamma=\operatorname{Reg}_p/\log(\gamma)^r\), precisely the normalized regulator used in Sage's \`sha_tate.an_padic\`. Thus **the supersingular printed \`Reg_p\` versus \`Reg_gamma\` discrepancy does not apply to p16231**. Kato's proven p-primary bound is zero **provided the genuine historical source/data and \(J_{\mathrm{ref}}\) identification are accepted**.

## 4. Remaining trust and publication boundary

- All original 263m full pair contributions are independently processed in two algorithms but share this original V65 eclib/Manin oracle. Authenticity of the V65 table and independent Sage samples are the target of the new test.
- Original V11 producer reproducibly built byte-identically from original sources; archived checkpoint chain and 57 original producer chunks have actually been replayed; neither is a formal compiler-correctness theorem.
- New Sage checker is **not yet executed**, so no new PASS claim is made here.
- The full original \`lp.series(n=3)\` and \`E.sha().p_primary_bound(16231)\` remain unexecuted. The ordinary Kato/Sage bound follows *mathematically* from the source-derived analytic coefficient if the finite authentic inputs are trusted; it does not follow from logs alone.
- No exact p-adic equality \`u_p=1\` and no all-prime BSD formula are claimed.

Tracked in [issue #7](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/7).
