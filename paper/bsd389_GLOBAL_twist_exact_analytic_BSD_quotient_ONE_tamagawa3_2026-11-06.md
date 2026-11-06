# Exact rank-ZERO analytic BSD quotient of E^(-3) is ONE (still not a theorem that Sha is trivial)

Date 2026-11-06. A global, p-independent calculation of the COMPLETE EXPLICIT ANALYTIC SIDE of the rank-zero BSD formula for the -3 twist, including the precise minimal period, real components, torsion and all Tamagawa factors. No previous p-primary test is repeated. **Does not assert any unproved all-prime Sha conclusion or complete BSD for rank-two E389a1.**

Set E/Q: y²+y=x³+x²−2x, conductor 389. For d=-3 use the integral twist model
\[
E_d:\quad y^2+y=x^3-3x^2-18x-7,
\]
with discriminant \(3^6\cdot389=283581\), conductor \(3^2\cdot389=3501\), and rank E_d(Q)=0, E_d(Q)_tors={O}, as established separately by exact nonzero L(E_d,1) and the prior full rational-points theorem E(Q(sqrt(-3)))=E(Q).

## 1. True minimal model and its real period

The only nonzero discriminant valuations are v_3(Delta)=6 and v_389(Delta)=1, both <12, so this integral model is minimal at every prime. Complete the square, write the original 3 real roots e1>e2>e3 of x³+x²−2x+1/4 and A=e1−e3. The twist has reverse-ordered roots -3e3>-3e2>-3e1, so the full real Neron period (TWO connected real components) obeys the EXACT relation
\[
\Omega_{E_d}=\frac4{\sqrt{3A}}K((e_1-e_2)/A)
=\frac{2}{\sqrt3}\Omega_E^-.
\]
Our previous new modular-symbol theorem with c_E=1 proves EXACTLY
\[
L(E_d,1)=\frac4{\sqrt3}\Omega_E^-.
\]
Consequently \(L(E_d,1)/\Omega_{E_d}=2\) **exactly, not to numerical precision**.

## 2. Exact Tamagawa factors (minimal Tate algorithm)

At the prime 389, the original E has multiplicative reduction of type I_1. Quadratic twisting by d=-3, unramified at 389, leaves the Kodaira type I_1 (possibly changing split/non-split), and in either case its component-group order is
\[
\boxed{c_{389}(E_d)=1.}
\]

At p=3 the minimal discriminant has valuation 6 and conductor exponent 2. The Tate algorithm identifies type I_0^*. To see the rational component count explicitly, make the **integral change of variables** y_old=Y+4, obtaining
\[
Y^2+9Y=x^3-3x^2-18x-27.
\]
Thus the relevant normalized cubic in Tate's Step 6 is
\[
\begin{aligned}
P(U)&=U^3+(a_2/3)U^2+(a_4/3^2)U+a_6/3^3\\
&=U^3-U^2-2U-1.
\end{aligned}
\]
Modulo 3, exact factorization gives
\[
\boxed{P(U)=(U-1)(U^2+1)\quad\text{in }\mathbf F_3[U].}
\]
The quadratic factor is irreducible over F3, and the cubic is squarefree because its discriminant is -31, a unit at 3. For type I_0^*, the Tamagawa number is \(1+\#\{\text{distinct roots of }P\text{ in }\mathbf F_3\}\), so **one** rational root gives
\[
\boxed{c_3(E_d)=2.}
\]
All other primes are good, so the global Tamagawa product is exactly 2.

This is the standard Tate-algorithm Step 6 component count; see Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, IV.9, or Barrios–Roy–Sahajpal–Tallana–Tobin–Wiersema, *Local data of elliptic curves under quadratic twist*, Research in Number Theory (2025/26) for local I0* root-count rules.

## 3. Nonconjectural identity for the *analytic BSD quotient* of the twist

Since E_d(Q)={O}, regulator in rank zero is 1 and torsion order is 1. Therefore all KNOWN terms on the rank-zero BSD right side give
\[
\boxed{
\frac{L(E_d,1)\cdot\#E_d(Q)_{\rm tors}^{2}}
{\Omega_{E_d}\operatorname{Reg}(E_d)\prod_\ell c_\ell(E_d)}
=\frac{2}{2}=\boxed1.
}
\]

This is an EXACT algebraic-analytic equality among known independently defined quantities, established WITHOUT assuming Sha finite or BSD.

**Do not infer \(\Sha(E_d/Q)=0\) from this identity alone.** Full rank-zero BSD would assert that this normalized number ALSO equals \(\#\Sha(E_d/Q)\), and that extra implication is a substantive separate theorem. We already know the twist's Sha is finite by the analytic-rank-zero theorem, but its order was not calculated from an independent Selmer bound in this note.

## 4. Role in the global rank-two E389a1 project

The quadratic twist now introduces no unknown algebraic MW index, torsion, total period, real component multiplicity, or Tamagawa correction. In the exact Artin factorization
\[
\frac{L''(E/K,1)}2=L(E_d,1)\frac{L''(E,1)}2,
\quad K=\mathbf Q(\sqrt{-3}),
\]
the twist's archimedean factor is exactly \((4/\sqrt3)\Omega_E^-\), and its *normalized rank-zero analytic BSD quotient* equals 1.

This removes real normalizations from a future rank-two Weil-restriction transfer. It is NOT a proof of:
- all-prime finiteness, triviality or a global order for Sha(E/Q),
- any p-independent Selmer Fitting bound,
- rationality or exact equality of Q_E=L''(E,1)/(2\Omega_E\operatorname{Reg}_E).

**All p=16231 first-layer projects remain de-prioritized**; this computation advances only the global complex/Weil-restriction workstream, not an isolated prime.

References: integral modular-symbol twist L-value note and exact twist real period note in the same PR; standard Tate algorithm and published local data.
