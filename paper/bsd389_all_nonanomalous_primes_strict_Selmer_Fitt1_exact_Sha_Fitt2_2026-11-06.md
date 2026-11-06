# An exact **integral** strict-Selmer Fitting formula for every nonanomalous good prime of E=389a1

Date: 2026-11-06. **New proof; the previous huge local certificates were not rerun.** This identity does NOT require any finiteness assumption on Sha. It connects the true Sha Fitting ideal to a genuinely defined strict Selmer group, but does NOT yet connect the generalized Kato class to that ideal.

## Set-up

Let E/Q be 389a1, E(Q)=Z P⊕Z Q with P=(-1,1), Q=(0,-1), torsion zero. For any good prime p≥5 such that p does **not** divide N_p=#E(F_p) (nonanomalous), put
\[
S_p=\operatorname{Sel}_{p^\infty}(E/\mathbf Q),\quad
S_p^0=\ker(S_p\to H_f^1(\mathbf Q_p,E[p^\infty])),\quad
A_p=\Sha(E/\mathbf Q)[p^\infty].
\]
At good nonanomalous p, reduction E(Q_p)→E(F_p) shows the p-adic completion of E(Q_p) is its formal subgroup E_1(Q_p), and the formal logarithm gives
\(E(Q_p)^\wedge_p\cong p\mathbf Z_p\).
Thus
\[
H_f^1(\mathbf Q_p,E[p^\infty])\cong\mathbf Q_p/\mathbf Z_p.
\]
The *local* Kummer homomorphism from MW p-infinity is represented by
\[
\lambda_p:(\mathbf Q_p/\mathbf Z_p)^2\to\mathbf Q_p/\mathbf Z_p,\qquad
(x,y)\mapsto a_p x+b_p y,
\]
where **these are log coefficients, NOT the trace of Frobenius**:
\(a_p=\log_{\omega_E}(P)/p\in\mathbf Z_p\), \(b_p=\log_{\omega_E}(Q)/p\in\mathbf Z_p\).
Define \(d_p=\min(v_p(a_p),v_p(b_p))\). It is finite since non-torsion Q-rational points have nonzero p-adic elliptic logarithm.

## Theorem: exact integral strict Selmer control, all nonanomalous good p

For every such p, the following statements hold without assuming Sha finite:

**(1)** Localisation restricted to MW is surjective, and
\[
\ker\lambda_p\cong
  (\mathbf Q_p/\mathbf Z_p)\oplus \mathbf Z/p^{d_p}\mathbf Z.
\]

