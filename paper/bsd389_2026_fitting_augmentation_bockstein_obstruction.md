# 389a1 — strong anticyclotomic Fitting theorem versus integral rank-two specialization

**Date:** 2026-11-22. **Status:** exact new algebraic counterexample, plus a checked admissible arithmetic specialization. Does **not** prove the BSD conjecture or identify an actual Selmer module of 389a1 with the example below.

## 1. Relevant published theorems and an eligible arithmetic setup

Chan-Ho Kim, *On the Fitting ideals of anticyclotomic Selmer groups of elliptic curves with good ordinary reduction*, Canadian Mathematical Bulletin **69** (2026), Theorem 1.1, proves under (Im), (Ram), (Spl), (Na), (Def) that for each anticyclotomic layer `K_n/K`,

    Fitt_0,Lambda_n( Sel(K_n, E[p^infinity])^vee )
       = (theta_n, nu_(n-1,n)(theta_(n-1)))^2.

Here `Lambda_n = Z_p[Gal(K_n/K)]`, and `theta_n` denotes the **Bertolini–Darmon** theta element with the paper's normalization. This is an initial (= zeroth) Fitting ideal, not the rank-two Fitt_2 at the augmentation. The recently posted Kim–Pal–Ray preprint, *Refined conjectures on Fitting ideals of BDP Selmer groups*, arXiv:2609.17003, is related but treats **BDP Selmer groups**, whose local conditions and theta elements are not interchangeable without a comparison theorem.

For E: `y^2+y=x^3+x^2-2x`, conductor 389, an explicit prime/field choice satisfying the clearly visible local conditions of Kim's 2026 theorem is `p=11`, `K=Q(sqrt(-43))`:

- `-43` is a negative odd fundamental discriminant with `43>4`, coprime to `11*389`;
- `(-43/11)=+1` and `(-43/389)=-1`, so 11 splits and `N^-=389` is one inert squarefree prime;
- point counts give `a_11(E)=-4`, so 11 is ordinary and `a_11 != 1 mod 11` (nonanomalous);
- `a_2(E)=-2`, and the mod-11 characteristic polynomial `X^2+2X+2` has discriminant `(-2)^2-8=-4≡7 mod11`, a nonsquare. Thus `E[11]` is irreducible. Multiplicative inertia at 389 (minimal discriminant exponent 1) contains a nontrivial 11-transvection; by Dickson's subgroup classification (or the standard irreducible transvection lemma for 2-dimensional representations in odd characteristic), the image contains `SL_2(F_11)`. Since the cyclotomic determinant surjects onto `F_11^*`, the image is all `GL_2(F_11)`. The mod-11 inertia at 389 is ramified, as required.

This does **not** assert an actual theta coefficient for K=-43, nor that the stronger BDP theorem applies to the same Selmer structure. It identifies a concrete setting for testing the proven classical anticyclotomic theorem.

## 2. Exact counterexample: theta and all initial Fitting ideals do not determine the specialized rank-two defect

Fix any odd prime `p` and any integer `e>=0`. Let `Lambda=Z_p[[T]]`. Define the 2x2 block

    B_e(T) = [ p^e   T ]
             [ T     0 ]

and the 4x4 matrix `A_e(T)=diag(B_e(T),B_e(T))`. Let `M_e=coker_Lambda(A_e)`.

**Theorem.** For *every* e, all the following hold:

1. `det A_e(T)=T^4`, so `Fitt_0,Lambda(M_e)=(T^4)=(theta(T)^2)` with the **same theta `theta=T^2`**, whose quadratic coefficient is the unit 1.
2. For each n>=0, put `omega_n=(1+T)^(p^n)-1`, `Lambda_n=Lambda/(omega_n)`, `M_(e,n)=M_e/omega_n M_e`, `theta_n=T^2 mod omega_n`. Base change of Fitting ideals gives `Fitt_0,Lambda_n(M_(e,n))=(theta_n^2)` **at every finite layer**. The theta are compatibly projected from the same series.
   Moreover, the published **two-generator** ideal also matches exactly: if `N_n=sum_(j=0)^(p-1) gamma^(j*p^(n-1))` is the transfer norm, then `nu_(n-1,n)(theta_(n-1)) = theta_n*N_n`. Therefore `(theta_n,nu(theta_(n-1)))=(theta_n)` and its square equals `(T^4)` in every `Lambda_n`.
3. At the augmentation `T=0`,

       M_e/T M_e  ≅  Z_p^2 ⊕ (Z_p/p^e Z_p)^2.

   Hence `Fitt_2,Z_p(M_e/TM_e)=(p^(2e))`, an *arbitrarily large* rank-two torsion defect. For `e=0`, the torsion summands vanish. For e>=1, the torsion order is `p^(2e)`, a square; an abstract perfect alternating pairing is available on the two identical cyclic factors.
4. `M_e` is `Z_p`-torsion-free. As an additive `Z_p`-module it is free of rank 4, and T acts nilpotently by

       T u_j = 0,       T v_j = -p^e u_j,       j=1,2.

   Thus the counterexample cannot be dismissed as introducing artificial p-power torsion into the *Iwasawa* module or a positive `mu`-invariant. (It is **not** asserted to satisfy the other special global arithmetic properties of a Selmer group.)

