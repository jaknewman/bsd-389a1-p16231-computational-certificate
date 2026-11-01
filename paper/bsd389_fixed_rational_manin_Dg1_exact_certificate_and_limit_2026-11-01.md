# A genuine global primitive integral modular-symbol vector for 389a1 — exact limits for rank-two Sha

## 2026-11-01 independent JSON audit PASS — an even shorter **ONE-CUSP** certificate

The user has now run \`verification/bsd389_fixed_rational_manin_independent_audit.py\` against the actual exported canonical JSON, without Sage or eclib. All assertions passed: exact matching SHA256 \`9719d0863045ef63fe3519b23da0c4bb74303ee3d84cb9791f95e2a29d456dd4\`; all 389 fractions, 228 nonzero, \`D=g=1\`, all 389 sign-plus evenness comparisons and an explicit two-term Bézout identity.

**Actual coefficients, not guessed:**
\[
v_{382}=m_E^+(382/389)=-1,\qquad
v_{384}=m_E^+(384/389)=-2,
\qquad
1\cdot v_{382}+(-1)\cdot v_{384}=(-1)-(-2)=1.
\]
In fact **Bézout is unnecessary**: \(\boxed{v_{382}=-1}\) alone is a unit at **every** prime. Since \(382\equiv-7\bmod389\), periodicity and the independently checked sign-plus evenness give
\[
\boxed{m_E^+(7/389)=m_E^+(382/389)=-1.}
\]
Similarly \(m_E^+(5/389)=-2\). A **one-cusp** rational normalized modular symbol furnishes a *completely fixed prime-uniform symbol nonvanishing certificate*. This conclusion is logically stronger in economy than just knowing \(\gcd(v_a)=1\), although it does not strengthen the bound on Selmer.

Verbatim [independent user-run stdout](../results/bsd389_fixed_rational_manin_independent_JSON_USER_RUN_PASS_2026-11-01.md). A new two-oracle one-cusp direct Sage/eclib regression is published at [\`verification/bsd389_single_cusp_global_unit.py\`](../verification/bsd389_single_cusp_global_unit.py), **not yet executed by the user**. It independently checks the four cusps \(a=382,384,7,5\) under both symbol implementations, instead of looking up the JSON again.

### Structural obstruction to a naive uniform Kurihara functional identity

For an auxiliary conductor \(n=q_1q_2\) with each \(q_i\equiv1\bmod p\), let \(j_i\) be the discrete logarithm modulo p on \((\mathbf Z/q_i\mathbf Z)^\times\). For p **odd**,
\[
\sum_{x\in(\mathbf Z/q_i\mathbf Z)^\times}j_i(x)
\equiv\sum_{k=0}^{q_i-2}k
=\frac{(q_i-1)(q_i-2)}2\equiv0\bmod p,
\]
since \(p\mid q_i-1\) and 2 is invertible. Via the Chinese remainder theorem, the two-prime Kurihara weight \(w(x)=j_1(x)j_2(x)\) has **augmentation zero**:
\[
\sum_{x\in(\mathbf Z/n\mathbf Z)^\times}w(x)
=\big(\sum j_1\big)\big(\sum j_2\big)\equiv0\bmod p.
\]

Thus the associated weighted functional annihilates the **constant function 1** on the full function space on \((\mathbf Z/n\mathbf Z)^\times\), whereas a single-cusp evaluation does not. Consequently **no universal identity between these functionals exists on the entire unrestricted ambient function space**. This does NOT say the particular cuspidal \(E\)-eigensymbol is killed. It shows the required bridge must **incorporate the cuspidal/Hecke eigenspace and compatibility of levels**, not simply equate a single cusp evaluation with a raw sum of all two-prime weights.

The additional *needed arithmetic statement* remains: some p-admissible \(n=q_1q_2\) must yield \(\widetilde\delta_n(E)\not\equiv0\bmod p\) for each target p, or a different integral Selmer comparison. The \(-1\) symbol in the fixed \(\{a/389\}\) sample does **not** prove this nonvanishing. At p covered by Kim, making that inference without further work is equivalent to assuming the desired \(\Sha[p^\infty]=0\) conclusion.

---

**Date 2026-11-01. Status:** the arithmetic source calculation has been **genuinely user executed** with 389/389 independent Sage/eclib equality checks. This is a strong global modular-symbol certificate, NOT a rank-two Euler-system class, two-prime Kurihara witness, all-p Fitting bound, Sha finiteness result or proof of strong BSD.

## 1. Fixed arithmetic input, constructed without using Sha

For E=389a1 with exact Néron-period normalization, the original exporter computed
\[
v_a=m_E^+(a/389)\in\mathbf Q\qquad(0\le a<389).
\]
Here \(m_E^+\) is the sign \(+1\) classical modular symbol with the `L_ratio` normalization. The user ran the production script with both independent symbol implementations, `implementation='sage'` and `implementation='eclib'`, and all **389 individual rational values** agreed.

The user-run stdout, with no inferred entries, reports:
```text
FIXED_M389_EXACT_ALL_SAGE_ECLIB_MATCH_PASS 389
FIXED_M389_NONZERO_SYMBOLS 228
FIXED_M389_RATIONAL_DENOMINATOR_LCM 1
FIXED_M389_INTEGRAL_SCALED_CONTENT 1
FIXED_M389_PRIMITIVE_VECTOR_CONTENT_PASS 1
FIXED_M389_EXACT_BEZOUT_WITNESS_PASS gcd 1 nonzero_coefficients 2
FIXED_M389_EXACT_CANONICAL_JSON_SHA256 9719d0863045ef63fe3519b23da0c4bb74303ee3d84cb9791f95e2a29d456dd4
```
Full original evidence: [user-executed log](../results/bsd389_fixed_rational_manin_content_USER_RUN_PASS_2026-11-01.md).

These results prove, **subject to the authenticity of the standard Sage/eclib arithmetic computations**, that
\[
\boxed{v\in\mathbf Z^{389},\quad \gcd(v_0,\ldots,v_{388})=1.}
\]
The exporter checks an exact integer Bézout identity \(\sum_a c_av_a=1\) with **exactly two nonzero terms**. The positions and individual integer coefficients are contained in the user-local canonical JSON and have **not yet been uploaded/reviewed**, so they are intentionally not invented here.

Consequently, the vector remains nonzero over \(\mathbf F_p\) for **every** rational prime p:
\[
\forall p,\quad v\bmod p\ne0.
\]
Indeed if all v_a were divisible by p, their gcd would be divisible by p, contradicting the exact gcd 1. This is a genuinely **all-p** modular-symbol primitive-vector result, not a finite scan or a p-adic extrapolation.

## 2. A one-line algebraic reason this does NOT imply the two-prime Kurihara criterion

A family of constrained linear functionals \(W_p\subseteq\operatorname{Hom}_{\mathbf F_p}(\mathbf F_p^d,\mathbf F_p)\) can annihilate a nonzero, even primitive, vector. Example for **every p**:
\[
v=(1,0)\in\mathbf Z^2,\qquad
W_p=\mathrm{span}_{\mathbf F_p}\{(x_1,x_2)\mapsto x_2\}.
\]
Then \(\gcd(v_1,v_2)=1\) and \(v\bmod p\ne0\), yet
\(\ell(v)=0\) for **every** \(\ell\in W_p\). Thus primitive rational-symbol values alone do not establish that even one *constrained* weighted Kurihara functional is nonzero.

In the actual BSD project, a two-prime \(\widetilde\delta_{q_1q_2}\) is a very specific weighted sum over units mod \(q_1q_2\), defined by local discrete logarithms and a p-dependent auxiliary admissibility condition. The ordinary fixed 389-cusp sample is **not** the family of those weighted sums. A rigorous bridge would require an **actual** comparison identifying those weights with functionals on a suitable fixed Manin module, plus a theorem that they cannot all annihilate the E eigensymbol modulo p.

**This missing non-annihilation statement is substantially stronger** than primitivity. By Mazur + Castella–Sano, unrestricted-degree Kurihara nonvanishing is already known for all good p≥11, but Kim's theorem requires nonvanishing at exactly **two** auxiliary primes to force \(\Sha[p^\infty]=0\). The new \(D=g=1\) computation does not bypass this degree-two constraint.

## 3. Reproducible independent audit without Sage or another 389-cusp run

[Verification script](../verification/bsd389_fixed_rational_manin_independent_audit.py), to run after pulling the repository, reads the original user-local `~/bsd389_fixed_rational_manin_content.json`. It recomputes the **canonical JSON SHA256** against the user-reported pinned digest, parses all 389 rational values with `fractions.Fraction`, checks nonzero count 228, denominator lcm 1, content gcd 1, integral primitive vector, and the **two-term exact Bézout identity**. It also checks the expected evenness under \(a\mapsto-a\bmod389\) for the sign+ modular symbols. Its output will print the two cusp positions and their individual symbol and Bézout coefficients, not just their number.

**This independent audit is not yet user-executed**, so neither the two indices nor an additional PASS are claimed. It does not recompute any modular-symbol value from Sage; independence here is from the exporter's **integer arithmetic and serialization checks**, not from the underlying two modular-symbol algorithms (which already agreed independently in the original user run).

## 4. What counts as genuine further progress toward strong BSD

The exact invariant needed is still, for every p,
\[
\operatorname{Fitt}_{2,\mathbf Z_p}
\bigl(\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee\bigr)
=\operatorname{Fitt}_{0,\mathbf Z_p}
\bigl(\Sha[p^\infty]^\vee\bigr).
\]
An actual proof from the new fixed modular-symbol vector would have to **construct and verify a p-independent integral, cohomological comparison** from the appropriate arithmetic special element to this Fitting ideal, with field-extension norm relations and local conditions; simply *naming* that comparison would be circular. The Mazur–Rubin *core rank* for the standard unramified elliptic \(T_pE\) Selmer setup is 1 under its hypotheses, not 2 simply because the Mordell–Weil rank is 2. One must not misapply theorems of higher core rank.

**Full BSD:** proving \(\Sha\) globally finite/trivial would still leave the exact complex leading-term formula \(L''(E,1)/2=\Omega_E\mathrm{Reg}(E)\#\Sha\) as a distinct obligation. No result of that kind follows from this modular-symbol table.

Tracking: [uniform Sha issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8), [complex leading-term issue #9](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/9).
