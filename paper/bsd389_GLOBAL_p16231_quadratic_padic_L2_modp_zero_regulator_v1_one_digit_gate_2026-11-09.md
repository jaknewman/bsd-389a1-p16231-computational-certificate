# BSD 389a1 — Independently computed **L₂ ≡ 0 mod 16231** and a published regulator of valuation ONE (9 Nov 2026)

**NEW EXACT computational arithmetic result. The 16231-primary Sha remains UNPROVED, as does uniform Sha finiteness and classical rank-two complex BSD.**

## Actual completely executed arithmetic

On E: y²+y=x³+x²−2x, prime conductor 389, Néron plus-symbol integral normalization, the prime p=16231 is ordinary:

    p=16231; a_p=128; #E(F_p)=16104 (nonanomalous).
    [T²]L_p(E,T) ≡ **0** (mod 16231).

**This is a certified finite congruence, not an assertion that the full p-adic coefficient equals zero.**

The coefficient was evaluated by a brand-new stand-alone C++17 program which reconstructs Sage's exact ordinary p-adic *measure* at depth p² from the archived 390-entry **integral** Manin plus-symbol table. This table was itself freshly regenerated from 1,559 exact integer Manin/plus/Hecke relations, a rank-389 mod-7 nullspace, the previously Sage/eclib certified cusps m⁺(7/389)=−1 and m⁺(5/389)=−2, and exact checks of Hecke at 3,5,7,11,13,17.

With γ=1+p and ω(a)=a^p mod p², write b=ω(a)γ^j, 0≤j<p, 1≤a<p. The ordinary measure and coefficient formula in Sage's official implementation are

    μ(b+p²Z_p)=α^(−2) m⁺(b/p²) − α^(−3) m⁺(b/p),
    L₂ ≡ (1/2) Σ_{j,a} binom(j,2) μ(b)   (mod p),

where α≡a_p mod p. For p≥5, the correction term disappears because Σ_j binom(j,2)=binom(p,3)≡0 mod p. Thus the certified one-digit identity is

    L₂ ≡ [2(a_p)²]^(−1) Σ_{j=0}^{p−1} binom(j,2) Σ_{a=1}^{p−1}
                 m⁺(ω(a)(1+p)^j/p²)   (mod p).

The error bound in Sage's \`series(n=2, prec=3)\` source guarantees the T² congruence modulo p, because the residual representation is surjective and the plus modular symbols are integral.

**Three independently executed complete summations:**

- Teichmüller γ-orbit algorithm with exact plus symmetry: 131,698,335 nonzero-weight terms, L₂=0 (mod 16231).
- Residue-by-residue algorithm using the *different* formula j=((b−ω(b mod p))/p)·(b mod p)^(−1) (mod p), first half: 131,698,335 terms, L₂ contribution=0.
- Same independent residue algorithm, disjoint second half: 131,698,335 terms, L₂ contribution=0.

Together, the latter two chunks **exhaust all units modulo p²**; 263,429,130 units exist and exactly 263,396,670 carry nonzero binomial weight. The output is **zero**. Independent small-prime checks give exactly the Sage-documented p=3 coefficient 2, p=5 coefficient 4, and identical Teichmüller-vs-residue results at p=7,11,13,17,101,1009. The integral Manin vector and logs have been checked by SHA256 and an autonomous audit script.

## Crucial independent published regulator datum

William Stein's *Math 583 Project Set 1* (March 28, 2007), question 4, reports David Harvey's computed p-adic regulator for E389a:

    Reg_{16231}(E) = 1930·16231 + 2051·16231² + ... ,

so **v_{16231}(Reg)=1**. This exact published valuation independently explains why p=16231 defeats a UNIT-only quadratic coefficient test. The local Euler factor is a unit because #E(F_p)=16104, and ε_p=(1−128^(−1))²≡10820 (mod 16231).

Sources:
- https://wstein.org/edu/2007/spring/bsd/hw/1.pdf (dated historical mathematical note, Q4)
- https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/schemes/elliptic_curves/padic_lseries.py (official exact measure, series algorithm and precision bounds)
- https://doc.sagemath.org/html/en/reference/modsym/sage/modular/pollack_stevens/padic_lseries.html (efficient overconvergent eigenlift)

**The next one-digit decisive test:** Determine L₂ modulo p². If **v_p(L₂)=1**, the proved ordinary Iwasawa main-conjecture comparison and Perrin–Riou–Schneider's leading-term/Selmer theorem, with published v_p(Reg)=1 and p-unit Euler/Tamagawa factors, would yield Sha(E/Q)[16231∞]=0. If L₂ vanishes modulo p², this route cannot conclude Sha triviality from the current data. The precise *value* of L₂/p (e.g. a guess based on ε·1930) is NOT deducible from an up-to-unit characteristic ideal alone.

**Cost control:** Sage's ordinary \`series(n=3)\` enumerates (p−1)p² = 4,275,718,209,030 residue terms, so the direct implementation is not a suitable next check. Pollack–Stevens' polynomial-time overconvergent modular-symbol algorithm is the appropriate next attempt. A separate Sage 10.x script using \`E.padic_lseries(p,implementation='pollackstevens',precision=6)\` tests the coefficient at certified p-adic precision ≥2. **It was prepared and syntax-checked but was NOT executed (Sage unavailable in the assistant runtime).**

## Reproducibility

The current-conversation ZIP \`bsd389_p16231_quadratic_L2_modp_exact_certificate_20261109.zip\` SHA256 \`b860337bffe242947b74a06850e2eecf873a0b17d5553e31aa48127260ed51ab\` contains the exact C++17 and Python sources, native complete execution logs, integral Manin vector and regeneration proof, high-precision OMS Sage gate and the SHA256SUMS manifest (16 files).

**Verdict:** a new EXACT non-unit quadratic L₂ mod p certificate and a previously published non-unit regulator produce a sharp one-digit p² target. No solution of 16231-primary Sha and no full complex BSD claimed.