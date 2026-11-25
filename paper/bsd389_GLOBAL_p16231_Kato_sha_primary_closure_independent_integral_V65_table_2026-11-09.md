# BSD 389a1 — Independent integral V65 regeneration and full-archive Kato certificate for p=16231 (9 November 2026)

**NEW independently executed work:** rebuild the complete 2,175,242-byte V65 modular-symbol/Hecke table with NO Sage/eclib, recalculate the level-two coefficient mod p² using safe 64-bit arithmetic, and prove/test the source correction n3−n2 against **seven independently enumerated small primes**. The published historical full J=4486 runs are **reused, NOT rerun**. Under those frozen computation certificates, the one-prime Kato upper-bound exponent is exactly ZERO. **No global Sha finiteness or complex BSD leading-term identity is claimed.**

## Curve, prime, and normalized inputs

E: y²+y=x³+x²−2x, conductor and minimal discriminant +389; MW rank two, saturated basis, torsion 1, Tamagawa product 1; p=16231 ordinary, a_p=128, #E(Fp)=16104.

The integral 390 Manin values have signed coefficients in [−2,2], independently fixed by m⁺(7/389)=−1, m⁺(5/389)=−2 and Hecke regression. SHA256 of bytes (V[i]+2) for i=0..389:

    31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee.

## New theorem-strength verification: the complete V65 table independently rebuilt

A stand-alone **C++17 generator**, with the archived 67 integer Manin generators and ONLY the self-contained 390 coefficients, evaluates the rational-cusp integral modular symbol F(G), F(PG), and F(beta_t G), for every t=0..16230 and g=0..66. All **67 exact Hecke identities** pass. The resulting 2,175,242-byte binary file has SHA256

    **aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c**.

This digest is **identically equal** to that of the historically frozen independent Sage/eclib V65 table, originally created by historical/v65/v65_generate_eclib_table.py and consumed by both complete J computations. Thus the most important common prior external data dependency has been independently reproduced at every byte without Sage or eclib.

