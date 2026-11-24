# 389a1 — proved two-sided Poitou–Tate determinant-square identity, and the exact remaining rank-two Euler-system comparison

**24 Nov 2026.** The linear-algebra/duality theorem below is PROVED without Euler-system conjectures. The equality identifying this arithmetic two-sided determinant volume with the genuine Mazur–Tate/Kurihara derivative is **NOT PROVED**. It must not be inferred from finite p=5,7,11 data or by choosing the scaling from those data.

## 1. A canonical source for the SQUARE, with no analytic conjecture

Let p≥5 and E/Q an elliptic curve for which \(\bar\rho_{E,p}\) is irreducible, E(Q)[p]=0 and rank E(Q)=2. Suppose further **only for this section** that \(\Sha(E/\mathbf Q)[p]=0\), so the genuinely arithmetic mod-p Selmer
\[
S=\operatorname{Sel}_p(E/\mathbf Q)=\mathbf F_p\kappa(P)\oplus\mathbf F_p\kappa(Q)
\]
has dimension 2. The latter finiteness/triviality is independently established at p=5,7,11 by previous Kurihara witnesses, and is NOT assumed for the desired all-prime theorem.

Choose two good \(\ell_i\ne p\) such that \(L_i=H_f^1(\mathbf Q_{\ell_i},E[p])\) each has dimension one. Fix any local bases, so localization gives an honest 2×2 matrix \(A_{ij}\) with rows the MW localization vectors \(v_i,v_j\):
\[
A_{ij}=\begin{pmatrix}
\ell_i(\kappa(P))&\ell_i(\kappa(Q))\\
\ell_j(\kappa(P))&\ell_j(\kappa(Q))
\end{pmatrix},\qquad
\Delta_{ij}=\det A_{ij}.
\]

By the local Tate perfect pairing, the *singular* local cohomology quotients \(L_i^s=H^1(\mathbf Q_{\ell_i},E[p])/L_i\) are canonically dual to \(L_i\) (once the Weil pairing is fixed). Poitou–Tate local-condition comparison shows that the boundary map
\[
\partial_{ij}:L_i^s\oplus L_j^s\longrightarrow S^\vee
\]
is the algebraic dual/transpose of the localization \(A_{ij}:S\to L_i\oplus L_j\).

**THEOREM (exact two-sided local volume).** In the compatible primal/dual bases,
\[
\boxed{
\det\!\begin{pmatrix}0&A_{ij}^{\mathsf T}\\ A_{ij}&0\end{pmatrix}
=(\det A_{ij})^2
=\Delta_{ij}^2.}
\]
Equivalently the product of the determinants of the primal and dual Poitou–Tate localization maps is exactly \(\Delta_{ij}^2\).

**Proof.** Local Tate duality identifies the boundary with \(A_{ij}^{\mathsf T}\). For any m×m matrix A over a commutative ring,
\[
\det\!\begin{pmatrix}0&A^{\mathsf T}\\A&0\end{pmatrix}
=(-1)^m\det(A^{\mathsf T}A).
\]
At m=2 the sign is +1, and \(\det(A^{\mathsf T}A)=\det(A)^2\). No analytic or Sha-size claim enters this identity beyond the explicitly stated dim S=2 hypothesis. QED.

The square-determinant phenomenon observed numerically in authentic two-factor Kurihara residues is therefore **exactly the square already forced by the two-sided Poitou–Tate local duality**, if those residues are given by one *globally normalized* cohomological determinant section.

**WARNING:** The theorem computes the determinant of a *different, explicitly constructed cohomological matrix*, not the Mazur–Tate θ coefficient. Its proof alone DOES NOT show δ_ij = scalar×local-weight×Δ_ij². The identification of the Kato-derived Mazur–Tate mixed derivative with the two-sided volume is the nontrivial missing global arithmetic step.

## 2. A precise independent definition of the proposed weights

Do NOT set \(w_q\) by dividing observed δ_{q,r} by Δ_{q,r}², since that is a fitted parameter and cannot prove a global statement.

The meaningful proposed construction is to take the genuine **finite-singular comparison** isomorphism at each Kolyvagin-admissible q between the one-dimensional finite and singular local E[p]-cohomologies,
\[
\phi_q^{fs}:L_q\longrightarrow L_q^s
\]
that enters Mazur–Rubin's finite-singular Kolyvagin-system relations (and includes the chosen primitive root/logarithm orientation). Local Tate duality identifies \(L_q^s\cong L_q^\vee\), so \(\phi_q^{fs}\) is equivalent to a nonzero quadratic bilinear form on \(L_q\). After choosing a local generator \(e_q\in L_q\), define the unit
\[
\boxed{w_q:=\langle \phi_q^{fs}(e_q),e_q\rangle_q\in\mathbf F_p^\times.}
\]
This weight is defined from **only the local Galois module, finite-singular comparison and primitive-root orientation**, and requires NO two-prime Kurihara residue.

