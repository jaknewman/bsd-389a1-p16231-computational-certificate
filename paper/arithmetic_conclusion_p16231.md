# Arithmetic closure for `389a1` at `p=16231`

**Research note — 2026-10-19. Author: Jerry Armando Kasa.**

**Status:** The *arithmetic implication* is established using Sage's published proved `p_primary_bound` theorem. The application to the historical global C01 number remains dependent on the archived computation implementing the mathematical reference functional faithfully. **This note does not claim a formally verified binary or full BSD.**

## 1. Data

```text
p = 16231                  p² = 263445361
E: y²+y = x³+x²−2x         conductor = 389
Mordell–Weil rank = 2       torsion = 1
Tamagawa product = 1        real components = 2
a_p = 128                   unit root alpha ≡ 128 (mod p)
residual representation surjective; p ordinary
minimal quadratic twist D = 1
Tate parameter at 389: valuation = 1
```

These gates were reported PASS in the certified arithmetic Sage terminal test. They satisfy Sage's documented conditions for its proved `Sha.p_primary_bound(p)` in rank greater than 1. The auxiliary Skinner–Urban prime condition is also consistent with `389 || N` and `v_389(q)=1`, but **Skinner–Urban is not necessary to deduce triviality from an upper bound of zero**.

## 2. Normalization and analytic coefficient

The ordinary p-adic L-series coefficient is `A2 = [T²] L_p(E,T)` for Sage's `eta=0`, `gamma=1+p`, `normalize='L_ratio'`, original curve (`D=1`) with its 2 real components. Sage's `_prec_bounds(3,3)` was reported as `[+Infinity, 2, 2]`: the level-3 coefficient `A2^(3)` determines `A2` modulo `p²`.

Independent finite-level computation:

`A2^(2) ≡ 1199*p ≡ 19460969 (mod p²)`.

The separate mathematical cyclotomic comparison gives:

`A2^(3)−A2^(2) ≡ p*J_ref/(4*alpha²) (mod p²)`.

The authentic archival terminal contraction V65 gives `J_V19=(16014+4703)%p=4486`. The exact source-to-specification audit of C01, 390/390 rational cusp-divisor Manin relations and bounded original-data comparisons substantiate `J_V19=J_ref`; historical binary-to-source/execution provenance is the remaining explicit computational trust requirement.

If the archived `J_V19` faithfully equals `J_ref`, then

```text
(4*128²)^(-1) mod p          = 9362
4486 / (4*128²) mod p        = 8335
A2/p mod p                    = (1199+8335) mod p = 9534
A2 mod p²                     = 154746354 = 9534*16231
v_p(A2)                      = 1
```

## 3. Algebraic BSD factor: independent p-adic regulator

Sage's `Sha.an_padic(p)` uses, in the good ordinary rank-`r` case,

`B_p = Tam * Reg_p * (1−alpha^(−1))² / (Tors² * log_p(1+p)^r)`.

The independent p-adic regulator computation reports

`Reg_p = 1930*p³ + 2051*p^4 + 6298*p^5 + O(p^6)`.

Since `v_p(log_p(1+p))=1`, with rank `r=2`, we deduce `v_p(B_p)=3−2=1`.

Furthermore,

```text
alpha^(-1) mod p               = 5199
(1−alpha^(-1))² mod p         = 10820
B_p/p mod p                    = 1930*10820 mod p = 9534
```

Thus `B_p ≡ 9534*p (mod p²)`, with the same leading nonzero digit as `A2`.

## 4. Exact arithmetical implication — no need for exact u_p=1

If the analytic coefficient has the certified congruence above, then

`A2/B_p ≡ 9534*(9534)^(-1) ≡ 1 (mod p)`,

hence `v_p(A2/B_p)=0`. This is **unit status**, not exact p-adic equality `A2/B_p=1`.

In Sage's published `sha_tate.py`:

```python
# an_padic: lstar = lp.series(n, quadratic_twist=D, prec=r+1)[r]
# an_padic: shan = lstar / bsdp
# p_primary_bound: shan = self.an_padic(p, prec=0, use_twists=True)
# p_primary_bound: return shan.valuation()
```

The documented `p_primary_bound` method produces a **proved** upper exponent `e` even for `r>1`, with `#Sha(E/Q)[p^infinity] ≤ p^e`, under verified hypotheses. For `e=0` the bound is 1, and therefore

`Sha(E/Q)[16231^infinity] = 0`.

**Conditional computational theorem.** Assume the historical C01 run faithfully computes the reference functional `J_ref`, with the archived level-2 and regulator computations in the stated Sage normalization. Then Kato's proved upper bound yields `Sha(389a1/Q)[16231^infinity]=0`.

This is a *single-prime* statement, strictly weaker than full BSD for 389a1. In particular, it **does not** imply the exact identity `u_16231=1` at all p-adic precisions.

## 5. Evidence and residual obligations

**Completed:** provable rank-2/MW basis and local gates (reported Sage run); V19 exhaustive chunk-to-checkpoint replay PASS; V65 independent full terminal moment contractions; original C01 source and JSON hashes; exact 390/390 cusp-divisor relation identities; mathematical transport lemma; bounded real-export native/aggregated equality tests.

**Open for unconditional publication:** a sufficiently transparent audit or independently reproducible certificate connecting the historical native binary to the *whole* reference computation (not simply archived sidecar checksums); review of exact Sage-version behavior/precision; external peer review of the source-to-formula normalization. Running `E.sha().p_primary_bound(16231)` directly has **not** been claimed and may trigger a full expensive L-series calculation.

## Primary references

- SageMath, `sha_tate.py`, `Sha.p_primary_bound`, `Sha.an_padic`: https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/sha_tate.py
- SageMath ordinary p-adic series and proven `_prec_bounds`: https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/padic_lseries.py
- [Independent original-export certificate](../results/v11_export_exact_manin_shapiro_certificate_2026-10-19.md)
- [V19 complete recomposition certificate](../results/v19_full_chain_audit_2026-10-19.md)
- [Source-to-specification proof](c01_source_to_specification_audit.md)
