# 389a1: exact odd-prime Selmer parity gap and the correct Kato core rank

Date: 2026-10-26. **Unconditional structural theorem in the good-ordinary range**, plus a corrected research target. This document does **not** establish a global bound or a complete Sha-finiteness theorem.

## Theorem 1: every ordinary odd p-Selmer dimension is even

Let `E: y²+y=x³+x²−2x` over Q, with rank E(Q)=2, no rational torsion, and analytic root number +1. Let p be any odd prime of good **ordinary** reduction (so p!=389). Write `s_p=corank_{Z_p}(Sel_{p^infinity}(E/Q))` and `d_p=dim_{F_p} Sel_p(E/Q)`.

**Proof.** Jan Nekovář's *On the parity of ranks of Selmer groups II*, Theorem A, establishes for an elliptic curve E/Q of good ordinary reduction at p that the analytic rank and s_p have equal parity. Here the analytic rank is 2, hence s_p is even.

Mazur–Rubin, *Kolyvagin systems*, Proposition 2.1 (see `https://annals.math.princeton.edu/wp-content/uploads/annals-v166-n2-p08.pdf`) establishes

`s_p ≡ d_p - dim_{F_p} E(Q)[p] mod 2`

by the self-dual Kummer Selmer structure and the alternating Cassels–Tate pairing on the finite p-primary Sha quotient modulo its maximal divisible subgroup. Since `E(Q)[p]=0`, it follows that `d_p` is even. The Kummer sequence also implies `d_p>=rank E(Q)=2`. Thus

`d_p ∈ {2,4,6,8,...}`.

**Important:** The proof neither presumes that Sha[p^infinity] is finite nor that p-adic BSD holds. It invokes two published **proved** parity statements.

### Stronger-than-expected exact vanishing criterion

For every such p,

`d_p <=3  =>  d_p=2  =>  Sha(E/Q)[p]=0  =>  Sha(E/Q)[p^infinity]=0`.

This is an exact parity-assisted criterion. To obtain a **uniform** vanishing theorem beyond a finite exceptional set, it now suffices to prove a uniform one-step Selmer bound `d_p<=3` for all sufficiently large good-ordinary p. That bound is **NOT derived** here or from the existing generalized Kato classes. Supersingular, bad, and p=2 require separate input.

## Theorem 2: core Selmer rank for T_p(E) is one, not two

Take the canonical Mazur–Rubin Selmer structure on `T=T_p(E)` for E/Q with p odd and the standard irreducibility/dual-invariant hypotheses. The expected/core Selmer rank of this representation is

`chi(T,F_can)=rank_{Z_p}(T^-) = 1`,

where `T^-` is the minus eigenspace of complex conjugation. More generally the formula is the archimedean corank of the Cartier dual's invariants, which equals one for the two-dimensional odd symplectic Galois representation E[p^infinity] over Q.

This is independent of the **actual** Mordell–Weil rank `rank_Z E(Q)=2` and independent of the analytic vanishing order of `L(E,s)`. A core-rank-two Kolyvagin system theorem **cannot be applied to the ordinary canonical T_p(E) Selmer structure simply because E(Q) has rank two**.

Theorems: Barry Mazur and Karl Rubin, *Controlling Selmer groups in the higher core rank case*, JTNB 28 (2016), Introduction and core-rank formula, `https://jtnb.centre-mersenne.org/item/10.5802/jtnb.933.pdf`; compare Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems II* (2025) `https://kclpure.kcl.ac.uk/portal/en/publications/on-the-theory-of-higher-rank-euler-kolyvagin-and-stark-systems-ii/`.

## What this changes in our 389a1 research program

The right object to seek is an **integral second-order derivative** of a norm-compatible Kato/Iwasawa Euler system, compatible with the canonical core-rank-one Selmer structure and carrying a provable **finite Sha upper bound**. Burns–Kurihara–Sano (JMSJ 76, 2024) prove higher-rank 'order of vanishing' properties of Kato derivatives and formulate the additional Generalized Perrin–Riou leading-term congruence; their abstract explicitly distinguishes proved vanishing-order statements from the still-conjectural leading-term normalization.

Neither the conditional `kappa_p != 0` from Castella–Hsieh nor any primitive generator in `Sel(Q,T_p E)` furnishes this required finite-Sha upper-bound without a theorem relating derived Euler/Kolyvagin systems to the **finite** Selmer quotient. The compact Tate module of a finite p-primary Sha is zero, so compact Selmer alone is blind to that finite torsion.

The genuine unproven target now becomes:

