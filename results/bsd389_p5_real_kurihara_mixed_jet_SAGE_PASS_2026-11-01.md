# Genuine p=5, q=(41,61) mixed Mazur–Tate jet — user-run Sage/eclib PASS (2026-11-01)

**Provenance:** this is the user's actual Ubuntu Sage terminal stdout from `verification/bsd389_p5_kurihara_mixed_jet_direct.py`, after fast-forward to source commit `d1bf81b`. This archive reproduces user-supplied output; it is **not** a new GitHub CI execution. The 2,400-element CRT distribution was held in memory by the script, not exported here.

## Exact terminal output

```text
P5_MIXED_JET_PROGRESS 200 / 1200
P5_MIXED_JET_PROGRESS 400 / 1200
P5_MIXED_JET_PROGRESS 600 / 1200
P5_MIXED_JET_PROGRESS 800 / 1200
P5_MIXED_JET_PROGRESS 1000 / 1200
P5_MIXED_JET_PROGRESS 1200 / 1200
P5_ALL_2400_CRT_UNITS_SYMMETRIC_COMPLETE_PASS eclib_evaluations 1200 direct_independent_sage_samples 24
P5_THETA_LOWEST_MOMENTS M00 0 M10 0 M01 0 M11 4
P5_MIXED_ANCHORED_JET_PASS direct 4 difference 4 matrix_rank 39 nonzero_mixed_entries 1846
P5_PRIMITIVE_ROOT_CHANGE_UNIT_SCALING_PASS old 4 new 3 factor 2
P5_INDEPENDENT_DIRECT_KURIHARA_DELTA_MATCH_PASS p 5 n 2501 delta_mod_p 4
BOUNDARY_P5_ONLY_NO_UNIFORM_TWO_PRIME_NONVANISHING
```

## Certified observations

1. **1,200 genuinely computed eclib sign-plus cusps** at denominator `2501=41*61`, plus 1,200 involution partners, fill all `(41−1)(61−1)=2,400` CRT unit positions. **24 independent Sage modular-symbol samples matched**.
2. The four `F_5` coefficients of the group-ring element's Taylor image `Theta(1+T,1+U)` are exactly
   [
   M_{00}=0,quad M_{10}=0,quad M_{01}=0,quad M_{11}=4.
   ]
   Thus `Theta(1+T,1+U) = 4 TU (mod 5,T²,U²)`. This is a statement about **the truncated two-variable image**, not a claim `Theta=4TU` as a full group-ring element.
3. The mixed anchored matrix is 40×60, has its first row and column zero, so its **maximum possible rank is 39**; the independently computed rank is **39/39 maximum**. It has **1,846 nonzero entries** (of 2,400). This demonstrates the genuine E modular-symbol distribution is highly non-additively-separable at this conductor; rank does not by itself force the Kurihara contraction to be nonzero.
4. The direct weighted sum and mixed anchored-difference formula agree at 4 mod 5. Changing the primitive roots from (6,2) to (6³,2¹¹) changes `4 -> 3` with unit scaling `2`, as predicted; root choice cannot change zero versus nonzero.
5. The result `delta_2501=4 mod 5` **independently agrees with the historical exhaustive p5 Kurihara witness**, providing a qualitatively different direct modular-symbol provenance.

### Additional theorem and boundary

The vanishing of the three lower bidegree-(0,0),(1,0),(0,1) coefficients is in fact **forced at every good odd p for a pair of admissible q** by the Hecke relation
[
a_q m(r)=m(qr)+sum_{t=0}^{q-1}m((r+t)/q).
]
After summing over CRT units in the other coordinate, the marginal is `(a_q-[q]-[q]^{-1})Theta`, and since `a_q≡q+1≡2 modp`, this operator is congruent to `-(sigma_q−1)^2/sigma_q` in the augmentation ideal squared. Therefore the **constant and linear marginal coefficients vanish**. Precise source algebra and assumptions are documented in [the new universal Hecke–marginal lemma](../paper/bsd389_kurihara_hecke_marginals_force_low_jets_2026-11-01.md). The **mixed** bidegree-(1,1) coefficient is NOT forced by these congruences; the new p5 source establishes it is 4.

**No proof for all p:** These statements neither bound the support of Sha nor give `delta_(q1q2)!=0` uniformly. The exact full BSD rank-two leading-term identity and finite Sha remain unresolved.
