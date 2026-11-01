# Two-prime Kurihara weights are *mixed* finite-difference functionals: exact algebraic lemma

**2026-11-01. Status:** self-contained combinatorial theorem about the weight appearing in Kurihara's numbers. Not a global Euler-system theorem, not a new \(\Sha\) vanishing result, and no claim that a primitive 389-cusp modular symbol forces any particular two-prime Kurihara number nonzero.

## 1. The actual new numerical source certificate

On the Sage user's Ubuntu system, after 389/389 independent Sage/eclib modular symbol comparisons, the user re-ran the direct one-cusp test and **all eight direct oracle evaluations passed**:
```text
ONE_CUSP_DIRECT_VALUE_PASS oracle sage a 382 value -1
ONE_CUSP_DIRECT_VALUE_PASS oracle sage a 384 value -2
ONE_CUSP_DIRECT_VALUE_PASS oracle sage a 7 value -1
ONE_CUSP_DIRECT_VALUE_PASS oracle sage a 5 value -2
ONE_CUSP_DIRECT_VALUE_PASS oracle eclib a 382 value -1
ONE_CUSP_DIRECT_VALUE_PASS oracle eclib a 384 value -2
ONE_CUSP_DIRECT_VALUE_PASS oracle eclib a 7 value -1
ONE_CUSP_DIRECT_VALUE_PASS oracle eclib a 5 value -2
ONE_CUSP_BOTH_SAGE_ECLIB_8_DIRECT_VALUES_PASS checks 8
ONE_CUSP_EXACT_BEZOUT_PASS (-1)-(-2)=1
ONE_CUSP_P_UNIFORM_CLASSICAL_SYMBOL_UNIT_PASS m_plus(7/389)=-1 all_rational_primes
BOUNDARY_NO_TWO_PRIME_KURIHARA_OR_SHA_FITTING_IMPLICATION
```
These are genuine user-reported outputs, not a new GitHub CI execution. [Verbatim log](../results/bsd389_single_cusp_global_unit_USER_RUN_PASS_2026-11-01.md).

Thus, for the Néron-period-normalized sign-plus symbol of E389a1,
\[
m_E^+(7/389)=-1,\quad m_E^+(5/389)=-2,
\]
which proves **only** that the classical modular-symbol eigensymbol has a p-unit value for *every* rational prime.

## 2. Exact CRT weight algebra

Fix an odd prime p. Let \(q_1,q_2\) be distinct auxiliary primes with \(p\mid q_i-1\), and let \(G_i=(\mathbf Z/q_i\mathbf Z)^\times\), of order \(h_i=q_i-1\). Let \(g_i\) be primitive roots and
\[
j_i:G_i\to\mathbf F_p,\quad j_i(g_i^k)=k\bmod p.
\]
Then \(\sum_{x\in G_i}j_i(x)=h_i(h_i-1)/2=0\) in \(\mathbf F_p\), because \(p\mid h_i\) and \(2\in\mathbf F_p^\times\).

Via the CRT, \(G=(\mathbf Z/q_1q_2\mathbf Z)^\times\simeq G_1\times G_2\).
For \(f:G_1\times G_2\to\mathbf F_p\) define the (un-normalized) weighted functional
\[
L_{q_1,q_2}(f)=
\sum_{x\in G_1}\sum_{y\in G_2}j_1(x)j_2(y)\,f(x,y).
\]
For **arbitrary anchor points** \(x_0\in G_1,y_0\in G_2\), let the mixed anchored finite difference be
\[
\Delta_{x_0,y_0}f(x,y)=
f(x,y)-f(x,y_0)-f(x_0,y)+f(x_0,y_0).
\]

**Theorem, exact for EVERY f and every p odd meeting q-admissibility:**
\[
\boxed{L_{q_1,q_2}(f)=L_{q_1,q_2}(\Delta_{x_0,y_0}f).}
\]

**Proof:** Expanding the right-hand side, the terms depending only on x are multiplied by \(\sum_yj_2(y)=0\); the terms depending only on y are multiplied by \(\sum_xj_1(x)=0\); the constant term is multiplied by the product of these two zero sums. The only remaining term is \(L_{q_1,q_2}(f)\). QED.

**Consequences:**
1. \(L_{q_1,q_2}(f)=0\) for every **additively separable** \(f(x,y)=u(x)+v(y)\), even if some \(f(x,y)=-1\) or even if the vector of f-values is primitive over \(\mathbf Z\).
2. Let \(V=\mathrm{Fun}(G_1\times G_2,\mathbf F_p)\) and \(V_1+V_2\subset V\) be the subspace of additively separable functions. Then
   \[
   \dim_{\mathbf F_p}V/(V_1+V_2)
   =h_1h_2-(h_1+h_2-1)=(h_1-1)(h_2-1).
   \]
   The functional \(L_{q_1,q_2}\) factors through this mixed-variation quotient. It is nonzero on the whole quotient (since j1,j2 are nonzero), but **may vanish on the particular 1-dimensional E modular-symbol eigenline**.
3. At odd p, \(j_i(-1)=h_i/2=0\) modp, so \(j_i(-x)=j_i(x)\). The mixed weight respects the sign-plus involution. This symmetry explains *compatibility* with plus symbols, not nonvanishing.

## 3. What the genuine Kurihara number adds

For the elliptic curve E, the function is **not arbitrary**, but
\[
f_E(x,y)=m_E^+\!\left(\frac{a(x,y)}{q_1q_2}\right)\bmod p,
\]
where \(a(x,y)\) is the CRT representative, with exact integral period/Manin normalization. Its weighted image is the Kurihara quantity \(\widetilde\delta_{q_1q_2}(E)\) modulo p **under the chosen established sign and scalar conventions**.

The single already-verified value \(m_E^+(7/389)=-1\) concerns a **different denominator** and does not determine the mixed \(\Delta f_E(x,y)\) at any auxiliary conductor \(q_1q_2\). No equality of the fixed-cusp evaluation and these mixed functionals exists on the entire ambient function space. The missing theorem must involve the E-eigenline, Hecke/distribution relations, and the arithmetic obstruction measured by the **second Selmer Fitting ideal**.

For the good primes covered by Kim and Castella–Sano on this curve, a nonzero two-prime Kurihara witness is **equivalent** to vanishing of the p-primary Sha group; postulating nonvanishing for all p would therefore assume the main uniform Sha goal, not prove it.

**Honest next research question:** Is there a theorem, with specified local Selmer conditions and a genuine Euler/Kolyvagin derivative, proving the *mixed* weighted functional cannot annihilate the integral E eigensymbol for every p outside a fixed finite set? This requires new arithmetic input; the pure mixed-difference lemma here supplies the exact functional target but **not** the needed non-annihilation.

[Source p-uniform one-cusp proof](bsd389_fixed_rational_manin_Dg1_exact_certificate_and_limit_2026-11-01.md) · [uniform prime-support issue](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8).
