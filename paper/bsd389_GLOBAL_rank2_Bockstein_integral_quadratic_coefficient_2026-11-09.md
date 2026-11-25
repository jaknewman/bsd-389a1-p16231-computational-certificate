# BSD 389a1 — Rank-two Bockstein determinant coefficient and a sharp integral torsion bound (9 November 2026)

**Scope: new exact algebraic theorem and independently executed Smith-normal-form audit. NOT a constructed Selmer presentation or actual global Sha annihilator.**

## Source audit and missing implication

Castella–Sano Theorem B (2026, https://web.math.ucsb.edu/~castella/Kurihara.pdf) establishes refined **some-length** Kurihara primitivity M_infty=ord_p(Tam) under good-prime large-image and Manin-unit hypotheses. Kim's Theorem 1.1 (2026 update, https://arxiv.org/abs/2505.09121) determines Selmer corank and finite structure from the **first nonzero** derivative order and valuation differences. Their combination **does not** automatically make the rank-two specialized leading coefficient a p-adic unit.

## Exact obstruction in a perfect two-term Iwasawa model

Fix odd p, arbitrary integer a>=1, R=Zp[[T]]. Define

    A_a(T)=diag(T,T,T+p^a,T+p^a).

Then

    det A_a(T)=T^4+2p^a T^3+p^(2a) T²,

which is globally primitive (coefficient [T^4] equals 1), while [T²]=p^(2a) has arbitrarily large p-valuation. At T=0,

    coker A_a(0)=Zp² ⊕ (Z/p^a)².

The finite summand has a perfect alternating pairing and exactly the even p-primary order expected of a finite Cassels–Tate module. Furthermore coker A_a(T) has NO nonzero finite R-submodules, because

    R/(T)≅Zp, R/(T+p^a)≅Zp

are torsionfree Zp-modules. Therefore a primitive *global* determinant plus exact specialized rank two, even plus absence of finite Iwasawa submodules and alternating finite pairing, cannot imply that the rank-two finite quotient vanishes.

The alternate model diag(T,T,T,T) has equally primitive characteristic determinant T^4 but specialized corank 4. This illustrates why all-length Kurihara nonvanishing does not by itself bound the first nonzero length by two.

**These are abstract exact models, not the actual Selmer complex or actual Kurihara family for E389a1.** Global 'primitivity' here is only analogous to the Iwasawa determinant content; no claimed identification of coefficient-wise systems.

## New sharp universal integer annihilator criterion

**Theorem.** Let A(T)∈M_m(Z[[T]]) with rank_Q A(0)=m−2. Write det A(T)=c2 T²+c3 T³+... . Let F=(coker A(0))_tors. Then

    **#F divides |c2|**.

In particular, c2!=0 implies c2 F=0.

Proof: in the determinant's T² coefficient, at least m−2 columns come from A(0). Terms containing m or m−1 constant columns vanish because rank A(0)=m−2. Expanding the remaining determinants along the two nonconstant columns expresses c2 as a Z-linear combination of maximal nonzero (m−2)×(m−2) minors of A(0). Their gcd equals #F by Smith normal form, hence divides c2. This is sharp for A(T)=diag(T,T,T+a,T+a), where #F=a²=c2.

**Local corollary.** For A_p(T)∈M_m(Zp[[T]]) with rank_Zp coker A_p(0)≥2, if [T²]det A_p(T) is a p-adic UNIT then coker A_p(0)≅Zp²: reduction mod p forces rank_Fp A_p(0)≥m−2, while generic rank must be <=m−2. Therefore Zp rank=2 and p-torsion=0.

## Exact, but conditional, 389a1 target

If a SINGLE A_E(T)∈M_m(Z[[T]]) with rational corank two at T=0 could be constructed and one PROVED for all p functorial injections

    Sha(E389a1)[p∞]^∨ → (coker A_E(0)⊗Zp)_tors,

then **C_E=[T²]det A_E(T) !=0 would annihilate all Sha**, proving its finiteness. Such a presentation or comparison has **NOT** been constructed. The separate p-cyclotomic Iwasawa parameters T_p depend on p and cannot simply be treated as specializations of a common integer T. The exact 390-entry Manin eigenvector gives no missing comparison. Strong complex BSD leading-term equality would still be separate.

## Executed exact verification

The code `verification/bsd389_ranktwo_Bockstein_integral_determinant_audit_20261109.py` checks a=1,2,3,5,6,25,125, performs independently unimodular integral row/column transforms, verifies Smith-normal-form torsion orders equal c2=a² and a rescaled Bockstein where c2=2a², and verifies the corank-four alternative model; all PASS. Neither script nor note computes an actual p-Selmer group.

**Primary sources:** Castella–Sano 2026 Theorems A/B https://web.math.ucsb.edu/~castella/Kurihara.pdf; Kim 2026 Th 1.1 https://arxiv.org/abs/2505.09121.