**Proof:** Each 2x2 block has determinant `-T^2`, so the 4x4 determinant is `T^4`. Fitting ideals commute with change of rings, giving statement 2. At `T=0`, `A_e(0)=diag(p^e,0,p^e,0)`, so its cokernel decomposes as in 3. Presentation by the generators `u_j,v_j` and relations `p^e u_j+Tv_j=0`, `Tu_j=0` gives the described `Z_p`-free model and proves 4. QED.

This shows that **even a unit quadratic theta coefficient and an exact zero-th Fitting identity at every finite layer do not, by themselves, control the second Fitting ideal at the augmentation**. No conclusion about `Sha` may be drawn solely from these two formal facts; an independent derived/specialization comparison is essential.

## 3. The missing integral datum is visible explicitly: an augmentation Bockstein

Let `N_e` be multiplication by `T` on the `Z_p`-free module `M_e`. We have

    ker(N_e) = Z_p u_1 + Z_p u_2,
    M_e / ker(N_e) = Z_p v_1 + Z_p v_2.

The induced injective integral map

    beta_e: M_e/ker(N_e) -> ker(N_e),     [m] |-> T m

has matrix `diag(-p^e,-p^e)` in these natural bases, and therefore

    det beta_e = p^(2e),
    coker beta_e = (Z_p/p^e)^2.

This determinant *does* detect the defect that `theta=T^2` and `Fitt_0=(T^4)` miss. Consequently, a viable application of the 2026 Fitting theorem to 389a1 must also furnish an integral augmentation control/Bockstein comparison (with the relevant actual Selmer complex and its local conditions), not only a leading theta coefficient. Such a comparison must be **proved**, not assumed as a consequence of the zeroth Fitting identity.

## 4. Correct finite-support proof target

The existing Kummer identity for the rank-two curve over Q is

    Fitt_2,Z_p( Sel(Q,E[p^infinity])^vee )
         = Fitt_0,Z_p( Sha(E/Q)[p^infinity]^vee ).

To prove `Sha[p^infinity]=0` for large p using a theta/Fitting argument, one would need a genuine integral specialization comparison identifying or bounding this **second** Fitting ideal, plus the descent from the chosen K to Q. The toy example proves this extra step is logically independent of the available initial Fitting identity. A fixed, nonzero rational global determinant satisfying this comparison outside finitely many primes would yield finite prime support, but **no such determinant is constructed here**.

## References

- Chan-Ho Kim, *On the Fitting ideals of anticyclotomic Selmer groups of elliptic curves with good ordinary reduction*, Canad. Math. Bull. 69 (2026), pp. 21–31, Theorem 1.1: https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/on-the-fitting-ideals-of-anticyclotomic-selmer-groups-of-elliptic-curves-with-good-ordinary-reduction/D7D2EA9FA52A23B92319F3D44F5E9884 .
- Chan-Ho Kim, Aprameyo Pal, Jishnu Ray, *Refined conjectures on Fitting ideals of BDP Selmer groups*, arXiv:2609.17003 (2026-09-15): https://arxiv.org/abs/2609.17003 .
- Kummer split rank-two Fitting identity, existing project note `paper/bsd389_unconditional_rank2_kummer_fitt2_identity_2026-10-30.md`.

## 5. Source-level derived comparison to investigate next

Takamichi Sano, *Derived Bockstein regulators and anticyclotomic p-adic Birch and Swinnerton-Dyer conjectures* (arXiv:2308.08875), establishes a descent formalism with derived Bockstein regulators and **up-to-p-adic-unit** implications from anticyclotomic main conjectures. Daniel Macias Castillo and Takamichi Sano, *On Selmer complexes, Stark systems and derived p-adic heights* (arXiv:2603.23978, March 2026), prove canonical identifications between suitable Selmer and Poitou–Tate complexes, between determinant lines and Stark-system modules, and between Bertolini–Darmon and Nekovář derived-height pairings. These are real comparison results. **Important hypothesis distinction:** Macias Castillo–Sano's Heegner-point Stark-system *application* in §1.3.2 assumes the Heegner splitting hypothesis (every prime dividing N splits in K); it cannot be applied verbatim to K=Q(sqrt(−43)), where 389 is inert. Its *general* determinant/Stark formalism is the relevant candidate, subject to a separate Selmer structure and verified hypotheses. **Neither citation, by itself, supplies** a canonically normalized rank-two, p-uniform integral Bockstein determinant over `Q` for `389a1`, nor the exact complex leading term.

**Specific next source check:** find in those comparison theorems an element-level, p-integral morphism from the actual theta/Gross or Kato system to the derived Selmer Bockstein lattice with all local Euler/Tamagawa factors and p-adic orientations included. A theorem proving that map carries a primitive generator would control the augmentation `Fitt_2`; a statement about `Fitt_0` alone cannot do so by §2. The `K`-to-`Q` descent and all-prime uniform integrality remain separate obligations.

References: https://arxiv.org/abs/2308.08875 and https://arxiv.org/abs/2603.23978 .