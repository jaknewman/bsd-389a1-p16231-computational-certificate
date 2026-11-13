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
