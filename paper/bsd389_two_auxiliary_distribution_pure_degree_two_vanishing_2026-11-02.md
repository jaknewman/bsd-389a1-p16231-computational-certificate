# E389a1 — Distribution forces the two-prime Mazur–Tate leading term to be purely mixed

**Date:** 2026-11-02. **Scope:** an exact algebraic lemma for properly normalized, p-integral Mazur–Tate elements, not a global Kurihara nonvanishing theorem.

## Setup and norm relation

Fix p>=5, E=389a1 (the general algebra works for any weight-two newform with the stated normalization) and distinct good auxiliary primes q1,q2, each satisfying
`q_i ≡ 1 (mod p)` and `a_(q_i)(E) ≡ q_i+1 ≡ 2 (mod p)`.

Let `Theta_m` denote a *compatible* family of Mazur–Tate group-ring elements formed from the same p-integral plus modular-symbol normalization. For `ell ∤ mN`, the standard Hecke distribution relation in the full cyclotomic group rings is

`pi_(m ell,m)(Theta_(m ell)) = (a_ell - sigma_ell - sigma_ell^(-1)) Theta_m`.

The Artin convention may replace sigma by its inverse (the displayed symmetric factor is unaffected). For m=1, the same distribution implies `epsilon(Theta_q)=(a_q-2) Theta_1`. Hence p-admissibility gives `epsilon(Theta_(q_i)) ≡ 0 (mod p)`. Sources: standard Mazur–Tate norm relations in Mazur–Tate, and e.g. Lemma 2.23(2) in <https://escholarship.mcgill.ca/downloads/6w924d346.pdf>.

## Exact lemma

Fix p-primary quotient coordinates of the two auxiliary cyclic factors and group-ring algebra map

`Phi_p: F_p[G_(q1q2)] -> F_p[X,Y]/(X^p,Y^p)`

with `sigma_a -> (1+X)^(e1(a))(1+Y)^(e2(a))`, where each e_i is the chosen mod-p discrete logarithm.

Write `F(X,Y)=Phi_p(Theta_(q1q2))` and `J=(X,Y)`. Then

**`F(X,Y) ≡ delta_(q1 q2) X Y (mod J^3)`.**

In particular, **all** coefficients of total degree 0 or 1, as well as the pure degree-two coefficients X² and Y², vanish; the *only* possible degree-two term is the Kurihara mixed coefficient.

### Proof

Consider the projection to q1, equivalently `F(X,0)`. The distribution factor at q2 maps, in the p-quotient of q1, to

`a_(q2) - (1+X)^t - (1+X)^(-t) ≡ 2-(1+X)^t-(1+X)^(-t) ≡ -t² X² (mod X³)`,

where `t=e1(q2)` modulo p. This factor lies in `(X²)`. On the other hand the q1 Mazur–Tate element has augmentation `(a_(q1)-2)Theta_1 ≡0 mod p`, hence its image in the q1 p-group algebra lies in `(X)`. Their product `F(X,0)` therefore lies in `(X³)`.

The same argument with indices reversed gives `F(0,Y) ∈ (Y³)`. These two projection statements kill the constant, linear and pure quadratic coefficients of F. The remaining degree-two monomial is XY, whose coefficient is by definition

`[XY] F = Σ_(a mod n)^× [a/n]^+ e1(a)e2(a) = delta_(q1q2) mod p`.

Thus `F ≡ delta XY (mod J³)`. QED.

The proof does **not** use the Mordell–Weil rank two, the finiteness of Sha, or any global nonvanishing statement. The rank two is used elsewhere to connect a unit delta to the desired Selmer/Sha conclusions via Kim.

### Three-projection consequence

Define `Q11=[T²]F(T,T)`, `Q10=[T²]F(T,0)`, `Q01=[T²]F(0,T)`. The lemma gives

`Q10=0, Q01=0, Q11=delta_(q1 q2)`.

This strengthens the earlier formal polarization identity `delta=Q11-Q10-Q01`, under the *actual* Hecke norm-compatibility and p-admissibility hypotheses.

For the archived p107 data (q1=369793, q2=383917), the reconstructed delta=34 predicts `Q10=Q01=0` and `Q11=34 mod107` **provided that the archived original modular-symbol table really implements this compatible normalization**. These are **predictions, not independently executed cyclic projection computations**.

### Sanity check

For p=5,7,107 and every t∈F_p, the polynomial congruence
`2-(1+X)^t-(1+X)^(-t) = -t² X²+O(X³)`
was directly checked with exact integer arithmetic for 5+7+107 total t-values. The proof itself is exact for all odd p.

## Why this does NOT settle the global primitive coefficient

The relation `F ≡ delta XY` allows **delta=0**. Distribution identities constrain the allowed *shape* of the degree-two class, not its nonvanishing. It remains necessary to establish, for all sufficiently large p, a genuine unit mixed coefficient for some p-admissible pair, or an independent Selmer/Fitting bound. A formal example `F=0` obeys all these lower-degree constraints and shows no unit follows merely from the constraints.

Important distinction: the norm relation must be applied to a truly compatible Mazur–Tate element, not to an arbitrary user-defined table of residues; the normalizations and Hecke distribution are substantive prerequisites.
