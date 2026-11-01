# Hecke forces the *entire degree-≤2 Mazur–Tate jet* into its mixed TU component

**2026-11-01.** New exact algebraic theorem from the published Hecke relation for modular symbols. Together with the user's genuine p5 direct computation, it shows why \`M00=M10=M01=0\` **and even the as-yet-unprinted pure quadratic moments vanish modulo p** for *all* pairs of p-admissible primes, not just p=5. This does **not** force the mixed coefficient \`M11\` to be nonzero, so it does not prove all-prime \(\Sha\) finite or full BSD.

## 1. Hypotheses and group-ring notation

Let \(E/\mathbf Q\) be a modular elliptic curve of conductor \(N\), let \(p\ge5\) be a prime and let \(q_1,q_2\) be distinct good primes away from \(pN\) with
\[
q_i\equiv1\pmod p,\qquad a_{q_i}(E)\equiv q_i+1\equiv2\pmod p.
\]
Let \(m(r)=[r]^+_E\in\mathbf Z_{(p)}\) be a common, p-integral Néron-normalized sign-plus modular symbol. Write \(h_i=q_i-1\), \(G_i=(\mathbf Z/q_i\mathbf Z)^\times\), and select primitive roots \(g_i\) and corresponding discrete logarithm exponents \(j_i:G_i\to\mathbf Z/h_i\mathbf Z\).

Define the **unregularized** modular-symbol group-ring elements
\[
\theta_{q_i}(X)=\sum_{x\in G_i}m(x/q_i)\,X^{j_i(x)}
  \ \in\ \mathbf Z_{(p)}[X]/(X^{h_i}-1),
\]
and
\[
\Theta_{q_1q_2}(X,Y)=
\sum_{\substack{x\in G_1\\y\in G_2}}
m(a(x,y)/(q_1q_2)) X^{j_1(x)}Y^{j_2(y)}
\]
in the two-variable group ring, with \(a(x,y)\) the CRT representative \(1\le a<q_1q_2\).

**Warning about naming:** these unregularized \(\theta,\Theta\) are the exact raw sums used in the user's p5 implementation. Some published Mazur–Tate conventions use a different *regularized* modular symbol; no unproved identification between those two conventions is made here. The Kurihara raw weighted sum agrees with the coefficient \([TU]\) of this explicit \(\Theta\) in the established project normalization.

## 2. The exact Hecke identity on the marginal: a second-order Euler factor

