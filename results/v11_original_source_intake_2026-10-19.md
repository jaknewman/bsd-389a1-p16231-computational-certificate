# V11/V19 original-source intake: exact digest and branch review (2026-10-19)

## Provenance

User-supplied archived original source bytes: `bsd389_sources_finales.tar.gz` (7,322 bytes), SHA-256 `fc8b30bc8045819efe7902be521fdd66efa40a5f3e2cd9403346405c30f99dd3`. All four exact member hashes match the previously frozen values in [historical manifest](../data/HISTORICAL_MANIFEST.md). The source files are **not yet copied into Git version control**, pending direct content import. No output data or Manin export is inside this archive.

## Static code analysis completed

- `bsd389_c01_v11_aggregated.cpp` loops over the exact pair-index range `0 ≤ id < p(p−1)`, with `a=1+id/p`, `b=id%p`, and `[L,R)` bounded by 512.
- `collect_fragments` forms **exact integer** SL2 fragment keys in a map (no unsafe cache collapse by mod 389 or mod p). It sums `W_B=−Σw`, `K_B=−Σw*kappa` mod `p`.
- The direct-generator branch adds `(q W_B−K_B, r W_B)`, with `q=−AB` and `r=A²` mod `p`.
- The relation branch adds `e((q+r qi)W_B−K_B, r ri W_B)`, implementing affine covariance and composition. These are linear in `(W_B,K_B)`, proving that exact-fragment grouping agrees algebraically with per-pair accumulation for any input satisfying the Manin/Shapiro preconditions.
- `kappa_ab` uses `a^(p²) mod p³`, `(1+p)^u mod p³` and performs a `p²` divisibility assertion.
- `mm()` reduces matrix entries mod `p` for **moment transport only**; Manin key lookup uses the original exact fragment matrix, modulo `389`.
- `v19_production.py` pins the executed V11 binary SHA, validates sparse sorted slots and checkpoints; the later independent full-chain PASS checks the complete output recomposition.
- `v4_load_export()` checks 67 generator uniqueness and relation indices. It **does not certify** SL2 determinants, projective key consistency, complete Sage Manin identities, or bounds on JSON coefficient narrowing. Those require the actual historic export JSON.

## Independent bounded oracle actually executed

```text
CONSTANTS_RINF_PASS
KAPPA_AND_WEIGHT_CONGRUENCES_PASS 4005
EUCLIDE_SL2_TELESCOPE_PASS 4005
SHAPIRO_AFFINE_FORMULA_PASS 10000
FINITE_AND_EXCEPTIONAL_COSETS_PASS 40
SOURCE_ORACLE_BOUNDED_PASS
```

A GCC 14.2 `-O2 -std=c++17 -DBSD389_EFFECTIVE -DBSD389_SPARSE_TOUCHED -Wall -Wextra -Wconversion -Wsign-conversion -c` compilation **succeeded**. GCC conversion and signed/unsigned index warnings were emitted. For the prescribed pair domain and reduced mod-p coefficient factors, intermediate arithmetic is comfortably within `int64_t`; exact values entering from the export JSON remain a precondition and should be checked independently. This local compilation is **not** a byte-identical rebuild of the historical executable.

## Mathematical significance

For the independent reference functional

`J_ref = −Σ_{a,b} w(a,b)(M1(D_x)−kappa(a,b)M0(D_x)) mod p`,

source-level fragment grouping and direct/relation branch formulas match the induced moment action. Thus no *formula-level* discrepancy was found between V11 aggregation and the mathematical definition, **provided** the original JSON has the correct Manin relations and SL2 matrices and the binary execution conforms to these source semantics.

**Do not promote this report to unconditional `J_V19=J_ref`** until original export/scalar data preconditions and historical binary provenance have been reviewed. The full V19 chunk-chain PASS is independent and already complete.

## Next bounded gate, not a repeated 263-million-pair run

Import the original `bsd389_tame_relation_export_p16231.json` and `bsd389_tame_scalar_values_p16231.json`, verify their frozen SHA-256s, audit every matrix determinant, every projective key-to-representative mapping, relation coefficient widths and generator references, and cross-check the Manin identities against Sage's canonical relations. This can be done with ~390 representatives rather than recomputing 263 million pairs.
