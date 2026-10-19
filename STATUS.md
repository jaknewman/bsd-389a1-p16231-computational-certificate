# Verification ledger — updated 2026-10-19

Legend: **PASS (reported)** means a complete terminal log was supplied and checked in this project, not a formal proof of the underlying mathematics. **THEOREM / ALGEBRA** means a mathematical derivation documented in a named source. **OPEN** means not certified at repository publication time. **CONDITIONAL** means dependent on a stated hypothesis.

| Assertion | Status | Supporting resource / boundary |
|---|---|---|
| Modular-symbol / C01 algebraic comparison | Mathematical derivation written; publication review pending | `paper/c01_comparison_proof.md` |
| Manin/Shapiro comparison V62 | PASS (reported; partial transport oracle) | `verification/v62` |
| Signs and 67 scalar generator checks V63 | PASS (reported) | `verification/v63` |
| Checkpoint and source integrity V64 | PASS (reported) | `verification/v64` |
| Independent terminal J0=16014, J1=4703 | PASS (reported; 67/67 per moment) | `verification/v65` |
| Independent last-39,946-pair replay | PASS (reported); NOT a full replay | `verification/v65` |
| Original V19 executable identified by SHA | PASS (reported) | `data/HISTORICAL_MANIFEST.md` |
| V66 byte-identical rebuild | **NO**; different SHA | V66 original `31fe...`, rebuilt `c6d9...` |
| V66 functional equivalence | PASS on three disjoint 8-pair intervals | not equivalent to full equivalence |
| Arithmetic gate | PASS (reported after `ZZ(389)` compatibility fix) | `verification/arithmetic` |
| All archived chunk-to-checkpoint recompositions | **PASS (reported, full 263,429,130-pair archive)**; 514,511 chunks, 4,019 checkpoints and 9,759,143,225 sparse rows; final hash matches frozen SHA-256 | [`results/v19_full_chain_audit_2026-10-19.md`](results/v19_full_chain_audit_2026-10-19.md). No independent per-chunk mathematical re-evaluation. |
| All chunk contents computed by proven faithful code | **OPEN** formal machine/source provenance | SHA validates integrity against adjacent SHA files, not producer identity |
| Exact global equality J_V19 = J_ref | **OPEN final end-to-end certificate** | key conditional bridge |
| Level-3 native A2 computed independently | **NOT RUN** | correction based on algebraic bridge |
| Bound `Sha(E/Q)[16231^infinity] = 0` | **CONDITIONAL**, not yet a theorem established unconditionally by this repository | requires certified bridge, arithmetic gate and relevant theorem applicability |
| Exact equality `u_16231 = 1` | **NOT PROVED** | congruence modulo p does not imply exact p-adic equality |
| Full Birch–Swinnerton-Dyer conjecture for 389a1 | **NOT PROVED** | p-primary consequence is strictly narrower |

No output of a preflight, checksum-only audit or source-level formula check should be promoted to a global mathematical proof without explicit justification. V19 recomposition PASS is now recorded from the user-supplied final log. It certifies the reconstruction of historical checkpoint states from authenticated archived chunks, **not** correctness of every producer invocation or unconditional equality of the computed global sum to the mathematical reference functional.