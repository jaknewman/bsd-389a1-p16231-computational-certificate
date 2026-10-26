# The exact obstruction: a uniform Fitting integer is equivalent to global Sha finiteness

Date: 2026-10-26. This note proves a structural equivalence and a squarefree corollary; it does **not** construct the arithmetic integer and therefore does **not** establish finiteness or full BSD for 389a1.

## Theorem (uniform integer iff Sha is finite)

Let E be **any** elliptic curve over Q; in our project E=389a1. For each prime p, write `A_p=Sha(E/Q)[p^infinity]` and `X_p=Hom_cont(A_p,Q_p/Z_p)`, a finitely generated Z_p-module by finite co-type of p-primary Sha. Then the following conditions are equivalent:

**(i)** `Sha(E/Q)` is finite;

**(ii)** there exists one nonzero integer `D_E` such that, for **all primes p**, `D_E in Fitt_0,Z_p(X_p)`.

Moreover, every such D_E satisfies `#Sha(E/Q) | |D_E|`.

**Proof.** The structure theorem for finitely generated modules over the DVR Z_p gives

`X_p ≅ Z_p^{r_p} ⊕ ⊕_{i=1}^{t_p} Z_p/(p^{e_{i,p}})`,

where r_p≥0 and e_{i,p}≥1. Its zeroth Fitting ideal is explicitly

`Fitt_0(X_p)= (0)` if `r_p>0`, and `(p^{sum_i e_{i,p}})` if `r_p=0`.

Assume (ii). Since D_E≠0, for every p we must have r_p=0. Every X_p, hence every A_p, is finite, and

`v_p(#A_p)=sum_i e_{i,p} <= v_p(D_E)`.

For p not dividing D_E, this forces A_p=0. Since Sha is torsion and the only possible nonzero p-primary components occur among the finitely many prime divisors of D_E, Sha is a finite direct sum of finite p-primary groups and `#Sha | |D_E|`.

Conversely, if Sha is finite, take `D_E=#Sha`. Then X_p is finite and `Fitt_0(X_p)=(p^{v_p(#Sha)})`; clearly D_E belongs to that ideal for every p. QED.

**Finite-exception variant.** Replacing 'all p' by 'all p outside a fixed finite set S' proves only finite support and finite p-components outside S; it says nothing about possible infinite p-divisible components at S. If p-primary finiteness is established separately at every p in S, the same equivalence follows with a modified D_E. This is why an 'outside S' integer does **not** alone prove global Sha finite.

## Squarefree integer implies Sha is zero

For an elliptic curve with finite Sha, Cassels–Tate's perfect alternating pairing implies `#Sha(E/Q)` is a perfect square, in fact each p-primary order is a square (Silverman, *Advanced Topics in Arithmetic of Elliptic Curves*, Chapter X, Theorem 4.17; Poonen–Stoll *The Cassels–Tate pairing on polarized abelian varieties*).

Therefore, under (ii), if `D_E` is **squarefree**, the only perfect square dividing `|D_E|` is 1, whence

`Sha(E/Q)=0`.

More generally, for every odd p a hypothetical finite p-primary group must have `v_p(#A_p)` even; thus if `v_p(D_E)≤1`, automatically A_p=0. This parity-of-order refinement is valid only after one has a **genuine** Fitting bound: it cannot turn an arbitrary fixed norm such as 729 into D_E.

## Practical consequence for 389a1

The complete existing data at p=16231 establish a source-conditional Sha-primary-zero implication by a proper Kato/Sage bound. The fixed conductor-53 Gross toric period has a nonzero algebraic norm `729=3^6`; this is an invariant of the **auxiliary Ring class character**, not an established Fitting bound on the integral Selmer defect of E/Q. No source comparison has shown `729 in Fitt_0(X_p)` for all p. Claiming such an inclusion merely because the period is nonzero would, by the theorem above, amount to claiming global finiteness of Sha: this is precisely the missing mathematical input.

Likewise, the nonzero derived generalized-Kato class over `Q_16231(zeta9)` supplies rational Selmer information at **one prime**, not an integral determinant uniform over all primes.

## Exact research target — not a reformulation of achieved results

Construct, using motivic zeta elements or norm-compatible rank-two derived Kato/Kolyvagin systems and a **proved integral leading-term theorem**, an arithmetic `D_E ∈Z\{0}` and establish the map

`D_E ∈ Fitt_0,Z_p(Sha(E/Q)[p^infinity]^vee)`

for all p, including supersingular/bad primes, or all but finitely many p together with explicit finiteness at the exceptions. To derive `Sha(E/Q)=0`, it is sufficient (not necessary) that D_E be squarefree, or to combine its finite square-prime divisors with separate proven p-primary zero gates.

Burns–Kurihara–Sano (2024) prove the higher-rank order-of-vanishing component under hypotheses; their **generalized Perrin–Riou leading-term congruence** remains a distinct conjectural input. Their 2025 Mazur–Tate companion adds unconditional evidence but is not a theorem constructing D_E. The deeper obstruction is the integral Fitting comparison, not a missing finite-field polynomial identity. We cannot honestly assert that a nonzero order-nine Gross period yields the comparison.

## References

- Burns–Kurihara–Sano, *On derivatives of Kato’s Euler system for elliptic curves* (2024): https://doi.org/10.2969/jmsj/90699069
- Burns–Kurihara–Sano, *On derivatives of Kato’s Euler system and the Mazur–Tate conjecture* (2025): https://doi.org/10.1093/imrn/rnaf012
- Poonen–Stoll, *The Cassels–Tate pairing on polarized abelian varieties*: https://math.mit.edu/~poonen/papers/sha.pdf
- Source-conditional finite-range theorem and p16231 application: [389a1 Stein–Wuthrich corollary](389a1_stein_wuthrich_2012_exception_16231_conditional_closure_2026-10-26.md)
- [Original abstract uniform Fitting implication and toy counterexample](389a1_uniform_sha_support_fitting_criterion_supersingular_obstruction_2026-10-26.md)

**Status:** theorem of algebraic equivalence **PROVED**; existence of D_E **OPEN** for 389a1; global Sha finiteness and BSD **NOT PROVED**.
