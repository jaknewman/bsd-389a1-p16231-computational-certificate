# p107: two independent user runs — Sage p² shortcut and frozen Kurihara archive (2026-10-30)

**Provenance:** The following outputs are reproduced verbatim from the user's Ubuntu Sage terminal after synchronization of the corresponding scripts to GitHub. This is **user-reported execution**, not a new GitHub Actions run. The p² shortcut is an actual newly executed computation; the Kim bridge verifies a frozen **archive hash and fresh two-prime finite-field counts** and uses the historical delta hardcoded from the earlier independently audited 710-block computation.

## Run 1 — genuinely executed Sage conductor-107² quadratic moment and regulator

```text
P107_SUPERSINGULAR_P2_START
P107_CONFIG p 107 modulus 11449 pairs 5671 a_p 0 real_components 2
P107_P2_PROGRESS 1000 / 5671
P107_P2_PROGRESS 2000 / 5671
P107_P2_PROGRESS 3000 / 5671
P107_P2_PROGRESS 4000 / 5671
P107_P2_PROGRESS 5000 / 5671
P107_ALL_HECKE_P2_FIBRES_PASS 106
P107_CYCLOTOMIC_P2_MOMENTS_PASS C0 0 C1 0 C2 86
P107_ANALYTIC_QUADRATIC_F0_DERIVED_MODP 43
P107_RANK2_SURJECTIVITY_TAMAGAWA_PASS generators [(-1 : 1 : 1), (0 : -1 : 1)] surjective True
P107_NORMALIZED_REGULATOR_VALUATIONS [0, 1]
P107_NORMALIZED_REGULATOR_0_RESIDUE 43
P107_STEIN_WUTHRICH_BOUND_ZERO_DERIVED analytic_val 0 regulator_val 0
P107_SHA_ZERO_CONDITIONAL_ON_PROVEN_HECKE_AND_KATO_BRIDGE
P107_SUPERSINGULAR_P2_FINISHED
```

Observed: `C0=0,C1=0,C2=86` (mod107), 5,671 sign pairs, 106 exact Hecke checks, `F0,2=43 mod107` **derived from a Hecke/Frobenius formula**, normalized regulator vector valuations `[0,1]` with residue `43` on coordinate zero, rank two and residual representation surjective. This is not a direct `Dp_valued_series(3)` call or a completed `p_primary_bound(107)` call. The formula/normalization must be considered separately from the **direct Kurihara–Kim proof route**.

## Run 2 — pinned 710-block archive and independently recomputed auxiliary-prime Frobenius traces

```text
BSD389_P107_AUXILIARY_PRIMES_INDEPENDENT_POINTCOUNT_PASS 369793 A_Q1 2 383917 A_Q2 -854
BSD389_P107_KURIHARA_ADMISSIBILITY_PASS p 107 n 141969819181 nu(n) 2
BSD389_P107_ARCHIVED_WITNESS_VALUE 34 mod 107
BSD389_P107_FULL_710_BLOCK_ARCHIVE_SHA256_MATCH_PASS b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754
KIM_THEOREM_1_8_HYPOTHESES_EXTERNAL: rank=2, residual surjectivity, p-integral/Manin-normalized modular symbols must be the already audited Sage assertions
KIM_THEOREM_1_8_CORANK_LE_2_FROM_DELTA_NONZERO
KUMMER_MORDELL_WEIL_RANK_GE_2
KIM_THEOREM_1_8_SELMER_CORANK_EQUALS_2
KIM_THEOREM_1_8_PART3_NON_DIVISIBLE_LENGTH_ZERO
SHA_107_PRIMARY_TRIVIAL_CONDITIONAL_ON_CERTIFIED_INPUTS_AND_THEOREM_PASS
BSD389_P107_KIM_BRIDGE_JSON /home/bsdadmin/bsd389_kim_kurihara_sha107_bridge.json
```

The script **does not re-extract the archive's 710 JSON payloads or recompute `delta=34`**. It hashes the complete tar.gz and checks that its SHA matches the previously certified, immutable run. `DELTA=34` is pinned in the script, not an independently computed value on this run. An earlier `verification/kurihara_k107_final_audit.py` was reported to have verified the 710 payloads, their dot products, the aggregate W390 vector, the coverage, `half=17` and `delta=34`; see the historical reports. This distinction matters for reproducibility.

## Theorem status

Kim, [*The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*](https://arxiv.org/pdf/2203.12159), **Theorem 1.8 (1),(3)**, without assuming finiteness of Sha, gives Selmer corank `rho=2` and nondivisible quotient length `0` once the genuine p-integral Néron-normalized `delta_n=34` at two auxiliary primes is authenticated, residual surjectivity and p-unit Manin constant verified. Combined with certified rank two and the Kummer exact sequence, this forces `Sha(E/Q)[107^infinity]=0`. No conjectural BSD or automatic consequence from a SHA alone.

**Important additional review boundary:** Stein–Wuthrich (2013) §4.4 and Conjecture 5.2 express the *T*-series normalizations in terms of `Reg_gamma = Reg_p/log(gamma)^r`, whereas the printed supersingular step (4) of Algorithm 11.1 writes `Reg_p`. Since p107 and p599 regulator outputs are explicitly normalized by `log(1+p)^2`, reconcile this factor with source conventions before independently promoting the new p² analytic route to a second theorem-level proof. The Kurihara–Kim route is mathematically independent of this discrepancy.
