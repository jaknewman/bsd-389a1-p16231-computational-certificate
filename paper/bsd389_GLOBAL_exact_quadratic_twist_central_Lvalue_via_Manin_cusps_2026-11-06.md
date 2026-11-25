# An EXACT global central L-value for the -3 twist of E=389a1, obtained without BSD

Date 2026-11-06. **This is a new direct complex modular-symbol proof.** No local p-primary, Gross/Brandt, Iwasawa, regulator or Sha certificate is rerun. The proof uses the previously rigorously certified *coarse* interval for the rank-zero twist, the known theorem of Manin–Drinfeld, Česnavičius's semistable optimal Manin-constant theorem, and a short exact rational interval audit. **This does NOT prove rank-two BSD, Sha finiteness or any rank-two analytic-to-height identity.**

## Definitions and exact statement

Let
\[
E/\mathbf Q:\quad y^2+y=x^3+x^2-2x
\]
be the optimal elliptic curve of conductor \(N=389\), equipped with minimal invariant differential \(\omega_E=dx/(2y+1)\). Its rational torsion is trivial; its analytic central value is 0 exactly. Let
\[
f_E(z)=\sum_{n\ge1}a_n e^{2\pi i n z}
\]
be the normalized modular newform.

The real cubic of E is
\(f_0(x)=x^3+x^2-2x+\frac14=(x-e_1)(x-e_2)(x-e_3)\)
with \(e_1>e_2>e_3\) real. Put \(A=e_1-e_3\), \(m=(e_1-e_2)/A\), and let
\[
\Omega_E^-:=\frac{2}{\sqrt{A}}K(m)
=\frac{\pi}{\sqrt A\ \operatorname{AGM}(1,\sqrt{1-m})}
\]
be the **least positive imaginary part of a period** of E; equivalently, the purely imaginary primitive period is \(i\Omega_E^-\). Here
\(K(m)=\int_0^{\pi/2}(1-m\sin^2\theta)^{-1/2}d\theta\)
uses the PARAMETER convention, not the elliptic modulus convention.

**THEOREM (exact global complex equality for the rank-zero -3 twist):**
\[
\boxed{\quad L(E^{(-3)},1)=\frac4{\sqrt3}\,\Omega_E^-
=\frac8{\sqrt{3A}}K(m).\quad}\tag{1}
\]
The identity is nonconjectural. It is NOT the rank-two BSD formula for E.

## Step 1: the optimal Manin constant is exactly one

The optimal modular parametrization \(\varphi:X_0(389)\to E\) sends the cusp \(\infty\) to the identity. Because N=389 is squarefree, the **proved** semistable Manin constant theorem of Kęstutis Česnavičius, *The Manin constant in the semistable case*, Compositio Math. 154 (2018), Theorem 1.2, gives
\[
\varphi^*\omega_E = \pm 2\pi i\, f_E(z)\,dz.
\]
Choose the sign consistent with the positive Fourier coefficient a1=1 (or absorb the harmless sign in the period lattice).

Since E(Q)_tors=0, the image of EVERY rational cusp on X0(389) is the identity: by Manin–Drinfeld, the difference of any two cusps is torsion in J0(389), so its image in E is a rational torsion point, hence zero. The cusps \(1/3\), \(2/3\) and \(\infty\) are all rational cusps. Thus the image of a modular path \(\infty\to1/3\) is a CLOSED LOOP on E, even though its endpoints on X0(389) are distinct.

Consequently
\[
F(1/3):=2\pi i\int_\infty^{1/3} f_E(z)\,dz
=\sum_{n\ge1}\frac{a_n}{n}e^{2\pi in/3}
\quad(\text{with radial/cuspidal Abel limit})
\]
lies in the full **integral** complex period lattice \(\Lambda_E\), not merely its rational span. This is where the *global integral Manin theorem* matters. No numerical observation proves lattice membership.

## Step 2: quadratic Gauss transform isolates the imaginary integer

Let \(\chi=\chi_{-3}\), primitive conductor three, with \(\chi(1)=1,\chi(2)=-1\) and \(\tau(\chi)=i\sqrt3\). The standard twisted modular-symbol/Gauss identity, obtained first in a convergent Mellin region and analytically continued, gives
\[
L(E,\chi,1)
=\frac{F(1/3)-F(2/3)}{i\sqrt3}.
\]
Since all a_n are real,
\(F(2/3)=\overline{F(1/3)}\).
The real cubic of E has three distinct roots (discriminant 389/16>0), so the period lattice has rectangular basis \(\Omega_E^+\) (positive real) and \(i\Omega_E^-\), with \(\Omega_E^-\) the primitive positive imaginary period. Since \(F(1/3)\in\Lambda_E\), there is an integer \(m_0\in\mathbf Z\) with
\[
\mathrm{Im}F(1/3)=m_0\Omega_E^-.
\]
Hence
\[
\boxed{L(E^{(-3)},1)=\frac{2m_0}{\sqrt3}\Omega_E^-,\qquad m_0\in\mathbf Z.}\tag{2}
\]
This rationality/integrality is a THEOREM from modular-symbol and Manin-Drinfeld geometry; it is not the unknown rank-two ratio \(L''(E,1)/(2\Omega_E\mathrm{Reg})\).

