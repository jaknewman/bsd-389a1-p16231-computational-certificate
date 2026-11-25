# BSD 389a1 — Three-prime exact zero-support data and high-rank obstruction (9 November 2026)

**STATUS:** An original computational result, fully reproducible with Python/C++ and no Sage, **NOT** a uniform reciprocity theorem, Sha finiteness/vanishing theorem, or a proof of complex rank-two BSD. No old rank/period/Sha certificates rerun.

## Summary of exact arithmetic

For E: y²+y=x³+x²−2x, use the certified full saturated Mordell–Weil basis P=(-1,1), Q=(0,-1) and the exact integral, 390-entry plus modular-symbol/Manin vector whose Néron normalization is uniquely determined by the archived m⁺(7/389)=−1 and m⁺(5/389)=−2. The integral vector is reconstructed independently via 1,559 Manin/plus/T₂ relations (rational eigenspace dimension one by mod-7 rank 389), and satisfies six independent additional Hecke operators *over Z*.

For each p, select good auxiliary q with
  q≡1 (mod p), a_q≡2 (mod p), v_p(#E(F_q))=1.
This forces nonidentity-unipotent Frobenius on E[p] and one-dimensional E(F_q)/p. Compute its local Mordell–Weil direction (P,Q) ∈ P¹(F_p) using full finite-field point operations. For every selected pair q<r, let
  D_{qr} = det([loc_q(P),loc_q(Q)]; [loc_r(P),loc_r(Q)]) (mod p);
  δ_{qr} = Σ_{a∈(Z/qr)×} m_E⁺(a/qr) log_q(a) log_r(a) (mod p).

### Newly executed results p=5, p=11
- p=5: **26** eligible q<4000; all **325** pairs. D=δ=0 for **49** pairs; D,δ both nonzero for **276**; **no mismatches**.
- p=11: first **10** of 15 eligible q<13000; **45** pairs. Both zero for **2**; both nonzero for **43**; **no mismatches**.
- Existing independently certified p=7 data: 11 eligible q, **55** pairs, with **9** both zero and **46** both nonzero.

Thus 425/425 checked pair zero indicators agree, at three different primes. **This is finite evidence, not a theorem for other q or other p.**

### Independent arithmetic checks

The C++ direct complete Kurihara sums were checked by a separately written Python finite sum for p=5 (41·61→4; 131·211→0; 41·251→3) and p=11 (397·991→1; 397·1321→9). Primitive-root choices can rescale nonzero values, so only vanishing and rank statements insensitive to local log units are interpreted canonically.

### Strong new non-factorization at TWO additional primes

Extend D and δ, arbitrarily but consistently, to alternating matrices indexed in increasing auxiliary-prime order (the actual δ_{qr} is symmetric in the unordered conductor pair; these alternating matrices are *formal*). Their ranks are:

| p | q count | rank(D) | rank(δ) | nonzero Plücker witness |
|---:|---:|---:|---:|---|
| 5 | 26 | 2 | **22** | q=(41,61,131,251), Plücker=4 mod5 |
| 7 | 11 | 2 | **10** | previously independently proved |
| 11 | 10 | 2 | **10** | q=(397,991,1321,2113), Plücker=5 mod11 |

At p=5, for q=(41,61,131,251) the Kurihara entries in increasing order satisfy
  δ12δ34 − δ13δ24 + δ14δ23 = 4·1 − 1·1 + 3·2 = 4 (mod 5).
At p=11, for q=(397,991,1321,2113):
  δ12δ34 − δ13δ24 + δ14δ23 = 1·8 − 9·0 + 3·10 = 5 (mod 11).

No rank-two determinant factorization of all δ_{qr} exists at these primes, even with nonzero per-prime multiplicative rescalings; they would preserve the Plücker equation. Their *zero sets* can still agree as observed.

## A rigorous mathematical consequence — and its hard limit

Fix p>=5, p≠389, with full residual image. Earlier Kummer–Chebotarev theorems prove the existence of infinitely many eligible nonidentity-unipotent pairs (q,r) with D_{qr}≠0. Therefore the following **unproved** pointwise comparison principle, if established independently for this E at a given p,

  for every such (q,r), D_{qr}≠0 ⇒ δ_{qr}≠0 (mod p),

would produce a genuine unit two-prime Kurihara witness. Under the source conditions of Kim's refined Selmer theorem and Castella–Sano's refined nonvanishing theorem, it would imply Sha(E/Q)[p∞]=0. If the principle held for all sufficiently large p, it would yield the missing uniform Sha support theorem after finitely many exceptional primes.

**This principle is NOT established by the 425 finite tests.** In particular, merely defining u_{qr}=δ_{qr}/D_{qr} for the nonzero checked pairs is tautological and provides no integral global Kato reciprocity or uniform nonvanishing. The simple separable normalizations u_qu_r have already been ruled out by Plücker at p=5,7,11. We do not claim a geometric or motivic meaning for the rank-22/10 formal matrices.

No known theorem reviewed here turns this empirical support pattern into a rank-two integral reciprocity for *all* p. Kim's rigidity/core-vertex results depend on the full global Selmer structure and hence do not bypass the unproved assertion that the strict Selmer obstruction Sha[p] vanishes.

The complex leading coefficient identity L''(E,1)/2=Ω_E·Reg(E) for predicted Sha=1 remains independently unproved, even if an all-prime p-primary Sha result were proved.

## Provenance and reproducibility

- Independently executed 9 November 2026: `modsym_integral_389.py`, `select_p5.py`, `select_p11.py`, `p5_kurihara_fast.cpp`, `p11_kurihara_fast.cpp`, `audit_p5_support.py`, `audit_p11_support.py`, `bsd389_kurihara_crossprime_audit_20261109.py`; full JSON output, source tables and execution logs in conversation ZIP `bsd389_p5_p11_kurihara_zero_support_20261109.zip`.
- Existing p=7 data: `paper/bsd389_GLOBAL_p7_55pair_support_rank10_fivechannel_2026-11-08.md`.
- Primary source: Chan-Ho Kim and Robert Pollack, *The refined Tamagawa number conjectures for GL₂* (updated March 2026), arXiv:2505.09121, Theorem 1.1 and §§3–5: https://arxiv.org/abs/2505.09121.
- Primary source: Castella–Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin* (Jan 2026), Theorem B: https://arxiv.org/abs/2601.14504.

**Verdict:** 425 finite zero-support matches across p=5,7,11 and high-rank non-decomposability are authenticated. The missing all-p Kurihara unit and exact complex BSD implication remain open.
