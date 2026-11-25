# BSD 389a1 — Two NEW independently checked two-prime Kurihara units (p=19,23), 9 November 2026

**New exact arithmetic result**: independently evaluated, integrally normalized full Kurihara sums at two previously uncertified primes, yielding two more p-primary Sha triviality results by the established rank-2 Kim structure theorem. **NOT** a prime-uniform Sha annihilator or exact archimedean BSD theorem.

Curve: \`E: y²+y=x³+x²−2x\`, N=389, positive minimal discriminant 389, certified full MW basis P=(-1,1), Q=(0,-1), rank 2, torsion 0, Tamagawa product 1.

## Data

| p | q1 | q2 | a_p | #E(Fp) | a_q1 | #E(F_q1) | a_q2 | #E(F_q2) | Local MW rows mod p | det | Full δ mod p |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 19 | 2243 | 3877 | 5 | 15 | -17 | 2261 | 97 | 3781 | (1,1); (0,1) | 1 | **4** |
| 23 | 1289 | 3727 | -4 | 28 | 25 | 1265 | 94 | 3634 | (1,5); (1,12) | 7 | **17** |

All four auxiliary primes q are good, q≡1 (mod p), a_q≡2 (mod p), and v_p(#E(F_q))=1: Frobenius is nonidentity unipotent, each local mod-p Kummer space is 1-dimensional. The nonzero local MW determinants are sanity checks, NOT the premise of a Kurihara unit claim.

A new C++17 direct complete half-sum computation using the **previously certified 390-entry integral Manin table** (Néron normalized by m_E⁺(7/389)=-1) yielded:

    FULL_KURIHARA_P19_NORMALIZED 2243 3877 4
    FULL_KURIHARA_P23_NORMALIZED 1289 3727 17

A **separate pure Python implementation**, with its own continued-fraction symbol evaluation and finite-field discrete logs, independently reproduced each result:

    BSD389_NEW_KURIHARA_WITNESS_PASS p19 q=2243,3877 delta=4; active_half_terms=3899664
    BSD389_NEW_KURIHARA_WITNESS_PASS p23 q=1289,3727 delta=17; active_half_terms=2195424

A third generic C++17 implementation taking the original table as text independently repeated both \`FULL_KURIHARA_CERT_PASS\` outputs. The complete current-conversation reproducible ZIP with scripts, table, logs and SHA256SUMS is named \`bsd389_p19_p23_new_Kurihara_Sha_certificates_20261109.zip\`, SHA-256 \`811df6fcd45c6f4edddd0bdf645394f8535dacee3c4d74c6eab5ac4487eeacdb\`. The ZIP files all passed \`sha256sum -c SHA256SUMS\`.

## Exact theorem-based implication

Kim, *The refined Tamagawa number conjectures for GL2*, arXiv:2505.09121, Theorem 1.1: a nonzero length-two Kurihara number with mod-p unit value and with previously known MW rank 2 yields \`ord(delta)=2\`, \`partial^(2)(delta)=0\`, and \`partial^(infty)(delta)=0\`, hence

    Sel_(p∞)(E/Q) ≅ (Qp/Zp)^2,   Sha(E/Q)[p∞]=0.

The mod-p representation has the already verified large image (E semistable, p≥11), the conductor is prime 389, p=19 and 23 are good ordinary and nonanomalous (#E(Fp)=15 and 28), and the optimal Manin constant is a p-unit. Thus this applies at both p and gives the two boxed deductions

    **Sha(E/Q)[19∞]=0 and Sha(E/Q)[23∞]=0**.

Castella–Sano, arXiv:2601.14504, Theorem 2.1.3, provides the integral-unit reciprocity factor for Kato-derived Kurihara numbers. This factor was mistakenly described as unknown in earlier notes and has been corrected there. Neither Castella–Sano's some-length nonvanishing nor these two specific units proves nonvanishing for all sufficiently large p.

**Not proven:** full \`Sha(E/Q)\` finiteness/triviality, a uniform finite support bound across p, or the exact complex formula \`L''(E,1)/2=Ω_E Reg(E)·#Sha(E/Q)\`. Avoid any uniform inference from the finite examples.

### Literature
- https://arxiv.org/pdf/2505.09121 — Kim, Theorem 1.1 (full Selmer module structure).
- https://arxiv.org/pdf/2601.14504 — Castella–Sano, Theorem 2.1.3 and Theorem B.
