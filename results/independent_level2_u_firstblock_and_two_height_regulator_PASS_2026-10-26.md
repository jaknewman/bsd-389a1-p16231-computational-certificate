# Two-algorithm regulator and independently u-indexed level-2 first-block PASS

**Date:** 2026-10-26. **Source:** user-supplied output from Sage-enabled Ubuntu on IONOS executing the new source programs:
- `verification/independent_p16231_regulator_two_height_algorithms.py`
- `verification/independent_p16231_level2_u_enumeration.py` (`pilot`, then `first-block`)

All three separately reported Bash process-status pairs were `0 0`.

## A. Two-regulator-algorithm independent comparison: PASS

```text
REGULATOR_BASIS_RANK2_PASS [(-1 : 1 : 1), (0 : -1 : 1)]
INDEPENDENT_REGULATOR_ALGORITHM_START prec 6 p 16231
HEIGHT_PARALLELOGRAM_SIGMA_PASS
HEIGHT_DET_VALUATION_SIGMA_PASS
HEIGHT_DETERMINANT_SIGMA_PASS Reg/p^3 mod p=1930
HEIGHT_ALGORITHM_TIME SIGMA 0.005 hP 1110940370413608664483 hQ 1095456689318842067897 hPplusQ 963506238419233012296 hPminusQ 69825289334425762011 off 505042119913805370109 det_mod_p5 142354745479287053001
HEIGHT_PARALLELOGRAM_MULTIPLY_PASS
HEIGHT_DET_VALUATION_MULTIPLY_PASS
HEIGHT_DETERMINANT_MULTIPLY_PASS Reg/p^3 mod p=1930
HEIGHT_ALGORITHM_TIME MULTIPLY 0.008 hP 1110940370413608664483 hQ 1095456689318842067897 hPplusQ 963506238419233012296 hPminusQ 69825289334425762011 off 505042119913805370109 det_mod_p5 142354745479287053001
INDEPENDENT_HEIGHT_VALUES_AGREE_MODP5_PASS
INDEPENDENT_REGULATOR_ALGORITHMS_AGREE_MODP5_PASS
INDEPENDENT_REGULATOR_B_FACTOR_VALUATION_PASS 1
INDEPENDENT_REGULATOR_B_OVER_P_9534_PASS B/p mod p=9534
BSD389_REGULATOR_ALTERNATE_HEIGHT_METHODS_PASS
REGULATOR_STATUS=0 0
```

All four independently evaluated height values agree mod p^5 in Sage's sigma- and multiplication-based height implementations. The induced polarized rank-2 determinants coincide mod p^5 and have p-adic valuation 3; their first nonzero digit is 1930. The Sage 10.9 BSD regulator factor satisfies `B_p/p=9534 mod p` with valuation `v_p(B_p)=1`.

**Independence boundary:** the algorithms are different Sage implementations of the cyclotomic p-adic height; they share Sage's elliptic curve/p-adic arithmetic, and do not evaluate the analytic L-series.

## B. Independent cyclotomic exponent u-index level-2 computation: pilots PASS

The new algorithm uses `x=omega(a)*(1+p*u) mod p^2` with `omega(a)=a^p mod p^2`, enumerating `u=2,...,p-1`, rather than V61's `x=a+p*b` with separately calculated Fermat quotient u.

```text
INDEPENDENT_U_A_CHECKPOINT_PASS 1 raw_mod_p2 222016103
INDEPENDENT_U_PROGRESS 1 / 1 raw_f2 222016103 f1 263445360
INDEPENDENT_U_ONE_A_PILOT_PASS a=1 raw_f2_mod_p2 222016103
LEVEL2_PILOT_STATUS=0 0
INDEPENDENT_U_A_CHECKPOINT_REUSED_PASS 1
INDEPENDENT_U_PROGRESS 32 / 32 raw_f2 120601021 f1 0
INDEPENDENT_U_FIRST_BLOCK_V61_AGREEMENT_PASS 120601021 0 pairs 519392
INDEPENDENT_U_FIRST_32_A_COMPLETE_PASS 519392
LEVEL2_BLOCK_STATUS=0 0
```

The first 32 lines covered exactly `32*16231=519392` indexed residues; `32*(16231-2)=519328` actual eclib evaluations of the nonzero `binom(u,2)` terms. The independently recomputed raw n=2 partial sum is `120601021 mod p^2`, identical to the archived first V61 block, and lower first moment sum is zero for this block. Per-a checkpoint files are individually checksummed and can be resumed.

**Strict boundary:** only the first 32 out of 8115 a-values have been independently reproduced with this new code. The whole `8115*16231=131714565` half-domain has **NOT YET** been recomputed by the new algorithm, and `A2^(2)=1199p` must not be marked as independently reverified at full level by this code until its `all` mode actually passes. The historic V61 full n=2 block recomposition (254/254) remains separately PASS.

This report records user-provided actual terminal output, not a fresh execution by the assistant.