**(2)** There is an exact sequence of p-primary groups
\[
\boxed{
0\to(\mathbf Q_p/\mathbf Z_p)\oplus\mathbf Z/p^{d_p}
\to S_p^0\to A_p\to0.
}\tag{1}
\]
The left term is the actual MW-localisation kernel, not a postulated higher Euler-system class. After splitting off its divisible summand one has
\[
S_p^0\cong(\mathbf Q_p/\mathbf Z_p)\oplus T_p',
\qquad
0\to\mathbf Z/p^{d_p}\to T_p'\to A_p\to0,
\]
for some cofinitely generated p-primary \(T_p'\). These splittings are noncanonical.

**(3)** For the *true* integral Selmer Pontryagin dual and *every* such p,
\[
\boxed{
\operatorname{Fitt}_{1,\mathbf Z_p}((S_p^0)^\vee)
 =
p^{d_p}\operatorname{Fitt}_{0,\mathbf Z_p}(A_p^\vee)
 =
p^{d_p}\operatorname{Fitt}_{2,\mathbf Z_p}(S_p^\vee).
}\tag{2}
\]

In particular, if \(d_p=0\) then \(S_p^0\cong(\mathbf Q_p/\mathbf Z_p)\oplus A_p\) and
\[
\boxed{
\operatorname{Fitt}_1((S_p^0)^\vee)
=\operatorname{Fitt}_0(A_p^\vee)
=\operatorname{Fitt}_2(S_p^\vee).
}
\]

### Proof

The standard Kummer exact sequence is
\[
0\to M_p:=
  E(\mathbf Q)\otimes(\mathbf Q_p/\mathbf Z_p)
 \to S_p\to A_p\to0,\qquad
M_p\simeq(\mathbf Q_p/\mathbf Z_p)^2.
\]
Because both a_p,b_p are nonzero p-adic numbers, the ideal they generate is \(p^{d_p}\mathbf Z_p\), with one of a_p/p^d,b_p/p^d a unit. An invertible change of basis of \(\mathbf Z_p^2\) transforms the row \((a_p,b_p)\) into \((p^{d_p},0)\). Multiplication by \(p^{d_p}\) on the divisible group \(\mathbf Q_p/\mathbf Z_p\) is SURJECTIVE, with kernel \(\mathbf Z/p^{d_p}\); hence (1) in the theorem.

Let s∈S_p represent any a∈A_p. Its p-local finite class can be canceled by a class m∈M_p, since \(\lambda_p(M_p)\) is all of the local target. Therefore \(s-m∈S_p^0\), proving the surjection \(S_p^0\to A_p\). Its kernel is exactly ker lambda_p. This proves (1) of the theorem.

The maximal divisible subgroup D=Qp/Zp of ker lambda is injective in the category of abelian groups, so it splits off from \(S_p^0\). This yields \(S_p^0\simeq D\oplus T_p'\) with \(0\to Z/p^{d_p}\to T_p'\to A_p\to0\).

By Pontryagin duality and the direct-sum rule for Fitting ideals,
\(\operatorname{Fitt}_1((S_p^0)^\vee)=\operatorname{Fitt}_0((T_p')^\vee)\).
If \(A_p\) is finite, \(T_p'\) is finite of cardinality \(p^{d_p}\#A_p\), so over the DVR Zp,
\(\operatorname{Fitt}_0((T_p')^\vee)=p^{d_p}(\#A_p)\mathbf Z_p
=p^{d_p}\operatorname{Fitt}_0(A_p^\vee)\).
If \(A_p\) is infinite, its Pontryagin dual has positive free Zp-rank (cofinitely generated Selmer), and so does \((T_p')^\vee\); therefore both Fitting-zero ideals are (0). This proves the FIRST equality (2) in all cases. The SECOND follows from the already proved Kummer splitting \(S_p^\vee\simeq Z_p^2\oplus A_p^\vee\), hence \(\operatorname{Fitt}_2(S_p^\vee)=\operatorname{Fitt}_0(A_p^\vee)\). QED.

### Important improvement over the earlier purely rational strict-Selmer statement

This is an exact **integral** comparison including the finite, Cassels–Tate-constrained torsion of Sha, not merely the rational corank. It separates the p-adic log saturation defect from the Sha defect. For \(d_p>0\), an unavoidable extra finite factor \(p^{d_p}\) must be included; a naive statement \(\operatorname{Fitt}_1(S_p^{0\vee})=\operatorname{Fitt}_2(S_p^\vee)\) for all p is FALSE in general.

## New, genuinely executed p=16231 numerical input

The **new** small pure-Python verification in \`verification/bsd389_p16231_integral_formal_log_saturation.py\` uses independent binary and Montgomery-ladder multiplication in the short Weierstrass chart
\[
U=4x+4/3,\quad V=8y+4,\quad V^2=U^3-\frac{112}{3}U+\frac{1712}{27}
\]
and the exact original formal parameter
\(t=-2(U-\frac43Z^2)Z/(V-4Z^3)\).
It computes \([N_p]P\) and \([N_p]Q\) at k=2,3,4 precision with N_p=16104, then uses log_E(t)=t mod p² to find
\[
\boxed{\frac{\log_p P}{p}\equiv6575,\qquad
\frac{\log_p Q}{p}\equiv12208\pmod{16231}.}
\]
Both residues are units, hence **\(d_{16231}=0\)**, with primitive logarithm-kernel vector \(12208P-6575Q\bmod p\). See \`results/bsd389_p16231_MW_formal_log_saturation_ASSISTANT_EXECUTED_2026-11-06.md\` for the full new output.

For p16231, the intrinsic strict-Selmer Fitting ideal therefore equals the actual Sha Fitting ideal **without any extra logarithm-index factor**.

## Explicit residual target — precisely what is NOT proved

Castella–Hsieh (2022), Theorem 5.5 gives a rational identity
\[
\kappa_p=C_p\,\frac{1-\alpha_p/p}{1-\alpha_p^{-1}}\,
\frac{\Theta_{f/K}^{(2)}}{h_p^{(2)}(P,Q)}
\cdot(\log_p(Q)P-\log_p(P)Q).
\]
The p-divisibility of logs removes the apparent denominator p for nonanomalous good p, and the just-proved \(d_{16231}=0\) removes the geometric lattice index there. HOWEVER the class is only given **rationally** in the cited formula, with algebraic comparison factor C_p depending on choices. No theorem in the cited results identifies its integral index with
\(\operatorname{Fitt}_1((S_p^0)^\vee)\).
**That particular class-to-Fitting comparison is the genuine remaining arithmetic implication**, and it must be non-circular and valid with uniform p-independent normalizations to bound all prime support.

Nothing here proves Sha finite, Sha trivial, the exact complex leading-term identity, or complete BSD for E389a1. No previous computational certificate was rerun.

## Source
- Kummer and local p-adic formal group for good reduction: Silverman, *Arithmetic of Elliptic Curves*, Chapters IV and VII.
- Cassels–Tate and structure of Sha: same standard references as the earlier project theorem, \`paper/bsd389_unconditional_rank2_kummer_fitt2_identity_2026-10-30.md\`.
- Castella–Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum Math Sigma 10 (2022), Theorem 5.5.
