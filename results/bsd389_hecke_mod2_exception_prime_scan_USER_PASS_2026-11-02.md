# Genuine user-run mod-2 prime-Hecke scan: rank 31 persists through 61 (2026-11-02)

**Provenance:** exact pasted Ubuntu/Sage terminal stdout from the user. The original Smith JSON was authenticated by SHA256; all 18 tested prime integral Hecke operators used the same 33-dimensional signed integral lattice and same primitive E eigenvector. This is user-run evidence, not CI, and it does NOT calculate actual `Sha`.

Source: [`verification/bsd389_hecke_mod2_exception_targeted_scan.py`](../verification/bsd389_hecke_mod2_exception_targeted_scan.py).

```text
HECKE_MOD2_ORIGINAL_USER_SMITH_SHA256_PASS 86e79229d1c60d38ec59ecd8776c0c471716a1ffdf1098d46d58a8a59253f02a
HECKE_MOD2_STURM_BOUND_CONTEXT 65 cuspidal_forms_not_automatic_full_mod2_base_change
HECKE_MOD2_PRIME_EIGENRANK ell 2 ap -2 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 3 ap -2 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 5 ap -3 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 7 ap -5 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 11 ap -4 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 13 ap -3 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 17 ap -6 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 19 ap 5 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 23 ap -4 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 29 ap -6 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 31 ap 4 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 37 ap -8 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 41 ap -3 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 43 ap 12 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 47 ap -2 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 53 ap -6 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 59 ap 3 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_PRIME_EIGENRANK ell 61 ap -8 rank 31 kernel_dim 2 exact_Smith_gcd_deduced 2
HECKE_MOD2_EXTRA_EIGENVECTOR_PERSISTS_WITH_TESTED_PRIMES largest_checked_prime 61
HECKE_MOD2_SCAN_EXACT_GLOBAL_SMITH_GCD_FROM_F2_RANK 2
HECKE_MOD2_SCAN_CANONICAL_JSON_SHA256 0e24d302d61882689fe6084e9ed7302ddc0b483096744dc047c7e6a523970cf5
HECKE_MOD2_SCAN_REPORT /home/bsdadmin/bsd389_hecke_mod2_exception_scan.json
BOUNDARY_HEKKE_CONGRUENCE_ONLY_NOT_SHA_FITTING_OR_BSD
```

**Verified:** the 2-dimensional common eigenspace modulo 2 survives all 18 good prime Hecke operators with prime index ≤61. Exact determinant gcd of all maximal minors of each growing integral stack stays **2**, by divisor monotonicity from the previously certified Smith gcd2 and the verified mod-2 rank31. The report exists at `~/bsd389_hecke_mod2_exception_scan.json` on the user's Ubuntu host and is pinned to the digest above; it has **not** been uploaded.

**New theorem-based further deduction (without extra user code):** the Hecke coprime multiplicativity and prime-power recurrence at weight2 imply that **every** composite operator `T_n` with n≤65 is polynomial in the 18 tested prime operators. Because all those operators have the prescribed E eigenvalues on the common 2-dimensional F2 kernel, the 2-dimensional common kernel survives **every T_n for 1≤n≤65**, with no further computation. The Sturm bound 65 rigorously governs the *cuspidal* Hecke algebra but does NOT, on its own, prove a completeness theorem for this whole rank33 signed integral modular-symbol lattice, which has an Eisenstein component; Sage's `hecke_bound()` documentation explicitly cautions that its noncuspidal bounds can be unproven guesses. [Detailed proof and scope](../paper/bsd389_hecke_mod2_persistence_through_sturm_window_2026-11-02.md).

**No BSD implication:** The extra mod2 eigenvector is a congruence phenomenon in a particular integral Hecke lattice; it is **not** a new element of `Sha[2]`, and cannot imply `Sha` finiteness or strong BSD. The relevant global Sha bound still requires an arithmetic Euler/Kolyvagin/Selmer Fitting comparison or other independent uniform input.
