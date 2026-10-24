# C01–V19 original-source audit — 24 October 2026

## Scope and evidence

The original files were committed on the private repository branch `main` as commit `6e97249`. The user executed `scripts/audit_c01_v19_release.py` on the IONOS host, reporting `C01_V19_ARCHIVE_IDENTITY_PASS` with eight of eight frozen original SHA-256 checks matching and exit status zero. **This establishes file identity, not mathematical execution or unconditional BSD.**

This review used the exact committed files:
- `historical/originals/bsd389_c01_v11_aggregated.cpp`
- `historical/originals/bsd389_c01_v11_loader.cpp`
- `historical/originals/bsd389_transposed_J_native.cpp`
- `historical/originals/v19_production.py`
- `historical/originals/bsd389_tame_relation_export_p16231.json`
- `historical/originals/bsd389_tame_scalar_values_p16231.json`

## Independent mathematical/data audit performed on the committed originals

Parsed the exact relation JSON and independently recomputed, using integer rational-cusp arithmetic:

- All 390 modular representative matrices have determinant +1.
- All 390 projective keys agree with the `key_to_rep` mapping.
- Exactly 67 distinct named generators occur.
- All 2,012 relation matrices have determinant +1 and lower-left entry divisible by 389.
- For each one of the 390 representatives `G_i`, the exact formal cusp-divisor relation

  `[G_i infinity]-[G_i 0] = sum_(epsilon,A,r) epsilon([A^{-1}G_r infinity]-[A^{-1}G_r 0])`

  has **zero residual cusp coefficients** (390/390 exact identities). This is an independent fresh check of the committed JSON, not an assertion based solely on a prior PASS log.

The scalar JSON contains exactly 67 residues. These are **not** the full Shapiro/level-3 moment arrays and are insufficient alone to recompute the historical terminal contraction.

## Original source semantics

The V11 C++ loops over the bounded pair interval `id in [L,R)`, with `a=1+id/p` and `b=id%p` and `p=16231`. Thus the full domain `[0,p(p-1))` covers precisely all `1<=a<p, 0<=b<p`.

The implemented `kappa_ab(a,b)` matches the separately stated Teichmüller lifting relation modulo `p^3`. An independent modular-arithmetic check on representative pairs validated divisibility by `p^2` and the computed kappa. This sampled check is not an all-input proof.

`collect_fragments` uses Euclidean continued-fraction matrices and aggregates signed weights `W=-sum(w)` and `K=-sum(w*kappa)`. `apply_group` uses the mod-p degree-one moment action `(q,r)=(-a*b,a*a)`. Relation compositions implement `(q,r) o (qi,ri)=(q+r*qi,r*ri)`. The exact cusp identities justify reducing each modular divisor through the exported relations; reduction of *moment-action coefficients* modulo p is distinct from (and must not be substituted for) reduction of rational cusps.

**Boundary:** These are source-level algebraic checks. A full source-to-Sage comparison of input moment normalization, the measured historical `M0/M1` arrays, and the finite-level `A2^(3)` correction remains the core theorem/computation bridge. The recent nonclosure of two moments modulo `p^3` in a different overconvergent model does not contradict C01's mod-p two-moment covariance.

## V19 producer audit

The committed `v19_production.py` checks the V11 executable SHA-256 at startup, uses bounded 512-pair chunks, verifies local chunk SHA sidecars, accumulates two arrays of 67*(p+1) unsigned 16-bit residues mod p, and writes fsync/replace checkpoint state bytes and metadata. The terminal frozen state has exactly 4,350,176 bytes.

Important limitations:

1. The seed code accumulates the initial `SEED=131072` pairs from existing verified chunk files; it does not invoke `run_chunk` to generate missing seed files. Consequently a cold, empty-data rerun using this driver alone is **not** self-contained.
2. Sidecar SHA files establish that the accumulated bytes agree with each adjacent digest, but do not by themselves establish that each byte sequence was produced by the authenticated binary.
3. No full independent 263,429,130-pair mathematical recomputation was undertaken by this audit. The earlier exhaustive V19 *recomposition*, V65 terminal contraction and bounded byte-for-byte binary replay remain separate evidence.

## Arithmetic implication (conditional on completing the bridge)

At p=16231, a_p=128:

- Frozen `J_V19 = 16014 + 4703 = 4486 (mod p)`.
- Level-2 `A2^(2)/p = 1199 (mod p)`.
- `J/(4*a_p^2) = 8335 (mod p)`.
- Therefore if the historic data compute the mathematical `J_ref` in the exact Sage normalization, then `A2/p = 9534 (mod p)`.
- The independently reported p-adic regulator yields `B_p/p = 9534 (mod p)`.
- Thus `A2/B_p = 1 (mod p)` and `v_p(A2/B_p)=0` under those hypotheses. This does **not** prove exact equality `A2/B_p=1` in Q_p.
- Subject to the documented Sage/Kato hypotheses and faithful analytic coefficient, exponent zero in Sage's proved `Sha.p_primary_bound` implies `Sha(E/Q)[16231^infinity]=0`.

The expensive direct Sage call `E.sha().p_primary_bound(16231)` has **not** been performed. The reported Sage 10.9 arithmetic gate used the conditional historic coefficient.

## Remaining targeted tasks (not a new stage series)

1. Trace provenance and independently check the original terminal `M0/M1` arrays against the mathematically defined modular-symbol moments (including period/sign normalization).
2. Perform a source-based audit of the level-2 to level-3 correction formula in the pinned Sage 10.9 implementation (including `eta=0`, `D=1`, `gamma=1+p` and division by the two real components).
3. Specify a reproducible cold-start seed generation and an independent, statistically designed or complete producer-to-chunk validation according to the standard of certification claimed.
4. Keep the p-primary theorem separate from the unresolved global prime support of Sha and the exact complex BSD leading-coefficient equality.

**Current verdict: SOURCE-LEVEL/DATA-CUSP-AUDIT PASS; HISTORICAL-NUMERICAL-TO-SAGE BRIDGE OPEN; UNCONDITIONAL p-PRIMARY THEOREM NOT CLAIMED; FULL BSD OPEN.**
