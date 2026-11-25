# Exact GLOBAL rank-zero algebraic special value: L(E^(-3),1)/Omega(E^(-3)) = 2

Date: 2026-11-06. **New exact arithmetic-normalization theorem, independent of BSD.** No old prime-local certificates have been rerun, and no all-p Sha finiteness or rank-two BSD assertion is made.

We previously proved using Manin–Drinfeld, the semistable optimal Manin constant c_E=1, the Gauss transform for chi_-3, and a rigorously certified *coarse* central L-value interval, that
\[
\boxed{L(E^{(-3)},1)=\frac4{\sqrt3}\,\Omega_E^-}
\]
with \(\Omega_E^-\) the least positive imaginary period of E (see preceding note \`bsd389_GLOBAL_exact_quadratic_twist_central_Lvalue_via_Manin_cusps_2026-11-06.md\`).

**THEOREM.** For the full BSD real Néron period of the quadratic twist, using its globally minimal model, one has
\[
\boxed{\,\Omega_{E^{(-3)}}^{\rm total}=\frac2{\sqrt3}\,\Omega_E^-\,,
\qquad\frac{L(E^{(-3)},1)}{\Omega_{E^{(-3)}}^{\rm total}}=2.}
\]

**Proof.** Complete the square in the original curve:
\[
Y=y+\frac12,\quad Y^2=f_0(x)=x^3+x^2-2x+\frac14.
\]
Twisting by d=-3 and using X=dx, Y_d=d^2Y gives
\[
Y_d^2=X^3-3X^2-18X-\frac{27}{4}.
\]
Shifting \(y_d=Y_d-\frac12\) gives the INTEGRAL model
\[
\boxed{E^{(-3)}:\quad y_d^2+y_d=X^3-3X^2-18X-7.}
\]
Its discriminant is \(d^6\Delta_E=729\cdot389=283581=3^6\cdot389\). As both nonzero valuations (6 at 3 and 1 at 389) are below 12, a change of variables cannot reduce its discriminant by a factor of \(p^{12}\) at either prime, and it is already minimal globally; it has good reduction everywhere else.

Write \(e_1>e_2>e_3\) for the three real roots of \(f_0\), with \(A=e_1-e_3\), \(m_-=(e_1-e_2)/A\). The roots of the twist's completed-square cubic are \(-3e_3>-3e_2>-3e_1\). For a cubic with 3 real roots \(v_1>v_2>v_3\), the TOTAL Néron real period of the 2-component real elliptic curve is
\[
\Omega^{\mathrm{total}}=\frac4{\sqrt{v_1-v_3}}K\left(\frac{v_2-v_3}{v_1-v_3}\right).
\]
Here \(v_1-v_3=3A\), and \((v_2-v_3)/(v_1-v_3)=(e_1-e_2)/A=m_-\), hence
\[
\Omega_{E^{(-3)}}^{\mathrm{total}}=\frac4{\sqrt{3A}}K(m_-).
\]
The least positive imaginary period of the original E is
\[
\Omega_E^-=\frac2{\sqrt A}K(m_-).
\]
Therefore the first boxed equality holds, and dividing the previously proved exact L-value by this period gives
\[
L(E^{(-3)},1)/\Omega_{E^{(-3)}}^{\rm total}
=\frac{4\Omega_E^-/\sqrt3}{2\Omega_E^-/\sqrt3}=\boxed2.
\]
QED.

For orientation only: using high-precision mpmath with the exact cubic coefficients gives
\(\Omega_E^-\approx1.97173770155164820442240769815134233485\),
\(\Omega_{E^{(-3)}}^{\rm total}\approx2.27676658552435615456977439318585953673\),
\(L(E^{(-3)},1)\approx4.5535331710487123091400161\).
The proof is the exact root transformation plus the already proved modular-symbol integer, NOT this numerical ratio.

**Significance for the *global* BSD objective:** The rank-zero twist contributes EXACTLY an algebraic special-value factor 2 (not just an unknown rational, and not a numerical guess) to quadratic Artin factorization. Its Mordell–Weil group has already been proved trivial, so no twist torsion/regulator ambiguity remains. Nevertheless BSD for this rank-zero twist would additionally require a theorem on its Sha and Tamagawa product; the identity \(L/\Omega=2\) ALONE DOES NOT prove \(\Sha(E^{-3})\) trivial.

More importantly, this proves NOTHING about the unknown rank-two ratio
\[
Q_E=\frac{L''(E,1)/2}{\Omega_E\operatorname{Reg}_E}.
\]
Even with the rank-zero twist's L/Omega factor known EXACTLY, that ratio's rationality and the global finiteness of Sha(E/Q) remain independent missing theorems.

Source: Česnavičius 2018 semistable Manin constant; Manin–Drinfeld cusp torsion; standard real/imag elliptic periods. Parent modular-symbol proof in the same PR.
