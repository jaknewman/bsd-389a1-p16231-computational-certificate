# Theorem: exact Néron normalization of the 390-edge Manin vector for 389a1

**27 November 2026 — precise scope.** The exact normalization of the 389a1 Manin rational modular-symbol eigenline is certified using (i) a proven integrality theorem for closed cusp paths, (ii) a rigorously bounded numerical Fourier/AGM computation of one or all 388 corresponding values, and (iii) an exact rank-one Manin/Hecke calculation. This is **not** a proof of BSD, nor a proof of any uniform Sha vanishing.

## Statement

Let \(E:y^2+y=x^3+x^2-2x\) be the \(\Gamma_0(389)\)-optimal curve, let \(f=\sum_{n\ge1}a_n q^n\) be its normalized weight-2 newform, and let \(\omega_E=dx/(2y+1)\) be its Néron differential.

Let \(v\in\mathbf Z^{390}\) be the integral Manin table in \`verification/manin_390.txt\`, SHA-256

\`9bce8b66c37b7f257f5a6015c08806c2b80c36d1e47356677e3819fc171e8360\`.

Then the rational plus modular symbols represented by \(v\) have exactly the standard *Néron real-period normalization*, and in particular, for every \(a\in\{1,\ldots,388\}\),

\[
m_v^+(a/389)=
\frac{\Re\left(2\pi i\int_{\infty}^{a/389}f(z)\,dz\right)}{\Omega_E^+}
\quad\text{exactly}.
\]

Here \(\Omega_E^+\approx2.49021256085505507532\) is the **least positive real period**, not the real BSD factor \(\Omega_E^{\rm BSD}=2\Omega_E^+\approx4.98042512171011015064\) (two real components).

## Proof 1: exact integrality at conductor denominator

For each \(a\) with \(\gcd(a,389)=1\), choose integers \(b,d\) with \(ad-389b=1\) and put

\[
\gamma_a=\begin{pmatrix}a&b\\389&d\end{pmatrix}\in\Gamma_0(389).
\]

The cusps \(\infty\) and \(a/389=\gamma_a\infty\) are equivalent on \(X_0(389)\); therefore \([\infty,a/389]\) is a closed homology cycle.

The curve E is \(X_0(389)\)-optimal and semistable. By Česnavičius' theorem on the Manin constant in the semistable case, \(c_E=1\). Hence for the optimal parametrization \(\phi:X_0(389)\to E\),

\[
\phi^*\omega_E=\pm2\pi i f(z)\,dz
\]

and the integral above lies, up to sign, in the Néron period lattice \(\Lambda_E\).

The minimal discriminant of E is \(+389\), so E(\(\mathbf R\)) has two components, the period lattice can be chosen rectangular, and every \(\lambda\in\Lambda_E\) has real part in \(\Omega_E^+\mathbf Z\). Consequently

\[
m_E^+(a/389)\in\mathbf Z.
\]

Primary references:
- Česnavičius, *The Manin constant in the semistable case*, Compositio Mathematica (2018), https://www.cambridge.org/core/journals/compositio-mathematica/article/abs/manin-constant-in-the-semistable-case/42D5D9E3E5F758E35C12E5FB5BA1781E
- LMFDB 389a1: optimal=yes, Manin constant=1, discriminant=389, BSD real period=4.980425..., https://www.lmfdb.org/EllipticCurve/Q/389a1/
- SageMath convention for normalized plus modular symbols: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/mod_sym_num.html

## Proof 2: certified Fourier and period enclosures

Define \(F(z)=\sum_{n\ge1}(a_n/n)e^{2\pi i n z}\). For \(ad-389b=1\), the automorphy \(f|_2\gamma=f\) gives the exact identity

\[
2\pi i\int_{\infty}^{a/389}f(z)\,dz
=F((a+i)/389)-F((-d+i)/389).
\]

The \(a_n\) are reconstructed **without using v** from finite-field point counts and exact Hecke recurrences. With \(e_3<e_2<e_1\) the three roots of \(4x^3+4x^2-8x+1\), the real Néron period is

\[
\Omega_E^+=\frac{\pi}{
\operatorname{AGM}\!\left(1,\sqrt{\frac{e_1-e_2}{e_1-e_3}}\right)
\sqrt{e_1-e_3}}.
\]

The code \`verification/bsd389_certified_interval_388.py\` isolates the three roots by 140 iterations of *rational* bisection, bounds the AGM from both sides, and evaluates the above Fourier expressions with **outward-rounded interval arithmetic** (\`mpmath.iv\`). Terms are grouped by their residue class modulo 389, reducing trigonometric operations to 195 cosines.

For any \(M\), Deligne's estimate \(|a_n|\le d(n)\sqrt n\le 2n\) gives the rigorously bounded absolute tail

\[
\left|\mathrm{tail}\right|\le
\frac{4e^{-2\pi(M+1)/389}}{1-e^{-2\pi/389}}.
\]

With \(M=2500\), 65 decimal interval digits, the exact interval tests prove for **all 388** values that

\[
\left|
\frac{\Re\bigl(2\pi i\int_\infty^{a/389}f(z)\,dz\bigr)}
{\Omega_E^+}
-m_v^+(a/389)
\right|<5\cdot10^{-16}.
\]

This strict inequality is checked by interval comparisons, *not* by ordinary floats. Together with **integrality from Proof 1**, each interval contains exactly one possible true value, namely the indicated integer. Thus the 388 values are equal **exactly**, without Sage/eclib.

The interval operations in \`mpmath.iv\` have rigorous enclosure semantics according to its documentation, although the library labels this support experimental. A second Arb/Sage interval implementation would be beneficial for external publication review.

## Proof 3: rank-one rational Hecke eigenspace fixes the entire vector

The preexisting exact \`universal_manin_exact_certificate.py\` verifier, rerun on this same table, reports:

- 1,170 exactly satisfied Manin \(S,R,+\) relations;
- 1,307 exactly satisfied \(T_2=-2\) Hecke relations;
- rank 389 of the combined linear relation matrix over \(\mathbf F_7\);
- a nonzero integral vector \(v\) in the kernel.

Hence the relation matrix has rank exactly 389 over \(\mathbf Q\) and its rational kernel is **one dimensional**. The genuine analytic modular-symbol vector satisfies the same relations and is consequently a scalar multiple of \(v\). The *exactly certified* anchor \(m_E^+(7/389)=-1=m_v^+(7/389)\) forces this scalar to be 1.

Therefore the **entire 390-component rational modular-symbol vector** is identified with the analytically Néron-normalized eigenvector, not merely its 388 evaluated values.

## How to reproduce

From the repository checkout:

\`\`\`bash
python3 -m pip install mpmath
python3 research/2026-11-27/verification/bsd389_certified_interval_388.py
\`\`\`

The program uses no Sage, Magma, external data service, or floating-point approximation in its formal assertions. It is fast on a typical machine (around a second with interval precision 65 digits). The source and the exact execution transcript are committed in this PR.

## Limits

1. The conclusion is **the exact normalization of the modular-symbol eigenline** for conductor 389, independent of BSD.
2. It validates a key input for p-adic L-function coefficients *at all p*, but does not by itself prove those coefficients never vanish for p>1999.
3. It does not establish the supersingular signed Selmer comparisons, the p-adic main conjecture, or the exact complex leading term in rank two.
