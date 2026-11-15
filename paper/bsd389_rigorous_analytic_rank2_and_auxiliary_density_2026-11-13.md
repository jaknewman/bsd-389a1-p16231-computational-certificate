# E389a1: rational analytic-rank-two certificate and quantitative Chebotarev

**2026-11-13. Mathematical scope:** rigorous independent pure-Python interval certificate and exact finite-group counting; neither global finiteness of Sha nor strong BSD follows.

## 1. The exact special-value integral

For E: y²+y=x³+x²−2x the conductor is N=389, the minimal discriminant is **+389** (not −389), and the global root sign is +1: exact reduction at 389 is split multiplicative with a_389=1. The project's certified Mordell–Weil rank is 2. The classical rank-zero theorem implies L(E,1)=0; the +1 functional equation then implies L'(E,1)=0.

Let f(z)=Σ_{n≥1} a_n exp(2πinz) be its newform, and c=2π/√389. Mellin inversion with the functional equation gives

$$
\Lambda(E,s)=\int_1^\infty f(it/\sqrt{389})(t^{s-1}+t^{1-s})\,dt.
$$

Since Λ(E,s)=389^{s/2}(2π)^{-s}Γ(s)L(E,s) and L(E,1)=L'(E,1)=0, differentiating twice gives

$$
\boxed{\frac{L''(E,1)}2=c\int_1^\infty
\left(\sum_{n\ge1}a_n e^{-cnt}\right)(\log t)^2\,dt.}
\tag{1}
$$

## 2. Fully rational, independently executed enclosure

The standalone [pure-Python certificate](../verification/bsd389_analytic_rank2_rational_interval_certificate.py) uses only exact integer/Fraction arithmetic for its inequalities:

- Exact Legendre point counts and Hecke recurrences for a_1,...,a_100;
- rational alternating Machin/arctan bounds for π and integer-square bounds for √389;
- alternating Taylor exp/log bounds and directed-rounding fixed-point interval arithmetic with scale 10^25;
- 59,000 signed monotone rectangular integration intervals on 1≤t≤60, with positive/negative Fourier coefficients enclosed separately;
- the Deligne/Hasse bound |a_n|≤d(n)√n≤2n, c>3/10, exp(−c)<3/4, and log t≤t−1 to bound the omitted n>100 tail by less than 1.398×10^−14;
- the same bound and log t≤t to bound the t>60 tail by less than 0.000856.

The output is the **outward-rounded exact enclosure**

$$
\boxed{0.7579486102< L''(E,1)/2 <0.7606840600.}
\tag{2}
$$

Its strict positivity proves analytically

$$
\boxed{\operatorname{ord}_{s=1} L(E,s)=2.}
\tag{3}
$$

The source was genuinely executed in the assistant's container on November 13, 2026, with exit code 0 and status BSD389_L_DOUBLE_PRIME_POSITIVE_CERTIFIED_PASS. Its pre-commit local SHA-256 was 1889b7f6e14e4f56d2009788b57e0d48bf0c34d8b27e47609c36aa0302c1b8ab. The high-precision reference from [LMFDB](https://www.lmfdb.org/EllipticCurve/Q/389a1/), 0.759316500288..., lies within the interval but is **not an input** to the proof.

## 3. Chebotarev frequency of genuine one-dimensional auxiliary conditions

Fix p≥5 such that the residual Galois image is GL₂(F_p). Good auxiliary q satisfying q≡1 and a_q≡2 mod p have mod-p Frobenius with characteristic polynomial (X−1)^2. Exactly one such matrix is scalar identity, while p²−1 are nontrivial unipotent. Since

$$
|\mathrm{GL}_2(\mathbf F_p)|=p(p-1)^2(p+1),
$$

Chebotarev gives absolute prime densities

$$
\delta_{\rm adm}=\frac{p}{(p-1)^2(p+1)},\quad
\boxed{\delta_{\rm unip,1D}=\frac{1}{p(p-1)}},\quad
\delta_{\rm scalar,2D}=\frac{1}{|\mathrm{GL}_2(\mathbf F_p)|}.
$$

Therefore among p-admissible primes the exact proportion with one-dimensional local Kummer condition is

$$
\boxed{1-\frac1{p^2}.}\tag{4}
$$

Assume also that the two rational MW generators have full Kummer translation image E[p]^2 over Q(E[p]), as in the project's earlier Galois/Kummer theorem. Conditional on nontrivial unipotent Frobenius, Kummer localization rows for P,Q are uniformly distributed in F_p², by the full translation fibres. Two independent auxiliary primes then give an invertible 2×2 MW localization matrix with conditional density

$$
\boxed{(1-p^{-1})(1-p^{-2}).}\tag{5}
$$

The asymptotic density among **ordered pairs** of distinct rational primes is therefore

$$
\boxed{\frac{(1-p^{-1})(1-p^{-2})}{p^2(p-1)^2}.}\tag{6}
$$

Here the pair-density assertion follows by applying Chebotarev to each prime and taking the product-density limit as q1,q2≤X tend to infinity; no effective least-prime bound is asserted. It counts *MW-local detection*, not Kurihara units. The companion verifier exhaustively counts GL2 matrices and row determinants for p5,7 and gives exact rational values also at p107 and p16231.

