# E389a1: Exact mixed augmentation coefficient identity, and the BKS cyclotomic mismatch

Date: 2026-11-02.

## 1. Exact mod-p coefficient extraction (elementary, unconditional)

Take odd p>=5 and p-admissible distinct q1,q2, n=q1q2. Fix primitive roots g_i in F_(q_i)^× and residue discrete log maps e_i : (Z/n)^× -> F_p, where e_i(a) = log_(g_i)(a mod q_i) mod p. This exists because p | q_i-1.

Let [a/n]^+ be the **correctly Néron-period normalized** plus modular symbol in F_p (the relevant integrality and Manin constant assumptions are mandatory). Define

Theta_n = Σ_(a mod n)^× [a/n]^+ [a] in F_p[(Z/n)^×].

Map the group ring to R = F_p[X,Y]/(X^p,Y^p) by

Phi_p([a])=(1+X)^{e_1(a)}(1+Y)^{e_2(a)}.

This is an algebra homomorphism: in characteristic p, (1+X)^p=(1+Y)^p=1 in R, and discrete logarithms are additive modulo p. Then the **identity**

[XY]Phi_p(Theta_n)=Σ_a [a/n]^+ e_1(a)e_2(a) = delta_(q1q2) (mod p)

is exact, without Selmer, BSD, or Sha finiteness assumptions. It is a reformulation of Kim, Section 1.4.3, not a new nonvanishing theorem. Reversing Artin conventions may alter coordinate signs, but cannot change unit/nonunit status when handled consistently.

The augmentation ideal J=(X,Y) gives XY in J²/J³. The coefficient extraction [XY] is well defined for the *specific full polynomial* Phi_p(Theta_n); if J^0 or J^1 coefficients are present, the operation [XY] is still meaningful but it is **not** correct to say Theta_n itself lies in J² without separately proving lower-degree vanishing.

For p107 with q1=369793, q2=383917, the genuine user frozen 710-block *archived data* reaggregation yielded half17 and delta34 mod107, hence the archived weighted coefficient [XY] is 34 mod107 **conditional on interpreting the archived 390 Manin entries as the correct plus Néron symbols**. The direct native 70.98bn terms and full normalization were not independently re-executed.

## 2. Burns–Kurihara–Sano 2024 is a *different augmentation problem*

Source: D. Burns, M. Kurihara, T. Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan 76 (2024), 855–919, <https://kurihara.math.keio.ac.jp/bks4.pdf>.

Conjecture 1.1, printed p857 (PDF page 3), uses a real abelian extension F/Q with group G and augmentation ideal I=ker(Z_p[G]->Z_p). For rank r, the proposed zeta norm leading class lives in H¹(O_(F,S),T_pE) ⊗ I^(r-1)/I^r, and conjecturally equals a Bockstein map of a BSD element in wedge^r H¹.

For r=2, this is an **I/I² class**, a first augmentation degree, unlike the **two-direction J²/J³ mixed XY coefficient** of the squarefree auxiliary n=q1q2 Mazur–Tate theta element. These cannot be identified by the rank alone. A new, explicit finite-level comparison map and its normalizations must be constructed.

Crucial theorem-hypothesis audit: BKS **Theorem 1.3** (printed p857, PDF page 3), a concrete theorem on the *order-of-vanishing containment*, assumes **Sha(E/F)[p∞] finite**, as well as p>3, large p-adic Galois image and vanishing local p-torsion. Therefore it CANNOT be used as a proof of p-primary Sha finiteness for a previously unproved F. BKS discuss other unconditional cyclotomic constructions (e.g. Section 4 and Proposition 4.4), which must be distinguished individually, and the leading term equality remains **Conjecture 1.1(iii)** in general.

Their **Conjecture 3.1**, printed p873 (PDF page 19), predicts a finite-level equality with Fitting ideals, rather than a fully established rank-two unit formula. Treating its equality as proved would assume precisely a missing arithmetic bridge.

## 3. Exact next mathematical task

Construct a finite-level cohomological or modular-symbol comparison between (A) the *mixed* double auxiliary augmentation [XY] of Theta_(q1q2) and (B) a properly normalized image of Kato's zeta element via explicit reciprocity at two auxiliary primes. Prove integrality and unit preservation. Any claimed all-large-p unit nonvanishing requires a further independent primitivity theorem; the coefficient identity alone gives none.

Useful independent primary source for the known Kurihara→Selmer result: C.-H. Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, Theorem 1.8 and Section 1.4.3, <https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf>.
