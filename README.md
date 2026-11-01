# Computational certificate for elliptic curve 389a1 at p = 16231

**Status: research-stage, independently corroborated numerical evidence; final certification in progress.**

This repository organizes the computational evidence and mathematical comparison needed to study the 16231-primary part of the Tate–Shafarevich group of the elliptic curve

\[
E/\mathbb Q:\quad y^2+y=x^3+x^2-2x,\qquad p=16231.
\]

**Do not cite this repository as an unconditional proof of BSD or of** `Sha(E/Q)[16231^infinity] = 0` **until the outstanding verification obligations are discharged and reviewed.** A first-digit congruence does not prove an exact p-adic equality or full BSD.

**New unconditional all-prime reduction:** For EVERY p, even 2,3,389, the proven Mordell–Weil rank two and the split Pontryagin-dual Kummer exact sequence give `Sel_{p∞}(E/Q)^dual ≅ Z_p^2 ⊕ Sha[p∞]^dual`; hence `Fitt_2(Sel^dual)=Fitt_0(Sha[p∞]^dual)`. Thus `Fitt_2=Z_p` iff that p-primary part is zero; `Fitt_2=p^e Z_p` iff it is finite of order `p^e`; and `Fitt_2=0` iff it is infinite. **No reduction-type or Iwasawa theorem is needed for this equivalence**, only for calculating `Fitt_2` from modular symbols. The missing proof remains a fixed p-independent integral determinant/control comparison, plus the separate exact complex BSD formula. [Unconditional theorem and proof](paper/bsd389_unconditional_rank2_kummer_fitt2_identity_2026-10-30.md).

## Uniform support: rigorous profinite-determinant obstruction and rational descent criterion (2026-11-01)

**Exact new algebraic result, NOT a new Sha vanishing claim:** a finitely presented rank-two module over `Zhat=∏_p Z_p` may have a nonzero determinant yet have `Fitt_2=(p²)` at **every** prime p. The specific counterexample `X=Zhat²⊕(Zhat/(p)_p)²` has a perfect two-term presentation and respects the square-order constraint of finite p-primary Sha. An elementary Euclid argument shows that **no single nonzero integer C**, even excluding any finite set of p, is forced into those local ideals. Thus merely constructing a global **profinite** Selmer determinant cannot prove the desired finite prime support. **This module is abstract, not asserted to be the actual Selmer group.**

A second exact result states that a finitely generated **Z**-module whose completions equal all genuine `Sel_{p∞}(389a1)^dual` exists **iff the entire Sha is finite**, using the already proved rank two and `Sha[5∞]=0`; assuming such a model would be circular.

**Non-circular sufficient target:** construct a single rational `Delta=a/b≠0` (or a genuine rational motivic determinant line with fixed integral lattice), an explicit finite S and a proof of **all-p integral membership** `Delta∈Fitt_2(Sel_{p∞}^dual)` outside S and p dividing b. Then the fixed integer `C=abs(a)` bounds all nonexceptional prime support. The rational descent and comparison are **not proved**. [Complete new proof and finite-exception Euclid witness](paper/bsd389_uniform_global_integral_det_vs_profinite_counterexample_2026-11-01.md) · [constructive checker](verification/bsd389_uniform_profinite_det_counterexample.py) · [open issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8).

## Where are we on COMPLETE BSD? Two logically distinct gaps remain (2026-10-30)

**Proven for 389a1:** Mordell–Weil rank 2 equals complex analytic rank 2; torsion trivial and Tamagawa product 1. Classical two-descent proves Sha[2]=0, and Sage's published `p_primary_bound(5)=p_primary_bound(7)=0` certify those two primes. This project's complete p107 archive, p599 supersingular moments and p16231 V65/Hecke certificate add substantial prime-specific computer-assisted evidence, with their existing normalization/source assumptions.

**NOT PROVEN:** (1) finiteness/triviality of **all** of `Sha(E/Q)`; (2) the **exact complex leading-coefficient formula** `L''(E,1)/2 = Omega_E*Reg(E)*#Sha(E/Q)`. Numerically the analytic Sha ratio is near 1, but a numerical approximation is not a proof of that exact identity. The new Mazur + Castella–Sano all-good-p Kurihara theorem is at **unrestricted auxiliary degree** and does not close the rank-two Fitting ideal.

