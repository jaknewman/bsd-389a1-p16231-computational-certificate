# BSD 389a1 — Exact Mellin–Fricke and AGM formulas with an explicit Fourier tail bound (10 November 2026)

**Status:** exact analytic/arithmetic reduction, independently executed high-precision numerical cross-check, and rigorously proved Fourier tail inequality. **NOT** an exact complex BSD proof, nonzero uniform Sha annihilator, or arithmetic–analytic comparison.

## 1. Exact Fricke–Mellin identity

For E:y²+y=x³+x²−2x, conductor N=389, root number +1, analytic rank two, let f(z)=Σ_{n>=1}a_n e^(2πinz). The completed L-function satisfies Λ(s)=N^(s/2) ∫_0^∞ f(it)t^(s−1)dt. Fricke with sign + gives f(i/(Nt))=Nt² f(it). Therefore

    Λ(1+u)=∫_1^∞ f(ix/√N)(x^u+x^(−u))dx,

so

    **L''(E,1)/2=(2π/√N) ∫_1^∞ f(ix/√N)(log x)²dx
                =(2π/√N) Σ_{n≥1}a_n K(2πn/√N)**,

where K(z)=∫_1^∞ e^(−zx)(log x)²dx=(2/z)∫_z^∞ e^(−t)log(t/z)dt/t. This identity is an unconditional consequence of modularity, Fricke, the analytic rank, and termwise dominated convergence.

## 2. Explicit rigorous truncation bound

Put c=2π/√389. For every n, Deligne and Hecke give |a_n|≤d(n)√n≤2n. Since log x≤x−1 for x≥1,

    K(cn) ≤ 2 exp(−cn)/(cn)³.

Thus for every M≥1,

    **| L''/2 − c Σ_(n=1)^M a_n K(cn) |
        ≤ (4/c²) exp(−c(M+1))/((M+1)²(1−exp(−c))).**

At M=300 the bound is <3.62×10^(−45). This rigorously bounds the Fourier *tail*, not mpmath quadrature rounding.

Finite-field exact point counts and Hecke recurrences generated the first 300 integer Fourier coefficients independently, including a₂=−2,a₃=−2,a₅=−3,a₇=−5,a₁₁=−4,a₁₃=−3,a₁₇=−6,a₁₉=5,a₂₃=−4.

## 3. Independent real Néron period via AGM

Let e1>e2>e3 be the three real algebraic roots of 4x³+4x²−8x+1. The positive minimal discriminant gives two real components and the **total** Néron period

    **Ω_E = 4∫_(e1)^∞ dx/√(4x³+4x²−8x+1)
          =2π/[√(e1−e3) AGM(1,√((e1−e2)/(e1−e3)))].**

This is independent of the modular form Fourier coefficients.

## 4. Exact rational point and height reduction

For the saturated MW generators P=(−1,1),Q=(0,−1), exact group-law computations give

    P+Q=(4,8), P−Q=(1,0).

Consequently, if h is the Néron–Tate height,

    **Reg_E = h(P)h(Q) − 1/4·(h(P)+h(Q)−h((1,0)))².**

The unresolved complex rank-two identity, in completely specified functions of one-dimensional integrals, Hecke coefficients, algebraic roots, AGM and three canonical heights, is

    c Σ_(n>=1) a_n K(cn) = Ω_E · Reg_E.

This equality is EXACTLY the strong BSD leading-term prediction when Sha=1, and it is **NOT proved by this computational exercise**. Numerical agreement does not imply an identity of real numbers.

## 5. Executed independent numerical cross-check

mpmath at 55 decimal places; sum truncated after 300 terms:

    L''(1)/2 ≈ 0.759316500288426770230192607894722019078097517
    Fourier tail upper bound 3.61679553e−45
    Ω_E ≈ 4.98042512171011015064271558388460492031211636
    external LMFDB regulator digits 0.15246017794314375162432475705
    quotient using those ROUNDED external regulator digits
       ≈ 0.9999999999999999999999999999964307

The regulator was **not independently recomputed to 29 digits**; the ratio is a numerical consistency test with the LMFDB regulator and is not a proof.

## 6. Limits of other 2026 results

The October 2026 full BSD formula at q-Selmer corank 0 or 1 does not apply because MW rank=2 forces q-Selmer corank≥2 at every q. Recent November 2026 rank-two elliptic-unit formulas for CM curves do not apply: j(E)=112³/389=1404928/389 is nonintegral, hence E has no CM. General all-rank conjectural papers and unreviewed proof claims are not substitutes for source-verified hypotheses.

## 7. Remaining exact proof requirements

(A) Prove a p-independent nonzero annihilator of Sha(E), or another uniform global finiteness/triviality result, across infinitely many prime supports. Partial p-primary certificates, however many, are not enough.

(B) Prove an exact rank-two height–Mellin comparison theorem for E389a1. Neither Fricke nor the AGM identity alone supplies it. The precision of finite numerical evaluation cannot close (B).

The executable script in the user's conversation is \`bsd389_archimedean_rank2_exact_20261110.py\`, with the companion document \`bsd389_archimedean_rank2_exact_20261110.md\`.

Sources: [LMFDB 389.a1](https://www.lmfdb.org/EllipticCurve/Q/389a1/); standard Mellin/Fricke equations of weight-two newforms; Deligne Ramanujan inequality; Stein–Wuthrich; [the 2026 CM rank-two paper](https://arxiv.org/abs/2611.09192).