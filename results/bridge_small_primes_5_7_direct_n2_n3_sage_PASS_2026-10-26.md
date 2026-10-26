# Direct finite-level n2/n3 C01–Sage analytic bridge, primes 5 and 7 — PASS

Date: 2026-10-26. Actual terminal output supplied by the user from their Sage-enabled IONOS Ubuntu environment while running `verification/bridge_local_small_prime_n2_n3_direct.py` with Sage 10.9. Both shell stages exited with 0 (`BRIDGE_STATUS=0 0`).

```text
BRIDGE_SMALL_PRIME_DATA 5 alpha 7 A2n2 14 A2n3 24 J 2 delta 10 expected 10
BRIDGE_SMALL_PRIME_N2_N3_CORRECTION_PASS 5
BRIDGE_SMALL_PRIME_N3_EQUALS_SAGE_SERIES_PASS 5
BRIDGE_SMALL_PRIME_DATA 7 alpha 16 A2n2 19 A2n3 33 J 4 delta 14 expected 14
BRIDGE_SMALL_PRIME_N2_N3_CORRECTION_PASS 7
BRIDGE_SMALL_PRIME_N3_EQUALS_SAGE_SERIES_PASS 7
BRIDGE_SMALL_PRIMES_5_7_DIRECT_ORACLE_PASS
BOUNDARY: small-prime test, not p16231 direct n3 execution.
BRIDGE_STATUS=0 0
```

All values A2n2, A2n3 and delta are taken modulo p²; J is modulo p. For p=5, alpha=7 mod 25, A2n3-A2n2=24-14=10 mod 25; p*J/(4*alpha²)=10 mod 25. For p=7, alpha=16 mod 49, A2n3-A2n2=33-19=14 mod 49 and p*J/(4*alpha²)=14 mod 49.

This standalone script computes exact n=2 and n=3 finite sums from Sage/eclib modular symbols, computes the independent scalar C01 reference J directly from M0/M1 and every small-prime (a,b) pair, and compares the directly enumerated level-3 T² coefficient with `E.padic_lseries(p, implementation='eclib').series(n=3,prec=3)[2]` when Sage's precision warrants it. Both direct Sage-series coefficient comparisons passed.

The tests verify the signs, Teichmuller lift conventions, 1/4 normalization, and the algebraic n2/n3 correction in two independently tractable instances. They do **not** prove the universal p=16231 identity or constitute full direct n3 Sage execution at that prime. Those conclusions still depend on a rigorous formal derivation from Sage's pinned source and the independently executed high-p level-2 and scalar J calculations.

Evidence: [small-prime script](../verification/bridge_local_small_prime_n2_n3_direct.py), [C01 to Sage algebraic bridge](../paper/c01_to_sage_quadratic_coefficient_identity_2026-10-24.md), [complete independent p16231 n2 result](independent_level2_u_full_131714565_residues_PASS_2026-10-26.md), [independent global C01 J](independent_scalar_J_global_263429130_pairs_PASS_2026-10-26.md).
