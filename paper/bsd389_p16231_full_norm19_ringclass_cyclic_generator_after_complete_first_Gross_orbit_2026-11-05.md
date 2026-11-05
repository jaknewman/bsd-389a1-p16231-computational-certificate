# New exact full ring-class generator and the first complete genuine Gross theta orbit

**2026-11-05**. E=389a1, K=Q(sqrt(-3)), p=16231. The user has now fully computed the real 16231-point n=1 P2 Gross orbit above Teich residue a=1 using exact p4 quaternionic local charts and witnessed Brandt class classification. This note gives an independent new cyclic generator result and clearly states the analytic boundary.

## Fully computed first orbit

User Ubuntu Sage aggregate \`P2_AGGREGATE_COVERAGE 16231 OF 16231 MISSING 0\` and \`P2_FULL_ONE_TEICH_ORBIT_MOMENTS_PASS\`, with

M0(1)=0, M1(1)=10775, M2(1)=5515 (mod 16231).

The normalized contributions to theta_n1 degree 0,1,2 are [0,460,13755] mod p, with alpha_p^(-2)=4986. In particular the first single-orbit quadratic contribution is a p-adic unit, **but so is the linear contribution 460**. These are contributions of ONE Teich coset only: global theta nonvanishing is NOT proved. The exact complete histogram of 33 Brandt values and independent re-addition of 32 chunk moments appear in [results/bsd389_p16231_P2_FULL_residue1_16231_gross_moments_USER_PASS_2026-11-05.md](../results/bsd389_p16231_P2_FULL_residue1_16231_gross_moments_USER_PASS_2026-11-05.md).

## New exact theorem: one norm-19 element generates ALL 87,809,710 ring classes

K has class number one, p splits, and the local CRT identifies

Pic(O_(p²)) ≅ (Z/p²)× / mu3,

so this ring-class group is **cyclic** of order H=p(p−1)/3=87,809,710. For the two Hensel roots r0=49689135, r1=213756225 and g=5+3omega, Norm_K/Q(g)=19, define

w=(5+3r0)/(5+3r1) mod p² = **138112843**.

Modulo p, w=3264. Exact finite arithmetic proves

w^(3H)=1 mod p²

and, for every prime q dividing H, w^(3H/q) !=1 mod p²:

q=2:   w^(3H/2)=263445360,
q=5:   w^(3H/5)=60363249,
q=541: w^(3H/541)=255236327,
q=16231: w^(3H/16231)=87890866.

Since an element has order H in a cyclic quotient by mu3 iff its H-th power belongs to mu3 and its (H/q)-th power does not for any prime q | H, **the ring-class of g has exact order H**. Thus *the same norm-19 prime already used in the conductor-53 historical orbit* is also a generator of the ENTIRE conductor-p² ring-class group (not just its order-p kernel).

A standard-library exact checker is committed at:
[verification/bsd389_p16231_norm19_whole_ringclass_generator.py](../verification/bsd389_p16231_norm19_whole_ringclass_generator.py).

The full generator result is derived by exact modular arithmetic on 2026-11-05 and checked in the assistant's container. **It has not yet been replayed by the user on their Ubuntu.**

## Explicit indexing suitable for subsequent quaternionic transport

The split ratio decomposes at level p² uniquely into a Teichmueller unit times a principal unit:

w=Teich(w)·(1+p)^s (mod p²),

Teich(w)=w^p=**121898074**, and s=**10816** (mod 16231).

The class of Teich(w) has exact order 5410 after the global mu3 quotient. Therefore the 5410 distinct Teich cosets may be indexed as

a_j=Teich(w)^j (mod p²), j=0,...,5409,

or by their nonzero residues r_j=3264^j mod 16231. Within each coset the p-part is u^i, 0<=i<16231. This gives a **single coherent cyclic enumeration** of all 87,809,710 ring classes, and the old norm19 p-part relation G=[g]^5410=U^1805 is compatible with it.

Important: a group-level enumeration **does not** automatically provide the Brandt eigenvalue \`phi_f(P2^a)\`. To speed up the 87.8-million-point theta calculation one needs a proven exact quaternionic 19-neighbor recurrence on the **correct conductor-p² oriented CM embedding**, with the Galois Artin/local split orientation correctly identified, or a separate height/regulator method avoiding this exhaustive sum. The historical 18-point conductor-53 orbit cannot be substituted.

The exact cyclic generator does not imply theta order 2 or any Sha finiteness statement. The p-adic nonzero single-orbit quadratic contribution does not exclude cancellations from the other 5409 Teich orbit contributions.

## Auditable next small step

Run:

\`\`\`bash
python -u verification/bsd389_p16231_norm19_whole_ringclass_generator.py
\`\`\`

and verify the four prime-order gates plus \`NORM19_FULL_RINGCLASS_GENERATOR_PASS 87809710\`. This checker uses only standard Python, no quaternionic computation. Then prioritize constructing a **real norm19 neighbor transition between actual p² conductor CM points**, rather than 5409 consecutive full runs of the existing Gross ideal classifier.
