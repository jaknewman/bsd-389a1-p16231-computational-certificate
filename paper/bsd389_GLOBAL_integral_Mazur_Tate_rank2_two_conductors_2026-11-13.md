# BSD 389a1 — Two independently audited p-independent integral Mazur–Tate group-ring elements

**2026-11-13: Genuine exact arithmetic construction at TWO finite abelian conductors; NOT a proof of global Sha finiteness or complex BSD.**

## 1. Integral level-zero theta independent of p

For E: y²+y=x³+x²−2x (389a1), let m(a/n)=[a/n]^+ be the 390-vector integer Manin-normalized modular symbol, uniquely fixed by m(7/389)=−1,m(5/389)=−2, Hecke eigenvalues and rational Manin relations. The 390-vector is checked in the standalone exact 2026-11-08 Manin certificate. Fix n=qr coprime to 389 and define

    θ_n = Σ_(a∈(Z/n)×) m(a/n) σ_a ∈ Z[G_n],
    G_n=(Z/n)× = C_(q−1) × C_(r−1).

This is the **UNREGULARIZED, WITHOUT 1/2** modular-symbol/Mazur–Tate-type theta, NOT the exact conventional regularized plus theta. Put X=[g_q]−1, Y=[g_r]−1 for primitive roots. Write S=(S0,SX,SY,SXX,SXY,SYY) for Σ_m (1,i,j,binom(i,2),ij,binom(j,2)). Exact group-ring algebra implies

    θ_n ∈ I_n² ⇔ S0=0, (q−1)|SX, (r−1)|SY,

and the exact quadratic class has representative

    (SXX−SX/(q−1)·binom(q−1,2), SXY, SYY−SY/(r−1)·binom(r−1,2))

in

    I_n²/I_n³ ≅ Z/(q−1)·X² ⊕ Z/gcd(q−1,r−1)·XY ⊕ Z/(r−1)·Y².

All integer sums were computed from the **complete** units in each conductor by pure Python with an independently audited 390-entry integral vector.

| n | roots | full six integer moments | quadratic representative | coordinates; exact order |
|---|---|---|---|---|
| 2501=41×61 | (6,2) | (0,280,60,5360,244,950) | (−100,244,−820) | (20 mod40, 4 mod20, 20 mod60), **30** |
| 76049=113×673 | (3,5) | (0,−448,−26208,−23408,−2604992,−9552816) | (1456,−2604992,−760032) | (0 mod112, 16 mod112, 0 mod672), **7** |

These are **two actual p-independent INTEGRAL nonzero rank-two theta classes**. Their mixed coordinates recover exactly earlier independently computed two-prime Kurihara digits: 244=4 (mod5), −2604992=2 (mod7). No new prime-primary Sha theorem is claimed from that recovery.

## 2. Conventional regularization and real G⁺ quotient (important 2-adic normalization)

The squarefree regularized modular symbol is

    m*(a/qr)=m(a/qr)−m(a·r^−1 mod q /q)−m(a·q^−1 mod r /r)+m(0).

Since m*(−a/n)=m*(a/n), the conventional element in Z[G_n^+] for G_n^+=G_n/{±1} is

    θ*_(n,+) = (1/2)Σ_(a∈G_n) m*(a/n)[a].

The 1/2 is exact **after passing to the real group-ring quotient**. For this curve m(0)=0; only one representative per ± pair is summed, so every coefficient is integral.

The plus group ring has the extra relation (1+X)^((q−1)/2)(1+Y)^((r−1)/2)=1. Modulo cubic augmentation its degree-two lattice in Z³ is generated, with m=q−1,k=r−1, by

    (m,0,0),(0,m,0),(0,k,0),(0,0,k),
    (m/2,k/2,0),(0,m/2,k/2),(-m²/4,mk/2,-k²/4).

For any actual θ*∈I² the exact order of its quadratic jet v is the index ratio [Z³:L]/[Z³:(L+Zv)], computed as gcds of all 3×3 integer minors. This is an **exact Smith lattice** computation, not a numerical approximation.

| n | complete plus moments | quadratic jet | invariant factors I²/I³ | exact order |
|---|---|---|---|---|
| 2501 | (0,−600,−1440,−9910,−46358,−33000) | (1790,−46358,9480) | (10,10,120) | **20** |
| 76049 | (0,−10752,415968,−6832,19186280,147637728) | (589904,19186280,8080464) | (56,56,672) | **7** |

The full integral sparse plus coefficients were computed: 939 nonzero out of 1200 at n=2501, and 32,408 nonzero out of 37,632 at n=76049. Both exact class orders were reverified using INVERSE primitive roots (7,31) and (38,404): unchanged. An independently written JAVASCRIPT evaluator reconstructed the 390 Manin vector from the historical 67 Hecke-generator scalar table and Γ₀(389) relation export and independently reproduced **all six entire-conductor regularized plus moments** at both n, exact integer equality. All arithmetic passed.

## 3. A sharp obstruction to all-prime Selmer control

For a finite abelian G, I²/I³ is a quotient of Sym²(G) and has exponent dividing exp(G). Equivalently I⊗Z_ℓ=(I⊗Z_ℓ)² for every ℓ∤|G| by semisimple augmentation splitting. Therefore **no finite-conductor rank-two jet can detect arbitrary large primes**.

The conventional n=2501 jet has exact order 20, supported only at primes 2,5. The n=76049 jet has exact order 7. Neither annihilates Sha at any p: these are classes of a **group ring**, not the global Selmer. The two prime-independent objects exist, but a uniform integral cohomological comparison and a family varying with prime support would still be required to annihilate the full Sha.

## 4. The exact unproved rank-two comparison

Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan 76 (2024), Conjecture 1.1, predict a **rank-two cohomological Bockstein leading-term identity** relating Kato's derived zeta class to L''(E,1)/(2Ω^+ Reg∞), in addition to an integrality statement. Their published Theorem 1.3 on order-of-vanishing for general real abelian F explicitly **assumes Sha(E/F)[p∞] finite**: it cannot be used to prove finiteness of Sha by itself. The rank-two leading-term equality remains conjectural. The 2025 Burns–Kurihara–Sano Mazur–Tate refinements likewise do not automatically establish the full classical rank-two BSD formula.

Primary literature:
- https://kurihara.math.keio.ac.jp/bks4.pdf (Conjecture 1.1, Theorem 1.3, Conjecture 1.6)
- https://doi.org/10.1093/imrn/rnaf012 (Mazur–Tate refined)
- https://www.math.lmu.de/~bley/etncIII_2.pdf (traditional squarefree regularization and factor 1/2)

## 5. Audit and files

Complete user-downloadable certificate (produced and SHA256 verified this turn):

    bsd389_integral_Mazur_Tate_rank2_two_conductors_20261113.zip
    sha256 18a1f63838a97ce36953979d003f0b664b65144079cb721aa7159d5b3c14e9a0

Includes regenerated 390-symbol data, three standalone integer algorithms, exact complete sparse coefficients at BOTH conductors, inverse-root audits, all JSON certificates, and SHA256SUMS. An independent GitHub-checkable 390-entry rational-symbol vector is also recorded in verification/bsd389_390_integral_manin_vector_20261113.json, commit 3f1ce94.

**VERDICT:** nontrivial integer theta elements at TWO finite abelian levels, their EXACT rank-two graded classes, and complete root-choice-invariance VERIFIED. An integer globally annihilating Sha and the exact complex rank-two BSD leading coefficient are **NOT** established.