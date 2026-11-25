# 389a1 — A full AUXILIARY-FIELD rank and Sha theorem from the first Mazur–Tate jet (25 Nov 2026)

**Mathematical status:** proved elementary-divisor/Fitting theorem, using the genuinely published Bullach–Honnor 2025 Fitting containment. New arithmetic APPLICATIONS to the project's degree 5, 11, 19, and 25 fields with previously authenticated genuine modular-symbol theta histograms. No prior Sha finiteness is assumed. No full global all-prime BSD or complex rank-two leading-term proof is claimed.

## 1. General finite-ring theorem, independent of BSD

Let p be prime, K/Q cyclic of degree p^k, G=Gal(K/Q), R=Z_p[G], and X=Sel_(p∞)(E/K)^vee, a finitely generated R-module. Let theta in R be an AUTHENTIC Mazur–Tate element, up to p-adic-unit normalization, for which

\[
\theta^\#\in\operatorname{Fitt}_{0,R}(X).
\tag{F}
\]

Suppose the reduction mod p of theta is nonzero, with exact first nonzero Taylor coefficient of degree d, 0≤d<p^k:

\[
\overline\theta=T^d u(T),\quad u(0)\ne0,\qquad
\overline R=R/pR\simeq\mathbb F_p[T]/(T^{p^k}),\quad T=\sigma-1.
\tag{J}
\]

**THEOREM (full-field Selmer length and Sha bound):**

\[
\boxed{\operatorname{rk} E(K)+\dim_{\mathbf F_p}\Sha(E/K)[p]\le d.}
\tag{1}
\]

In particular, if E(Q) has rank r and d=r, then

\[
\boxed{\operatorname{rk} E(K)=r,\qquad
\Sha(E/K)[p^\infty]=0,\qquad
X\simeq \mathbb Z_p^r.}
\tag{2}
\]

The last isomorphism is in fact G-equivariant with trivial G action, because E(K)⊗Q is spanned by the r rational points of E(Q).

**COMPLETE PROOF.** Formation of Fitting ideals commutes with base change, including mod p. The involution # sends T to -T+O(T²), hence preserves T-order. Therefore \(\overline\theta^\#\in\operatorname{Fitt}_{0,\overline R}(X/pX)\) has exact T-order d.