The nonzero claim holds only when \(\phi_q^{fs}\) is genuinely an isomorphism at the selected q; this is part of Kolyvagin admissibility and choice of auxiliary primes. Under a basis rescaling \(e_q\mapsto c_q e_q\), the scalar \(w_q\) changes predictably; it is safest to regard the one-dimensional form \(w_q\ell_q\otimes\ell_q\) as the invariant, rather than the number alone.

**PROPOSED RECIPROCITY THEOREM (unproved):** The authentic mixed two-prime Kurihara–Mazur–Tate coefficient is, up to a single **globally defined** scalar \(\mathcal C_p\), the two-sided local volume of the rank-two Selmer complex, corrected by these genuine local finite-singular forms:
\[
\boxed{
\widetilde\delta_{q_iq_j}
=\mathcal C_p\,w_{q_i}w_{q_j}
\det(v_{q_i},v_{q_j})^2\pmod p
}
\]
for all suitable q_i,q_j. The global scalar \(\mathcal C_p\) must be constructed **independently of δ** as a normalized Kato zeta/determinant-line coordinate, not fitted from anchor pairs; likewise its p-unit status must not be assumed.

If this arithmetic theorem were proved, the four-prime QLVR identities would follow automatically from cancellation of the local forms. The only remaining uniform Sha obstruction would then be to prove nonvanishing/finite prime support of this independently defined global scalar, not to reconstruct one-prime local data.

## 3. A direct falsification of the easy q-only scalar theta-jet proposal

Using the authenticated 390-Manin table and direct exact enumeration, both the single-prime rank-two Mazur–Tate polynomials for q41 and q61 at p=5 are **identically zero** in the 5-dimensional group ring: their entire histograms in \(\mathbf Z^5\) vanish for the primitive roots g41=6 and g61=2. However the independently verified genuine mixed two-prime derivative δ_(41·61)=4 mod5 is a unit.

Thus no weight \(w_q\in\mathbf F_5^\times\) can be obtained by multiplying ANY coefficient of those single-prime theta polynomials by a p-unit. This rules out an appealing shortcut; the cohomological finite-singular comparison \(\phi_q^{fs}\) is genuinely richer data and is nonzero even when the single-prime scalar theta vanishes.

## 4. Third-prime genuine check + predictive holdout

For p=11, six primes (397,991,1321,3389,3433,4643) give localization slopes (10,7,2,8,9,4), all pairwise distinct. The genuine 15 two-prime Kurihara residues are

    q_i/q_j 991 1321 3389 3433 4643
    397       1    9    4    7    5
    991           10    7    9    6
    1321                2    5    2
    3389                     1    8
    3433                          5

Six anchor-edge values (five edges from 397, plus (991,1321)) determine C=7 and weights
\[
u=(1,7,8,8,1,6)\in(\mathbf F_{11}^\times)^6.
\]
The **remaining nine pair values**, not used in the fit, are predicted exactly by \(7u_i u_j\Delta_{ij}^2\), matching nine independent complete authentic modular-symbol enumerations. All **15 four-prime identities** hold on these six primes. This extends earlier p5 105 pairs and p7 10 pairs to **130** verified total pair residues. The third prime is particularly useful because p11 was not used when the squared-determinant law was originally proposed.

These holdout predictions are genuine finite empirical tests of the *shape* of the reciprocity assertion, but DO NOT validate the independently defined \(\phi_q^{fs}\)-based local weights, nor prove any p-tail theorem.

## 5. Next proof obligations — no brute force

(1) Write an explicit finite-singular local Tate pairing formula for the proposed \(w_q\) and confirm, using *only local E(Fq), Frobenius and primitive-root data*, that the ratios of these genuine weights agree with the fitted u_q ratios at p5,7,11. This test would be independent of the pairwise Kurihara data and is the first meaningful falsification test for the NEW specific reciprocity conjecture.

(2) Prove an arithmetic determinant-line map from the actual Kato zeta element to the two-sided Poitou–Tate determinant section, with all integrality factors. The existence of a two-sided determinant matrix DOES NOT prove this map.

(3) Prove the global scalar \(\mathcal C_p\) is a p-unit for all sufficiently large p, or its exceptional prime support is controlled by one independent nonzero integer; this is genuinely as hard as the previously identified rank-two Sha obstruction and cannot be supplied by Chebotarev.

Even if (1)–(3) were solved, the separate exact complex rank-two BSD leading coefficient still requires an archimedean comparison.

**Reference framework:** Mazur–Rubin, Kolyvagin systems, local finite-singular comparison; Poitou–Tate duality; Chan-Ho Kim, Theorem 1.10; Castella–Sano (2026); Burns–Kurihara–Sano (2024), generalized Perrin–Riou conjecture. No new published exact rank-two Kato determinant comparison is claimed.
