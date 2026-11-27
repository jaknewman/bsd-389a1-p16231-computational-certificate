# Independent analytic normalization audit of the integral level-389 Manin table

Date: 27 November 2026

**New result:** 388/388 *numerical* plus modular-symbol values at denominator 389 agree with the table used in the p-adic computations, using an independent Fourier construction and an independently evaluated Néron real period. This checks the overall sign and scale of the table, not just its Manin/Hecke relations.

## Construction without modular-symbol input

Work with \(E:y^2+y=x^3+x^2-2x\), conductor \(N=389\). Let

\[
f(z)=\sum_{n\ge1}a_n e^{2\pi i n z}
\]

be the attached normalized newform, \(a_\ell=\ell+1-\#E(\mathbf F_\ell)\) at good primes and \(a_{389}=1\) at split multiplicative reduction. Generate the \(a_n\) by the Hecke recursions; **no cached modular symbol is used**.

Define

\[
F(z)=\sum_{n\ge1}\frac{a_n}{n}e^{2\pi i n z}.
\]

For any \(1\le u<389\), let \(d\in\mathbf Z\) satisfy \(ud\equiv1\pmod{389}\), and choose \(b\) such that \(ud-389b=1\). Then
\(\gamma=\bigl(\begin{smallmatrix}u&b\\389&d\end{smallmatrix}\bigr)\in\Gamma_0(389)\). The differential \(2\pi i f(z)\,dz\) is \(\Gamma_0(389)\)-invariant, and

\[
F(\gamma z)-F(z)=2\pi i\int_{\infty}^{u/389} f(w)\,dw
\]

is constant in \(z\). With \(z_0=(-d+i)/389\), one has \(\gamma z_0=(u+i)/389\). Thus **exactly**

\[
\boxed{\;
2\pi i\int_{\infty}^{u/389}f(w)\,dw
=
\sum_{n\ge1}\frac{a_n}{n}e^{-2\pi n/389}
\left(e^{2\pi i n u/389}-e^{-2\pi i n d/389}\right).
\;}
\]

The plus modular symbol is the real part divided by the **least positive real Néron period** \(\Omega_E^+\).

## Independent Néron period

Complete the square:

\[
(2y+1)^2=4x^3+4x^2-8x+1.
\]

Let \(e_1>e_2>e_3\) be its three distinct real roots. The least positive period of \(dx/(2y+1)\) is

\[
\boxed{\;
\Omega_E^+
=\frac{2 K((e_2-e_3)/(e_1-e_3))}{\sqrt{e_1-e_3}}
=\frac{\pi}{\operatorname{AGM}(1,\sqrt{(e_1-e_2)/(e_1-e_3)})\sqrt{e_1-e_3}}.
\;}
\]

The roots and AGM are computed directly, without period data from Sage/eclib or LMFDB.

## Truncation bound and actual result

For all n the Deligne bounds give \(|a_n|\le d(n)\sqrt n\le2n\); hence after truncation at \(M\), the *absolute complex integration tail* is bounded by

\[
\left|\mathrm{tail}\right|\le
4\frac{e^{-2\pi(M+1)/389}}{1-e^{-2\pi/389}}.
\]

With \(M=6800\), this is \(\le4.90\times10^{-46}\), while double-precision summation and the AGM introduce separate rounding errors (not yet bounded by intervals).

### Executed

\`\`\`bash
python3 research/2026-11-27/verification/bsd389_independent_analytic_manin_audit.py
\`\`\`

- Integral Manin-table SHA-256: \`9bce8b66c37b7f257f5a6015c08806c2b80c36d1e47356677e3819fc171e8360\`.
- \(\Omega_E^+=2.4902125608550545\) (AGM floating-point).
- \(m^+(5/389)=-2\) and \(m^+(7/389)=-1\) to about \(10^{-15}\).
- All 388 symbols match their exact integer Manin-table entries with maximum observed absolute difference \(\approx1.62\times10^{-14}\).
- The input table appears **only in the final comparison**, not in the calculation of \(a_n\), \(F\), or \(\Omega_E^+\).

This is a genuinely independent numerical **global-normalization audit**. It is much stronger than comparing internal Hecke and Manin identities, but a proof-quality certified analytic comparison needs interval arithmetic to rigorously bound floating point errors.

## Exact follow-up available in Sage/eclib

The file \`verification/bsd389_sage_eclib_exact_anchors.py\` implements independent exact rational comparison of the same 388 symbols through \`E.modular_symbol(sign=1,implementation="eclib")\`. It requires Sage/eclib and is **provided but not executed here**. See [SageMath modular symbol documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_modular_symbols.html), which defines the Néron real period normalization and documents correctly normalized modern eclib symbols.

## Remaining BSD limitations

The analytic comparison supports the source table's scale and sign and thus greatly strengthens the basis for interpreting its p-adic moments. It does not establish the finite-order Sha vanishing uniformly at all primes, the supersingular exceptional cases, or the *exact complex BSD leading-term equality*.