For any prime \(q\nmid N\) and rational r the weight-2 newform modular symbol satisfies the **exact identity**
\[
a_q\,m(r)=m(qr)+\sum_{t=0}^{q-1}m((r+t)/q).
\tag{H}
\]
This is reproduced, with precisely this normalization, in [Mazur–Rubin lecture notes *Modular symbols (continued)*, Lemma 1.1(vii)(a)](https://bpb-us-e1.wpmucdn.com/sites.harvard.edu/dist/a/189/files/2023/01/MODULAR-SYMBOLS-CONTINUED.pdf) and is consistent with the [standard \(T_q\) operator](https://docs.magma-maths.org/ModularArithmeticGeometry/ModularSymbols/operators.html).

Fix \(x\in G_1\) and apply (H) with \(r=x/q_1\), \(q=q_2\). Its \(q_2\) terms \(m((x+tq_1)/(q_1q_2))\) sweep every CRT residue in the \(q_2\)-coordinate, including **one nonunit** term at \(a(x,0)=q_2z\), where \(z\equiv q_2^{-1}x\pmod{q_1}\). Since \(m(r+1)=m(r)\), the nonunit term equals \(m(q_2^{-1}x/q_1)\). Hence
\[
\boxed{
\sum_{y\in G_2}m(a(x,y)/(q_1q_2))
=a_{q_2}m(x/q_1)-m(q_2x/q_1)
-m(q_2^{-1}x/q_1).}\tag{1}
\]
This identity holds over the original rational coefficient ring, before reducing modulo p.

Put \(d_1=j_1(q_2\bmod q_1)\in\mathbf Z/h_1\mathbf Z\). Taking the \(X\)-weighted sum over \(x\in G_1\) and reindexing the two multiplication actions gives an **exact group-ring identity**:
\[
\boxed{
\Theta_{q_1q_2}(X,1)
=\bigl(a_{q_2}-X^{d_1}-X^{-d_1}\bigr)\theta_{q_1}(X).}\tag{2}
\]
Similarly with \(d_2=j_2(q_1\bmod q_2)\),
\[
\boxed{
\Theta_{q_1q_2}(1,Y)
=\bigl(a_{q_1}-Y^{d_2}-Y^{-d_2}\bigr)\theta_{q_2}(Y).}\tag{3}
\]

## 3. The *triple* augmentation-ideal consequence (strictly stronger than only three zero coefficients)

Let \(I_i=(X-1)\) or \((Y-1)\) denote the augmentation ideal in the respective \(\mathbf F_p[G_i]\).

By q-admissibility \(a_{q_2}\equiv2\bmod p\). Thus, modulo p, the factor in (2) is
\[
2-X^{d_1}-X^{-d_1}=
-X^{-d_1}(X^{d_1}-1)^2\in I_1^2.
\tag{4}
\]
Likewise the factor in (3) belongs to \(I_2^2\).

**Furthermore, each one-prime theta has zero augmentation mod p.** Apply the exact Hecke identity (H) at \(r=0\) and \(q=q_1\):
\[
a_{q_1}m(0)=m(0)+\sum_{t=0}^{q_1-1}m(t/q_1)
\quad\Longrightarrow\quad
\boxed{\theta_{q_1}(1)=(a_{q_1}-2)m(0).}\tag{5}
\]
So, since \(a_{q_1}\equiv2\bmod p\) and \(m(0)\) is p-integral, \(\bar\theta_{q_1}(1)=0\), i.e. \(\bar\theta_{q_1}\in I_1\). Likewise \(\bar\theta_{q_2}\in I_2\). **For 389a1, \(m(0)=0\) also holds exactly because \(L(E,1)=0\), but this extra fact is unnecessary here.**

Combining (2)–(5) gives the uniform stronger congruences
\[
\boxed{
\bar\Theta_{q_1q_2}(X,1)\in I_1^3,\qquad
\bar\Theta_{q_1q_2}(1,Y)\in I_2^3.
}\tag{6}
\]
This holds **for all p≥5 and admissible pairs**, with no assumption on analytic/MW rank or \(\Sha\).

Since p divides h_i, the group-ring relation \((1+T)^{h_i}-1\) has no terms of degree \(\le2\) mod p; degree-2 Taylor expansion is well defined. If
\[
\Theta_{q_1q_2}(1+T,1+U)
=\sum_{i,j\ge0}M_{ij}T^iU^j,
\]
then (6) immediately forces
\[
M_{00}=M_{10}=M_{20}=M_{01}=M_{02}=0
\quad(\bmod p).
\]
**The only possibly nonzero term of TOTAL degree ≤2 is \(M_{11}TU\)**:
\[
\boxed{
\Theta_{q_1q_2}(1+T,1+U)
\equiv \widetilde\delta_{q_1q_2}\,TU
\pmod{p,(T,U)^3}.}\tag{7}
\]
The coefficient is the two-prime Kurihara sum since
\([TU](1+T)^k(1+U)^\ell=k\ell\).

This is stronger than the previously published \(\bmod(T^2,U^2)\) statement: the two **pure quadratic moments** vanish automatically as well. **Crucially, (7) does NOT assert \(\widetilde\delta_{q_1q_2}\ne0\)**; it shows that the entire lower jet has a unique *possible* nonzero component, not that the component survives.

## 4. Actual p5 user-run evidence, and the genuine new interpretation

The user's p5 direct Sage/eclib computation at \(q_1=41,q_2=61\) reports
\[
(M_{00},M_{10},M_{01},M_{11})=(0,0,0,4)\pmod5,
\]
plus independently verified \(\widetilde\delta_{2501}=4\pmod5\), root-change \(4\to3\) by factor 2, and maximal mixed matrix rank 39. [Verbatim successful user run](../results/bsd389_p5_real_kurihara_mixed_jet_SAGE_PASS_2026-11-01.md).

By the exact universal Hecke argument above **we can now deduce** (without guessing or claiming new terminal output)
\[
M_{20}=M_{02}=0\pmod5
\]
for those same p5 modular-symbol data, and hence
\[
\boxed{
\Theta_{2501}(1+T,1+U)\equiv4TU
\pmod{5,(T,U)^3}.}
\]
This is an **arithmetically and algebraically justified** bivariate leading jet, not an extrapolation to other p. If someone wants an independent numeric regression for pure quadratic coefficients, the existing p5 direct script could be extended to output these two values, but no extra heavy computation is mathematically required to prove their vanishing.

## 5. Why the result is not a global BSD theorem

The same Hecke structure applies to every admissible pair at every good p≥5. It **does not distinguish which p** have \(\widetilde\delta_{q_1q_2}\not\equiv0\). The mixed term is left free by Hecke, and a p-unit single classical modular symbol at denominator 389 supplies no lower bound on this specific mixed functional at varying n.

Under Kim's exact theorem (at good p with its Galois/normalization hypotheses), the *existence* of a unit mixed term for some admissible pair is precisely the \(\Sha[p^\infty]=0\) issue, not an automatic conclusion from (7).

**Remaining global challenge:** give a p-independent integral arithmetic mechanism that forces the *mixed coefficient itself* to be nonzero for at least one p-admissible pair for every p outside an explicit finite set, or construct a genuinely global integral Selmer/Fitting comparison. No such mechanism has been proved here. Full \(\Sha\) finiteness and exact complex rank-two BSD leading term remain unproved.