## 3 bis. New proof: the rank-two Kummer translation hypothesis is AUTOMATIC, independent of Sha

**Updated 2026-11-15.** This closes an actual hypothesis left conditional in §3 above and thus upgrades the genuine MW-localization pair-density result to an **unconditional theorem for every p≥5 with full residual GL₂**. It does **NOT** close Sha[p], force a nonzero Kurihara coefficient or prove BSD.

Let V=E[p] be the natural irreducible two-dimensional Fp-representation, F=Q(E[p]), Γ=Gal(F/Q)=GL₂(Fp), and let
P=(-1,1), Q=(0,-1)
be the **proved saturated integral MW basis**. The Kummer map gives an injection

  E(Q)/pE(Q)=Fp·P ⊕ Fp·Q ↪ H¹(G_Q,V).

Because the central −I∈Γ acts as −1 on V and p is odd, Sah's lemma yields H¹(Γ,V)=0. Inflation–restriction therefore injects H¹(G_Q,V) into Hom_cont(G_F,V)^Γ. Denote the images of the two Kummer classes by h_P,h_Q. They are Fp-linearly INDEPENDENT by injectivity. Their combined image

  H = im((h_P,h_Q): G_F→V⊕V)

is a Γ-stable subspace of V². Each coordinate projection of H is nonzero and hence onto V, by the irreducibility of V. If H were proper, Goursat's lemma for Γ-modules would give an isomorphism of the two simple Γ-quotients and hence, by Schur's lemma End_Γ(V)=Fp, force H to be the graph of a scalar endomorphism: h_Q=λh_P. This contradicts their linear independence. Thus

  **H=V²**,

and the genuine finite Galois field
  M_p=F([p]^{-1}P,[p]^{-1}Q)
satisfies

  **Gal(M_p/F)=E[p]⊕E[p]  and [M_p:F]=p^4.**

No Sha finiteness, analytic L-value hypothesis or p-adic height primitivity is used. In particular, this proof holds for anomalous primes as well when residual GL₂ is surjective.

For every nonidentity unipotent g in Γ, (g−1)V is a one-dimensional subspace, so the local quotient V/(g−1)V has dimension1. Given any g-lift to Gal(M_p/Q), translation by the whole kernel V² realizes EVERY pair of quotient values

  (h_P(Frob_q),h_Q(Frob_q)) mod (g−1)V ∈ Fp²,

each with exactly p² preimages. These quotient pairs are independent of the choice of local conjugation up to a common nonzero scalar. Chebotarev's theorem applied to the union of corresponding conjugacy classes gives a positive density of primes with ANY chosen projective local MW direction. There are p²−1 nonidentity unipotents in Γ, and |Γ|=p(p−1)²(p+1), so the density of genuine 1D local conditions is exactly

  **δ_1D=(p²−1)/|Γ| = 1/[p(p−1)].**

Conditional on this event the ordered pair of MW local values is UNIFORM on Fp², without an extra Kummer-image assumption. Choosing two independent rational primes therefore yields independent MW local lines with exact conditional proportion

  **(1−1/p²)(1−1/p)**,

and their pair density is exactly the formula (6) in §3. Thus §3's previous 'Assume also that ... full Kummer translation image' can be deleted **for every p≥5 with residual GL₂**.

**Sharp separation of the remaining obstruction.** This theorem proves the abundance of *well-typed auxiliary prime pairs with invertible Mordell–Weil localization matrices*. It does **NOT** prove their rank-two Kurihara derivative is a p-unit. That derivative is a genuinely independent global Euler-system/Selmer invariant; replacing it by the MW localization determinant without proving the relevant Kato–Kurihara integral reciprocity and torsion control would be circular. In general a curve can have rank2 and nonzero Sha[p], yet its two MW points still have the full V² Kummer image over its division field. Hence positive density of MW-detecting auxiliary pairs **cannot** by itself give Sha[p]=0.

This unconditional theorem removes a genuine *global Galois extension hypothesis* from the existing route to the desired all-p Kurihara witnesses. It is not the desired uniform nonvanishing theorem.

## 4. Correction of the published Kurihara coefficient modulus

Castella–Sano, [§1.1.1](https://web.math.ucsb.edu/~castella/Kurihara.pdf), explicitly define

$$
I_q=(q-1,a_q-q-1)\mathbf Z_p,\quad
\boxed{I_n=\sum_{q\mid n}I_q},
$$

not a product. Thus for both old p7 examples I_{113·281}=I_{113·673}=7 Z_7, **not** 49 Z_7. The older draft PR #19 has been corrected directly (commit 2c841edfd42c8627e0182a2ae46839a6471137f8). Do not replace the finite-level Kato–Kurihara reciprocity modulus by the separate oldform mixed-eigenvalue divisibility.

## 5. Boundary

The exact analytic rank equals the certified algebraic rank 2, but **the exact leading-coefficient BSD identity is still missing**, as is the all-large-p two-prime Kurihara nonvanishing or independently proved global Selmer Fitt₂ control. The quantitative Chebotarev result guarantees plenty of correctly typed auxiliary primes; it cannot force global derived Euler/Kolyvagin coefficients to be nonzero.

**Verdict:** new independent exact analytic certificate and quantitative local-density theorem; BSD remains unproved.
