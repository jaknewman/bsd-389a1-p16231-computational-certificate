# A genuine global primitive integral modular-symbol vector for 389a1 — exact limits for rank-two Sha

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
