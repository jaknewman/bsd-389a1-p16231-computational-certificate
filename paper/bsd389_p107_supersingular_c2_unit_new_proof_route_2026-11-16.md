# E389a1: independent supersingular p=107 cyclotomic quadratic moment (2026-11-16)

## Arithmetic theorem actually checked

For E: y²+y=x³+x²−2x, p=107, the exact point count is #E(F_107)=108 and a_107=0, so 107 is supersingular. Let n=p² and let m⁺(a/n) be the rational plus modular-symbol cusp sum defined by the previously archived independently reconstructed 390-entry integer Manin vector. Define j(a) in F_p through

    a = omega(a) (1+p)^j(a) (mod p²), omega(a)=a^p (mod p²).

Define C_k=sum_{a in (Z/p²)^×} binom(j(a),k) m⁺(a/p²) (mod p), for k=0,1,2.

Exact direct enumeration of all 5671 plus-symmetry representatives, with an independent discrete-log lookup for all j(a), gives

    C0=0, C1=0, C2=86 (mod 107).

Every representative passed the independent sym(a)=sym(p²-a) check and the agreement of the Fermat-quotient cyclotomic exponent with the discrete-log lookup. The p-adic signed-minus coefficient predicted by the p=599 derivation is -C2/2=64 (mod 107), a unit.

This establishes a NEW finite arithmetic input, independent of the historical huge p107 two-prime Kurihara archive, though it shares the archived 390-integer Manin-vector provenance. It does not independently reconstruct the 390-vector from q-expansions, and is not an independent proof of modular-symbol normalization.

## Arithmetic -> Sha bridge: scoped as a separate theorem-level review obligation

If the genuine Pollack/Kobayashi integral signed-minus p-adic L-function at p=107 has order >=2 and quadratic coefficient equal to 64 modulo 107, then L_p^-(T)=T²*unit in Z_107[[T]]. Together with:

  (i) the integral supersingular signed main-conjecture characteristic-ideal equality in the normalization used,
  (ii) no finite Lambda-submodule of the signed Selmer dual (B.D. Kim's theorem, with all its hypotheses),
  (iii) injective base-field control map with the saturated rank-two Mordell–Weil subgroup landing in the signed invariants,

the rank-two algebraic lemma from the p599 note proves Sha(E/Q)[107^infty]=0. The argument is prime-specific and does not supply a p-independent integer D.

**IMPORTANT:** The signed-minus identification -C2/2=64 as a coefficient of the *genuine* analytic signed p-adic L-function, including integral n=3 precision and sign normalization, is **not** independently reverified by this new arithmetic script. Therefore the new script proves C2=86, not a fresh unconditional p107 Sha theorem. The prior p107 p-primary vanishing already has independent Sage proof-mode provenance in project archives.

The published supersingular main conjecture: Burungale–Skinner–Tian–Wan, 'Zeta elements for elliptic curves and applications', arXiv:2409.01350.
Signed no-finite-submodule / control: B.D. Kim, 'The plus/minus Selmer groups for supersingular primes', Journal of the Australian Mathematical Society 95 (2013), 189–200; Kim–Kurihara, 'Refined conjectures on Fitting ideals...', sections on exact +/- control.

## Uniform D verdict

A single supersingular unit at p=107 is not a prime-independent annihilator. The algebraic equivalence from the parent commit still makes a uniform nonzero D the outstanding target. A map from the p-independent integral modular symbol lattice to the p-primary Selmer dual in the correct arithmetic direction, with a proven all-p normalization, remains missing. No global Sha finiteness or full complex BSD identity follows from this calculation.
