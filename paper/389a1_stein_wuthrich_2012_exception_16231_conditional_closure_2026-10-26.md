# 389a1: closing the exact Stein–Wuthrich 2012 ordinary-prime exception (conditional on our finite-input certificate)

**Date:** 2026-10-26. **Status:** a newly recognized combination of a published theorem with our extensive, but still **source- and normalization-conditional**, user-executed computational certificate. Do **not** describe this as peer-reviewed new proof or an unconditional all-prime BSD theorem.

## Primary published theorem (rigorously sourced)

William Stein and Christian Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, **Mathematics of Computation 82 (2013), 1757–1792**, electronically published 2012-09-14, **Theorem 12.3**, page 1788:

- For curve 389a1 of rank two, they proved `Sha(E/Q)[p]=0` for **p=2** and the **5,005 good ordinary primes p<48,859 other than p=16,231**.
- The relevant finite-level p-adic BSD conjectural order was `1 mod p` for their cases.
- They excluded the bad reduction prime p=389, a list of supersingular odd primes, and the one ordinary exception **p=16,231**.
- **Remark 12.4** explicitly states that `ord_16231(Reg_16231)=3`, instead of ordinary expected rank-two valuation 2; their earlier implementation would be roughly 16,231 times costlier, taking years of CPU time, and they proposed using Pollack–Stevens overconvergent modular symbols for the exception.

Peer-reviewed source: https://wstein.org/papers/mcom2649-iwasawa-alg.pdf — theorem/remark on printed page **1788** (PDF page 32, zero-index page 31). Accessible slide summary: https://www.wstein.org/talks/2013-jmm-pbsd/ .

## What our 2026 computation contributes

Our complete user-run C01/Shapiro project independently recovers `J=4486 mod 16231` using two entire 263,429,130-pair algorithms, independently recomputes `A_2^(2)=1199p mod p²` with two entire 131,714,565-residue algorithms, and verifies `Reg_p/p³=1930 mod p` through two different Sage height methods. The direct source-derived correction
`A_2^(3)-A_2^(2)=p*J/(4*alpha²) mod p²`
gives `A_2^(3)/p=9534 mod p`, matching the independent normalized regulator BSD factor `B_p/p=9534 mod p`. The quotient is thus a p-adic unit; by the Kato/Stein–Wuthrich upper-bound method, the 16231-primary Sha component is trivial **provided** the algebraic source-to-reference and common normalized Sage/eclib input gates are faithful.

Evidence beyond computational agreement:
- 8,115/8,115 independently computed n=2 cyclotomic-u checkpoint records, with exact comparison to 254/254 V61 archived chunks;
- 264 full global J checkpoints, 7 pinned frozen SHA-256 source/data/execution artifacts and complete output provenance;
- all 390/390 exact rational Manin cusp-divisor relations, comprising 2,012 transport relation terms;
- direct n=3 finite-level Sage verification at p=5 and p=7;
- six independent direct high-p Sage/eclib level-3 weighted-moment evaluations that exactly agree with frozen C++ pair contributions, including inner and outer infinity Shapiro transitions at id=38 and id=67.

All project findings are archived as user-executed evidence. **The direct full native Sage `lp.series(n=3,prec=3)` and `E.sha().p_primary_bound(16231)` have not been run.** This is a narrowly stated computer-assisted, proof-source-dependent supplement to Stein–Wuthrich's proven finite-range theorem.

## New finite-range corollary, with exact exclusions

**Conditional corollary.** Assume all source-level algebra, Sage normalizations, p-adic precision, global finite computations, and Kato/Sage hypotheses required for the previously stated **p=16,231** computer-assisted certificate are correct. Combining that one extra case with published Stein–Wuthrich Theorem 12.3 proves

`Sha(389a1/Q)[p^infinity]=0`

for **p=2** and **every good ordinary prime p<48,859**.

Since nontrivial p-primary torsion must contain an element killed by p, published conclusions `Sha[p]=0` immediately imply `Sha[p^infinity]=0` without assuming finiteness of the full Sha.

The only prime numbers **strictly below 48,859** not included are the bad prime **389** and the **16 supersingular odd primes**:

`107, 599, 1049, 2957, 6661, 8263, 9397, 9551, 14633, 15101, 28591, 30671, 30869, 31799, 34781, 36263, 45161`.

**Correction while transcribing the list:** count the original published list carefully: it contains **17 supersingular odd primes**, not 16. The set above has 17 values. Together with bad p=389, there are **18 unresolved primes** below 48,859. The displayed list is the exact list in Theorem 12.3 after removing ordinary p=16,231; do not use the earlier mistaken count of 16. The theorem's prime count should be recomputed before publishing a numeric total of fully covered primes.

This covers a large **bounded** interval of primes, not a uniform theorem for all primes and not the complete BSD conjecture. It uses a published theorem for all old cases plus one **conditionally certified** new case, and does not require any new 5,005-prime run.

## Mathematical obstacle beyond this bounded range

The local Skinner–Urban ramification hypothesis is uniform because `v_389(q_E)=1`, but it does **not** force the `p`-adic analytic quotient to be a unit for every p. No fixed nonzero integer bounding every p-primary Sha component has been deduced from the existing Hecke/Shapiro identities; obtaining one would require a new uniform Euler-system/height or Selmer-theoretic argument. The unresolved supersingular primes need different p-adic control, and infinitely many primes lie beyond the published bound.

## References

- [Our minimal prime-primary conditional theorem](p16231_minimal_prime_primary_sha_certificate_2026-10-26.md)
- [Our full direct n2 and J computations](../results/independent_level2_u_full_131714565_residues_PASS_2026-10-26.md)
- [Our exact high-p exceptional Shapiro oracles](../results/c01_shapiro_exact_and_adversarial_high_p_sage_PASS_2026-10-26.md)
- W. Stein & C. Wuthrich, Theorem 12.3 and Remark 12.4: https://wstein.org/papers/mcom2649-iwasawa-alg.pdf
