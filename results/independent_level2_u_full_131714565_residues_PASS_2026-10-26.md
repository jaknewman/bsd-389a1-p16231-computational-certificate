# Full independent cyclotomic-u level-2 coefficient — 8,115/8,115 rows PASS

Date: 2026-10-26. Source: user-reported terminal of the independently implemented `verification/independent_p16231_level2_u_enumeration.py all` in Sage-enabled Ubuntu; the execution finished, and the pipeline status was `0 0`.

## Authentic terminal ending

```text
INDEPENDENT_U_PROGRESS 8115 / 8115 raw_f2 79629286 f1 0 elapsed_min 56.53
INDEPENDENT_U_FIRST_BLOCK_V61_AGREEMENT_PASS 120601021 0 pairs 519392
INDEPENDENT_U_FULL_A2_LEVEL2_MODP2 19460969
INDEPENDENT_U_FULL_A2_LEVEL2_OVER_P 1199
INDEPENDENT_U_FULL_LEVEL2_1199P_PASS terms 131714565
BOUNDARY: independent cyclotomic u-indexing and original Sage/eclib modular symbol implementation; not a different elliptic modular-symbol oracle.
LEVEL2_FULL_STATUS=0 0
```

The new computation covers all 8,115 positive representatives of the plus-symmetry half-domain, each with 16,231 cyclotomic residues, or 131,714,565 indexed residues. In each row, `u=0,1` have binomial weight zero, so 16,229 nonzero-weight eclib terms per `a`; 131,698,335 such calls total. Each row's result is stored in independently checksummed `~/bsd389_independent_level2_u/a_XXXXX.json` for crash recovery. This was **not** a simple recomposition of the V61 archived chunk values: the new engine calls Sage/eclib again using the independent cyclotomic-u parametrization.

## Method and verified value

V61 loops over `x=a+p*b` and computes `u` by a Fermat quotient; the second complete implementation loops directly over u and constructs `x=omega(a)*(1+p*u) mod p^2`, where `omega(a)=a^p mod p^2`. It directly computes the weighted sum `R2=sum binom(u,2)*m(x/p^2) mod p²` and the lower `R1=sum m(a/p) mod p²` from Sage/eclib's common `L_ratio` modular symbol.

At `p=16231`, `p²=263445361`, the newly computed full sums are:

- `R2 = 79629286 mod p²`;
- `R1 = 0 mod p²`;
- `A2^(2) = 19460969 = 1199*p mod p²`.

The independently recomputed first 32-row block, `R2=120601021, R1=0`, also agrees with old V61. The complete independent **global level-2 coefficient** now matches the archived V61 result, while reusing Sage/eclib as a common modular-symbol oracle.

## Strict proof and provenance boundary

This is a second **complete numerical recomputation** of `A2^(2)` with a mathematically equivalent but different cyclotomic indexing, not a new independent implementation of the eclib plus modular symbols or of Sage's normalization. Per-a output files and complete log are still awaiting a separate post-run row-by-row evidence audit; the user supplied the terminal ending and zero exit-status pair. The analytic level-3 coefficient is still inferred from the separately established universal C01/Sage correction and twice fully reproduced `J=4486`; `lp.series(n=3)` and `E.sha().p_primary_bound(16231)` have not been directly executed. No exact p-adic equality `u_p=1` or all-prime BSD claim.

Related: [independent u engine](../verification/independent_p16231_level2_u_enumeration.py), [two-algorithm regulator and 32-row pilot](independent_level2_u_firstblock_and_two_height_regulator_PASS_2026-10-26.md), [independent complete scalar J](independent_scalar_J_global_263429130_pairs_PASS_2026-10-26.md).
