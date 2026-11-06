# BSD 389a1 — ONE uniform integral modular projector for all p except 2 and 5

Date: 2026-11-06. New exact global correspondence and Selmer/height theorem. **Not** proof of Sha finiteness or the complex rank-two BSD leading term. No old prime-local certificate rerun.

Let E=389a1, X=X_0(389), J=J_0(389), and φ:X→E be its optimal degree-40 parametrization (independently documented via modular symbols, Sage E.modular_degree()=40). Put
α=φ_*:J→E, β=φ^*:E=Pic^0(E)→J=Pic^0(X).
Then the degree formula for divisor push-pull gives, exactly over Q,
\[
\boxed{\alpha\beta=[40]_E.}\tag{1}
\]
The connected kernel A=ker α (optimality) has dimension g(X)-1=31.

## Theorem 1 — a prime-INDEPENDENT integral projector

\[
\boxed{e_E=(1/40)\beta\alpha\in
\mathrm{End}_{\mathbf Q}(J)\otimes\mathbf Z[1/10],
\quad e_E^2=e_E.}\tag{2}
\]
Proof: \(e_E^2=40^{-2}\beta(\alpha\beta)\alpha
=40^{-1}\beta\alpha=e_E\). Also e_Eβ=β and e_E A=0.

For EVERY rational p≠2,5, e_E is an **integral G_Q-equivariant idempotent on T_pJ**. The unique arithmetic E factor is isolated over \(\mathbf Z_p\), without any ordinary/supersingular assumption or p-specific Gross-point normalisation.

## Theorem 2 — an explicit degree-1600 Q-isogeny and ALL-p-primary Selmer/Sha split

Define \(\Phi:E\times A\to J\) by
\(\Phi(P,a)=\beta(P)+a\).
It is surjective: its image contains A, and αΦ=[40] on E is surjective. Its kernel is
\(\{(P,-\beta P): P\in E[40]\}\simeq E[40]\).
Therefore
\[
\boxed{\deg\Phi=40^2=1600.}\tag{3}
\]

For every p∤1600 (i.e. p≠2,5), Φ induces an isomorphism on the p∞ Galois modules and the **global and local p-adic Kummer conditions**, since its kernel/cokernel on points is killed by a p-unit isogeny degree. Hence exact cohomological isomorphisms, including bad prime 389 and the small p=3:
\[
\boxed{\operatorname{Sel}_{p^\infty}(J/\mathbf Q)
\simeq \operatorname{Sel}_{p^\infty}(E/\mathbf Q)
\oplus\operatorname{Sel}_{p^\infty}(A/\mathbf Q),}\tag{4}
\]
\[
\boxed{\Sha(J/\mathbf Q)[p^\infty]\simeq
\Sha(E/\mathbf Q)[p^\infty]\oplus
\Sha(A/\mathbf Q)[p^\infty]\quad(p\ne2,5).}\tag{5}
\]
No finiteness assumption on Sha is made. These results hold at ALL rational p outside the explicitly fixed two-prime set, and no CM field or prime-dependent twist is used.

IMPORTANT: A denominator 40 for a projector DOES NOT annihilate Sha(E). It proves a uniform **direct-factor decomposition** of Sha(J) and its integral Selmer, and NOTHING about the actual orders or finite prime support of the two Sha summands. Conflating these assertions would be a major false inference.

## Theorem 3 — exact Néron–Tate height pull-back and global regulator

Using the canonical principal polarisations on E and J, α and β are Rosati adjoints, so the projection formula gives
\[
\boxed{\langle\beta P,\beta Q\rangle_J
=\langle P,\alpha\beta Q\rangle_E
=40\langle P,Q\rangle_E.}\tag{6}
\]
Let P=(-1,1), Q=(0,-1) be the certified full saturated MW generators of E(Q). Set
\(D_P=\beta P,D_Q=\beta Q\in J(\mathbf Q)\);
equivalently \(D_P\) is the class of the degree-zero divisor
\(\phi^*(P)-\phi^*(O)\) of degree 40−40 on X, and similarly for Q.
Then
\[
\boxed{
\det[\langle D_i,D_j\rangle_J]_{i,j=P,Q}
=1600\operatorname{Reg}(E).}\tag{7}
\]

Further, let L=Z D_P+Z D_Q in J(Q)/tors and L_sat its saturation in that free group. The finite group L_sat/L is **killed by 40**. Proof: for v∈L_sat, v belongs to the Q-span of βE(Q). On this span β α v=40v rationally, and αv∈E(Q); thus 40v differs from β(αv)∈L by torsion in J(Q). Therefore at ALL p≠2,5 the modular MW image is already p-saturated. (Order of L_sat/L need not itself divide 40; its exponent divides 40.)

## The exact (still OPEN) archimedean rank-two target

With already rigorously fixed L''(E,1)/2 by Mellin and the full real Néron period Ω_E, strong BSD with conjectural Sha=1 is equivalent to
\[
\boxed{
\frac{L''(E,1)}2
\overset{?}{=}
\frac{\Omega_E}{1600}\det[\langle D_i,D_j\rangle_J].}\tag{8}
\]
Equation (8) is a **nonconjectural reduction to explicit integral arithmetic divisors on one modular Jacobian**, but its equality with L'' remains conjectural. Gross–Zagier controls a first derivative in rank one, NOT this rank-two determinant. The latter would require genuinely new rank-two arithmetic height reciprocity, not a period/degree identity.

## Scope and genuine global research obligation

- Theorem 1–3 are proved from a SINGLE fixed degree-40 correspondence over Q, simultaneously at all p except 2,5, with no p-specific computational input.
- Neither Theorem 1–3 nor the exact value 40 supplies the missing nonzero p-INDEPENDENT global Selmer/Fitting determinant D. The corresponding vanishing of finite Sha at large p is NOT proved.
- The complement A contains positive-rank modular abelian factors A_2,A_3,A_6; the rank-zero theorem for A_20 (Stein, level 389) does not prove Sha(A) finite. Thus the global projector does NOT evade the original rank-two challenge via a rank-zero complement.
- The next potential serious theorem is a genuine **integral rank-two zeta/height comparison on the fixed e_E motive over Z[1/10]** that simultaneously controls the Selmer Fitting ideal and the REAL height determinant. Its existence is not assumed or proved.

Sources: Sage E.modular_degree()=40, https://more-sagemath-tutorials.readthedocs.io/en/latest/demo-number-theory.html ; Stein, X0(389) modular Jacobian 32-dimensional splitting https://wstein.org/Tables/389/389/node1.html ; standard Abel–Jacobi and Néron–Tate functoriality.
