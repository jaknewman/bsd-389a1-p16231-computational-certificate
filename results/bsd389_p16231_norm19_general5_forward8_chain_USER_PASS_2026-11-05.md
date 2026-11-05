# USER PASS: norm19 oriented Gross-point strict identities for five anchors and eight-step chain

Date: 2026-11-05. This is the genuine stdout posted by the user after executing the Sage script [verification/bsd389_p16231_P2_norm19_general_a_and_chain.py](../verification/bsd389_p16231_P2_norm19_general_a_and_chain.py) with `--steps 8`, `set -o pipefail` and `timeout 240s`.

Decisive verbatim output:

```text
P2_NORM19_GENERAL_ANCHOR_BOTH_STRICT_IDENTITIES_PASS A 16232 CLASS 15 VALUE -1 FORWARD_CLASS 16 FORWARD_VALUE -1 INVERSE_CLASS 30 INVERSE_VALUE -2
P2_NORM19_GENERAL_ANCHOR_BOTH_STRICT_IDENTITIES_PASS A 32463 CLASS 21 VALUE 1 FORWARD_CLASS 1 FORWARD_VALUE 0 INVERSE_CLASS 5 INVERSE_VALUE 1
P2_NORM19_GENERAL_ANCHOR_BOTH_STRICT_IDENTITIES_PASS A 164371339 CLASS 13 VALUE 0 FORWARD_CLASS 29 FORWARD_VALUE -2 INVERSE_CLASS 24 INVERSE_VALUE 0
P2_NORM19_GENERAL_ANCHOR_BOTH_STRICT_IDENTITIES_PASS A 121898074 CLASS 24 VALUE 0 FORWARD_CLASS 27 FORWARD_VALUE -2 INVERSE_CLASS 27 INVERSE_VALUE -2
P2_NORM19_GENERAL_ANCHOR_BOTH_STRICT_IDENTITIES_PASS A 138112843 CLASS 2 VALUE 0 FORWARD_CLASS 1 FORWARD_VALUE 0 INVERSE_CLASS 9 INVERSE_VALUE -1
P2_NORM19_NONTRIVIAL_ANCHORS_PASS 5
P2_NORM19_ITERATED_GROSS_P2_CHAIN_PASS STEP 1 A 138112843 CLASS 2 VALUE 0
P2_NORM19_ITERATED_GROSS_P2_CHAIN_PASS STEP 2 A 79960066 CLASS 1 VALUE 0
P2_NORM19_ITERATED_GROSS_P2_CHAIN_PASS STEP 3 A 5238644 CLASS 21 VALUE 1
P2_NORM19_ITERATED_GROSS_P2_CHAIN_PASS STEP 4 A 47862741 CLASS 9 VALUE -1
P2_NORM19_ITERATED_GROSS_P2_CHAIN_PASS STEP 5 A 244320089 CLASS 1 VALUE 0
P2_NORM19_ITERATED_GROSS_P2_CHAIN_PASS STEP 6 A 24258005 CLASS 26 VALUE 1
P2_NORM19_ITERATED_GROSS_P2_CHAIN_PASS STEP 7 A 157959288 CLASS 3 VALUE 1
P2_NORM19_ITERATED_GROSS_P2_CHAIN_PASS STEP 8 A 150385381 CLASS 12 VALUE 0
P2_NORM19_ITERATED_CHAIN_COMPLETE_PASS 8
P2_NORM19_GENERAL_A_AND_CHAIN_AUDIT_PASS SECONDS 0.834
BOUNDARY_PILOT_ANCHORS_NOT_FULL_87809710_ORBIT
BOUNDARY_NO_GLOBAL_THETA_C2_OR_SHA_PROOF
NORM19_CHAIN_STATUS=0
```

## Scope

For five nontrivial unit parameters a, **both** strict equality of global rational right ideals with their direct Gross targets T(w*a), T(w^-1*a) passed. Independent class/value coordinates are given for every source and both target directions. A forward-only eight-step iteration from T(1) then passed strict equality against independently rebuilt T(w^n) for all n=1..8, and reported the displayed actual 33-class Brandt labels and eigenvector values.

This establishes a meaningful multi-anchor and finite-orbit test of the universal formula, not merely a local modular identity or 33-class coincidence. The general all-a identity was derived separately in [paper/bsd389_p16231_norm19_universal_Gross_transport_identity_local_global_proof_2026-11-05.md](../paper/bsd389_p16231_norm19_universal_Gross_transport_identity_local_global_proof_2026-11-05.md).

The unnormalized quaternionic right ideals can have growing coefficients on further iterations. The next [Brandt-normalized oriented CM state pilot](../verification/bsd389_p16231_P2_norm19_reduced_oriented_chain_moment_pilot.py) returns each ideal to one of the fixed 33 Brandt representatives and transports q by the exact quaternion equivalence witness, thereby keeping the embedding norm fixed and allowing class/value accumulation. New pilot source is committed but **NOT YET USER-RUN**. No global theta c2 or Sha/ BSD conclusion follows.
