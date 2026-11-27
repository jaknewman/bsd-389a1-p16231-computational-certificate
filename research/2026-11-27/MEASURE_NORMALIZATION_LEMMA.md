# Uniform finite-level \(p^2\) stabilization in the tame-trivial cyclotomic component

**Independent mathematical lemma, 27 November 2026.**
This verifies an analytic *normalization step*, not a global proof of BSD or a full comparison of the cyclotomic Selmer group.

## Setup

Take an odd prime \(p\ge5\) and a periodic rational modular symbol \(m^+(x)\) integral at \(p\). For ordinary reduction let \(\alpha\in\mathbf Z_p^\times\) satisfy \(\alpha^2-a_p\alpha+p=0\). For split multiplicative reduction put \(\alpha=a_p=1\).

The standard ordinary \(p\)-adic measure on units is

\[
\mu_\alpha(a+p^2\mathbf Z_p)
=\alpha^{-2}m^+(a/p^2)-\alpha^{-3}m^+(a/p).
\]

[SageMath reference for the measure formula](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/padic_lseries.html). The split multiplicative case requires the usual exceptional Euler factor and the matching \(p\)-adic L-function convention.

Define

\[
j_p(a)\equiv-\frac{a^{p-1}-1}{p}\pmod p,\quad p\nmid a.
\]

Then \(j_p(a)\) is the exponent of the pro-\(p\) part of \(a\) with respect to \(\gamma=1+p\) modulo \(p^2\); the group of tame characters is killed by pushing the measure forward to \(\Gamma\simeq 1+p\mathbf Z_p\). For each \(0\le k<p-1\), put

\[
R_{p,k}=\sum_{a\in(\mathbf Z/p^2)^\times}m^+(a/p^2)\binom{j_p(a)}k.
\]

## Exact lemma (all \(p\ge5\))

For any \(0\le k\le p-2\),

\[
\boxed{\quad
[T^k]\bigl(\mu_\alpha|_{\Gamma}\bigr)
\equiv \alpha^{-2}R_{p,k}\pmod p.\quad}
\]

**Proof.** Fix \(r\in(\mathbf Z/p)^\times\) and consider its \(p\) lifts \(a=r+pt\) modulo \(p^2\). The binomial theorem yields

\[
j_p(r+pt)\equiv j_p(r)+tr^{-1}\pmod p.
\]

Thus \(j_p(r+pt)\) ranges through the entire \(\mathbf F_p\). Periodicity makes \(m^+((r+pt)/p)=m^+(r/p)\) independent of \(t\). The contribution of the \(\alpha^{-3}\) stabilization term in coefficient \(T^k\) is therefore, for this fixed \(r\),

\[
m^+(r/p)\sum_{j=0}^{p-1}\binom jk
=m^+(r/p)\binom p{k+1}\equiv0\pmod p
\]

whenever \(k+1<p\). Summing over \(r\) gives the assertion. \(\square\)

At a **good ordinary prime**, \(\alpha\equiv a_p\bmod p\), so in particular

\[
[T^2]L_p^{(\eta=0)}(E,T)
\equiv a_p^{-2}R_{p,2}\pmod p.
\]

This is the usual integral unit-root-normalized p-adic L-function, subject to identifying the chosen modular-symbol normalization with the Néron-period normalization of the primary source. The identity is **uniform in \(p\)**; its proof does not use that the rank is 2 or that any Sha group is finite.

## Executed regressions

Command from this PR:

\`\`\`bash
cd research/2026-11-27/verification
python3 bsd389_measure_projection_audit.py --primes 5 7 11 13 17 89 389
\`\`\`

| Prime | \(a_p\) | Raw \(R_{p,2}\) | Normalized \([T^2]\) |
|---:|---:|---:|---:|
| 5 | -3 | 2 | 3 |
| 7 | -5 | 5 | 3 |
| 11 | -4 | 2 | 7 |
| 13 | -3 | 2 | 6 |
| 17 | -6 | 1 | 9 |
| 89 | -8 | 8 | 78 |

All stabilization corrections in degrees \(\le2\) are zero mod \(p\) (the exact log is in \`results/measure_projection_audit.log\`). For split multiplicative \(p=389\), with \(\alpha=1\), degrees \(0,1,2,3\) equal \((0,0,0,321)\) mod \(389\).

## What is and is not closed

**Closed:** cancellation of the finite-level \(p^2\) stabilization correction in degrees \(k\le p-2\); the precise tame-trivial cyclotomic coordinate; six independently computed small good-ordinary instances and the split multiplicative coefficient at 389.

**Still requires source-specific verification:** a correct Néron-period identification for the 390-entry Manin table, the \(p=389\) exceptional-zero normalization in the exact analytic \(L_p\), the relevant full-cyclotomic-versus-\(\Gamma\)-Selmer projection in Wuthrich's corollary 19, Greenberg's hypotheses, and an independent full re-run of all 297 ordinary primes. **The above lemma does not claim the complete BSD formula.**