The new C++ script and regenerated binary are in the user-downloadable current-conversation archive
\`bsd389_p16231_Kato_via_independent_V65_reconciliation_20261109.zip\` (archive SHA256 \`46315a64801cc1814e1c3ff01637db0e8be47aeab24f6326c232aa681c9e3a42\`).

## Second independent native calculation: level n=2

Using the same 390 normalized symbols, a **new 64-bit-safe C++17 evaluator** sums all 131,714,565 half-domain values and correctly includes the α^(−2) and α^(−3) measure terms, the real-components normalization 1/2, and the p² ordinary root α=179060520. It obtains

    raw doubled sum mod p² = 159258572,
    lower correction mod p² = 0,
    **A_2(n=2)=19460969=1199·16231 (mod 16231²).**

This independently matches the old V61 value, and its code does **not read that old V61 value**.

## Third independent direct source-level identity regression

For each p in {5,7,11,13,17,19,23}, a new integer C++ evaluator directly computes **both** the full n=2 and n=3 finite measures from the 390 Manin table and independently forms the C01 moment

    J_ref = −Σ_(a,b) w(a,b)[ M1(D_x) − κ(a,b)M0(D_x)] mod p.

It checks, for each p, the exact integer congruence

    A_2(n=3) − A_2(n=2) = p J_ref/(4 α²) mod p².

All **seven** cases PASS:

| p | α mod p² | A₂(n=2) | A₂(n=3) | J_ref |
|---:|---:|---:|---:|---:|
| 5 | 7 | 14 | 24 | 2 |
| 7 | 16 | 19 | 33 | 4 |
| 11 | 29 | 108 | 42 | 1 |
| 13 | 114 | 120 | 81 | 9 |
| 17 | 45 | 64 | 200 | 13 |
| 19 | 290 | 331 | 255 | 18 |
| 23 | 134 | 373 | 511 | 16 |

The **general identity** is proved algebraically using Sage's ordinary measure definition, its distribution property, and Hecke. The regressions are independent consistency tests, not a substitute for that general proof; see paper/c01_sage_n3_minus_n2_universal_lemma_auditable_2026-10-26.md.

## Reuse of two fully executed, frozen historical J scalar runs

Two independent historical producer/consumer algorithms previously evaluated the **complete 263,429,130-pair domain** and gave

    J_ref ≡4486 mod16231.

Source and binary, final checkpoints and complete logs have archived SHA256 manifests, terminal exit statuses and an independent provenance audit in:

- results/independent_scalar_J_global_263429130_pairs_PASS_2026-10-26.md
- results/independent_scalar_J_full_provenance_audit_PASS_2026-10-26.md
- results/independent_scalar_J_frozen_sha256_manifest_2026-10-26.json
- historical/v65/v65_terminal_certificate.json

**This 9 November session did NOT reexecute either complete 263m-pair J sum, and did NOT directly run Sage's level-three L-series or Sha.p_primary_bound.** The scalar is accepted as historical finite computation, as for any imported independently audited certificate. The new exact bytewise V65 reproduction materially strengthens the chain of evidence.

## Algebraic conclusion and Kato theorem

The derived correction factor is

    (4·128²)^(−1) ≡9362 mod16231;
    4486·9362 ≡8335 mod16231.

Thus source identity and n2 give

    A_2(n=3)/16231 ≡1199+8335 = **9534** mod16231,

equivalently

    **A_2(n=3) ≡154746354 mod 263445361**.

Sage 10.9's independently audited \`_prec_bounds(n=3,prec=3)[2]=2\` makes this an actual p-adic L₂ congruence mod p².

The independently previously certified p-adic regulator, from two Sage height algorithms, satisfies normalized raw

    Reg_raw /p³ ≡1930 mod p,

and with χ(γ)=1+p, rank 2, Tamagawa 1, torsion 1, the Euler factor

    ε=(1−128^(−1))² ≡10820 mod16231,

its algebraic BSD factor satisfies

    B_p / p ≡1930·10820 ≡9534 mod16231.

Therefore

    **(L₂/B_p) ≡1 (mod16231)**,

and in particular **v_p(L₂/B_p)=0**. The fact that the quotient digit is 1 is a mod-p congruence only; no exact p-adic BSD equality is inferred.

Stein–Wuthrich/Kato's rigorous *upper-bound* theorem, as implemented in \`Sha.p_primary_bound\`, uses precisely the (nonnegative) p-valuation of this quotient under good ordinary and surjective Galois hypotheses, already checked on the user's Sage 10.9 host in results/kato389_sage10_9_terminal_pass_2026-10-19.md. Consequently, **accepting the full archived J=4486 finite computations**,

    **Sha(E/Q)[16231^∞]=0.**

This is a **one-prime arithmetic result**, not a global BSD theorem. If an absolutely independent third evaluation of J is demanded, that further reproduction is still outstanding; this certificate's dependency is openly identified rather than hidden.

The reproducible current-turn auditor \`bsd389_16231_reconciliation_audit_20261109.py\` compiles/runs the new three C++ modules; it recomputes all the new facts and marks the historic J as NOT REEXECUTED.

## Scope and citations

- Stein–Wuthrich, *Algorithms for the Arithmetic of Elliptic Curves Using Iwasawa Theory*, Math. Comp. 82 (2013), rank-two p-adic Selmer bound.
- SageMath \`sha_tate.py\`, method \`p_primary_bound\`: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/sha_tate.html
- SageMath \`padic_lseries.py\`, methods \`measure\`, \`series\` and \`_prec_bounds\`: https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/schemes/elliptic_curves/padic_lseries.py
- William Stein (2007), notes documenting Harvey's exceptional regulator value: https://wstein.org/edu/2007/spring/bsd/hw/1.pdf

**Global boundaries:** Sha at other unproved primes, global Sha finiteness, a nonzero p-independent annihilator, and the exact complex rank-two BSD leading-term identity are all still open.
