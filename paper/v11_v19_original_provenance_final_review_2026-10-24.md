# V11/V19 original provenance: detailed review — 2026-10-24

## Status and evidence basis

This review inspects the *actual uploaded* five small files at
`historical/provenance/`, committed as `d6ce07b`, plus the original
V11 producer source and V19 driver at `historical/originals/`.
The user ran `scripts/prepare_v11_v19_provenance_bundle.py`
on IONOS and obtained `V11_V19_PROVENANCE_BUNDLE_PREPARED_PASS`,
exit status 0. This is **source review plus user-reported execution**,
not a new full multi-hour audit by GitHub Actions.

## V11 binary provenance — what is supported

The original JSON report
`v11_provenance_report_2026-10-19.json` contains:
- Original V11 x86-64 ELF SHA-256:
  `31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63`.
- Ubuntu GCC 13.3.0 and flags:
  `-O2 -std=c++17 -DBSD389_EFFECTIVE -DBSD389_SPARSE_TOUCHED -lboost_json`.
- **Byte-identical** source rebuild (`same_bytes_as_original: true`).
  An alternate `-O3` build has a different hash, as expected.
- Four test intervals `[0,512)`, `[512,1024)`,
  `[131714560,131715072)`, and
  `[263429120,263429130)`. Original and rebuild have
  equal per-interval output hashes and output sizes.
- Pinned export JSON containing 390 representatives, 67 generators,
  and 2012 relations, and expected final V19 state SHA.
The report's own SHA-256 is
`a9b853ee30d95bb48565bc99c35799dcc40c57b2bc8b9915792b81e72e3e9371`,
which the IONOS preparation script verified.

**Interpretation:** executable ↔ archived source build provenance is
exceptionally well documented. The four windows do not establish the
computation of all other 514,507 chunks, and compilation byte identity
does not constitute a proof of C++ semantic correctness.

## V19 independent full-chain recomposition — exact source behavior

The uploaded `bsd389_audit_chaine_v19.py` uses
`TOTAL=p(p-1)=263429130`, `STEP=512`, `SEED=131072`,
`BLOCK=65536`, `NG=67`, `SLOTS=67*(p+1)`.
It pins executable, export, production-driver, and V11-source SHA-256
before consuming data.

For each one of 514511 archived chunks, it checks the expected
contiguous `[L,R)` filename, its SHA-256 sidecar and strictly
increasing sparse slot indexes with two valid nonzero residue
coefficients. It accumulates both C0/C1 arrays mod p.

For each seed and 4018 subsequent block endpoints (4019 checkpoint
states total), the recomposed `c0.tobytes()+c1.tobytes()` is
**byte-for-byte compared** to the checkpoint state. The metadata
must pin both the historic binary SHA and relation export SHA. The
last checkpoint must also match the independently frozen terminal
state SHA-256
`5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e`.

The user's original terminal log excerpt, final independent progress
JSON and IONOS run all agree:
`263429130` pair indices;
`514511` chunks;
`4019` checkpoint states;
`9759143225` sparse rows;
`blocks_done=4018`;
final SHA-256 as above.

This is a **complete independent recomposition of archived producer
outputs**, but not a complete fresh mathematical *production*.

## Cross-checks already complete

1. Original eight SHA-256 source/binary/export artifacts recovered.
2. Full exact cusp-divisor identities: 390/390; group lifts: 2012/2012.
3. V23 `J0=16014` / V26 `J1=4703` recomposition: 67/67 each.
4. Independently generated V65 eclib/Hecke table pin and all 134
   per-generator terminal quantities matched via direct user-run audit.
5. All 254 level-2 V54/V61 archived chunks recomposed; cross-reduced,
   and `A2^(2)=19460969=1199*p (mod p²)`.
6. Algebraic `A2^(3)-A2^(2)=p*J_ref/(4*alpha²) (mod p²)`
   derived from the definitions of Sage's measure/series,
   including the two real-components divisor.

## One additional bounded source-to-data check

To strengthen the trust link **native producer → archived chunk bytes**
without redoing all 263 million pairs, a new
`scripts/audit_v19_stratified_producer.py` selects deterministic
anchors, equally-spaced intervals and seeded pseudo-random chunk
indices throughout the corpus. On IONOS, it will rerun the original
SHA-pinned binary for every selected interval in a temporary folder,
then require a **byte-identical** match with both archived chunk and
SHA sidecar. No original data is mutated.

**Not run at time of writing:** This additional replay is prepared
but its result must be reported by IONOS before claiming PASS. Its
deterministic sample is not a formal probabilistic error bound.

## Rigorous conclusion and remaining boundaries

The V11/V19 chain and now-imported reports are strong reproducible
evidence for the global C01 terminal `J_V19=4486 (mod p)`.
The source-to-mathematical-functional derivation identifies how
the program is *intended to* compute `J_ref`, and the original source
has been reviewed branch by branch. Standard computer-assisted proof
standards still require a trusted compilation/execution environment,
precise source behavior, and independent verification appropriate to
the claimed theorem; hashes and archived full recomposition alone
cannot prove the mathematical correctness of every producer output.

Conditional on that trusted finite computation and the documented
Sage analytic normalization/precision, `A2/p=9534` and the
p-adic regulator gives `B_p/p=9534`; the quotient is a **unit**,
not exactly 1 in `Q_p`. The Kato/Sage p-primary bound then yields
`Sha(E/Q)[16231^infinity]=0`.

**There is no claim here of a direct execution of
`p_primary_bound(16231)`, exact `u_p=1` in `Q_p`,
global finiteness of `Sha`, or full BSD for 389a1.**
