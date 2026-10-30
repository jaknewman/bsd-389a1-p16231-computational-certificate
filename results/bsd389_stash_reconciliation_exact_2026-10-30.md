# Exact Sage-stash ↔ GitHub reconciliation — 2026-10-30

## Inputs / provenance
- User-supplied archive: `bsd389_reconciliation_20261030.zip` (87,272 bytes); contains 7 `local_only/` scripts and 17 `divergent_local/` / `github_main/` file pairs.
- Ubuntu source stash: `stash@{0}`, commit `a71cdcda0e337811c3ada91b306fd29098a52ac2`; local divergent backup `/home/bsdadmin/bsd389_stash_review_20261030_194956`. Stash and backup remain intact.
- All 24 comparisons were performed from the uploaded archive. Initial local `main` was `df4b0ae`, clean except seven restored untracked scripts.

## Exact reconciliation
- **15** divergent pairs: local = GitHub main bytes + **one extra terminal LF**. No logical/code differences; retain GitHub version.
- **1** divergent pair: `verification/kurihara_p599_denominator_automaton_differential.py` uses `statistics.median(speeds)` on GitHub versus local `sorted(speeds)[len(speeds)//2]`. Retain GitHub version (correct statistical median for even count).
- **1** divergent pair: `verification/sha599_short_certificate.py` has meaningful prose/formatting and message differences. Replaced GitHub version with **the exact locally executed bytes**, git blob `9acda8de4c526f96b96ad4e89847c782933c1528`, and amended README/STATUS/run-log provenance wording.
- **7** local-only scripts: imported individually into `verification/` with **exact matching Git blob SHA1** (not rewritten), as follows:

| Script | Git blob SHA1 | Execution / proof scope |
|---|---|---|
| `bsd389_a2_sha_16231.py` | `e38657e52923b35ba3dd89c7db1df853ece6ba67` | `--selftest` assistant-local PASS; no exhaustive Gross-point input, no p16231 Sha bound |
| `bsd389_chi53_order9_from_archive.py` | `05d562ca8854736a27bd06ae72264a4fa9caa741` | Syntax PASS; authentic Sage JSON archival verification NOT RUN |
| `bsd389_chi53_rank2_gate.py` | `3674d622130323fb7de90c5aedf669c0a9007db9` | Syntax PASS; Sage `twist_nonvanishing` NOT RUN here |
| `bsd389_kim_kurihara_sha107_bridge.py` | `2c0040d3a3f3b0cb77e614ec559cf4feeffe929d` | `--selftest` assistant-local PASS including independent finite-field point counts; archived full `tar.gz` not present, theorem application is conditional |
| `bsd389_stage73_factorization.py` | `2261dfa459c40eb21a17f43b31af3b256c9f40c6` | Syntax PASS; Sage `--selftest` not executed here |
| `k107_static_bounds_audit.py` | `e1842b2640c05a01475a34e5427874008a10db07` | Assistant-local exact integer execution PASS; no proof of full native implementation |
| `kurihara_k107_independent_manin_audit.py` | `a6cb5bb8e24943200d6b9aa2164d0b5f8bb7b694` | Syntax PASS; Sage authentic table required for execution |

The previously executed `sha599_short_certificate.py` and the seven local-only scripts are now exactly matched on GitHub by **Git's blob SHA**, not merely filename or line counts.

## Final synchronization — confirmed 2026-10-30

The user verified all seven restored files against `origin/main` with `EXACT_MATCH` and moved them into `/home/bsdadmin/bsd389_reconciled_20261030_201422`. Their `git pull --ff-only origin main` fast-forwarded `df4b0ae..ffcef89`; subsequent `git status --short` was empty, and `git log -1 --oneline` reported `ffcef89` on `HEAD -> main, origin/main, origin/HEAD`. Original stash untouched. **Issue #5 closed as completed.** Later status-documentation commits do not invalidate that successful synchronization; those can be fast-forwarded separately.

## User-local final step (completed; historical instructions below)

The Sage server will still have seven `??` untracked scripts. Because the files were now added to remote `main`, blindly running `git pull --ff-only` could fail again with "untracked working tree files would be overwritten". Move those seven files to a separate backup **after** comparing `git hash-object` to `origin/main:path`, then fast-forward pull. Do not `stash pop`, `stash drop` or overwrite other files. Keep [Issue #5](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/5) open until user-local synchronization confirmed.

## Mathematical boundaries

All imported code is research-stage source. Source recovery is **not** independent evidence that its mathematical conclusions hold. In particular the `p=599` finite-level coefficient `C2=543` has authentic user-reported PASS, but the supersingular Hecke/precision bridge and the Sha upper-bound theorem application still require independent audit in [Issue #4](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/4). No claim of complete BSD proof or unconditional vanishing of all Sha-primary components.