[Full independently source-audited BSD status and consistency ledger](paper/bsd389_full_BSD_state_and_uniform_Fitt2_checkpoint_2026-10-30.md) — [Issue #8: p-uniform Sha second Fitting ideal](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8) — [Issue #9: exact complex BSD leading term](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/9).

## New exact uniform Kurihara theorem for 389a1 — every good p≥11 (2026-10-30)

**Not merely a finite-prime computation:** Combining **Mazur's 1978 semistable Galois-surjectivity theorem** (all `p≥11`) with **Castella–Sano's January 2026 Theorem B** (refined Kurihara nonvanishing for good ordinary and, when N is squarefree, supersingular p) shows rigorously that **for EVERY prime `p≥11` except the multiplicative prime `389`**, the Kurihara family has an **admissible squarefree conductor `n(p)` with nonzero mod-p delta**, with no bound on `nu(n)`. Precisely `M_infinity(delta_p)=0` for all these p, because `Tam(E)=1`. There are **no unknown surjectivity exceptions** in this explicit large-prime range; the omitted small p are 2,3,5,7 and p389. Historical Sage checks at p5,7 exist separately.

**Crucial:** This theorem does **not** force `nu(n)=2` and does **not** prove any new Sha-primary triviality. Kim Theorem 1.8 gives an exact classification for our rank-two curve using `m2(p)`, the minimum valuation of **two-prime** Kurihara numbers: `m2=0 <=> Sha[p^infinity]=0`; finite positive `m2` gives a finite p-group of size `p^m2`; `m2=infinity` yields a positive-corank divisible Sha. Finding an all-p **two-prime unit** is therefore equivalent to the original Sha-support goal and remains open. [Complete proof and original 2026 theorem citation](paper/bsd389_uniform_kurihara_castella_sano_kim_2026-10-30.md) · [issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8).

## Uniform prime-support program — exact fixed factor, Selmer bridge outstanding (2026-10-30)

**A new rigorous all-prime algebraic result**, not another finite prime scan: for the archived conductor-53 order-9 Gross orbit on `Q(sqrt(-3))`, an independently executed exact integral polynomial/matrix computation finds `F(zeta9) = -3*zeta9*u` with an explicit unit `u` in `Z[zeta9]`, hence **Norm(F)=3^6=729**. This particular toric algebraic factor is a **p-adic unit at every p≠3**, not merely for p up to a chosen bound. The input is the historical ordered 18-class coefficient vector; identifying it with the intended adelic toric period still depends on the separate Gross/Brandt archive and normalization. [Independent pure-Python exact certificate](verification/bsd389_uniform_chi53_toric_unit.py).

**No all-prime Sha deduction follows yet:** the Kummer sequence shows `dim_Fp Sel_p(E)=2+dim_Fp Sha(E)[p]`; an actual *uniform finite support theorem* requires a single nonzero integer `C` and a proof for all p (outside finitely many local exceptions) that `Sha(E)[p]≠0 => p|C`. The toric norm 729 has **not** been connected to such an integral Selmer implication. Moreover, no finite number of fixed imaginary quadratic fields covers all but finitely many primes under split-p-only anticyclotomic theorems: infinitely many `p≡-1 mod lcm(|D_i|)` remain inert in every field. The [precise algebraic note and proof boundaries](paper/bsd389_uniform_prime_support_chi53_unit_and_split_obstruction_2026-10-30.md) and [issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8) now identify the **missing integral Selmer bridge** rather than demanding further massive p-specific scans. This does not prove finite Sha or full BSD.

**Updated after authentic Ubuntu execution and new exact theorems:** The chi53 norm-729 polynomial/determinant verifier has now run successfully on the user's Ubuntu host; [verbatim PASS stdout](results/chi53_uniform_toric_norm729_USER_SAGE_PASS_2026-10-30.md). Two additional universal Kurihara lemmas sharpen the main proof target: (i) a **fixed** auxiliary conductor `n=q1*...*qr` is p-admissible only if `p|gcd(q_i−1)`, so finitely many fixed n can cover only finitely many p; (ii) **for every p with surjective mod-p Galois image**, Chebotarev furnishes infinitely many good basic p-admissible primes q with nontrivial unipotent Frobenius, of exact natural density `1/[p(p−1)]`. Thus the precise unproved step is **uniform nonvanishing `delta_(q1(p)q2(p)) != 0 modp`** (and any extra integrality/higher-level conditions), *not* existence of elementary auxiliary primes. [Full source-level proof](paper/bsd389_uniform_prime_support_chi53_unit_and_split_obstruction_2026-10-30.md) and [issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8). None of these new universal auxiliary-prime statements alone imply a Sha support bound.

## p=16231 — independent V65 Sage source-oracle PASS (2026-10-30)

The **new genuine Sage server run** authenticates the original binary eclib V65 reference table and Manin/Shapiro relations by exact SHA256 and verifies all **16,232** Shapiro integer matrix identities, all **67 Hecke fibres** (1,087,477 stored beta-symbol entries), all **134** generator anchor symbols, **536** direct beta samples with `implementation='sage'` independent of eclib, and **335** Shapiro `M0` checks including **all 67 infinity cosets**. [Verbatim user-run evidence](results/p16231_v65_independent_sage_manin_shapiro_PASS_2026-10-30.md).

This narrows the shared-source risk of the two archived complete `J=4486` engines. With the independently reproduced `A2(n2)/p=1199`, the source-level ordinary correction `8335`, and independently computed regulator factor `B/p=9534`, the derived leading coefficient is `A2(n3)/p=9534 mod16231`, giving a valuation-zero analytic quotient **conditional on the authenticated historic source-to-`J_ref` computations and the published Kato theorem**. Thus the evidence supports a computer-assisted conditional implication `Sha(389a1/Q)[16231^infinity]=0`; this is not a direct successful `p_primary_bound` run, a formal proof of the binary, or an all-prime BSD theorem. [Updated minimal dependency proof](paper/p16231_minimal_prime_primary_sha_certificate_2026-10-26.md) and [review issue #7](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/7).

## p=107 — archived two-prime Kurihara witness and Kim criterion (2026-10-30)

The historical 710-block exhaustive computation reports `delta_(369793*383917)=34 (mod 107)`. The precise application of **Chan-Ho Kim's Theorem 1.8** shows that an authentic normalized **unit two-prime witness**, combined with certified Mordell–Weil rank 2 and residual surjectivity, forces the finite Selmer quotient to vanish and hence `Sha(389a1/Q)[107^infinity]=0` **without assuming Sha finiteness**. The original 710-block archive is now **cryptographically re-authenticated** by a fresh user run (SHA256 `b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754`) and its auxiliary-prime arithmetic recomputed. That hash does **not** redo the 710 JSON contractions; the historical exhaustive and Manin audits remain the computational inputs to the Kim proof. External reproducibility review remains open.

The conductor-`107²` alternative has now **PASSED a genuine user Sage execution**: 5,671 plus-symmetric modular symbols, 106 Hecke fibres, `C0=C1=0,C2=86 (mod107)`, Hecke/Frobenius-derived analytic residue `43 (mod107)`, and normalized regulator first residue `43` with valuations `[0,1]`. It supplies numerically independent support. The **separate Stein–Wuthrich/Kato analytic upper-bound normalization** (printed `Reg_p` versus `Reg_gamma`) still needs a targeted check and should not be conflated with the independently applicable Kurihara–Kim theorem. [Exact p107 user-run logs](results/p107_two_routes_user_run_PASS_2026-10-30.md).

- [Precise p107/Kim proof and trust boundary](paper/bsd389_p107_kim_two_prime_sha_criterion_2026-10-30.md).
- [Fast independent p107 supersingular probe](verification/bsd389_p107_supersingular_p2_shortcut.py).
- [Archive hash and point-count bridge](verification/bsd389_kim_kurihara_sha107_bridge.py).
- [Live validation issue #6](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/6).

## p=599 — source-verified analytic candidate bound; supersingular regulator normalization under review (2026-10-30)

**New independently regressed arithmetic evidence and a complete mathematical reduction:** the original genuine conductor-`599²` Manin moment `C2=543 (mod 599)`, the exact `390/390` normalization comparison to Sage's analytic modular symbols, and a direct small supersingular `Dp_valued_series` regression together validate the computational conventions. The exact Hecke lift/Frobenius/precision argument determines the quadratic Dieudonné-valued analytic coefficient's first residue `571 mod 599`; the normalized p-adic regulator is also a unit. Interpreting the p-adic L-function and regulator in **matching normalized T-series conventions** suggests the computer-assisted conclusion `Sha(389a1/Q)[599^infinity]=0`. However the printed supersingular Algorithm 11.1 involves `Reg_p`, whereas §4.4 and Conjecture 5.2 use `Reg_gamma=Reg_p/log(gamma)^r`. **This discrepancy requires an explicit normalization audit before promoting the derived upper bound to an unconditional theorem.** The independent finite PASS certificates remain valid. It was **not** produced by a successful run of `p_primary_bound(599)`. External independent mathematical review is still recommended before claiming publication-grade verification. This result concerns *only* p=599, not the p=16231 project or BSD as a whole.

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