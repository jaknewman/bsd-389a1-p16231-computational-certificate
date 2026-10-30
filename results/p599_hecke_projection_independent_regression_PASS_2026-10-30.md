# p599 Hecke–Frobenius independent regression — user-executed PASS (2026-10-30)

## Provenance

The following terminal output was supplied directly by the user running Sage on Ubuntu after `git pull --ff-only origin main`, from GitHub commit `9ed19970e9a32ba6c29dbe97ee0805474036302b`. Script `verification/bsd389_p599_hecke_projection_regression.py`, with authentic Manin table stored outside Git. This record reports a **user execution**, not a GitHub Actions run.

```text
P599_ANALYTIC_BRIDGE_INDEPENDENT_REGRESSION_START
P599_ALL_390_MANIN_ENTRIES_SAGE_MATCH_PASS p 599 sha256 fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8
P599_ECLIB_NORMALIZATION_PASS real_components 2
P5_HECKE_EXACT_ALL_FIBRES_PASS 20
P5_A3_MODP_ZERO_B3_OVER_P_MATCH_C2_PASS
P5_SUPERSINGULAR_FULL_DP_VS_P2_SHORTCUT_PASS p 5 real_components 1 C2 1 derived_F0 1 direct_Dp_F0 1
BOUNDARY: this p5 regression is independent convention testing, not a direct p599 analytic computation
P599_ANALYTIC_BRIDGE_INDEPENDENT_REGRESSION_FINISHED
```

## Scope and mathematical relevance

1. Every one of the **390** genuine `p=599` normalized Manin-table residues agrees with Sage 10.9's actual `E.padic_lseries(599)._modular_symbol`, including `S(0)`. Thus conductor-`599²` finite moments are in the **correct analytic symbol normalization**, not merely a congruent or arbitrarily scaled symbol.
2. At `p=5` for `1483a1`, the exact Hecke identity was tested on **20** fibres; the lift moment identities were checked; Sage directly computed `Dp_valued_series(n=3,prec=3)` and its first quadratic coefficient equals the p² Hecke prediction, both 1 mod5. This validates conventions and matrix projection in a small end-to-end case.
3. This p5 test is **not** a direct p599 level-`p³` evaluation. At p599 the analytic coefficient is determined algebraically using exact Hecke and lift identities plus Sage 10.9's proven alpha-adic precision bound, as shown in [the proof](../paper/bsd389_p599_hecke_frobenius_precise_lemma_2026-10-30.md).
4. The resulting `p599` leading coefficient first coordinate `571 mod599` has valuation zero, while the normalized regulator first coordinate is also `571 mod599` (user-computed via Sage with proven full Mordell–Weil generators). The corresponding bound by Stein–Wuthrich Algorithm 11.1 is `b599=0` **if the exact algebraic derivation and computational prerequisites are accepted**. The Sage call `p_primary_bound(599)` itself was **not** completed.

The distinct status of `Sha[599^infinity]` and next peer-review steps appear in `STATUS.md` and [issue #4](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/4).
