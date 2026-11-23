# 389a1, supersingular p=1049: genuine user Ubuntu rerun of the complete quadratic moment

Date: 2026-11-23. **Actual user terminal evidence**, not an assistant-side extrapolation.

## Invocation

The user fast-forwarded branch `research/bsd389-theta2-finite-depth-20261122` to commit `a31c734`, then executed:

```bash
python -u verification/bsd389_supersingular_p2_signed_moments_exact.py --p 1049
```

## Exact printed result

```json
{
  "C0": 0,
  "C1": 0,
  "C2": 202,
  "Pollack_scalar_signed_coefficient_modp": 948,
  "ap": 0,
  "complete": true,
  "count": 549676,
  "input_manin390_sha256": "31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee",
  "p": 1049,
  "theorem_scope": "signed analytic coefficient gate; Sha implication uses the published theorems with checked local hypotheses",
  "unit": true
}
```

Elementary checks:

- `1049` is prime, and `a_1049(E)=0`; good supersingular with `#E(F_1049)=1050`, so local p-torsion vanishes.
- The source loops over *all* `p(p−1)/2=1049*1048/2=549676` nonzero plus-involution representatives modulo `p²=1100401`.
- `-202·2^{-1}=−101=948 (mod 1049)`, a nonzero unit. `(C0,C1)=(0,0)` mod p are **finite-level** moment statements.
- The source Manin vector SHA256 matches the repository's fixed integral 390-vector used to compute the original suite. This records its provenance, but the rerun itself is not a new independent reconstruction of that vector.

## Mathematical scope

The *finite* p² moment `C2=202 mod1049` and full enumeration are now **user-reproduced**. Turning the output into a coefficient of the **actual infinite Pollack signed p-adic L-function** requires the p³-to-p² distribution identity, correct signed logarithmic normalization, and an explicit precision bound, as articulated in the associated research note:
`paper/bsd389_p599_Pollack_scalar_signed_unit_and_Sha_zero_proof_2026-11-23.md`.

The proposed Selmer implication additionally invokes Burungale–Skinner–Tian–Wan (2024) Theorem 1.3 (integral supersingular main conjecture), B. D. Kim (2013) Theorem 1.1 (no finite `Lambda`-submodule of the signed dual under cotorsion), the base-field-to-signed Iwasawa restriction map, and Mordell–Weil rank 2. These are theorem-level inputs and **not proved by the JSON**. Their precise normalization and control compatibility should be independently reviewed before publishing `Sha[1049∞]=0` as unqualified.

This prime-by-prime success **does not** construct the global all-large-primes annihilator, an effective finite-support bound on Sha, or the exact complex rank-two BSD leading coefficient.

References:
- Burungale–Skinner–Tian–Wan, https://arxiv.org/pdf/2409.01350 , Thm 1.3.
- B. D. Kim, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7AD9B7AB53A73F23F8E78F78488FA75C/S1446788713000165a.pdf/the-plusminus-selmer-groups-for-supersingular-primes.pdf , Thm 1.1.