**Target U:** Construct a norm-compatible, integral, second-derived Kato/Kolyvagin system for E with a source theorem bounding the *finite* mod-p Selmer defect; prove the bound `dim Sel_p(E/Q)<=3` for all sufficiently large odd good-ordinary p. Then Theorem 1 proves the vanishing of Sha[p^infinity] for all such p. An alternative is a genuinely uniform Fitting-ideal bound from a fixed nonzero arithmetic integer D; such a D is **not currently constructed**.

### Optional square-factor refinement

Whenever a legitimate arithmetic theorem supplies a fixed positive integer D such that the finite p-primary group satisfies `#Sha(E/Q)[p^infinity] | D` for every eligible odd p, Cassels–Tate's nondegenerate alternating pairing implies each p-primary order is a square. Therefore any *nontrivial* component forces `p² | D`. So only the squared-prime-divisor support `{p:p²|D}` could remain. This conditional refinement further motivates seeking a single integral Fitting bound, but it does **not** conjure one into existence.

## Why the bounded 2026 computations don't prove Target U

The completed p=16231 numerical Sage/Kato upper bound and the published Stein–Wuthrich finite range below 48859 prove/localize many individual p-primary cases; a finite collection gives no control of arbitrarily large primes. The exact 390 Manin relations are fixed arithmetic data of modular symbols, **not** a uniform presentation of the changing p-Selmer groups. The conductor53 order-nine Gross period proves a conditional auxiliary Rankin central nonvanishing statement at one p, not an integral second-derived zeta-element compatible simultaneously with all ordinary p.

**Status:** New verified parity criterion and corrected representation core rank; **uniform Selmer bound and full Sha/BSD remain OPEN**.

Primary citations:

- Nekovář, *On the parity of ranks of Selmer groups II*, Theorem A, `https://webusers.imj-prg.fr/~jan.nekovar/pu/parity2.pdf`.
- Mazur–Rubin, *Proposition 2.1: self-dual Selmer parity*, `https://annals.math.princeton.edu/wp-content/uploads/annals-v166-n2-p08.pdf`.
- Mazur–Rubin, *Controlling Selmer groups in the higher core rank case*, `https://jtnb.centre-mersenne.org/item/10.5802/jtnb.933.pdf`.
- Burns–Kurihara–Sano, *On derivatives of Kato’s Euler system for elliptic curves*, JMSJ 76 (2024) 855–919, `https://doi.org/10.2969/jmsj/90699069`.
- [Prior integral gap of generalized Kato at p16231](389a1_p16231_generalised_kato_theoremA_and_integral_shasupport_gap_2026-10-26.md).

---

## Major upgrade (2026-10-26): parity holds for **every odd prime**, including supersingular and 389

The earlier restriction to good ordinary primes in Theorem 1 was unnecessarily narrow. Tim and Vladimir Dokchitser, *On the Birch–Swinnerton-Dyer quotients modulo squares*, Annals of Mathematics 172 (2010), 567–596, **prove the p-parity theorem for all elliptic curves E/Q and ALL primes p**, with no ordinary reduction or Sha finiteness hypothesis: `(-1)^{corank_Zp Sel_{p^infinity}(E/Q)}=w(E)`. See https://annals.math.princeton.edu/2010/172-1/p11 .

For E=389a1 the root number w(E)=+1. For an odd prime p, let `A=Sha(E/Q)[p^infinity]`. As A is of cofinite Zp-type, split `A=(Qp/Zp)^t ⊕ A_fin` (noncanonically) where `A_fin` is finite. The Dokchitser parity theorem says `rank(E(Q))+t=2+t` is even, hence t is even. The nondegenerate alternating Cassels–Tate pairing on the finite quotient `A_fin=A/A_div` implies `dim_Fp A_fin[p]` is even. Since `A[p]` has dimension `t+dim_Fp A_fin[p]`, this is even.

By the exact p-Kummer sequence and E(Q)_tors=0:

`dim_Fp Sel_p(E/Q)=2+dim_Fp A[p] ∈ {2,4,6,8,...}`

for **EVERY odd prime p**, whether E has good ordinary reduction, good supersingular reduction, or multiplicative reduction at p=389. Therefore:

`[dim_Fp Sel_p(E/Q) ≤3] ⇒ Sha(E/Q)[p^infinity]=0`

for **every odd p**, without assuming Sha finite beforehand. The only remaining prime for separate parity/2-descent treatment is 2.

**Crucial nonclaim:** Although a uniform `dim Sel_p≤3` for sufficiently large odd p would now cover *both* ordinary and supersingular primes, no known result in our current project supplies this upper bound. Elkies proved there are infinitely many supersingular primes (https://people.math.harvard.edu/~elkies/math_pubs.html), so a theorem limited to ordinary primes is not sufficient for global BSD even up to finite exceptions. The improvement is that the **parity implication**, unlike ordinary p-adic L-series methods, is fully uniform across reduction types.
