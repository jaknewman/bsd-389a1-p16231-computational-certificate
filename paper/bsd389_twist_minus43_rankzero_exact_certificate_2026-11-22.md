# 389a1: rigorous central-value interval for the quadratic twist by −43; rank-two anticyclotomic base

**Date:** 22 November 2026. **Status:** independent exact-rational certificate actually executed in the assistant's container. **New arithmetic result**: the quadratic twist by fundamental discriminant `−43` has analytic and algebraic rank zero, so the base change to `K=Q(sqrt(−43))` has Mordell–Weil rank exactly two. This does not prove any missing part of the strong BSD conjecture for `389a1` over Q.

## 1. Curve, discriminant and root sign

Let `E: y^2+y=x^3+x^2−2x`, with `N_E=389`. The original curve has split multiplicative reduction at 389 (a_389=+1) and hence global sign +1 (the only finite bad place is 389). Let `D=−43`, a negative fundamental discriminant prime to 389, and `χ_D` its primitive quadratic character. The conductor of the twisted newform is

    N_D = N_E * D^2 = 389*43^2 = 719261.

By quadratic reciprocity `χ_D(n)=(n/43)` for `gcd(n,43)=1`, with zero for `43|n`. We have `χ_D(389)=−1`, `χ_D(−1)=−1`, so `χ_D(−389)=+1`. The standard coprime quadratic-twist root-number formula gives

    w(E^D)=w(E)*χ_D(−389)=+1.

This also verifies the relevant splitting data for the classical anticyclotomic setup:

    χ_D(11)=+1,   χ_D(389)=−1.

A direct exact finite-field point count gives `a_11(E)=−4`, so p=11 is ordinary and satisfies the nonanomalous condition `a_11≠1 (mod 11)`. Moreover `a_2(E)=−2`; the mod-11 Frobenius discriminant at 2 is `a_2²−8=−4≡7 mod11`, a nonsquare, proving residual irreducibility. Inertia at the split-multiplicative place 389 contains a nontrivial 11-transvection because `v_389(Δ_min)=1`. By the standard 2-dimensional subgroup classification (p≥5), the image contains SL2, and cyclotomic determinant surjectivity gives GL2(F_11). Thus all visible (Im),(Ram),(Spl),(Na),(Def) hypotheses of **Chan-Ho Kim, Canad. Math. Bull. 69 (2026), Theorem 1.1** hold for `(E,p,K)=(389a1,11,Q(sqrt(−43)))`.

## 2. Exact approximate functional equation, with only one exponentially weighted series

Let `a_n` be the integer coefficients of the normalized weight-two newform of E. The quadratic-twist L-series has coefficients `a_nχ_D(n)`. Since its root number is **+1**, the Mellin-transform functional equation at the center gives the **exact convergent identity**

    L(E^D,1) = 2 * SUM_(n>=1) [ a_n χ_D(n)/n ] * exp(−c*n),
    c = 2π/sqrt(719261).

This identity is not a truncated approximate formula: it is exact, with the tail bounded separately below.

For each prime `q` up to M=1500, the program counts points on the original long Weierstrass model over F_q with exact integer arithmetic, obtaining `a_q=q+1−#E(F_q)`. It forms every `a_n` for `n<=1500` from Hecke multiplicativity and

    a_(q^j) = a_q*a_(q^(j−1)) − q*a_(q^(j−2))

at good primes, with the multiplicative-local Euler factor at q=389. It evaluates `χ_D(n)` with the elementary Euler criterion mod 43. There are no Sage/GP calls, external data files or floating-point operations in any mathematical comparison.

## 3. Fully rational exponential bounds

The elementary rigorous constants

    3.14159 < π < 3.14160,
    848²=719104 < 719261 < 720801=849²

yield rational bounds `c_lo < c < c_hi`, with

    c_lo = 2*(314159/100000)/849 = 314159/42450000,
    c_hi = 2*(314160/100000)/848 = 3927/530000.

For `1<=n<=M=1500`, `0<c_hi*n/16<1`. The alternating Taylor expansion gives, for `0<=y<=1`,

    P3(y) := 1−y+y²/2−y³/6 <= exp(−y)
           <= P4(y) := P3(y)+y⁴/24.

Thus the fully rational inequalities

    [P3(c_hi*n/16)]^16 <= exp(−c*n)
         <= [P4(c_lo*n/16)]^16

hold for all n in the finite sum. Multiply by the signed exact rational coefficient `2a_nχ_D(n)/n`, reversing the interval for negative coefficients, and sum all 1500 lower/upper endpoints using `fractions.Fraction`.

The exact-rational sums (decimal approximations printed only for readability) are

    10.8088920895... < S_1500 < 10.8398718608... .

No numerical rounding is used to justify the inequalities.

For the tail, Deligne's bound plus the divisor bound gives `|a_n|<=d(n)*sqrt(n)<=2n`, so

    |L(E^D,1)−S_M| <= 4*exp(−c*(M+1))/(1−exp(−c)).

Using `exp(z)>=1+z`, we obtain the **completely rational** upper bound

    4 * (1+c_lo)/c_lo * (1+c_lo*(M+1)/16)^(−16)
       < 0.118098   [M=1500].

Consequently the fully rational endpoint calculations prove

    10.6907943829... < L(E^D,1) < 10.9579695673...,

and in particular the exact rational comparisons in the program certify

    **10 < L(E^(-43),1) < 11.**

The program prints `TWIST_MINUS43_L_INTERVAL_10_TO_11_RATIONAL_CERTIFICATE_PASS` and exits successfully. Every internal comparison supporting the conclusion uses integers and rational numbers; displayed decimals are not the basis of the proof.

## 4. Arithmetic consequences and strict limitation

The analytically nonzero central value implies analytic rank zero for the twist. By the established analytic-rank-zero theorem (modularity plus Kolyvagin and related results),

    rank E^(−43)(Q) = 0,    Sha(E^(−43)/Q) finite.

The standard rank decomposition for quadratic base change gives

    rank E(Q(sqrt(−43)))
       = rank E(Q) + rank E^(−43)(Q)
       = 2 + 0 = **2**.

This is a genuine rank-two base field for Kim's 2026 anticyclotomic Fitting theorem at p=11, with no unwanted additional Mordell–Weil rank from the quadratic twist. Because the theorem determines only **Fitt_0** over finite layers, the rank-two **Fitt_2** at augmentation still needs integral Bockstein/Stark-system comparison. The separate paper `bsd389_2026_fitting_augmentation_bockstein_obstruction.md` gives an exact counterexample showing that no purely formal inference from initial Fitting and a theta quadratic unit can supply this missing information.

**NOT CLAIMED:** triviality or finiteness of Sha(E/Q); the exact complex equality `L''(E,1)/2=Ω_E Reg(E)#Sha`; an actual Gross theta coefficient at the new field K; p-uniform arithmetic across all primes. All of those require additional theorems.

## Verifier and sources

- `verification/bsd389_twist_minus43_Lvalue_exact_rational_certificate.py` (standard library only; M=1500; run status PASS in assistant container on 2026-11-22).
- Chan-Ho Kim, *On the Fitting ideals of anticyclotomic Selmer groups of elliptic curves with good ordinary reduction*, Theorem 1.1, https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/on-the-fitting-ideals-of-anticyclotomic-selmer-groups-of-elliptic-curves-with-good-ordinary-reduction/D7D2EA9FA52A23B92319F3D44F5E9884 .
- Daniel Macias Castillo and Takamichi Sano, *On Selmer complexes, Stark systems and derived p-adic heights* (2026), Theorems 1.5 and 1.8, https://arxiv.org/abs/2603.23978 .