## Step 3: determine the integer from a very coarse RIGOROUS bound

The project's existing Fraction-only rational approximate-functional-equation certificate proved
\[
\frac92<L(E^{(-3)},1)<\frac{23}5.
\]
To enclose \(\Omega_E^-\) without floating-point assumptions, put \(g(x)=x^3+x^2-2x+1/4\). Its sign changes (checked by exact rational arithmetic) at each of the following disjoint pairs:
\[
e_3\in(-2041/1000,-2039/1000),\quad
e_2\in(134/1000,136/1000),\quad
e_1\in(904/1000,906/1000).
\]
Therefore
\[
2.94<A<2.96,\quad 0.26<m<0.27.
\]
The positive coefficient series for \(K(m)\) is
\[
K(m)=\frac\pi2\sum_{j\ge0}
 \left(\binom{2j}{j}4^{-j}\right)^2m^j,
\]
where \(c_0=1,c_1=\frac14,c_2=\frac9{64}\) and all \(c_j\le\frac9{64}\) for j≥2. Hence
\[
1+\frac m4
\le \frac{2K(m)}\pi
\le 1+\frac m4+\frac9{64}\frac{m^2}{1-m}.
\]
Using the classical rational bounds \(3.14<\pi<22/7\),
\[
1.714<\sqrt A<1.721,
\]
we get the entirely rational certificate
\[
\frac{33441}{17210}<\Omega_E^-<
\frac{27791335}{14013664},
\]
in particular
\[
\boxed{1.9<\Omega_E^-<2.1.}
\]

Since \(1.7<\sqrt3<1.75\), equation (2) gives
\[
\boxed{
\frac{51}{28}<m_0<\frac{161}{76}.}
\]
The ONLY integer in that interval is \(m_0=2\). Substitution into (2) proves exact identity (1). QED.

The entire interval/sign/root proof is independently executable with standard Python fractions in the companion verifier and was actually executed by the assistant. The interval for the twist L-value itself is an ALREADY ARCHIVED independent exact-rational result, not reevaluated here.

## Step 4: real-period normalization (exact, independent of any p)

For the same three real roots, the standard period formula is
\[
\boxed{
\Omega_E^{\mathrm{total}}=\frac4{\sqrt{e_1-e_3}}\,
K\!\left(\frac{e_2-e_3}{e_1-e_3}\right)
=\frac{2\pi}{\sqrt A\,\operatorname{AGM}
(1,\sqrt{1-(e_2-e_3)/A})}.
}\tag{3}
\]
There are exactly TWO connected components in E(R) because discriminant 389>0, hence the total Néron period is **twice** its least positive real period. This formula is an exact normalization check and does NOT prove equality with the Néron–Tate regulator.

For orientation only (not the proof):
\(\Omega_E^{\mathrm{total}}\approx4.9804251217101101506427155838846049203\),
\(\Omega_E^-\approx1.97173770155164820442240769815134233485\),
\(L(E^{(-3)},1)\approx4.553533171048712\).

## Scope: this is a global analytic rank-zero input, not full BSD

The proof makes the twist's rank-zero **complex L-value** exactly equal to an explicit period multiple, and simultaneously fixes the real Néron period of E with an AGM expression. These are useful fixed factors in the global quadratic Artin factorization
\[
\frac{L''(E/K,1)}2
=L(E^{(-3)},1)\frac{L''(E,1)}2.
\]

The two truly missing GLOBAL rank-two obligations remain:
- an arithmetic theorem proving Sha(E/Q) finite for **all p at once** (and its exact order, ideally 1);
- an independent proof that the complex rank-two quotient \(L''(E,1)/(2\Omega_E\operatorname{Reg}(E))\) is exactly rational and equal to that order.

The new exact identity (1) establishes neither of these. In particular it would be WRONG to replace \(L''(E,1)/2\) by \(L(E^{(-3)},1)\), use a rank-zero theorem to infer rank-two BSD, or claim exact rationality of the rank-two quotient from the rank-zero modular symbol argument.

## Sources
- Kęstutis Česnavičius, *The Manin constant in the semistable case*, Compositio Math. 154 (2018), Theorem 1.2: https://arxiv.org/abs/1703.02951 .
- Manin–Drinfeld torsion theorem for differences of cusps, classical modular curves; e.g. Cremona's standard modular-symbol references.
- Sage/eclib modular-symbol algorithm's documented sign conventions and period normalization: https://sporadic.stanford.edu/reference/arithmetic_curves/sage/schemes/elliptic_curves/mod_sym_num.html .
- Existing exact twist interval in repo: paper/bsd389_Kminus3_conductor53_p16231_Castella_Hsieh_exact_gates_2026-11-05.md (Section 3).
- Existing direct all-p attack in this branch: paper/bsd389_DIRECT_GLOBAL_exact_Mellin_Lstar_uniform_Sha_two_gates_2026-11-06.md .
