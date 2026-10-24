# Full 32,658,784 C01–Shapiro relation/coset transports — PASS

**Date:** 2026-10-24. **Execution:** user-run IONOS Ubuntu (Sage shell). **Scope:** exact integer `Gamma0(389*16231)` membership and covariance coefficients, not full V19 producer recomputation.

## Versioned primary files

- `verification/export_shapiro_transport_stream.py`, converting the SHA-pinned original `historical/originals/bsd389_tame_relation_export_p16231.json` to an integer-only stream. Frozen export SHA-256: `9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8`.
- `verification/c01_all_shapiro_transports_noboost.cpp`, self-contained C++17 (no Boost and no Sage), checks exact 64-bit matrix products using 128-bit temporaries and rejects overflow, checks group membership and reduction to the native C01 mod-p matrix action.
- All exact cusp divisor identities in the independent Manin relation verifier were previously checked 390/390, 2,012 group lifts.

## Terminal record supplied by user

```text
ORIGINAL_EXPORT_SHA256_PASS 9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8
ORIGINAL_EXPORT_RELATIONS_PASS 390 2012
C01_SHAPIRO_TRANSPORT_PROGRESS processed_classes=10 total_transitions=20120
C01_SHAPIRO_TRANSPORT_PROGRESS processed_classes=11 total_transitions=22132
C01_ALL_COSETS_PILOT_PASS transitions=22132 exceptional_input=2012 exceptional_output=983 checksum=10101084879415674431
PILOT_EXIT_STATUS=0

ORIGINAL_EXPORT_SHA256_PASS 9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8
ORIGINAL_EXPORT_RELATIONS_PASS 390 2012
C01_SHAPIRO_TRANSPORT_PROGRESS processed_classes=10 total_transitions=20120
C01_SHAPIRO_TRANSPORT_PROGRESS processed_classes=4096 total_transitions=8241152
C01_SHAPIRO_TRANSPORT_PROGRESS processed_classes=8192 total_transitions=16482304
C01_SHAPIRO_TRANSPORT_PROGRESS processed_classes=12288 total_transitions=24723456
C01_SHAPIRO_TRANSPORT_PROGRESS processed_classes=16232 total_transitions=32658784
C01_ALL_32658784_SHAPIRO_TRANSPORTS_EXACT_PASS transitions=32658784 input_exceptional=2012 output_exceptional=2012 both_exceptional=983 checksum=13306773584111587599
FULL_EXIT_STATUS=0
```

A source comment warning `-Wcomment` was emitted during the C++17 compilation owing to a backslash continued `//` command example. The executable compiled and produced exit-zero PASS; the warning does not affect the arithmetic result. The earlier Boost-dependent verifier was not executed: this PASS belongs to the explicitly **no-Boost** version.

## What was checked exhaustively

For every one of 2,012 original relation terms `A in Gamma0(389)` and every Shapiro input class `j in P1(F_16231)`, including `j=inf`, form `X=r_j A^-1`. The original `qidx(X)` selects `j1`. Then

`h=X*r_j1^-1`

is checked over **exact integers** to have determinant one and `h.c=0 (mod 389*16231)`. The four entries of `h mod 16231` are checked against independently assembled mod-p matrix products in the same order as the native C01 program. The induced moment coefficients

`q(h)=-h.a*h.b`, `r(h)=h.a^2`,

and their nontrivial affine-composition law are checked. Projective keys, unique generator indices and the original relation target structure are checked. Overflow is rejected.

**All 32,658,784 transitions passed** with no detected discrepancy. The 2,012 exceptional inputs, 2,012 exceptional outputs and 983 exceptional-to-exceptional transitions were visited. The full deterministic output checksum is `13306773584111587599`.

## Logical distinction

This closes **implementation-level exhaustive verification of the finite Manin/Shapiro relation transitions and their two-moment mod-p covariance**. It does not compute elliptic-curve modular symbols, reproduce each 512-pair C01 chunk, prove the correctness of every eclib call, or by itself apply the global p-primary Kato upper bound.

Other audited pieces: 514,511 historical chunks-to-checkpoint recomposition, byte-identical V11 rebuild, 57/57 native replayed chunk-byte matches, 67/67 V23 and 67/67 V26 moment contractions, 254/254 V54 and 254/254 V61 level-2 archives, and the Sage 10.9 source-level analytic identity.

The arithmetic deduction `Sha(389a1/Q)[16231^infinity]=0` remains a **computer-assisted conditional conclusion** until the remaining producer/execution/normalization assumptions receive the required proof standard; it does **not** establish the full BSD conjecture or exact `u_16231=1`.
