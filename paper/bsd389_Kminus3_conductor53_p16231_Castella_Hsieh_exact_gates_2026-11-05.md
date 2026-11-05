# E389a1 at p=16231: exact K=-3, conductor-53 class character and analytic twist nonvanishing

**Date:** 2026-11-05. Two new, independently reproducible arithmetic gates for the non-CM rank-two Castella–Hsieh framework. **NO** claim of Sha[p∞] finiteness at p16231, global finiteness, or BSD.

## 1. Configuration

E : y²+y=x³+x²−2x, N=389, Delta_min=389, MW rank 2. Let
K=Q(sqrt(-3)), O_K=Z[ω], ω²+ω+1=0, ring class conductor f=53, and p=16231.

389≡2 (mod 3), hence 389 is inert in K; 16231≡1 (mod 3), hence p splits in K. E has a_p=128 at 16231, confirmed by an independent point count over F_p (i.e. #E(F_p)=16104), and is good ordinary at p. The residual p-adic representation is surjective by the project's separate previously certified semistable GL2 proof; the ring-class script itself does not re-prove that. Since the discriminant at 389 has valuation 1, the residual representation is ramified at the inert conductor prime 389 for p>=5.

## 2. Complete elementary class-group computation

Since 53≡2 (mod 3), it is inert in K, so O_K/53 ≅ F_(53²). Since K has class number one and [O_K×:O_f×]=3, the ring class group is

C_f ≅ F_(53²)× / (F_53× μ_6),

of cardinality (53²−1)/(52·3)=18. This quotient is cyclic.

Let g=5+3ω, with Norm(g)=25−15+9=19. Working modulo 53 in the basis (1,ω), and using ω²=−ω−1:

- g^6 ≡ 33+48ω;
- g^9 ≡ 4+49ω;
- g^18 ≡ 5ω.

The element g^18 belongs to F_53× μ_6, but g^6 and g^9 do not. Therefore its class has **exact order 18** and generates C_f.

The split prime p=16231 has a generator

π=145+51ω,   Norm(π)=145²−145·51+51²=16231.

A direct finite-field calculation gives

g^4 ≡ 27+19ω (mod 53),
25g^4 ≡ 39+51ω ≡ π (mod 53).

Thus, up to the harmless inversion convention between residue elements and ideal classes, the prime above p has class [g]^(±4), of exact order 18/gcd(18,4)=9.

Take a primitive ring-class character ψ of order 18. Complex conjugation acts by inversion on C_f, so χ=ψ/ψ^τ=ψ² has order 9. Therefore

χ(pbar) = ζ_18^(±8),

an element of exact order 9, **not 1**. This explicitly verifies the condition χ(pbar)≠1 required in Castella–Hsieh's Theorem A. The result applies to a primitive character ψ as specified; it does not assert every possible lower-order character works.

Pure-standard-library verification:
[verification/bsd389_Kminus3_conductor53_p16231_ringclass_gate.py](../verification/bsd389_Kminus3_conductor53_p16231_ringclass_gate.py).

## 3. New rigorous bound for L(E^(-3),1)

The quadratic twist by the fundamental discriminant D=-3 has conductor N_D=389·3²=3501. Because E has split multiplicative reduction at 389 (a389=1), its global sign is +1, and χ_D(-389)=+1, so the twist also has sign +1.

By the modular functional equation, with α=2π/sqrt(3501) and the original Fourier coefficients a_n of E,

L(E^(-3),1) = 2Σ_(n≥1) a_n χ_(-3)(n) exp(-αn)/n.

This is an **identity**, not a BSD approximation. The coefficients a_n for n≤64 are computed exactly by counting E(F_q) for each prime q≤64 and using Hecke recurrences. Archimedes' 223/71 < π < 22/7 and the rational inequalities (59169/1000)² < 3501 < (59170/1000)² give rigorous rational bounds α_-<α<α_+. For 0<x<1, the alternating Taylor polynomials satisfy T9(x)≤exp(-x)≤T8(x); apply them to x=αn/16 and raise the resulting bounds to the 16th power for every n≤64.

Deligne's |a_n|≤d(n)√n≤2n gives the tail bound

|2 Σ_(n>64) a_nχ_(-3)(n) exp(-αn)/n|
≤ 4 exp(-65α)/(1−exp(-α)).

This too is bounded **from above by an explicit rational number**, using T8 at α_-. On the local assistant execution, all inequalities were checked with Python's exact Fraction arithmetic, yielding:

- 64-term sum lower bound ≈ 4.552573780109;
- upper bound ≈ 4.555645450723;
- absolute tail < 0.039997400578.

The exact *rational* comparisons, not the printed floating-point approximations, prove

**4.51 < L(E^(-3),1) < 4.60**, hence in particular **L(E^K,1)≠0** in Castella–Hsieh's notation for the quadratic twist E^K. This analytic result is independent of the unknown Sha and BSD leading-term equality. The L-value computation was **executed inside the assistant's Python environment**, not on the user's Ubuntu yet.

Source: [verification/bsd389_Kminus3_twist_Lvalue_rational_interval.py](../verification/bsd389_Kminus3_twist_Lvalue_rational_interval.py).

## 4. Theorem application — what actually remains

Castella–Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum of Mathematics, Sigma 10 (2022), Theorems A, B:

https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864

Theorem A requires L(E,ad^0(g),1)=L(E^K,1)·L(E/K,χ,1) ≠0 and the indicated residual/ramification/split-ordinary hypotheses. The present certificate **verifies the first factor exactly** and χ(pbar)≠1, as well as the local N^− and p hypotheses.

**Still unproved by this note**:
1. Nonvanishing of the *other* central factor L(E/K,χ,1) for the chosen order-nine anticyclotomic χ. This should be attacked by an exact finite quaternionic toric period at N^−=389, potentially reusing prior 33 right ideal classes and the conductor-53 optimal embeddings.
2. The anticyclotomic theta element Θ_(f/K) having exact order of vanishing 2. This is the hypothesis in Theorem B that would imply the nonzero generalized Kato class.
3. Even a verified κ_p≠0 only forces dim_(Q_p) Sel(Q,V_pE)=2 (corank 2), hence *finiteness* of Sha[p∞]; it does not force its p-primary finite quotient to be zero. A p-integral unit/Kurihara or independent upper bound is still needed for triviality.
4. No all-large-p theorem follows from this individual p16231 computation.

**Bottom line:** the concrete CM auxiliary field and ring-character gate, and the analytic twist factor, are now checked. The two remaining analytic/theta gates are much narrower than a vague uniform regulator conjecture, but are genuinely open in this local project.
