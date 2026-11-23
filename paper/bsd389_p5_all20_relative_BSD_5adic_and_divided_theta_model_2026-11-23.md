# E389a1 — relative analytic BSD 5-valuations and an exact divided-theta Selmer comparison model

**2026-11-23. Status:** A mathematically exact *relative analytic* 5-adic valuation, given previously authenticated original theta histograms and the standard modular-symbol interpolation; and an **abstract candidate** Selmer module matching the analytic prediction. Predicted orders of the *true* Sha require exact BSD over Q and K; they are NOT proved by the present note or by a Fitting inclusion.

## 1. Degree-25 fields and discriminant

Let E:y^2+y=x^3+x^2−2x, with conductor389, rank2, no rational torsion and Tamagawa product1. The twenty real cyclic K_r/Q are defined by primitive even degree25 characters of conductor n=q1*q2=5351*13001=69568351. Every nontrivial Galois character of K_r has conductor n; thus the conductor–discriminant formula gives

\[
[K_r:\mathbf Q]=25,\quad |\Delta_{K_r}|=n^{24},\quad\sqrt{|\Delta_{K_r}|}=n^{12}.
\]

The original 20 Mazur–Tate polynomials F_r have the genuine nontrivial character-product valuations

\[
a_r=v_5\!\left(\operatorname{Res}(F_r,(X^{25}-1)/(X-1))\right)=
\begin{cases}8& r\bmod5\in\{1,2\},\\12&r\bmod5\in\{3,4\}.\end{cases}
\]

All 40 exact order5/order25 cyclotomic resultants were separately certified as nonzero. Input SHA256 is 1a22c0ed1b4ac336a648ec0a0bf1d6121fd6224993c37e928713117cd1d4c463.

The earlier genuine twisted nonvanishing certifies that E(K_r)=E(Q) has rank2 and torsion 0 under the documented arithmetic hypotheses.

## 2. Where exactly FOUR powers of 5 go: BSD regulator

The Néron–Tate height *for BSD* over K is non-normalized: on points rational over Q, height over K is [K:Q] times height over Q. With the same saturated rational generators P,Q,

\[
\boxed{\operatorname{Reg}(E/K_r)=25^2\operatorname{Reg}(E/\mathbf Q)},
\qquad v_5(\mathrm{Reg}_K/\mathrm{Reg}_Q)=4.
\]

**Do not use** the base-change-invariant normalized height, which would incorrectly remove these four powers. Sage official reference for height_pairing_matrix and regulator_of_points, option normalised=False:
https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_number_field.html .

## 3. The relative *analytic* BSD quotient has exact 5-valuation a_r−4

Birch–Stevens/Mazur–Tate evaluation of the original even modular symbol yields, for each of the 24 nontrivial characters chi,
\[
F_r(\chi)\doteq_5 \tau(\chi)\,\frac{L(E,\chi^{-1},1)}{\Omega_E^+}.
\]
The factor denoted by \(\doteq_5\) is a 5-adic **unit** (a harmless 2-power and convention-dependent p-unit); this is a source-normalization obligation already audited in the project. The character conductor n is prime to 5.

All characters occur in inverse pairs, are even and primitive of conductor n. Thus their Gauss sums obey
\[
\tau(\chi)\tau(\chi^{-1})=\chi(-1)n=n,
\quad\prod_{\chi\ne1}\tau(\chi)=n^{12}=\sqrt{|\Delta_{K_r}|}.
\]
This is an **exact** Gauss-sum/discriminant cancellation. Archimedean periods over totally real K_r are 25 copies of the real period of E/Q, up to powers of 2; these are 5-adic units. The sole bad reduction at 389 is I_1, and K_r is unramified there, so all finite-place Tamagawa factors are 5-units (indeed equal 1 under the established reduction data).

