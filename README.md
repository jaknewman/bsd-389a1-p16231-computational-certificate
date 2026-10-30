# Computational certificate for elliptic curve 389a1 at p = 16231

**Status: research-stage, independently corroborated numerical evidence; final certification in progress.**

This repository organizes the computational evidence and mathematical comparison needed to study the 16231-primary part of the Tate–Shafarevich group of the elliptic curve

\[
E/\mathbb Q:\quad y^2+y=x^3+x^2-2x,\qquad p=16231.
\]

**Do not cite this repository as an unconditional proof of BSD or of** `Sha(E/Q)[16231^infinity] = 0` **until the outstanding verification obligations are discharged and reviewed.** A first-digit congruence does not prove an exact p-adic equality or full BSD.

## p=107 — archived two-prime Kurihara witness and Kim criterion (2026-10-30)

The historical 710-block exhaustive computation reports `delta_(369793*383917)=34 (mod 107)`. The precise application of **Chan-Ho Kim's Theorem 1.8** shows that an authentic normalized **unit two-prime witness**, combined with certified Mordell–Weil rank 2 and residual surjectivity, forces the finite Selmer quotient to vanish and hence `Sha(389a1/Q)[107^infinity]=0` **without assuming Sha finiteness**. This conclusion remains conditional on the published archive and normalization being authenticated and reviewed: do not confuse the old user-reported full computation with a fresh source replay.

A new conductor-`107²` alternative uses **only 5,671 plus-symmetric modular symbols** (instead of `107³`-level enumeration or a 71-billion-term Kurihara sum) to test whether the (p=599) Hecke/Frobenius shortcut also gives a direct Stein–Wuthrich/Kato unit-regulator bound at p107. That new probe is **not yet user-executed**.

