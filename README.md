# Computational certificate for elliptic curve 389a1 at p = 16231

**Status: research-stage, independently corroborated numerical evidence; final certification in progress.**

This repository organizes the computational evidence and mathematical comparison needed to study the 16231-primary part of the Tate–Shafarevich group of the elliptic curve

\[
E/\mathbb Q:\quad y^2+y=x^3+x^2-2x,\qquad p=16231.
\]

**Do not cite this repository as an unconditional proof of BSD or of** `Sha(E/Q)[16231^infinity] = 0` **until the outstanding verification obligations are discharged and reviewed.** A first-digit congruence does not prove an exact p-adic equality or full BSD.

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
| Full V19 checkpoint replay | **PASS (reported)**: 263,429,130 pairs; 514,511 chunks; 4,019 checkpoints; 9,759,143,225 rows; final SHA matches historical checkpoint | [Full chain audit completion record](results/v19_full_chain_audit_2026-10-19.md); does **not** independently recalculate each chunk |

For the precise logical status of every statement, see [STATUS.md](STATUS.md). The comparison formula and its conditions are in [the conditional manuscript](paper/theorem_conditional_draft.md).

## Reproduce

- [Reproducibility guide](REPRODUCIBILITY.md): quick integrity tests, independent checks, full historical run.
- [Required source imports](data/REQUIRED_IONOS_IMPORTS.md): original V19 producer, loader, driver, canonical relations and scalar data were **not** available as native files when this bundle was prepared. They are intentionally not simulated or reconstructed from conversation snippets.
- [Dataset policy](DATA_AVAILABILITY.md): large checkpoints/chunks are not embedded in Git.
- [Original checksums](data/HISTORICAL_MANIFEST.md) and [bundle source hashes](MANIFEST.sha256).

Run `python scripts/verify_bundle.py` for a local structural and checksum check. This is not a proof of mathematical correctness. Some heavyweight verification scripts require full external datasets and a SageMath environment.

## Research integrity and citation

Author: **Jerry Armando Kasa**. See `CITATION.cff`. The repository is prepared **privately**, with license to be chosen before public release. Corrections and objections should be recorded explicitly in [STATUS.md](STATUS.md); failed or conditional tests must not be silently relabeled as successful.