Let \(\mathcal B(E/F)\) denote the real analytic BSD leading quotient: first nonzero Taylor coefficient of \(L(E/F,s)\), multiplied by torsion-order squared, divided by the full BSD period (including \(1/\sqrt{|\Delta_F|}\)), the *non-normalized* Néron–Tate regulator and all Tamagawa factors. No assumption that \(\mathcal B(E/F)=\#\Sha(E/F)\) is made in this definition.

Artin factorization, nonvanishing of all twists, period cancellation, and the above Gauss identity give an algebraic, in fact rational, *relative* quotient \(\mathcal B(E/K_r)/\mathcal B(E/\mathbf Q)\) with

\[
\boxed{v_5\!\left(\frac{\mathcal B(E/K_r)}
{\mathcal B(E/\mathbf Q)}\right)
=a_r-4=
\begin{cases}4& r\bmod5=1,2,\\8&r\bmod5=3,4.\end{cases}}
\]

The transcendental leading coefficient of the rank-two base curve cancels in this relative expression. The calculation of this algebraic 5-valuation does **not** assume full BSD, but depends on authentic theta/period normalization.

**Strong BSD prediction only:** If the exact formula is assumed over Q and every K_r, then \(\mathcal B(E/F)=\#\Sha(E/F)\). The previously certified base \(\Sha(E/\mathbf Q)[5^\infty]=0\) therefore yields the following **conditional predicted true Sha orders**:

\[
\boxed{\#\Sha(E/K_r)[5^\infty]
\overset{\mathrm{BSD}}=
\begin{cases}5^4=625& r\bmod5=1,2,\\
5^8=390625&r\bmod5=3,4.\end{cases}}
\]

These predictions are coherent with the previously **proved conditional-on-inputs** lower bound 25 via genuine Poitou–Tate local defect. They are not themselves certified Sha computations.

## 4. An exact candidate X whose Fitting ideal equals the REAL theta

Let R=Z5[C25], T=sigma-1, N=sum_{i=0}^{24}sigma^i. Write the authentic F_r(1+T)=sum_{j=0}^{25}c_jT^j, with c0=0, c25=0 and c1=25k integral.

The actual group ring relation is
\[
(1+T)^{25}-1=25T+\sum_{j=2}^{25}{25\choose j}T^j=0.
\]
It gives an **integral exact factorization in R**, not division inside a domain:
\[
\boxed{\theta_r=T^2H_r,\quad
H_r(T)=\sum_{j=0}^{23}\left(c_{j+2}-k{25\choose j+2}\right)T^j.}
\]

Define the explicitly computable finite group-ring module

\[
Y_r^{\rm model}=R/(N,H_r),\qquad
X_r^{\rm model}=(R/(T))^2\oplus Y_r^{\rm model}.
\]

Because N*T=0 exactly, multiplicativity of Fitting ideals yields

\[
\boxed{\operatorname{Fitt}_{0,R}(X_r^{\rm model})
=(T^2)(N,H_r)=(\theta_r).}
\]

This **equality** is stronger than the known one-sided Bullach–Honnor theorem for actual arithmetic Selmer. The model also has free rank-two trivial Mordell–Weil quotient, norm-annihilated torsion, and three generators. But this algebra does NOT construct an isomorphism with the true Selmer module.

The determinant of multiplication by T on the free rank24 Z5 module R/(N) is N(1)=25, so its square has valuation4. The exact factorization theta=T²H gives

\[
v_5\det(H_r|R/(N))=a_r-4,\quad
\boxed{\#Y_r^{\rm model}=5^{a_r-4}}.
\]

Thus the algebraic candidate reproduces **exactly** the conditional analytic BSD prediction. This singles out a very concrete conjectural Sha module size, not a proof that this module equals the true Sha.

An independent pure-Python exact computation of the AUTHENTIC r=1 histogram has already produced the Smith structure
\[
\boxed{Y_1^{\rm model}\cong(\mathbf Z/25\mathbf Z)^2,\qquad\#Y_1^{\rm model}=5^4,}
\]
while R/(N,theta_1) had elementary factors (25,25,25,25), order5^8. For r=3,4 mod5, do NOT guess the model's finer elementary factors until the complete 20-row source program runs.

Reproducer: verification/bsd389_p5_all20_theta_divided_T2_candidate_Sha_smith_gate.py, which derives all20 H_r from the genuine histogram, certifies SHA256, recomputes the two Smith matrices and checks the exact length subtraction4. The user has NOT run this new script yet.

## 5. The single genuine remaining arithmetic gap for these fields

One needs a **two-sided arithmetic comparison** (or actual full Selmer presentation) fixing the genuine norm coinvariant length
\[
\operatorname{length}_{\mathbf Z_5}(X_r/NX_r)
\overset{?}=4+(a_r-4)=a_r,
\]
equivalently (by the existing proved norm-quotient exact sequence), proving \(\#\Sha(E/K_r)[5^\infty]=5^{a_r-4}\). The one-sided Fitting containment alone does not imply this: explicit countermodels with smaller nonzero Sha groups have already been constructed and verified.

This note advances a **precise numerical target and explicit algebraic comparison model**, but does not prove exact Sha orders, the all-large-p uniform Sha support bound over Q, or the complex exact BSD identity for 389a1 over Q.


## 6. An explicit order-25 symplectic Galois representation in the r=1 candidate

The authentic r=1 25-integer theta histogram is
\[
(-424,9536,-424,3388,5172,-8022,-2658,-1240,-9294,-1588,
-1580,-1512,9782,3208,3208,9782,-1512,-1580,-1588,-9294,
-1240,-2658,-8022,5172,3388).
\]
The exact divided theta H_1 has Taylor coefficients modulo 25
\[
(H_0,H_1,H_2,H_3)\equiv(15,0,11,14)\pmod{25}.
\]
The previously independently computed Smith form of \(R/(N,H_1)\) is \((25,25)\). Since \(H_1\bmod5\) begins at \(T^2\), the classes \(1,T\) generate this 25-torsion module. The exact quotient relation obtained from H and the group relation is
\[
\boxed{T^2=10+10T\quad\text{on }Y_1^{\rm model}.}
\]
Consequently the Galois generator \(\sigma=1+T\), in basis (1,T), acts as
\[
\boxed{
S=\begin{pmatrix}1&10\\1&11\end{pmatrix}\in SL_2(\mathbf Z/25).
}
\]
Direct arithmetic yields \(S^5=\begin{pmatrix}1&0\\5&1\end{pmatrix}\ne I\), but \(S^{25}=I\). Therefore this action has **exact order 25** and its restriction to 5-torsion is the nontrivial unipotent matrix
\[
S\bmod5=\begin{pmatrix}1&0\\1&1\end{pmatrix},
\]
with precisely one dimension of G-invariants. Because \(\det S=1\), it preserves the perfect alternating form \(((x,y),(u,v))\mapsto(xv-yu)/25\bmod\mathbf Z\).

This is an exact **Cassels–Tate-compatible algebraic candidate**, satisfying the earlier genuine Poitou–Tate invariant-dimension obstruction as well as the relative BSD predicted 5-order \(5^4\). It is **not a calculation of actual Sha**, nor a reason to assert the true Sha is isomorphic to the candidate.

Executable independent check: verification/bsd389_p5_val1_r1_divided_theta_symplectic_candidate_gate.py .
