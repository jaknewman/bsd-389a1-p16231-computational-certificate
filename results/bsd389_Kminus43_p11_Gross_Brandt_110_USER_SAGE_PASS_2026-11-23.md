# USER UBUNTU SAGE — 110/110 genuine Gross–Brandt classifications at p=11, K=Q(sqrt(-43))

**Date: November 23, 2026. Actual user-provided terminal output, not an assistant-generated simulation.**

Run from branch `research/bsd389-theta2-finite-depth-20261122`:
```bash
python -u verification/bsd389_Kminus43_p11_Gross_Brandt_110_sage.py --max-new 0
python -u verification/bsd389_Kminus43_p11_Gross_Brandt_110_independent_audit.py \
  ~/bsd389_Kminus43_p11_Gross_Brandt_110.json
```

## Exact completion gates

```text
REAL_BRANDT_PRIMITIVE_EIGENLINE_AND_MAXIMAL_ORDER_PASS
ACTUAL_BRANDT_ORDER_CONJUGATOR_PASS 18 -17/2 - 97/2*i - 7/2*j + k
RESTART_FROM_CHECKPOINT 2 status PARTIAL_110_GENUINE_BRANDT
ALL_110_GENUINE_GROSS_BRANDT_CLASSES_CERTIFIED
RAW_THETA_MOMENTS_MOD11 [0, 0, 3]
AUTHENTIC_THETA2_MOD11 6 UNIT True
BOUNDARY_NO_SEL_MER_GAMMA_ACTION_OR_FULL_BSD
```

Independent audit (exact reported keys):
```text
"status": "ALL_110_INDEPENDENT_MOMENTS_PASS"
"complete": true
"count": 110
"canonical_record_sha256": "273c9e80c7ce0e1ced0fed318d90f60e7b7f20fb5c674a0a433d104d8b3ccf95"
"grouped_weight_sums_mod11": [6,2,6,5,5,6,2,6,4,9,4]
"moments_mod11": [0,0,3]
"theta2_mod11_up_to_JL_unit": 6
"theta2_unit": true
```

## Full source trace: 110 Brandt class indices

These are transcribed from the user's `GENUINE_GROSS_BRANDT_VALUE_PASS k j(k) V[j(k)]` lines, in increasing order `k=0,...,109`:

```text
16,23,23,17,10,9,5,29,1,6,25,13,19,12,24,30,20,17,27,27,17,20,30,24,13,19,12,21,7,2,29,14,10,9,17,22,22,15,22,22,15,3,8,29,31,11,19,8,10,9,26,7,5,1,19,3,16,30,8,24,0,8,24,1,5,25,6,28,11,25,30,17,20,27,27,20,17,30,21,4,26,7,21,14,2,24,3,0,24,3,30,15,8,19,2,14,6,28,10,9,3,19,4,31,29,3,8,16,23,23
```

The **preexisting** primitive eigenvector (33 classes, from the separate authenticated Hecke eigenspace test) is:

```text
0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0
```

The complete sequence of actual Brandt values is `w_k=V[j(k)]`. This note contains the indices and vector, making the full 110 ordered integer weights independently recoverable **without** the local JSON. It does **not** reproduce the full Sage equivalence witnesses in the original JSON, whose SHA256 commitment is reported above. Those witnesses remain archived on the user's Ubuntu machine.

## Independent exact integer symmetry (new deduction from the completed transcript)

Define `W_i=sum_{0<=k<110; (k-4) mod 11=i} w_k` (no reduction mod 11). The reconstructed integer vector is

```text
W = [-5,2,6,-6,-6,6,2,-5,4,-2,4]
```

and its first three integral binomial moments are

```text
M0=0; M1=33; M2=157
```

The coefficients satisfy **exactly** `W_i=W_{-4-i mod 11}` for all `i=0,...,10`. Hence for `F(X)=sum_i W_i X^i` in `Z[X]/(X^11-1)`, we have the genuine **finite-level** reciprocity identity

```text
F(X^-1) = X^4 * F(X).
```

Multiplying by `X^2` produces an inversion-symmetric group-ring element `X^2 F(X)`. This is an independent orientation-consistency check. It is **not** the exact functional equation for the Iwasawa-limit theta (which still needs the source theorem and full normalization).

As `M2 mod 11 = 157 mod 11 = 3` and `-alpha_11^-2 = 2 mod 11` for `a11(E)=-4`,

```text
[T^2] theta_(E/K,11) = 2*3 = 6 mod 11 (up to a primitive JL unit).
```

This proves a **unit** quadratic coefficient for the authenticated finite theta. The published finite-to-infinite comparison transfers the quadratic unit to the actual p-adic theta, assuming the source-normalized ideal identification already proved in the companion note. Establishing exact order 2 further uses the exact constant-term vanishing and the published anticyclotomic functional equation.

## Boundaries

This result **does not show** `Sha(E/Q)[11^infinity]=0`, nor the global finiteness or exact archimedean leading coefficient of BSD. An independent arithmetic Selmer/Kurihara unit witness remains necessary to eliminate p11-primary Sha. The next efficient target is the admissible pair `q1=397, q2=991`, whose two-prime Kurihara sum has only 196713 half representatives.
