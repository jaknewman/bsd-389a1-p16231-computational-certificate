# E389a1 — a canonical integral *divided* Mazur–Tate regulator at Kolyvagin primes, and a uniform Sha-obstruction theorem

**25 November 2026.** **PROVED in this note:** (I) a true p-adic Mordell–Weil reduction-lattice identity that salvages the otherwise inapplicable BKS tame-conductor regulator setup; (II) a canonical bilinear derived Mazur–Tate pairing, **independent** of the Mazur–Tate theta and of any Sha finiteness assumption; (III) a quantitative p-depth divisibility theorem that proves exactly how genuine \(\Sha[p]\) forces every deep rank-two Mazur–Tate coefficient to vanish. **NOT PROVED:** that the derived global regulator equals the sum of reduced-Tate local forms; the global leading-term comparison with Kato; the uniform triviality of Sha(E/Q); the exact complex BSD formula. These implications must not be upgraded by numerical agreement.

## I. Where the published regulator comparison breaks, exactly

Let \(E:y^2+y=x^3+x^2-2x\) (389a1) and \(M=E(\mathbf Q)/E(\mathbf Q)_{\rm tor}=\mathbf Z P\oplus\mathbf Z Q\). The conductor is 389, the Tamagawa product is 1. Fix an odd p≥5 and **two GOOD distinct auxiliary primes** q1,q2 such that
\[
p\parallel\#E(\mathbf F_{q_i}),\qquad
\dim_{\mathbf F_p}E(\mathbf F_{q_i})/pE(\mathbf F_{q_i})=1,\qquad
\lambda: M/pM\xrightarrow{\sim}
\bigoplus_{i=1}^{2}E(\mathbf F_{q_i})/p
\]
is an isomorphism. In the sufficiently large-p residual GL₂ tail Chebotarev/Kummer supplies such pairs, including p||#E(Fq) through a mod-p² Frobenius lift.

Set \(S=\{q_1,q_2\}\) and use the actual Mazur–Tate **integral second lattice**
\[
M_S=\ker\!\left(M\to E(\mathbf F_{q_1})\oplus E(\mathbf F_{q_2})\right).
\]
The BKS paper *On derivatives of Kato's Euler system and the Mazur–Tate Conjecture*, §2.2, defines precisely this lattice (also with bad-prime component groups, which contribute no p-primary index for 389a1). Its Hypothesis 2.2(iii) requires p to be COPRIME to the local #E(F_q). Our primes satisfy the opposite. The BKS construction therefore cannot be applied with \(M_S\otimes\mathbf Z_p=M\otimes\mathbf Z_p\) as was sometimes implicitly assumed.

**THEOREM I.1 (exact local-conductor lattice identity).** With \(M_p=M\otimes\mathbf Z_p\simeq\mathbf Z_p^2\), one has, as concrete sublattices of \(M_p\),
\[
\boxed{M_S\otimes\mathbf Z_p=pM_p.}
\tag{1}
\]

**Proof.** Let \(H\) be the actual image of \(M\to E(\mathbf F_{q_1})\oplus E(\mathbf F_{q_2})\), a finite group. Each local p-Sylow is cyclic of order p, so \(H[p^\infty]\) embeds into \((\mathbf Z/p)^2\). The assumed isomorphism of reductions modulo p implies \(H[p^\infty]=(\mathbf Z/p)^2\): multiplication by the prime-to-p part of the product of local group orders projects onto the full local p-Sylow, and the resulting global image has rank two. The exact sequence \(0\to M_S\to M\to H\to0\) remains exact after tensoring with the flat ring \(\mathbf Z_p\), giving \(M_p/(M_S\otimes\mathbf Z_p)\simeq H[p^\infty]\simeq(\mathbf Z/p)^2\). The embedded sublattice \(M_S\otimes\mathbf Z_p\) must coincide with pM_p because the composite \(M_p\to (\mathbf Z/p)^2\) is precisely the assumed isomorphism after reduction modulo p. QED.

In particular, the correction index is **exactly p²**. This is not a source of arithmetic Sha: it is a mandatory change of lattice whenever the two local MW reductions form a basis.