- [Precise p107/Kim proof and trust boundary](paper/bsd389_p107_kim_two_prime_sha_criterion_2026-10-30.md).
- [Fast independent p107 supersingular probe](verification/bsd389_p107_supersingular_p2_shortcut.py).
- [Archive hash and point-count bridge](verification/bsd389_kim_kurihara_sha107_bridge.py).
- [Live validation issue #6](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/6).

## p=599 — computer-assisted primary Sha vanishing (2026-10-30)

**New independently regressed arithmetic evidence and a complete mathematical reduction:** the original genuine conductor-`599²` Manin moment `C2=543 (mod 599)`, the exact `390/390` normalization comparison to Sage's analytic modular symbols, and a direct small supersingular `Dp_valued_series` regression together validate the computational conventions. The exact Hecke lift/Frobenius/precision argument determines the quadratic Dieudonné-valued analytic coefficient's first residue `571 mod 599`; the normalized p-adic regulator is also a unit. Applying the published Stein–Wuthrich Algorithm 11.1 and Kato/Perrin-Riou yields **a computer-assisted proof of `Sha(389a1/Q)[599^infinity]=0`** from the pinned, user-executed certificates. It was **not** produced by a successful run of `p_primary_bound(599)`. External independent mathematical review is still recommended before claiming publication-grade verification. This result concerns *only* p=599, not the p=16231 project or BSD as a whole.

- [Complete computer-assisted mathematical proof](paper/bsd389_p599_sha_vanishing_computer_assisted_proof_2026-10-30.md).
- [Independent user-run normalization and small-prime direct regression](results/p599_hecke_projection_independent_regression_PASS_2026-10-30.md).
- [Theorem/proof audit and peer-review tracking](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/4).

## p=599 finite-level certificate — 2026-10-30

**Source provenance reconciled:** GitHub's `sha599_short_certificate.py` now matches the user's executed local source **byte for byte** (blob `9acda8de4c526f96b96ad4e89847c782933c1528`). Its PASS log is user-executed on Sage with the authentic external table, not a GitHub Actions execution. The conditional analytic/Kato bridge **still requires independent mathematical review** ([issue #4](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/4)). The seven other local-only research scripts were recovered from the stash; see [reconciliation issue #5](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/5).

The user-executed independent finite conductor-`599^2` moment audits agree: `C0=C1=0`, `C2=543 mod 599`, across 179,101 sign pairs and 1,924,081 continued-fraction edges. The independent C++ engine reported PASS. A new bounded-memory Python verifier also completed on the user's Sage system with certified rank-2 Mordell–Weil generators, residual surjectivity, and normalized regulator first residue `571 mod 599`.

A proposed Hecke/Frobenius/precision reduction yields the **derived** analytic residue `F0=571 mod 599`; it is not a direct calculation of `Dp_valued_series` and the `p_primary_bound(599)` calculation did not finish. **Do not cite this as a completed unconditional proof that Sha[599^infinity] vanishes** until the reduction and Stein–Wuthrich/Kato theorem application receive independent review.

- [Verifier](verification/sha599_short_certificate.py) — requires external SHA256-pinned 390-entry Manin table.
- [Mathematical derivation and proof obligations](verification/README_sha599.md).
- [Verification ledger](STATUS.md) — detailed PASS / REVIEW-REQUIRED distinction.

## Current numerical record (updated 2026-10-19)

| Object | Result | Evidence |
|---|---:|---|
| V19 full-domain checkpoint | 263,429,130 pair indices; 1,087,544 Shapiro slots | Historical archived state, final SHA256 in `data/HISTORICAL_MANIFEST.md` |
| C01 terminal moments | J0 = 16,014; J1 = 4,703; J = 4,486 (mod p) | Independently recomputed V65 for 67 generators and both moments |
| V65 independent tail replay | 39,946 pairs; 2,175,088 coordinates; 0 differences | Exact-integer independent program and historic checkpoints |
| V66 reconstructed executable | Compiled; output equal on three 8-pair intervals | **Binary SHA different** from original; no byte-identical rebuild |
| Level 2 coefficient | A2^(2) = 1,199 p (mod p²) | V54/V61, 254 archived chunks |
| Conditional level 3 coefficient | A2^(3) = 9,534 p (mod p²) | **Only after identification of global J_V19 with mathematical J_ref** |
| Arithmetic Sage gate | PASS reported on IONOS; Bp/p = 9,534 (mod p) | Certified rank=2, MW generators, local hypotheses, regulator and precision |
| Manin–Shapiro source/export identities | **PASS**, 390/390 exact rational-cusp divisor equalities, 2,012 SL₂/Gamma0(389) relation terms, Manin rank 325, 65-dimensional quotient; eight real-export C++ pair/aggregation comparison windows | [Independent exact-data certificate](results/v11_export_exact_manin_shapiro_certificate_2026-10-19.md) |
| Full V19 checkpoint replay | **PASS (reported)**: 263,429,130 pairs; 514,511 chunks; 4,019 checkpoints; 9,759,143,225 rows; final SHA matches historical checkpoint | [Full chain audit completion record](results/v19_full_chain_audit_2026-10-19.md); does **not** independently recalculate each chunk |

The original production **source files and canonical JSON input archives have now been received and authenticated by exact SHA-256**, although their full bytes still await individual Git repository import. The main source-to-specification mathematical equalities have been independently validated over rational cusp divisors; compiler/binary provenance and theorem applicability remain separate checks.

For the precise logical status of every statement, see [STATUS.md](STATUS.md). The comparison formula and its conditions are in [the conditional manuscript](paper/theorem_conditional_draft.md).

## Reproduce

- [Reproducibility guide](REPRODUCIBILITY.md): quick integrity tests, independent checks, full historical run.
- [Required source imports](data/REQUIRED_IONOS_IMPORTS.md): original V19 producer, loader, driver, canonical relations and scalar data were **not** available as native files when this bundle was prepared. They are intentionally not simulated or reconstructed from conversation snippets.
- [Dataset policy](DATA_AVAILABILITY.md): large checkpoints/chunks are not embedded in Git.
- [Original checksums](data/HISTORICAL_MANIFEST.md) and [bundle source hashes](MANIFEST.sha256).

Run `python scripts/verify_bundle.py` for a local structural and checksum check. This is not a proof of mathematical correctness. Some heavyweight verification scripts require full external datasets and a SageMath environment.

## Research integrity and citation

Author: **Jerry Armando Kasa**. See `CITATION.cff`. The repository is prepared **privately**, with license to be chosen before public release. Corrections and objections should be recorded explicitly in [STATUS.md](STATUS.md); failed or conditional tests must not be silently relabeled as successful.