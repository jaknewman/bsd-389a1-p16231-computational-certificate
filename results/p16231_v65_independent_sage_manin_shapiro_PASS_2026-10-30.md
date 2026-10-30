# p=16231 — independent Sage V65/Manin/Hecke/Shapiro oracle PASS (2026-10-30)

**Provenance:** exact user-supplied Sage/Ubuntu terminal output. Script `verification/bsd389_p16231_v65_direct_sage_oracle.py` was run after the source was published to GitHub (the user previously fast-forwarded and invoked the matching script). The transcript is **user-executed**, not a fresh GitHub Actions run. Its checks explicitly require authentic SHA256-pinned local files:

- 390-Manin original relation export: `9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8`.
- V65 independent eclib beta table: `aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c`.

## Original successful stdout

```text
P16231_V65_ORIGINAL_SHAPIRO_SHA256_PASS 9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8
P16231_V65_BINARY_TABLE_SHA256_PASS aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c
P16231_ALL_16232_EXACT_SHAPIRO_P_BETA_FACTORIZATIONS_PASS infinity 1
P16231_V65_ORACLE_PROGRESS 10 / 67
P16231_V65_ORACLE_PROGRESS 20 / 67
P16231_V65_ORACLE_PROGRESS 30 / 67
P16231_V65_ORACLE_PROGRESS 40 / 67
P16231_V65_ORACLE_PROGRESS 50 / 67
P16231_V65_ORACLE_PROGRESS 60 / 67
P16231_V65_ORACLE_PROGRESS 67 / 67
P16231_V65_ALL_67_COMPLETE_HECKE_FIBRES_PASS entries 1087477
P16231_V65_INDEPENDENT_SAGE_FG_FP_PASS checks 134 oracle sage
P16231_V65_INDEPENDENT_SAGE_BETA_SAMPLES_PASS checks 536
P16231_V65_INDEPENDENT_SAGE_SHAPIRO_M0_PASS checks 335 infinity_representatives 67
P16231_V65_SHARED_MANIN_ORACLE_AUDIT_PASS
BOUNDARY This independently checks shared V65 table provenance, all Hecke sums and sampled true Sage cusps; it does not recompute J=4486 or the full n3 analytic series.
```

## Exactly what this certifies

1. Exact SHA256 identity of both shared inputs; the V65 binary table is the same numerical oracle for the V19 source contraction and the independently completed 263,429,130-pair J engine.
2. **16,232 / 16,232** integer matrix factorizations `P*r_j=H_j*beta_s` checked (including the exceptional infinity class) with determinant-one and exact `Gamma_0(389)` membership assertions.
3. All **67** 16,231-element stored Hecke-fibre sums: `67 * 16231 = 1,087,477` table entries inspected, with `f_P + sum_t f_t = 128 f_G (mod 16231)` for every generator.
4. Independently regenerated from the alternative Sage modular symbol implementation (`implementation='sage'`, not eclib): all **134** `F(G), F(PG)` anchor values; **536** strategically distributed `F(beta_t G)` entries; and **335** `M0(r_j G)` transport comparisons from direct Sage cusp values, including **all 67 exceptional infinity cosets**.

The entire full 1,087,477-entry V65 binary table was **not** regenerated independently using Sage; only its Hecke sums plus 536 independent direct beta samples were tested. Neither of the two historical 263m-pair global J summations was rerun; previous distinct engines both produced `J=4486 (mod16231)`, and direct high-p n=3 oracles tested six adversarial pairs. The source-level global `J_ref=J` identity is a mathematical proof given the Manin/Shapiro and numeric/source inputs, **not** a consequence of these finite samples alone.

## Relevance to p-primary Sha claim

Prior user-executed historical certificates give `A2(n2)/p=1199`, `J=4486`, exact universal correction `J/(4*alpha^2)=8335 mod16231`, derived `A2(n3)/p=9534`, and Sage normalized regulator BSD factor `B_p/p=9534 (mod16231)`. For the good **ordinary** prime 16231, Stein–Wuthrich's ordinary Kato upper-bound theorem uses the corresponding normalized `Reg_gamma`. Thus the inferred valuation of the leading-term quotient is zero **conditional on faithful source-computation identification and the authentic historical inputs**. This new independent Sage oracle substantially narrows the remaining shared-oracle trust surface but does **not** independently execute the full level-3 L-series, prove the compiled binary is correct, nor justify unconditional all-prime BSD or the exact equality `u_p=1`.

See [source-level proof cut](../paper/bsd389_p16231_v65_sage_oracle_and_proof_cut_2026-10-30.md) and [tracking issue #7](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/7).
