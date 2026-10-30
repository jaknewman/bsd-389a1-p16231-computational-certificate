# p=599 finite cyclotomic certificate and conditional supersingular bridge (2026-10-30)

> **Version integrity resolved:** The current GitHub verifier matches the exact user-executed file in the recovered stash: Git blob SHA1 `9acda8de4c526f96b96ad4e89847c782933c1528` (7,053 UTF-8 bytes). The historical PASS transcript thus has exact source provenance, but it is **not a fresh GitHub Actions run**. The analytic and theorem applicability review remains OPEN ([issue #4](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/4)).

**Status: finite arithmetic checks PASS (user-run); supersingular analytic bridge DERIVED, NOT independently certified; Sha[599^infinity] remains REVIEW-REQUIRED.** Do not label this as an unconditional proof or as the successful execution of `p_primary_bound(599)`.

## User-run evidence

- The finite-level plus-symbol, tame-trivial Mazur–Tate calculation with the authentic 390-entry Manin table (SHA256 `fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8`) produced `C0=0, C1=0, C2=543 (mod 599)`.
- Independent native C++ and Python full-convergent calculations agree on 179,101 sign-pairs, 1,924,081 continued-fraction edges and checksum 779927018. All 598 Hecke fibres vanish in the mod-599 test.
- Sage: rank 2 proved; `gens_certain() == True`; generators `(-1:1:1), (0:-1:1)`; torsion order 1; Tamagawa list `[1]`; `a_599=0` and supersingular; `E.galois_representation().is_surjective(599) == True`; `real_components()=2`; eclib positive-symbol scaling 1.
- Regulator coordinates: `(571*599^2 + O(599^3), 416*599^3 + O(599^4))`; dividing by `log_599(600)^2` gives first residue 571 and second valuation 1.
- On the user's Sage machine the lightweight script `verification/sha599_short_certificate.py --table ~/bsd389_p599_manin_table.txt --sage` printed `LIFT_WEIGHT_IDENTITIES_PASS`, `P599_LEVEL_P2_INDEPENDENT_PASS`, `ANALYTIC_FROBENIUS_DERIVED F0_modp 571 F1_modp 0`, `SAGE_ARITHMETIC_GATES_PASS`, and `SHA599_SHORT_CERTIFICATE_FINISHED`. It **does not** enumerate level p^3 or call `p_primary_bound`.

## Conditional finite-to-analytic derivation — check carefully

Let p=599, gamma=1+p, and for units a modulo p^n write a=omega(a)gamma^{j_n(a)}. Put w_n(a)=binom(j_n(a),2), S_n(a)=[a/p^n]^+ in the Sage/eclib normalization. At n=3 set

```text
A3 = sum_{a mod p^3 unit} w_3(a) S_3(a)
B3 = sum_{a mod p^3 unit} w_3(a) S_2(a mod p^2).
```

Using the Hecke relation `sum_t S_3(b+t p^2) = a_p S_2(b)-S_1(b) = -S_1(b)`, constancy of w3 mod p on each p^2-fibre, and `sum_{j=0}^{p-1} binom(j,2) == 0 (mod p)`, the proposed conclusion is `A3 == 0 (mod p)`. The exact sum of weights of the p lifts of a unit b mod p^2 is `p*w_2(b) (mod p^2)`, so `B3/p == C2 (mod p)`. Both assertions require the indicated p-integrality and the precise conventions for j_n and S_n.

For Frobenius Phi=[[0,-1/p],[1,0]], and the Sage Dp-valued normalizations including division by `real_components()=2`, the finite n=3 projection is

```text
F0^(3) = [2*A3-(p-1)*B3/p] / [2*(p+1)^2]
F1^(3) = [-(p-1)*A3-2*B3] / [2*(p+1)^2].
```

If the Hecke and lift congruences hold, `F0^(3)==C2/2==571 (mod p)`, `F1^(3)==0 (mod p)`. Sage's `_prec_bounds(3,3)=[+Infinity,-1,-1]` is **alpha-adic**, not initially p-adic. With `alpha^2=-p`, an error in `O(alpha^-1)` has integral scalar part and an alpha coefficient in p^-1 Zp. The Frobenius projection then makes both coordinate errors divisible by p. This propagation has been reasoned from Sage code but has not been independently certified as a formal proof of the analytic bridge.

## Theorem and status boundary

In the supersingular branch of Sage's `sha.an_padic`, `bsdp=reg/log_p(1+p)^r` (Tamagawa/torsion factors 1 here) and `Dp_valued_series(n=3,prec=3)` supplies the analytic leading coefficient. If that coefficient is certified with enough precision to be a unit, the theorem underlying Stein–Wuthrich's `p_primary_bound` is a potential way to bound the p-primary Sha by 1. **However the short script does not execute the bound and an independently reviewed derivation of the exact series/precision/theorem applicability is still outstanding.** Present `Sha(E/Q)[599^infinity]=0` only as a **conditional mathematical claim**, not as a software-verified theorem.

The previous `p_primary_bound(599)` process PID 95133 consumed ~11 GiB RSS, was suspended and subsequently disappeared without a logged result; no output `SHA599_PROVEN_BOUND` exists. The full two-auxiliary-prime Kurihara delta599 is also not computed.

## Reproduce on the user's Sage server

```bash
python -u verification/sha599_short_certificate.py \
  --table ~/bsd389_p599_manin_table.txt --sage \
  2>&1 | tee ~/bsd389_p599_short_certificate.log
```

The table is external to the repository and is pinned by its SHA256. Do not infer full computational reproducibility without that file.

## External review questions

1. Check the p^3 Hecke formula with exact base-point/normalization and every p-integrality assumption.
2. Prove the lift weight congruence and its compatibility with the Sage `teichmuller`, `gamma=1+p` parametrization.
3. Audit `measure`, the alpha-adic bound and Frobenius coordinates against the user's installed Sage version (not just current develop).
4. Verify the exact statement and local hypotheses of the Kato/Stein–Wuthrich upper-bound inequality for supersingular p=599, and that the projected coefficient is the one used there.
5. Have another implementation or independent mathematical reviewer certify these steps before advancing the status to **SHA599_PROVED**.

## References

- Stein–Wuthrich, *Algorithms for the Arithmetic of Elliptic Curves Using Iwasawa Theory*, Math. Comp. 82 (2013), esp. Algorithm 11.1: https://wstein.org/papers/mcom2649-iwasawa-alg.pdf
- Sage: https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/padic_lseries.py
- Sage: https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/sha_tate.py
