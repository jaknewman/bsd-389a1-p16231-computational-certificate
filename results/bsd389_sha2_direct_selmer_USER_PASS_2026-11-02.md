# E389a1: genuine SageMath 10.9 2-Selmer Sha[2∞] vanishing certificate

**Date:** 2026-11-02. **Provenance:** exact terminal output supplied by the user, rather than direct access to the bytes of the user's local log. The script itself is `verification/bsd389_sha2_direct_selmer_gate.sage`.

## User's Sage output

```text
SHA2_CURVE_PASS (0, 1, 1, -2, 0)
SHA2_RANK_PROVED 2
SHA2_TORSION_DIMENSION_UPPER_BOUND 0
SHA2_PRIMARY_ZERO_PASS
BOUNDARY_SHA_ALL_PRIMES_NOT_PROVED
PIPELINE_STATUS=0
```

Run command:

```bash
set -o pipefail
sage verification/bsd389_sha2_direct_selmer_gate.sage 2>&1 | tee ~/bsd389_sha2_direct_selmer.log
echo "PIPELINE_STATUS=$?"
```

## Mathematical conclusion

Sage proves the algebraic rank `E.rank(proof=True)=2` and `E.sha().two_selmer_bound()=0`. The upper bound 0 means the 2-torsion in the Tate–Shafarevich group is trivial. The 2-Selmer exact sequence is

`0 -> E(Q)/2E(Q) -> Sel_2(E/Q) -> Sha(E/Q)[2] -> 0`.

Therefore `Sha(E/Q)[2]=0`, and since any nonzero 2-primary torsion group contains an element of order 2, `Sha(E/Q)[2∞]=0`. This argument does not assume the whole Sha finite.

**Scope:** a genuinely executed independent proof-mode 2-Selmer certificate for p=2, not a uniform all-prime Sha result. Other user-executed Sage p-primary upper bounds are p=5,7,11,13,107. Published Heegner nonvanishing at p=3 is separately documented and not a user-executed quaternionic derivative replay.

**Log authentication:** this Markdown accurately transcribes the user's supplied stdout but is not a SHA256-pinned copy of the local Ubuntu log.
