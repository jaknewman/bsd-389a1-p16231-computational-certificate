# Reproducibility levels

## Level A — bundle integrity (fast, no Sage)

```bash
python scripts/verify_bundle.py
python -m compileall -q verification scripts
```

Checks listed source-file digests and evaluates a simple independent modular-arithmetic identity. This validates packaging only, not large-scale historical computations.

## Level B — arithmetic gate (Sage)

Install a compatible SageMath release and provide `389a1` through Sage's elliptic-curve database. On the IONOS environment the historical script was executed after correcting `E.tate_curve(389)` to `E.tate_curve(ZZ(389))`:

```bash
python verification/arithmetic/bsd389_porte_arithmetique_finale.py
```

Expected log ending (reported 2026-10-18): `FINAL_ARITHMETIC_GATE_PASS` and `BOUNDARY: no level-3 independent calculation; no independent certification of all V19 pair updates.`

## Level C — V65 independent terminal checks (Sage + C++ + archived data)

The scripts in `verification/v65/` were written for historical paths under `$HOME/bsd389-c01-v14-production` and `$HOME/bsd389-portable-c01-v2`. See `verification/v65/INSTRUCTIONS.md`; run on a machine with the relation export, the archived checkpoint and terminal progress files.

These scripts do not derive the production coefficients independently over all 263,429,130 pairs. The V65 tail replay checks exactly 39,946 pairs using arbitrary-precision Python integers.

## Level D — archived V19 end-to-end accumulation (large I/O)

`verification/v19_chain/bsd389_audit_chaine_v19.py` reads archived V19 `chunks/*.tsv`, per-chunk checksums and the checkpoint metadata/binaries. The pilot is expected to process **514,511 chunks** and **4,019 checkpoint states**. It does not recompute the mathematics of each chunk independently.

```bash
# Copy the script to its original expected directory first, or adjust paths.
python -u verification/v19_chain/bsd389_audit_chaine_v19.py --max-blocks 2
# Then, after verifying the preflight logs:
python -u verification/v19_chain/bsd389_audit_chaine_v19.py --resume
```

**Do not start a second audit on the same output/progress paths while an existing one is running.** At initial repository preparation the remote audit was already in progress. Preserve its logs and final SHA, and append the actual verdict to STATUS.md.

## Level E — complete fresh numerical reproduction

Requires original C++ producer sources, exact compile options, frozen export/scalar tables, complete Sage/eclib environment, sufficient memory, CPU and storage, and time for all historical evaluations. These prerequisites are not part of this starter repository. Refer to `data/REQUIRED_IONOS_IMPORTS.md` and `DATA_AVAILABILITY.md`.

**A fully reproducible archival DOI should not be minted claiming completeness until datasets, versioned environment, manifests and all claims have been audited.**