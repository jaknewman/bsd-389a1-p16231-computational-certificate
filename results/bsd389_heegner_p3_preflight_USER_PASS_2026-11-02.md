# E389a1: user-run Sage p=3 Heegner arithmetic preflight PASS

**2026-11-02.** Verbatim user Ubuntu Sage output reproduced from this conversation. No direct access to user's local log bytes or SHA256 of the log; not falsely presented as an authenticated file hash.

```text
HEEGNER_CURVE_AND_CONDUCTOR_PASS
HEEGNER_SPLIT_389_INERT_C41_ELL5_PASS
HEEGNER_KOLYVAGIN_C41_ADMISSIBLE_PASS -3
HEEGNER_LOCAL_ELL5_GROUP_ORDER_PASS 9
HEEGNER_P3_ARITHMETIC_PREFLIGHT_PASS
BOUNDARY_STEIN_TABLE_NONVANISHING_NOT_RECOMPUTED
BOUNDARY_SHA3_NOT_INDEPENDENTLY_CERTIFIED_BY_THIS_SCRIPT
PIPELINE_STATUS=0
```

Source: [verification/bsd389_heegner_stein_p3_preflight.sage](../verification/bsd389_heegner_stein_p3_preflight.sage).

## Source audit: Stein's 2009 preliminary article

William Stein, *Heegner Points on Rank Two Elliptic Curves* (preliminary version, October 2009):
<https://wstein.org/misc/sagedays18_papers/stein-heegner_points_on_rank_two_elliptic_curves.pdf>

- **Theorem 2.7, printed p. 5**: under the article's standing hypotheses, a nonzero local Kolyvagin derivative `z_{c,sigma,ell}` implies rank <=2; when MW rank=2 and q=p is prime, `Sha(E/Q)[p]=0`.
- **Table 3.2, printed p. 9** lists `E=389a1, D=-7, q=3, ell=5`: first nonzero derivative conductors `41,59,83,587`. In particular the c=41 witness is explicitly listed as nonzero.
- **Warning immediately before Table 3.2, printed p. 7–8**: the listed computations can fail to be rigorous when q divides the modular degree. The paper identifies exceptional pairs `(389a1,5), (571b1,3), (655a1,3), (681b1,3), (997c1,3)`. **The case (389a1,3) is NOT among the caveated pairs.**
- The text states the mod-q Galois representation is surjective for all cases under consideration. The paper assumes analytic rank of E is 2 and analytic rank of the relevant quadratic twist is 1; review these assumptions when exporting the claim as a fully independent proof.

## Precise status

1. **User-executed reproducible arithmetic preflight: PASS.** It checks E model, conductor, splitting/inertness, `a_41=-3`, 3-admissibility, and `#E(F5)=9`.
2. **Published nonvanishing evidence:** Stein's Table 3.2 asserts `z_(41,sigma,5) != 0` for (389a1, D=-7, q=3, ell=5), and the author's stated nonrigorous modular-degree exception does not apply.
3. **Conditional mathematical consequence from published proof:** accepting the paper's computed witness, and confirming its standing theorem hypotheses, Theorem 2.7 implies `Sha(E/Q)[3]=0`, hence `Sha(E/Q)[3^infinity]=0`. This is **literature-based evidence**, not an independent user replay of the quaternionic derivative.
4. The Sage `p_primary_bound(3)` shortcut is **not applicable** to this rank-two curve: Sage's official documentation imposes rank zero at p=3. Do not present it as a substitute independent p3 certificate.

This source-based route is separate from the genuine Sage 10.9 p-primary upper-bound results for p=5,7,11,13,107; neither yields all-prime uniform Sha finiteness.