## II. Construct a genuine derived Mazur–Tate height pairing without dividing by p in the target

Let \(K\) be any real cyclic extension of degree p contained in \(\mathbf Q(\zeta_{q_1q_2})^+\), with character
\[
\chi_r(a)=\zeta_p^{\lambda_1(a)+r\lambda_2(a)},\quad r\in(\mathbf Z/p)^\times.
\]
The established Mazur–Tate biextension pairing [MT87, Chap. II], as recalled in BKS §2.2 and Darmon's exposition §2.2, is
\[
h_S:E(\mathbf Q)\times E_S(\mathbf Q)
 \longrightarrow G_S=\operatorname{Gal}(\mathbf Q(\zeta_{q_1q_2})^+/\mathbf Q).
\]
Project to \(G_K\simeq\mathbf Z/p\), choose the character/primitive-root normalization, and extend \(\mathbf Z_p\)-bilinearly to
\[
h_{\chi,p}:M_p\times(M_S\otimes\mathbf Z_p)\to\mathbf F_p.
\]

**THEOREM II.1 (canonical divided regulator).** The formula
\[
\boxed{
\mathscr H_{\chi,p}(x,y):=h_{\chi,p}(x,p y)
\in\mathbf F_p\qquad(x,y\in M_p)
}
\tag{2}
\]
defines a canonical bilinear form \(\mathscr H_{\chi,p}:M_p/pM_p\times M_p/pM_p\to\mathbf F_p\), independent of the chosen integral representative for p y in the lattice \(M_S\). It depends only on the ACTUAL Mazur–Tate pairing, the cyclic character \(\chi\), and the exact p-local lattice (1); it does not reference \(\Theta\), Kurihara coefficients, or the finiteness of Sha.

**Proof.** The sublattice equality (1) makes p y an honest element of the completed domain of h. The \(\mathbf Z_p\)-bilinear extension and the projection to the exponent-p group \(G_K\) imply bi-additivity and show that changing x or y by p times an element changes the value by p times a group element, hence zero. The multiplication-by-p map \(M_p\to pM_p=M_{S,p}\) is an isomorphism of free \(\mathbf Z_p\)-modules and is canonical. A different \(\mathbf Z_p\)-basis changes the determinant by the square of its determinant; for the fixed saturated integral MW basis P,Q this factor is 1 under \(\mathrm{GL}_2(\mathbf Z)\). QED.

**Integral representative recipe.** If one wants actual rational points in \(M_S\), choose a positive integer u multiple of the prime-to-p exponents of the two E(Fq)'s with \(u\equiv1\bmod p\). Then \(upP,upQ\in M_S\), and their p-adic images agree with pP,pQ modulo p²M_p. The mod-p pairing \(h_{\chi,p}(x,up y)\) equals \(\mathscr H_{\chi,p}(x,y)\), because u≡1 modp and the target has exponent p. Thus (2) is **constructive at the level of the authentic biextension pairing**, not a formal extension of a pairing outside its domain.

**Corollary (true regulator component).** Choose the basis P,Q of M and the p-adic basis pP,pQ of \(M_{S,p}\). The actual degree-two Mazur–Tate regulator discriminant in the cyclic p-projection is
\[
\boxed{
\operatorname{Reg}^{\rm MT}_{\chi,p}
=\det\left(\mathscr H_{\chi,p}(P_i,P_j)\right)\,T^2
\in I^2/I^3\simeq\mathbf F_p T^2,\qquad(P_1,P_2)=(P,Q).
}
\tag{3}
\]
This is an identity **by the original regulator's definition**, not an assertion identifying it with the analytic Mazur–Tate coefficient. In particular the p² lattice index is already handled; inserting another factor p^{-2} would double-correct the regulator.

The matrix need not be assumed symmetric before a separate check of the biextension normalization. The determinant and intrinsic bilinearity exist regardless.

## III. Exactly what remains in the proposed ILTR reciprocity

