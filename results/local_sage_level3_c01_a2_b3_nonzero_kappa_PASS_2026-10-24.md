# Direct local Sage/eclib level-3 bridge with nonzero kappa — PASS

**Date:** 2026-10-24. **Execution:** IONOS Sage shell, user-supplied terminal transcript; the versioned source is `verification/local_level3_native_eclib_oracle.py`.

## New test case, deliberately different from (1,0)

Let `E=389a1`, `p=16231`, `a=2`, `b=3`, and `x=a+pb`. The independent elementary arithmetic gives

- `u=11169`
- `w=(2u-1)/a =3053 (mod p)`
- `kappa=11458 (mod p)`

Unlike `(1,0)`, `kappa != 0`, so this case tests the nontrivial `-kappa*M0` contribution and the nonzero Teichmuller exponent.

## Complete terminal transcript

```text
LOCAL_NATIVE_V65_CONTRACTION 2 3 sparse_slots 13 J_mod_p 11725
LOCAL_LEVEL3_PROGRESS 2 3 lifts_done 1
LOCAL_LEVEL3_PROGRESS 2 3 lifts_done 4096
LOCAL_LEVEL3_PROGRESS 2 3 lifts_done 8192
LOCAL_LEVEL3_PROGRESS 2 3 lifts_done 12288
LOCAL_LEVEL3_PROGRESS 2 3 lifts_done 16231
LOCAL_NATIVE_DIRECT_ECLIB_J_PASS 2 3 11725
LOCAL_SAGE_HECKE_DISTRIBUTION_PASS 2 3
LOCAL_SAGE_LEVEL3_MINUS_LEVEL2_PASS 2 3 difference_mod_p2 250411868 J_over_4alpha2_mod_p 15428
LOCAL_INDEPENDENT_ANALYTIC_C01_BRIDGE_PASS 2 3
BOUNDARY: verified a single x=a+p*b, not the sum over p(p-1) residues
EXIT_STATUS=0
```

## Exact numerical identity

`16231*15428=250411868`.

`11725*(4*128^2)^(-1) = 15428 (mod 16231)`.

The original SHA-256-pinned native V11 producer, independently regenerated V65 eclib table and all `16231` eclib modular-symbol values for the level-3 lifts of this residue independently agree on the finite-level n3-minus-n2 formula

`(A2^(3)-A2^(2))_(2,3)=p*J_ref(2,3)/(4*alpha^2) (mod p^2)`.

Sage's ordinary measure distribution was tested as a separate identity. The native one-pair output has 13 nonzero sparse slots, versus four at `(1,0)`.

## Proof boundary

This is direct evidence on a **single base residue** and independently checks a nonzero `kappa` branch; combined with the earlier `(1,0)` run it gives two successful `p=16231` local oracles. The universal source-level analytic identity is algebraic and is not inferred merely from these two samples.

This does NOT compute all `p(p-1)=263429130` base residues, rerun Sage's global `lp.series(n=3)`, or execute `E.sha().p_primary_bound(16231)`. The p-primary conclusion remains a computer-assisted implication involving the authenticated historical full C01 execution and the proven Kato/Sage arithmetic gate.