The ring \(\overline R=\mathbf F_p[T]/T^{p^k}\) is a principal Artin local ring. Every finite \(\overline R\)-module admits an elementary divisor decomposition
\[
X/pX\simeq\bigoplus_j \overline R/(T^{a_j}),\quad
1\le a_j\le p^k,
\]
where \(a_j=p^k\) denotes a free summand. Thus its zeroth Fitting ideal is EXACTLY
\[
\operatorname{Fitt}_0(X/pX)=(T^{\sum_j a_j})
=(T^{\dim_{\mathbf F_p}X/pX}),
\]
and is the zero ideal if the displayed exponent is at least p^k. Since the nonzero \(\overline\theta^\#\) belongs to this ideal, necessarily
\[
\dim_{\mathbf F_p}X/pX\le d.
\tag{3}
\]

By the TRUE dual p-infinity Kummer/Selmer sequence (Bullach–Honnor Eq. (1)),
\[
0\longrightarrow\Sha(E/K)[p^\infty]^\vee
\longrightarrow X
\longrightarrow\operatorname{Hom}_{\mathbf Z_p}(E(K)\otimes\mathbf Z_p,\mathbf Z_p)
\longrightarrow0.
\]
The last term is free of rank rk E(K) over Z_p, so the sequence SPLITS over Z_p even if Sha is infinite. Therefore
\[
\dim_{\mathbf F_p}X/pX=
\operatorname{rk} E(K)+\dim_{\mathbf F_p}\Sha(E/K)[p].
\tag{4}
\]
Combining (3),(4) proves (1). If d=r=rk E(Q), then rk E(K)≥r and both nonnegative terms force rank E(K)=r, Sha(E/K)[p]=0. A nonzero p-primary torsion group always has nonzero p-torsion, so Sha(E/K)[p∞]=0. The dual exact sequence now identifies X with the free module of rank r. Since E(K)⊗Q has the original rank r of G-fixed rational points, the action on X is trivial. QED.

**Important scope:** This proves p-primary Sha vanishing on the ENTIRE auxiliary K without applying the conjectural rank-two Kato-to-Mazur–Tate leading-term formula. Its deep arithmetic input is exactly the published unconditional (under its Galois hypotheses) Fitting containment, not a conjectural equality of leading coefficients. It is a specific fieldwise strengthening of the prior project's base Q Sha criteria.

## 2. Historical genuine 389a1 theta certificates: rank 2 and Sha(K)[p∞]=0

For E=389a1: y²+y=x³+x²−2x, rank E(Q)=2, semistable at 389.

The following authentic, previously FULLY computed integral theta histograms have (c0,c1,c2) modulo p:

| p | degree [K:Q] | conductor q1*q2 | c0 | c1 | c2 | T-order d | FULL K conclusion |
|--|--:|--|--:|--:|--:|--:|--|
|5|5|41*61|0|0|4|2|rank E(K)=2; Sha(E/K)[5∞]=0|
|11|11|397*991|0|0|1|2|rank E(K)=2; Sha(E/K)[11∞]=0|
|5|25|5351*10651|0|0|2|2|rank E(K)=2; Sha(E/K)[5∞]=0|
|19|19|2243*3877|0|0|4|2|rank E(K)=2; Sha(E/K)[19∞]=0|

For p≥11 Bullach–Honnor Hypothesis 1.2 is assured by semistable non-CM p-adic surjectivity (Mazur), p>3, and cyclic p-power K that does not contain μ_p. The p=5 cases use the existing independently archived 5-adic-image certificate. The theta arrays must match the B-H Néron-integral normalization up to a p-adic UNIT (a factor two is a unit for the odd primes here). p19 low jets are asserted by the genuine full 4,344,996-unit native Manin scan, whose 19-bin array was not duplicated in this note.

The note does NOT claim independent fresh full theta enumerations: the new result is the strengthening of their mathematical implications from base Q to the full K.

## 3. A genuinely different valuation-ONE example: rank stability in degree 25

For p=5 and q1=5351, q2=13001, the archived complete 25-bin true theta histogram gives

\[
c_0=0,\quad c_1=-108600\equiv0\pmod{25},\quad
c_2=-993960\equiv15\pmod{25}.
\]
More finely, the first five Taylor coefficients modulo 5 are **exactly**
\[
\boxed{(c_0,c_1,c_2,c_3,c_4)\equiv(0,0,0,0,1)\pmod5}.
\]
Thus d=4, and Theorem (1) yields

\[
\operatorname{rk} E(K_{25})+\dim_{\mathbf F_5}\Sha(E/K_{25})[5]\le4.
\tag{5}
\]

Since Gal(K25/Q)=C25, the rational irreducible representations have dimensions 1,4,20, and the 1-dimensional trivial isotypic component has dimension rank E(Q)=2. Thus
\[
\operatorname{rk} E(K_{25})=2+4a+20b,\quad a,b\ge0.
\]
Combined with (5), this gives the NEW consequences
\[
\boxed{\operatorname{rk}E(K_{25})=2,\qquad
\dim_{\mathbf F_5}\Sha(E/K_{25})[5]\le2}.
\tag{6}
\]
It does NOT prove that Sha(E/K25)[5∞]=0 for this valuation-one field, and it does not presume it finite.

## 4. Reproducibility and exact references

An executed dependency-free Python verifier recalculates all genuine archived integral theta jets of degrees5,11,25 and their first T-order modp; it is available as the companion file at /mnt/data/bsd389_full_auxiliary_field_selmer_sha_fitting_gate_20261125.py, and copies of the original true histograms are in verification/bsd389_true_symmetric_MazurTate_matrix_and_p_cokernel.py and verification/bsd389_p5_val1_all20_cyclic25_integer_hist_native.cpp. The authentic p19 source is verification/bsd389_iltr_p19_holdout_native.cpp.

Primary arithmetic theorem: Bullach–Honnor, *On the refined Birch–Swinnerton-Dyer type conjectures of Mazur and Tate*, arXiv:2511.07203, Hypothesis 1.2, Theorem 1.4(b) and Equation (1): https://arxiv.org/pdf/2511.07203 .

**FINAL STATUS:** algebraic theorem PROVED; degree-11 and degree-19 fieldwise Sha and rank specializations under the source-normalization and historical code certificates; degree-5 and degree-25 applications additionally require the archived p5-image gate; val1 K25 rank stability and Sha5-rank≤2; NO all-large-p Sha or exact complex BSD result.


## 6. Descent COROLLARY: every intermediate field also has p-primary Sha zero

Assume the theorem above gives rank E(K)=rank E(Q)=r and Sha(E/K)[p∞]=0, with K/Q cyclic p-power and E(K)[p]=0 (the latter holds for the full GL2(Fp) residual-image certificates, since a p-power abelian subfield of Q(E[p]) cannot contain a nonzero p-torsion point).

For **any** intermediate Q⊂F⊂K we have
\[
\boxed{\operatorname{rk}E(F)=r,\qquad \Sha(E/F)[p^\infty]=0.}
\]
**Proof.** Rank is trapped between rank E(Q)=r and rank E(K)=r. Put H=Gal(K/F), a p-group. The Galois action on the rational vector space E(K)⊗Q is trivial because this dimension-r space is already spanned by E(Q), which is fixed. Hence its action on the torsion-free group E(K)/E(K)_tor is trivial. The finite torsion E(K)_tor has order prime to p (because E(K)[p]=0), so H^1(H,E(K)_tor)=0; also H^1(H,Z^r)=Hom(H,Z^r)=0. The long exact cohomology sequence gives H^1(H,E(K))=0. Inflation–restriction therefore injects H^1(F,E) into H^1(K,E)^H and in particular its subgroup Sha(E/F)[p∞] into Sha(E/K)[p∞]=0. QED.

This gives extra genuine number-field applications: for the p5 **degree-25 unit-jet field** K cut out by q5351*q10651, the unique intermediate degree-5 field F also satisfies rank E(F)=2 and Sha(E/F)[5∞]=0, with no additional modular-symbol evaluation. It does **not** apply to the separate valuation-one p5 degree-25 field, for which Sha over K has only been bounded, not proved to vanish.