Independently, the reduced-Tate pairing at each good q_i defines a symmetric, rank-one form
\[
\mathcal B_{q_i,p}(x,y)=
\log_{\zeta_i}
t_{p,q_i}\left([\#E(\mathbf F_{q_i})/p]\bar x,\bar y\right)
\quad(x,y\in M_p/pM_p),
\]
constructed solely from the local Frobenius/Kummer pairings, with no global \Theta or Sha input.

The genuinely **new independent local-height comparison to prove** is:
\[
\boxed{
\mathscr H_{\chi_r,p}\stackrel{?}{=}
\mathcal B_{q_1,p}+r\,\mathcal B_{q_2,p}
\quad\text{as bilinear forms on }M_p/pM_p.
}
\tag{4}
\]
The character exponent r must not be dropped: \(\det(\mathcal B_1+r\mathcal B_2)=r\det(\mathcal B_1+\mathcal B_2)\) because each local form has rank one.

If (4) is established **arithmetically from the actual MT biextension and local reciprocity**, the rank-two Cauchy–Binet theorem proves the intrinsic regulator formula
\[
\boxed{
\operatorname{Reg}^{\rm MT}_{\chi_r,p}
=r\,w_{q_1}w_{q_2}\det(v_{q_1},v_{q_2})^2T^2.
}
\tag{5}
\]
This is independent of the global Kato class and p-primary Sha; it does NOT prove the Kato/Mazur–Tate coefficient equals any fixed multiple of the regulator.

There is then a **second, genuinely BSD-strength comparison**
\[
\boxed{
[\Theta^{\rm MT}_{K}]_{T^2}
\stackrel{?}{=}
U_{p,S}\,\mathscr A_{E,p}\,
\operatorname{Reg}^{\rm MT}_{\chi,p}\pmod p,
}
\tag{6}
\]
where \(U_{p,S}\) tracks the actual Néron-Manin period and normalization (the finite sample suggests a factor 2), and \(\mathscr A_{E,p}\) is a Selmer/determinant-line leading scalar, not automatically 1. If full Sha is finite the classical MT leading-term conjecture includes its ORDER; if Sha[p]\ne0, the correction has zero residue modp. Formula (6) is **not a theorem**, and we must not insert \(\mathscr A_{E,p}=1\) based on a numerical BSD ratio.

This splits the former ILTR universal conjecture into a local-global biextension comparison (4), potentially independently provable, and a separate deep Kato-to-regulator leading-term assertion (6).

## IV. A proved, uniform quantitative Sha obstruction at arbitrary depth

Let E/Q be any elliptic curve of rank r<p with E(Q)[p]=0. Fix a cyclic p^k extension K/Q with \(E[p](K)=0\) and \(R=\mathbf Z_p[\operatorname{Gal}(K/\mathbf Q)]\simeq\mathbf Z_p[T]/((1+T)^{p^k}-1)\), maximal ideal \(\mathfrak m=(p,T)\). Let \(X_K=\operatorname{Sel}_{p^\infty}(E/K)^\vee\), and suppose **the actual** arithmetic Mazur–Tate element \(\Theta_K\) belongs to \(\operatorname{Fitt}_{0,R}(X_K)\), as guaranteed by Bullach–Honnor's Theorem 1.4(b) when its hypotheses hold (up to the harmless involution #). Put
\[
t_p=\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p],\quad
d_K=\dim_{\mathbf F_p}(X_K/\mathfrak m X_K).
\]

**THEOREM IV.1 (uniform Sha-depth obstruction).** Without assuming Sha(E/Q) finite,
\[
\boxed{\Theta_K\in\mathfrak m^{r+t_p}.}
\tag{7}
\]
If \(\Theta_K=\sum_{j\ge0}c_jT^j\) and \(c_j\equiv0\bmod p^k\) for every \(0\le j<r\), then
\[
\boxed{c_r\equiv0\bmod p^{\min(k,t_p)}.}
\tag{8}
\]

**Proof.** Inflation–restriction and ordinary local Kummer compatibility inject
\(\operatorname{Sel}_p(E/\mathbf Q)\to\operatorname{Sel}_p(E/K)^G\)
because \(E[p](K)=0\). This is an injection of Fp vector spaces. Base Kummer gives
\(\dim\operatorname{Sel}_p(E/\mathbf Q)=r+t_p\).
Pontryagin duality identifies
\(\dim\operatorname{Sel}_p(E/K)^G=\dim X_K/\mathfrak mX_K=d_K\)
when E[p](K)=0. Therefore \(d_K\ge r+t_p\).

Choose a minimal finite R-presentation \(R^m\to R^{d_K}\to X_K\to0\). Its entries lie in \(\mathfrak m\), so all \(d_K\times d_K\) minors, and thus the entire \(\operatorname{Fitt}_{0,R}(X_K)\), are in \(\mathfrak m^{d_K}\subseteq\mathfrak m^{r+t_p}\). The assumed inclusion of true \Theta proves (7).

For (8) there is nothing to prove if \(t_p=0\). Otherwise put \(b=\min(k,t_p)\). Since r<p, every binomial coefficient \(\binom{p^k}{j}\) for 1≤j≤r is divisible by p^k, so the natural map
\[
R\twoheadrightarrow B_b=(\mathbf Z/p^b)[T]/T^{r+1}
\]
is a well-defined ring surjection. Because \((p,T)^{r+b}B_b=0\) and \(r+t_p\ge r+b\), (7) implies that the image of \Theta in B_b is zero. The lower Taylor coefficients c_j, j<r, vanish mod p^b by hypothesis, so this image is \(c_rT^r\). Since \(T^r\ne0\) in B_b, it follows that c_r≡0 mod p^b, proving (8). QED.

**Corollary IV.2 (389a1 p² universal exclusion).** For E389a1, with analytic rank and MW rank both 2 and positive root number, odd-p Cassels–Tate alternating pairing and the proved p-parity theorem imply \(t_p\) is EVEN. Hence if any \(\Sha(E/\mathbf Q)[p]\ne0\), then \(t_p\ge2\) and for **every genuine depth-p² two-auxiliary Mazur–Tate theta satisfying the low-jet normalization**,
\[
\boxed{\Theta_K\in\mathfrak m^4,\qquad
c_2\equiv0\bmod p^2,\qquad
\tilde\delta_{q_1q_2}\equiv0\bmod p^2
}
\tag{9}
\]
where the final equality uses the independently established Hecke-norm diagonal identity \(c_2\equiv r\tilde\delta_{q_1q_2}\bmod p^2\), with r a p-unit.

This is a REAL all-pairs arithmetic DIVISIBILITY THEOREM; it does not require or infer global Sha finiteness. Its converse for one witness with c2 nonzero modp² is the already proved valuation-one gate. The strength here is the quantified **FOR EVERY deep pair** conclusion if Sha[p] is nonzero.

### Comparison with real archived data

- p=5, depth 25, q=(5351,13001): actual c2≡15 mod25, so (9) excludes nonzero Sha(Q)[5]; the user-reported real histogram and prior Fitting theorem agree.
- p=19, depth19, q=(2243,3877): actual c2≡4 mod19, so (7) at k=1 excludes Sha(Q)[19] directly.
These finite examples are consistent with the general theorem; they are NOT evidence for its antecedent Sha nonzero.

## V. Why local Tate weights alone cannot conclude BSD, now at p² precision

For any sufficiently large p, the Kummer–Chebotarev theorem produces two deep admissible primes with rank-one local quotients, \(p\parallel\#E(\mathbf F_q)\), and local MW determinant a p-unit. Their independent local reduced-Tate forms have
\[
2\det(\mathcal B_{q_1}+\mathcal B_{q_2})\in\mathbf F_p^\times.
\]
This local arithmetic is available **whether or not Sha[p] is zero**. However Theorem IV.1 says that if t_p≥2, every authentic depth-p² quadratic coefficient is zero mod p², and in particular the genuine two-factor Kurihara coefficient is zero modp. Thus there is an explicit formal obstruction to deriving
\(\tilde\delta_{q_1q_2}=2\det(\mathcal B_1+\mathcal B_2)\bmod p\)
from local linear algebra and Chebotarev alone: the proposed identity would *itself* force Sha[p]=0. This is mathematically legitimate as a NEW conjecture, but it cannot be relabeled a theorem until a genuine global Kato/BSD-strength comparison eliminates the extra Selmer obstruction.

The correct immediate research target is (4), a comparison of TWO genuine height pairings that are defined independently of Sha. After that, the required coefficient-to-regulator comparison (6) must be attacked explicitly as a statement about a Kato zeta element in a determinant line, **with its Sha correction**. A simple equality without any Sha factor would assume the desired conclusion.

## Primary sources

- Burns–Kurihara–Sano, *On derivatives of Kato's Euler system and the Mazur–Tate Conjecture*, §2.2, Hypothesis 2.2(iii), Conjecture 2.3, Remark 2.7, and formula (8), https://arxiv.org/pdf/2103.11535 .
- Bullach–Honnor, *On the refined Birch–Swinnerton–Dyer type conjectures of Mazur and Tate*, Theorem 1.4(b) and Hypothesis 1.2, https://dominikbullach.github.io/MazurTate.pdf .
- Darmon, *Euler systems and refined conjectures of Birch–Swinnerton-Dyer type*, §2.2, https://www.math.mcgill.ca/darmon/pub/Articles/Research/06.Euler-systems/paper.pdf .
- Earlier authentic p² certificate and Kummer restriction: paper/bsd389_p2_valuation_one_Kurihara_true_Selmer_Fitting_parity_improvement_2026-11-23.md
- Independently constructed reduced Tate forms: paper/bsd389_independent_reduced_Tate_local_weights_rank2_global_delta_conjecture_2026-11-24.md

**Verdict:** the p-adic local-conductor lattice and its canonical divided Mazur–Tate regulator are now INTEGRALLY DEFINED AND PROVED; the general arithmetic Sha-depth obstruction is PROVED; the derived biextension-to-reduced-Tate identity (4) and global leading coefficient equality (6) remain OPEN. No new computation was needed.


## VI. The auxiliary cokernel factor is a p-UNIT, but its precise residue must still be retained

BKS §2.2, Remark 2.7, formula (8), uses **both** the height discriminant \(R_S\) and
\[
J_S:=\#\operatorname{coker}\left(
E(\mathbf Q)\longrightarrow
 E(\mathbf F_{q_1})\oplus E(\mathbf F_{q_2})\oplus
 \bigoplus_{\ell\mid 389}E(\mathbf Q_\ell)/E^0(\mathbf Q_\ell)
\right).
\]
For 389a1 the bad-prime component group at 389 is trivial. The assumed local reduction isomorphism \(M/pM\to\bigoplus E(\mathbf F_{q_i})/p\) means that **the cokernel has no p-primary part**:
\[
\boxed{v_p(J_S)=0.}
\]
Proof: at both q_i, the local Sylow-p subgroup has order exactly p, and the reductions of P,Q generate their product; all other local group factors have order prime to p. Thus any cokernel of the full reduction map has order prime to p. QED.

This is a further useful arithmetic simplification: the factor \(J_S\) will NEVER cause an additional p-divisibility in our MW-independent-pair setting. Nevertheless \(J_S\) may reduce to an arbitrary **nonzero** residue mod p and must be kept in the **EXACT scalar normalization** of any true coefficient-to-regulator formula; it is not automatically congruent to 1 mod p.

**Critical source-scope note:** BKS §2.1 begins its discussion of the **algebraic BSD constant** under an explicit hypothesis that Sha is finite. The *geometric Mazur–Tate biextension height* \(h_S\) itself is defined independently of that hypothesis, so our lattice and definition (2) do not assume it. The conjectural global leading term involving \(\#\Sha\) does, and can NOT be invoked as a theorem in the unknown-finite case. Likewise BKS Hypothesis 2.2(iii) fails for our auxiliary q_i, so their normalizing comparison cannot be imported verbatim.

**Important two-stage theorem target:** first establish the genuine height identity (4), with all local reciprocity normalizations. This is a theorem about EXISTING arithmetic pairings and does not involve Sha. Only then attempt the independent Kato/Mazur–Tate leading term, retaining \(J_S\), the real components, and the potential Selmer/Sha factor. In particular observing the scalar 2 at finitely many p does NOT determine the p-independent value of \(J_S\), the algebraic BSD constant, or the universal global map.


## VII. Source-audit correction: Burns–Macías Castillo Theorem 10.3 is the closest EXISTING comparison, but anomalous tame primes violate TWO explicit hypotheses

Burns and Macías Castillo, *On refined conjectures of Birch and Swinnerton-Dyer type for Hasse–Weil–Artin L-series*, original author arXiv manuscript https://nms.kcl.ac.uk/david.burns/web_page/rbsd-arXiv.pdf , **Theorem 10.3**, proves coincidence of the Mazur–Tate biextension height and Nekovář Bockstein height **under hypotheses (H1)–(H6) from §6**, plus absence of p-torsion over F and Hypothesis 10.1.

Two conditions prohibit its immediate application to the auxiliary fields constructed here:

- **(H4)**: for every finite place v away from p lying over a place ramified in the extension, the reduction \(E(\kappa_v)[p^\infty]\) must vanish. Our q1,q2 are **ramified** and satisfy \(p\parallel\#E(\mathbf F_{q_i})\); in particular \(E(\mathbf F_{q_i})[p]\ne0\). Thus H4 **fails at each chosen q_i**. The exact local one-dimensional defect is the Frobenius finite–singular module already studied and proved nonzero in paper/bsd389_local_Frobenius_Kummer_reduced_Tate_finite_singular_theorem_p19_2026-11-24.md. This is a genuine missing local complex, not an ignorable scalar factor.
- **(H6)**: the relevant \(\Sha(E/F)\) is assumed FINITE, for F the top extension in the theorem. Finiteness over these ramified auxiliary fields is NOT a prerequisite we may silently invoke. Even a separate numerical norm or theta model is not an automatic verification of H6; one would need an independent theorem at each F.

The published proof explicitly uses H4 in §6 to deduce vanishing of the local p-completed points at ramified non-p places (around original lines 2925–2936). Thus *quoting Theorem 10.3 as an unconditional proof of our equation (4) would be mathematically wrong*. Its canonical Bockstein construction is nonetheless the proper existing framework from which to attempt a NEW anomalous tame comparison.

### Concrete new theorem target, without hiding the obstruction

Prove a *corrected* Nekovář/Bockstein–Mazur–Tate identity over cyclic p-extensions with precisely two anomalous tame ramified primes, using the **modified** Selmer complex that retains the two rank-one finite–singular local modules rather than requiring H4. The target must:

1. identify the local boundary form in the determinant triangle with the independently proved local \(-N_q\)-Tate quadratic form, with primitive-root orientation;
2. prove, by functoriality of the actual biextension height, that the genuine divided lattice pairing \(\mathscr H_{\chi_r,p}\) equals \(\mathcal B_{q_1,p}+r\mathcal B_{q_2,p}\) on \(E(\mathbf Q)/p\), including any nontrivial explicit local unit corrections;
3. avoid assuming H6 or \(\Sha(E/F)\) finite by working with suitable perfect Selmer complexes and determinant lines; **do not claim the resulting determinant is automatically a p-unit**. The natural torsion/Sha determinant component must remain visible and is exactly the independent obstruction to completing BSD.

The local comparison (1) is proved as a piece of finite-field Kummer/Tate arithmetic in previous notes. The two GLOBAL comparisons (2), (3) **are not proved**; these statements are a concrete proposed extension of published theorem 10.3, not a citation of an existing implication.

**Mathematical boundary:** the fact that a canonical local correction is one-dimensional does NOT prove its Bockstein lift equals the authentic global Mazur–Tate biextension derivative. That equality still requires constructing a morphism of arithmetic complexes, checking all signs and unit normalizations, and proving the relevant determinant section does not acquire an uncontrolled Selmer factor.

Primary source exact scope: Burns–Macías Castillo, Theorem 10.3 (around original lines 6393–6399), hypotheses (H4) and (H6) in §6 (around lines 2772–2779), and their proof of local vanishing (around lines 2925–2936), https://nms.kcl.ac.uk/david.burns/web_page/rbsd-arXiv.pdf .
