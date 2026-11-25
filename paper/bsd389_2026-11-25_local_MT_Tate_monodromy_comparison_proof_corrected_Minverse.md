# 389a1 — PROOF of the tame Mazur–Tate / finite-field Tate-monodromy comparison with the mandatory M_q^{-1} factor

**25 November 2026.** This note proves a **LOCAL HEIGHT** statement, not a Kato leading-term or BSD theorem. It relies on (i) canonical tame Néron/Poincaré biextension trivialization of Mazur–Tate/Tan, (ii) the standard identification of finite-field Poincaré p-monodromy with the Tate pairing (Robert 2024, Cor. 2.5/3.12), and (iii) elementary finite-group algebra. The sign of the composite of Artin reciprocity convention and self-dual polarization convention is retained as a single \(\varepsilon=\pm1\), the SAME for all auxiliary q in a consistently normalized family. The old uncorrected height formula \(\mathscr H=\mathcal B_{q_1}+r\mathcal B_{q_2}\) is not the right normalization.

## 1. Setup with exactly specified domains

E/Q = 389a1: y²+y=x³+x²−2x, E(Q)/tors = ZP⊕ZQ; c_389=1. Let p≥5 and q≠p,389 be a good prime with q≡1 modp, \(N_q=\#E(\mathbf F_q)=pM_q\), \(p\nmid M_q\), and let the global MW reduction at q span the cyclic one-dimensional Fp quotient \(E(\mathbf F_q)/p\).

Let \(\ell_q:M_p\to\mathbf F_p\) denote a normalized surjective MW reduction functional, \(M_p=(E(\mathbf Q)/tors)\otimes\mathbf Z_p\). The actual second Mazur–Tate p-adic lattice is \(M_{q,p}=\ker\ell_q\). Choose a GLOBAL rational MW point e with \(\ell_q(e)=1\) and an integer \(u>0\) such that
\[
M_q\mid u,\qquad u\equiv1\bmod p.
\]
Such u always exists since p∤M_q. Then \(b=up e\) reduces to the origin at q, so \(b\in E_{\{q\}}(\mathbf Q)\) is an honest second-variable point. In the p-adic completion \(u p e\equiv p e\bmod pM_{q,p}\), since \(p(u-1)e\in p^2M_p\).

Project the TRUE Mazur–Tate biextension height to the one-prime ray-class character of order p:
\(h_q:M_p\times M_{q,p}\to\mathbf F_p\).
Define the divided height \(H_q(x,y)=h_q(x,py)\). Previous proof using Tan equation (60) establishes exactly
\[
H_q(x,y)=\alpha_q\ell_q(x)\ell_q(y),\qquad
\alpha_q= h_q(e,up e).
\]
No finiteness of Sha or BSD assumption is made.

Separately define the reduced finite-field Tate form (with chosen primitive root \(\gamma_q\) and \(\zeta_q=\gamma_q^{(q-1)/p}\)):
\[
\mathcal B_q(x,y)=
\log_{\zeta_q}
t^{\rm red}_{p,q}([M_q]\bar x,\bar y)
=w_q\ell_q(x)\ell_q(y).
\]

## 2. Canonical tame splitting equals reduction in the rigidified Poincaré fiber — a local geometric lemma

Write F=Q_q, O=Z_q, k=F_q. Because E has GOOD reduction, its Néron model \(\mathcal E/O\) is an abelian scheme. The principally polarised Poincaré biextension \(\mathscr P\) extends over \(\mathcal E\times\mathcal E^\vee\) and is canonically rigidified on both zero axes.

For \(x\in E(F)=\mathcal E(O)\), \(z\in E_1(F)=\ker(\mathcal E(O)\to E(k))\), the fiber \(\mathscr P_{(x,z)}\) is an O-G_m torsor. As Pic(O)=0, choose an O-integral point \(\eta_0\) in this fiber. Reduction gives an element of \(\mathscr P_{(\bar x,0)}(k)\simeq k^\times\) via the canonical zero-axis rigidification. If \(\eta\in\mathscr P_{(x,z)}(F)\) is any element, write \(\eta=c\eta_0\) with c∈F×, and combine the valuation of c with the residue of its unit part times the rigidified reduction of \(\eta_0\). This constructs a continuous bi-additive splitting
\[
\operatorname{redrig}_q:\mathscr P(E(F),E_1(F))
\to F^\times/(1+qO)\simeq\mathbf Z\times k^\times.
\]
It is independent of \(\eta_0\) by the change-of-integral-trivialization cancellation. It extends the unramified Néron splitting and is symmetric on the intersection E_1×E_1 by the symmetry of the Poincaré rigidification. By the uniqueness of the canonical tame splitting in Tan 1995 §2.1 (L4), Remark (1)-(3), it equals Tan's actual \(\psi_q\). **This is the precise local bridge** that was missing in the earlier draft.

This construction avoids incorrectly identifying the arbitrary *global* Poincaré lift with an integral local unit: it uses an integral local lift to define the canonical splitting and only reduces the invariant obtained after p multiplication.

## 3. p-monodromy at the single anomalous prime = nonreduced finite-field Tate pairing

Let \(\eta\in\mathscr P(\mathbf Q)\) be ANY rational biextension lift over \((e,u e)\); it exists because a G_m torsor over Spec(Q) has a Q-rational point. Let
\[
\eta^{[p]}=p_{\mathrm{second}}\eta
\]
over \((e,p u e)\), an honest element of the restricted MT pairing domain.

At all places v≠q, the first and second rational points e,ue belong to the intersection of the two local splitting domains: at all good primes unramified, E_0=E, and at the bad prime 389, the Tamagawa component group has size one. Tan's canonical mirror symmetry, §2.1 Remark (3) and §4.4 eq (60), implies
\[
\psi_v(\eta_v^{[p]})=p\,\psi'_v(\eta_v).
\]
Since the global q-ray-class character has exponent p, these contributions vanish. The real place contributes nothing because p is odd. The global height is therefore exactly the q-component of \(\psi_q(\eta_q^{[p]})\), modulo the global principal-ideles and local pth powers.

Now decompose the local second coordinate \(u e\in E(F)\). Since \(p[u]\bar e=0\in E(k)\), the point
\[
z=[u]\bar e\in E(k)[p]
\]
has a UNIQUE lift \(\widetilde z\in E(F)[p]\) by finite étaleness of the p-torsion abelian scheme (p≠q). Thus
\[
u e=\widetilde z+f,\qquad f\in E_1(F).
\]
Biextension bi-additivity decomposes a local lift of (e,ue) into a torsion-part lift and a formal-part lift. The p-fold SECOND product of the formal-part lift has q-tame splitting a pth multiple, hence it is invisible to the order-p q-ray-class character. The only surviving component is the p-monodromy of the local Poincaré biextension over \((\bar e,z)\).

By the definition of the Poincaré extension classified by the torsion point \(z\in E^\vee[p](k)\), p-fold second-axis monodromy is the **nonreduced p-Tate pairing** of \(z\) against \(\bar e\), in \(k^\times/(k^\times)^p\). This is the standard Poincaré-biextension identification, explicitly proved for the arithmetic finite-field Tate pairing by Damien Robert, *Fast pairings via biextensions and cubical arithmetic* (2024), Cor. 2.5 and 3.12. A reversal of the two Poincaré axes / self-duality identification can invert the pairing; the choice of local arithmetic versus geometric Artin reciprocity can also invert it. Record their product as ONE fixed sign \(\varepsilon\in\{\pm1\}\), independent of q under coherent conventions.

Consequently, using \(\operatorname{logrec}_{q,p}\) for the actual order-p q-ray-class projection, and the same primitive root \(\gamma_q\) as in the Kurihara logarithms, we have the **genuine local height identity**
\[
\boxed{\alpha_q=h_q(e,up e)
=\varepsilon\cdot
\log_{\zeta_q}t^{\rm red}_{p,q}([u]\bar e,\bar e).}
\tag{LOCAL-MONODROMY}
\]
This is a comparison of the actual canonical tame splitting with Tate monodromy, not a guess from two-prime modular-symbol computations. If the q-ray-class coordinate is defined directly as \(\log_{\gamma_q}\) on local unit residues and the principal polarization is normalized by the corresponding second-axis Tate convention, then \(\varepsilon=+1\); under the inverse Artin convention it is \(-1\).

## 4. EXACT mandatory M_q^{-1} correction

Let \(g_q=[M_q]\bar e\), the canonical p-torsion generator used in the independently computed \(w_q\). Because \(u\equiv1\bmod p\) and \(M_q\mid u\),
\[
[u]\bar e=[u/M_q]g_q=[M_q^{-1}\bmod p]g_q.
\]
By Tate bilinearity,
\[
\log_{\zeta_q}t^{\rm red}_{p,q}([u]\bar e,\bar e)
=M_q^{-1}w_q.
\]
Combining the previous section with the already PROVED symmetric rank-one structure of H_q gives the **corrected local comparison theorem**
\[
\boxed{
H_q=\varepsilon\,M_q^{-1}\mathcal B_q
\quad\text{on }E(\mathbf Q)/p.
}
\tag{CORRECTED-ONE-PRIME}
\]

For two MW-independent q1,q2, functoriality under ray-class characters \(\chi_r=\chi_{q_1}+r\chi_{q_2}\) now gives
\[
\boxed{
\mathscr H_{\chi_r,p}
=\varepsilon\left(M_{q_1}^{-1}\mathcal B_{q_1}
+rM_{q_2}^{-1}\mathcal B_{q_2}\right)
}
\tag{CORRECTED-HEIGHT}
\]
with the **same** sign convention across both primes. This is the derived Mazur–Tate HEIGHT comparison, not the Kato/Mazur–Tate leading-term comparison.

Consequently, by Cauchy–Binet, the true derived height discriminant is
\[
\boxed{
\det\mathscr H_{\chi_r,p}
=r(M_{q_1}M_{q_2})^{-1}
\det(\mathcal B_{q_1}+\mathcal B_{q_2}).
}
\tag{DETERMINANT}
\]
The global sign disappears from the rank-two determinant. The old uncorrected equality \(\mathscr H_{\chi_r,p}=\mathcal B_{q_1}+r\mathcal B_{q_2}\) is generally FALSE with these normalizations (even after allowing a common sign).

## 5. A concrete p=19 consequence and normalization countertest

Take q1=2243, q2=3877. Their exact finite-field orders are
\(N_1=2261=19\cdot119\), \(N_2=3781=19\cdot199\), and local Tate reduction matrices on (P,Q) are
\[
\mathcal B_{2243}=\begin{pmatrix}17&17\\17&17\end{pmatrix},\qquad
\mathcal B_{3877}=\begin{pmatrix}0&0\\0&18\end{pmatrix}.
\]
Modulo 19,
\(M_1=119\equiv5,\ M_1^{-1}=4\),
\(M_2=199\equiv9,\ M_2^{-1}=17\).
Thus the **corrected actual MT height matrix**, up to one global orientation sign, is
\[
\boxed{
\mathscr H_{\chi_r,19}
=\varepsilon\begin{pmatrix}11&11\\11&11+2r\end{pmatrix}
\bmod19
}
\]
with determinant \(3r\pmod{19}\). The old uncorrected candidate would give \(\left(\begin{smallmatrix}17&17\\17&17+18r\end{smallmatrix}\right)\) and determinant \(2r\). This difference is a unit discrepancy, not a Sha-divisibility discrepancy.

The genuine modular-symbol Kurihara coefficient is independently known to be \(4\bmod19\). It is **not** predicted to equal \(2\det\mathscr H\): the corrected height would give 6 mod19 rather than 4. Instead the finite empirical ILTR equality can be restated as the **STILL UNPROVED** global leading-term comparison
\[
\boxed{
\widetilde\delta_{q_1q_2}
\overset?=2M_{q_1}M_{q_2}\det\mathscr H_{\chi_1,p}
\pmod p.
}
\tag{KATO-HEIGHT-TARGET}
\]
For p=19 this yields \(2\cdot(5\cdot9)\cdot3\equiv4\bmod19\), matching the actual coefficient. This consistency is not a proof of the global comparison, and a possible Selmer/Sha factor must be retained.

## 6. Exact scope / remaining global BSD obligation

What has been proved from standard Poincaré-biextension geometry and the source definitions:
- the true one-prime divided Mazur–Tate height is symmetric of rank one (Tan eq. 60);
- its scalar is the finite-field p-monodromy of the **actual** q-reduced second point [u]bar e;
- p-monodromy is the nonreduced finite-field Tate pairing, hence the correction \(M_q^{-1}\) relative to the project's older weight defined with [M_q]bar e;
- two-prime derived MT HEIGHT regulator follows by character additivity and Cauchy–Binet.

What has NOT been proved: any equality between the true global Kato/Mazur–Tate theta coefficient and this derived height regulator; a theorem proving the empirical coefficient 2 at unbounded p; uniform Sha[p]=0; Sha finiteness over Q; the exact complex rank-two BSD leading term. Such statements require a new global determinant-line/Euler-system comparison, not local Tate monodromy.

**Key primary sources inspected:**
- Ki-Seng Tan, *Refined theorems of the Birch and Swinnerton-Dyer type*, Ann. Inst. Fourier 45 (1995), §2.1 (L4), Remarks (1)–(3), §2.2 Definition 2.6 and §4.4 equation (60), and proof of Lemma 4.11 pp. 361–363. https://www.numdam.org/article/AIF_1995__45_2_317_0.pdf
- Damien Robert, *Fast pairings via biextensions and cubical arithmetic* (2024), Corollaries 2.5 and 3.12, including the warning that the unreduced Tate pairing must be placed in the correct quotient \(k^\times/k^{\times p}\). https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/articles/biextensions.pdf
- Earlier project note: paper/bsd389_one_prime_mazur_tate_biextension_height_factorization_and_scalar_reciprocity_cut_2026-11-25.md

**Integrity rule:** The choice of \(\varepsilon\) must be frozen by matching the local Artin reciprocity normalization to the project’s Kurihara primitive-root logarithm, before any statement of exact equality in the unqualified original Tan conventions. No p19 value is alleged to have been computed using an independent full original global biextension implementation; the values (11,2) are THEOREM consequences of the standard monodromy identification and fixed finite-field Tate computations, with the stated sign ambiguity.


## 7. NEW UNIFORM NONDEGENERACY COROLLARY for the TRUE derived MT height — no BSD/Sha hypothesis

For every sufficiently large p, full Kummer Galois image and Chebotarev provide q1,q2 where: (a) q_i≡1 mod p, (b) the Frobenius modp has nonidentity unipotent Jordan block, (c) a mod-p² lift forces \(p\parallel\#E(\mathbf F_{q_i})\), and (d) the MW local rows v_i form a basis of Fp². These choices require NO hypothesis about Sha or Kato.

The actual derived Mazur–Tate height matrices satisfy the corrected comparison theorem, so each w_i is nonzero by perfection of the reduced Tate pairing, each M_i inverse is a unit, and
\[
\boxed{\det\mathscr H_{\chi_r,p}
=r(M_1M_2)^{-1} w_1w_2\det(v_1,v_2)^2
\in\mathbf F_p^\times}
\qquad(r\in\mathbf F_p^\times).
\]
This proves that **the actual divided Mazur–Tate regulator can be made nondegenerate for every sufficiently large p** by a suitable **order-p auxiliary conductor**, independently of the unknown Sha group. Tan's Lemma 4.11 assumes "good" (including BSD), but that lemma is NOT used: this restricted rank-two conclusion follows from the explicit good-reduction finite-field monodromy formula plus Chebotarev/MW full image.

**No false implication:** This uniform *HEIGHT* nondegeneracy does NOT force any genuine Mazur–Tate theta coefficient to be a p-unit. If Sha(E/Q)[p] is nonzero, the previously proved Fitting/jet-depth theorem forces every *true* deep rank-two theta coefficient to vanish modulo p² even though a suitable MT regulator determinant is a unit. Exactly the missing Kato-to-regulator comparison, including the possible Selmer/Sha determinant factor, separates these statements.

## 8. Independent arithmetic normalization consistency checks at four primes

Finite-field orders can be independently counted from the equation E, and the w_i come from the original independent Miller implementation. The complete genuine Kurihara coefficients are archived separately.

| p | q1,q2 | M1 modp, M2 modp | w1,w2 | det(v1,v2)^2 | derived true-height determinant modp | earlier independently verified delta |
|---|---|---|---|---|---|---|
| 5 | 41,61 | 4,4 | 3,1 | 4 | 2 | 4 |
| 7 | 113,673 | 1,5 | 1,4 | 2 | 3 | 2 |
| 11 | 397,991 | 1,7 | 8,1 | 9 | 4 | 1 |
| 19 | 2243,3877 | 5,9 | 17,18 | 1 | 3 | 4 |

For each row, \(2M_1M_2\det\mathscr H_{\chi_1,p}\equiv\delta_{q_1q_2}\bmod p\) holds, as a finite consistency check. This uses already certified δ-values and is NOT a proof of the **universal Kato leading-term identity**. The height determinant is independent of the common \(\varepsilon\) sign, and our computational matrix values are normalized accordingly.


## 9. Critical admissibility distinction

The hypothesis \(p\parallel\#E(\mathbf F_q)\) **cannot** hold simultaneously with the **p²-deep** Kurihara conditions \(q\equiv1\bmod p^2\) and \(a_q(E)\equiv2\bmod p^2\), since these imply \(\#E(\mathbf F_q)=q+1-a_q\equiv0\bmod p^2\). Thus the geometric comparison of this note is a theorem at **p-level anomalous tame primes with p-Sylow of exact order p**, and does not automatically extend to p²-deep auxiliary primes. The uniform p-level Kato-to-theta leading coefficient would suffice to show Sha[p]=0 if proved (via the p-level Fitting gate), but the earlier p² valuation-one gate is a separate situation. Extension of local monodromy to p^k and groups with p²-torsion requires a new integral filtration / higher pairing and is not covered by the present mod-p proof.


## 10. INDEPENDENT AUDIT NOTE (2026-11-25): monodromy proof vs. directly computed original Mazur–Tate height

The later index-cancellation audit, paper/bsd389_2026-11-25_exact_global_MT_index_cancellation_p19_J1_and_real_period_factor2.md, confirms that the previous p19 numerical regulator claim rests on the local Poincaré/Néron comparison IN THIS NOTE. Its value has **not** been independently obtained by evaluating the original \(\mathbf Q_q\)-valued tame Mazur–Tate biextension height from disjoint rational divisors.

Robert Corollary 3.12 establishes finite-field monodromy = Tate. Tan §2.1(L4) establishes canonical uniqueness of the tame \(\mathbf Q_q^\times/(1+q\mathcal O_q)\) splitting. A proof equating these must verify that the specific reduction-and-rigidification map actually satisfies the required biextension homomorphism properties, is compatible with scalar pullback under multiplication by p, and matches the Artin/primitive-root generator. Those source-level links have been ARGUED in §§2–3, but neither is independently supplied as a single theorem by the cited papers. The remaining sign ε is explicitly un-fixed.

For responsible publication, regard the numerical value \(\det\mathscr H\equiv3\bmod19\) as a **consequence of this proposed/argued comparison**, not as an independently observed original-MT-height certificate. The exact group-theoretic \(J_S=1\), honest integral restricted lattice, and period factor of two are independent of this bridge and fully certified in the later note.

This qualification does not weaken the finite-field Tate-pairing computations or the historically authenticated modular-symbol coefficients; it prevents accidental circular validation of a global Kato regulator identity through an unverified local normalization.
