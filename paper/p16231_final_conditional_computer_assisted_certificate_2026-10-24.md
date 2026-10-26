# 389a1 at p=16231 — final computer-assisted certificate and publication boundary

**Date:** 2026-10-24  
**Status:** **CONDITIONAL COMPUTATIONAL THEOREM**, with fully auditable archived
source/evidence; **NOT** an unconditional claim of full BSD or exact
p-adic quotient 1.  
**Target:** E: y²+y=x³+x²−2x over Q; N=389, p=16231.

This certificate gives the exact chain of sufficient propositions,
the numerical dependencies, and the distinction between
source-level algebra, historical computational evidence, and missing
independent verification of every original producer invocation.
It intentionally does not call the expensive full Sage
`E.sha().p_primary_bound(16231)` or `lp.series(n=3)`.

## Conditional theorem

**Theorem (conditional on the finite certified analytic inputs).**
Suppose the 2026-10-19 original V11/V19 archived computation,
whose executable/source/export hashes are pinned below,
faithfully evaluates the independently defined C01 reference
functional `J_ref` at p=16231, and that the recorded exact
Sage/eclib level-2 and regulator computations are faithful with the
Sage 10.9 normalization described below. Suppose also that the
reported Mordell–Weil rank, good ordinary reduction and surjectivity
checks are valid. Then

`Sha(E/Q)[16231^infinity]=0`.

There is **no assertion** here that every hypothesis has been
formally proved by independently rerunning its original computation,
nor that `u_16231=1` as an element of `Q_16231`.

### Proof, step by step

**1. Pinned mathematical objects and local arithmetic.**
Sage 10.9's previously executed arithmetic gate reports:
`rank(E)=2`, `#E(Q)_tors=1`, conductor 389,
`Tam(E)=1`, real components 2, good ordinary at 16231,
`a_16231=128`, residual representation surjective,
and minimal quadratic twist `D=1`. The p-adic Frobenius unit
root `alpha` satisfies `alpha²-128alpha+p=0`,
`alpha=128 (mod p)`; one mod-p² lift is `179060520`.
Sage's `_prec_bounds(3,3)=[+Infinity,2,2]`, so the level-3
T² coefficient determines the *actual* L_p coefficient
modulo p². This depends on the proven error estimate implemented
in Sage, not on convergence by wishful extrapolation.

**2. Define `J_ref` independently of the V19 output.**
Set `D_x=[1,x;0,p²]` for `x=a+pb`,
`1<=a<p`, `0<=b<p`; let
`m(r)=E.modular_symbol(sign=+1,implementation='eclib',normalize='L_ratio')(r)`.
For positive-determinant integral matrices G define
`F(G)=m(G.infinity)-m(G.0)`.
Set `Pmat=diag(p,1)`, `beta_t=[1,t;0,p]` and
`M0(G)=F(G)-alpha^-1 F(Pmat G)`,
`M1(G)=alpha^-1 sum_(t=0)^(p-1) t F(beta_t G)`
in F_p.
Let
`u=b*a^-1-((a^(p-1)-1)/p) mod p`,
`w=(2u-1)*a^-1 mod p`,
and `kappa=(omega(a)*(1+p)^u-x)/p² mod p`.
Then

`J_ref=-sum_(a,b)w(a,b)*(M1(D_x)-kappa(a,b)*M0(D_x)) mod p`.

This is an independent mathematical definition and does not
incorporate or assume the historical value 4486.

**3. Universal Manin–Shapiro source/functional identity.**
For `h=[A,B;C,D] in Gamma0(389p)`, the two moments satisfy

`M0(hG)=M0(G)`,
`M1(hG)=(-AB)*M0(G)+(A²)*M1(G) mod p`.

The proof follows from the Hecke eigenidentity and the
permutation `s=(B+tD)/A (mod p)`.
The moment action composes by
`(q,r)∘(q',r')=(q+r*q',r*r')`.
All original 390 Manin cusp identities and 2012 relation matrices
have been checked by exact arithmetic. The full 2012×16232
relation/coset transport audit has **actually been run**, checking
all 32,658,784 transitions over Z and modulo p, including
2012 exceptional inputs and 2012 exceptional outputs,
with exact native transport checksum `13306773584111587599`.
The native C01 source's direct branch contributes
`(qW-K,rW)` and its relation branch contributes
`e*((q+r*qi)W-K,r*ri*W)`, with
`W=-sum w` and `K=-sum w*kappa`.
Its continued fractions telescope from infinity to x/p².
These are exactly the pushforwards of the `J_ref` summands.
The universal algebra does **not** rest on sample frequency.

**4. Historical numeric evaluation.**
The original V11 ELF at SHA-256
`31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63`
was exactly reproduced byte-for-byte by GCC 13.3 `-O2`
from the pinned V11 source. Original/export source SHA is
`9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8`.
The user-run independent V19 archived-output recomposition covered
514,511 full chunk intervals over 263,429,130 pair IDs,
4019 saved checkpoints and 9,759,143,225 sparse lines.
The final double-moment state SHA is
`5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e`.
A deterministic 57-chunk 28,682-pair sample was also *reproduced
from the authentic original binary byte-for-byte*.
The separate Sage/eclib V65 table and exact independent
NTT/CRT contractions gave
`J0=16014`, `J1=4703`, hence
`J_V19=4486 mod 16231`.

Under the stated faithful-historical-computation hypothesis,
the source-level identity from step 3 identifies
`J_ref=J_V19=4486`. The full archived recomposition
authenticates stored outputs, not independently re-evaluated
mathematical contributions of all 514,511 blocks.

**5. Finite-level Sage p-adic L-series formula.**
For the Sage 10.9 ordinary `eta=0`, `D=1`, `gamma=1+p`
measure
`mu_n(y)=alpha^-n*(m(y/p^n)-alpha^-1*m(y/p^(n-1)))`,
the `T²` coefficient at level n is a sum of
`binom(j,2)*mu_n`, divided by two real components.
For each level-2 `x=a+pb`, its level-3 lifts
`y=x+p²c` satisfy
`j=u+p*v`, `v=(c-kappa)*a^-1 mod p`.
Distribution of the measures, the binomial identity mod p²,
and the Hecke relation imply, **for every x**,

`(A2^(3)-A2^(2))_x =
    p*[ -w*(M1(D_x)-kappa*M0(D_x)) ]/(4*alpha²) mod p²`.

Summing gives

`A2^(3)-A2^(2)=p*J_ref/(4*alpha²) mod p²`.

The local direct-Sage oracle has been run on all 16231 lifts
for `(a,b)=(1,0)` and `(2,3)`, directly comparing native C01,
independent V65 moments, and Sage/eclib finite-level measures;
both PASS. In the second case `kappa=11458 != 0`,
`J(2,3)=11725` and `Delta/p=15428`.
These tests confirm the normalization at representative residues,
not the global 263-million-pair sum.

**6. Independent level-2 value and level-3 precision.**
The historical Sage/eclib V54/V61 level-2 computation
covers all required half-range residues, with 254/254 block
digest/reduction audits. The plus-modular-symbol pairing
`m(-r)=m(r)` permits the half-range over a with its factor two
cancelling the real-components divisor two; the code's
`sum_u binom(u,2)=binom(p,3)` is exact.
The recorded output is

`A2^(2)=19460969=1199*p (mod p²)`.

Using `alpha=128 mod p` and `J_ref=4486 mod p`:

`(4*128²)^(-1) mod p=9362`,
`4486*9362 mod p=8335`, and
`A2^(3)/p=1199+8335=9534 (mod p)`.

Thus `A2^(3)=154746354 (mod p²)`.
By Sage's precision guarantee for n=3, the *true p-adic
coefficient* `A2=[T²]L_p(E,T)` has the same residue
and valuation `v_p(A2)=1`.

**7. Independently normalized p-adic regulator.**
The reported exact Sage 10.9 computation gives
`Reg_p=1930*p³+2051*p⁴+6298*p⁵+O(p⁶)`.
For r=2, torsion=1 and Tamagawa product=1, define

`B_p=Reg_p*(1-alpha^-1)^2/(log_p(1+p)^2)`.

As `log_p(1+p)/p=1 mod p`, one has
`v_p(B_p)=1`, with

`B_p/p=1930*(1-5199)^2=9534 (mod p)`.

Consequently `v_p(A2/B_p)=0`, and its first digit
is `A2/B_p=1 (mod p)`. This digit identity is
**not** exact equality in Q_p.

**8. The proved p-primary upper bound.**
The actual Sage 10.9 `Sha.p_primary_bound(p)` source
uses the Galois/reduction gates and returns the valuation of
`Sha.an_padic(p,prec=0,use_twists=True)`.
For this curve the previously checked minimal twist is `D=1`.
The method's documentation states that, if its hypotheses pass,
the returned integer `e` is a **proved upper exponent**
`#Sha(E/Q)[p^infinity] <= p^e` even for rank >1.
The user-run arithmetic audit verified the gates, installed
Sage source fingerprint, and normalization, but **did not
directly invoke** `p_primary_bound(16231)`.
The prior steps substitute a mathematically derived,
conditionally trusted analytic coefficient into precisely the
same leading-term valuation, giving `e=0`. Under the theorem's
hypotheses, `#Sha(E/Q)[16231^infinity]<=1`,
so the p-primary group is zero. QED, conditional as stated.

## Evidence taxonomy and limitations

| Link | Status | What is actually established |
|---|---|---|
| Exact 390 Manin cusp identities | PASS | all rational cusp divisor identities for the 390 original reps |
| 2,012 × 16,232 relation transports | EXHAUSTIVE PASS | exact-Z Gamma0 membership and native mod-p two-moment matrices; all exceptional classes |
| Native V11 → archived outputs | REPRODUCIBLE BUILD + 57-SAMPLE PASS | binary SHA-identical rebuild and 57 original producer chunk reruns |
| All V19 chunk data → saved checkpoints | EXHAUSTIVE ARCHIVE PASS | *recomposition* of all 514,511 archived chunks, not regenerated native arithmetic of each chunk |
| V19 final checkpoint → `J` | INDEPENDENT TERMINAL PASS | 67 per-generator J0 and 67 J1 eclib/NTT contractions, authenticated table state |
| V54/V61 level-2 `A2^(2)` | ARCHIVED RECOMPOSITION PASS | 254 level-2 checksummed blocks; exact original run not reproduced end-to-end |
| C01/Sage analytic formula | ALGEBRAIC DERIVATION + TWO DIRECT LOCAL PASSES | universal formula and two 16,231-lift direct tests including nonzero kappa |
| p-adic regulator and Kato/Sage hypotheses | REPORTED SAGE PASS | rank 2, surjective at p, precision n3 and `B_p/p=9534` |
| Direct `lp.series(n=3)` and `Sha.p_primary_bound(16231)` | NOT RUN | their outcome inferred *conditionally*, not observed |
| All original 263m pairs independently recomputed | NOT RUN | trusted historical computing base remains |
| Exact p-adic `u_p=1` | NOT PROVED | only `u_p=1 (mod p)` |
| All-prime `Sha=0` / full complex BSD | NOT PROVED | not implied by one p-primary result |

## Reproducible final integrity self-audit

From the local repository with the original historical V11 executable
still present on IONOS:

```bash
git pull --ff-only
python -u scripts/audit_p16231_final_certificate.py
```

The verifier checks every available small original source and
log SHA-256, original byte-identical rebuild report, V19 chain
and 57-chunk producer sample transcripts, archived V61/V65
mathematical invariants, exact mod-p arithmetic, and the
presence of Kato/Sage and full Shapiro run reports.
It prints `FINAL_CERT_ARCHIVED_EVIDENCE_AND_ARITHMETIC_PASS`
**only for this evidence/arithmetic audit**, followed by
a prominent *conditional theorem* and publication-boundary warning.
The script cannot turn historical logs into a formal
machine-code proof; it is a convenient independent manifest check.

## Source code and archived reports

- [Universal algebra and precise Sage source bridge](c01_shapiro_universal_transport_and_sage10_9_2026-10-24.md)
- [32,658,784 Shapiro transport PASS](../results/c01_all_32658784_shapiro_transports_PASS_2026-10-24.md)
- [Original V11 build/V19 provenance review](v11_v19_original_provenance_final_review_2026-10-24.md)
- [Full original V19 chain log](../historical/provenance/v19_chain_full.log)
- [Sage local analytical nonzero-kappa (2,3)](../results/local_sage_level3_c01_a2_b3_nonzero_kappa_PASS_2026-10-24.md)
- [Original level-2 254/254 audit](../results/v54_v61_all_254_chunks_ionos_PASS_2026-10-24.md)
- [Sage 10.9 arithmetic theorem gate](../results/kato389_sage10_9_terminal_pass_2026-10-19.md)
- [Sage 10.9 p-adic L-series implementation](https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/padic_lseries.py)
- [Sage 10.9 proved p-primary bound](https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/sha_tate.py)

---

## Addendum — 2026-10-26: full independent scalar outer sum PASS

The initial 2026-10-24 certificate assumed the historical V19 producer had faithfully computed the mathematical reference J_ref. This is now **substantially independently corroborated** by a second, completely executed algorithm, not merely by an increased sample size.

The user executed `verification/independent_c01_scalar_J.cpp` on the whole domain and supplied:

```text
INDEPENDENT_SCALAR_CHECKPOINT_PASS next=263429130 sum_mod_p=4486 of=263429130
INDEPENDENT_SCALAR_INTERVAL_PASS start=0 end=263429130 J_mod_p=4486
INDEPENDENT_SCALAR_GLOBAL_J_4486_PASS pairs=263429130
FULL_STATUS=0 0 0
```

This second method uses dense **dual scalar moments** and evaluates all 263,429,130 pair contributions directly; it does not reconstruct or read the old sparse C0/C1 producer, V19 chunk files or old global state. It shares only the independently evaluated V65 Sage/eclib moment table (using the audited NTT/CRT kernel) and the original mathematically audited Manin export. Both local (1,0) and nonzero-kappa (2,3) analytic Sage/eclib oracles passed before the full run.

**Updated numeric fact:** Two different full-corpus accumulation algorithms return `J=4486 mod 16231`. The previous unreplicated *historical numerical execution* is no longer a necessary **sole** source of the scalar number. The derivation of `J_ref=4486` as a computer-assisted result now rests on the demonstrated independent full run, correctness of the dual-evaluation source and shared authenticated symbolic/eclib inputs, and the universal algebraic C01/Sage identity.

The other mathematical gates remain: archived V54/V61 n=2 coefficient, Sage 10.9 n=3 precision and Hecke normalization, independent p-adic regulator and rank/surjectivity, and the actual proved Kato/Sage p-primary bound theorem. Those were audited but the full `lp.series(n=3)` and direct `E.sha().p_primary_bound(16231)` were not run. The complete second-run log, checkpoint and executable SHA still merit preservation for independent researchers. This update is **not** a proof of full BSD and cannot upgrade `u_p=1 mod p` to exact p-adic equality.

Evidence: [second full independent scalar run](../results/independent_scalar_J_global_263429130_pairs_PASS_2026-10-26.md), [dual-scalar source](../verification/independent_c01_scalar_J.cpp), [two local pilot tests](../results/independent_scalar_J_two_pilots_PASS_2026-10-26.md).

---

## Addendum — 2026-10-26: full second level-2 and regulator calculations PASS

The complete independent scalar C01 `J=4486` recomputation was documented above. Two more independently implemented computations have now finished successfully on the user's Sage-enabled Ubuntu server:

**1. Full level-2 `A2^(2)`:** Instead of V61's Fermat-quotient indexed `x=a+p*b`, the new `verification/independent_p16231_level2_u_enumeration.py` exhaustively runs its own cyclotomic exponent `u` on all 8,115 plus-symmetry representatives: `x=omega(a)*(1+p*u) mod p²`, `omega(a)=a^p mod p²`. It evaluates 131,698,335 nonzero-weight Sage/eclib modular symbol terms over 131,714,565 indexed residues. The user-reported output at `8115/8115` states `R2=79629286`, `R1=0`, `A2^(2)=19460969=1199p mod p²`, `LEVEL2_FULL_STATUS=0 0`. Thus the complete level-2 numerical value no longer depends solely on the earlier V61 iteration/chunks. It still shares the Sage/eclib normalized modular-symbol implementation. Evidence: [full second level-2 report](../results/independent_level2_u_full_131714565_residues_PASS_2026-10-26.md). New separate per-a and all-V61-block checksum auditor has been published but not yet run.

**2. Regulator:** `verification/independent_p16231_regulator_two_height_algorithms.py` compared Sage 10.9 `padic_height` (sigma method) and `padic_height_via_multiply` (alternate method) on the two rank-2 generators. The user-reported transcript records exactly matching `h(P),h(Q),h(P+Q),h(P-Q)` and polarized determinant modulo p^5, `Reg_p/p³=1930 mod p`, plus BSD factor `B_p/p=9534 mod p`, with status `0 0`. These methods share underlying Sage arithmetic but compute heights by different algorithms. Evidence: [two-height comparison](../results/independent_level2_u_firstblock_and_two_height_regulator_PASS_2026-10-26.md).

**Updated numerical chain:**

`J=4486 (two full global C01 computations)`;

`A2^(2)/p=1199 (two full level-2 computations)`;

`J/(4*128²)=8335 mod p`;

`A2^(3)/p=(1199+8335)=9534 mod p` (via the algebraically derived universal C01/Sage bridge, **not** full direct level-3 Sage execution);

`B_p/p=9534 mod p` (two different Sage height algorithms).

These now distinguish verified computation-level redundancies from still-shared theorem/normalization dependencies. They reinforce the claimed computer-assisted **conditional p-primary Sha consequence**, but cannot upgrade the quotient congruence `1 mod p` to an exact p-adic identity, and do not establish the global BSD conjecture. Publication still requires careful independent mathematical and machine-environment audit; direct Sage `lp.series(n=3)` and `Sha.p_primary_bound(16231)` have not run.

---

## Addendum — 2026-10-26: 8,115-row full level-2 archive cross-audit PASS

The independent cyclotomic-u level-2 complete recomputation described above was followed by an independent read-only audit of **all 8,115 generated row checkpoints** and a **block-for-block comparison with all 254 old V61 chunks**, each with verified checksums. The user-executed audit returned `INDEPENDENT_U_FULL_1199P_EVIDENCE_AND_V61_254_BLOCK_AGREEMENT_PASS` and process exit status `0 0`.

Total independently recomputed mathematical domain: 131,714,565 indexed residues, 131,698,335 nonzero-weight eclib symbol evaluations; level-2 raw R2=79,629,286, R1=0; `A2^(2)=19,460,969=1199p (mod p²)`.

The source, row-checkpoint Merkle-like ordered digest, old V61 ordered block digest and complete run log SHA-256 are captured in the [full evidence audit certificate](../results/independent_level2_u_full_checkpoint_audit_PASS_2026-10-26.md). The resulting numerical level-2 claim is fully reproduced and audited, not merely the old V61 archive recomposed.

**Residual conceptual gate:** Both independent complete level-2 algorithms rely on Sage/eclib modular symbols. The central high-p analytic identification of the complete C01 scalar with Sage's level-3 T² coefficient is derived algebraically and checked at two local p=16231 oracles, but full direct n=3 series evaluation at p=16231 has not been carried out. A new **UNEXECUTED** small-prime direct finite n2/n3 oracle regression is available at [bridge_local_small_prime_n2_n3_direct.py](../verification/bridge_local_small_prime_n2_n3_direct.py) to test the orientation, Teichmüller lifts, and the 1/4 normalization independently of the high-p Shapiro accumulators.

---

## Addendum — 2026-10-26: direct Sage n=3 bridge regressions at p=5 and p=7 PASS

A standalone, newly authored small-prime independent finite-level checker computed n=2 and n=3 ordinary modular-symbol measures with Sage/eclib, the scalar C01 M0/M1 reference J directly, and Sage's actual n=3 quadratic coefficient. The user's reported execution passed all three comparisons for both test primes, with `BRIDGE_STATUS=0 0`: 

- p=5: `alpha=7`, `A2(n2)=14`, `A2(n3)=24`, `J=2 mod5`, `delta=10 mod25`, predicted `p*J/(4alpha²)=10 mod25`, direct Sage n3 comparison PASS.
- p=7: `alpha=16`, `A2(n2)=19`, `A2(n3)=33`, `J=4 mod7`, `delta=14 mod49`, predicted `p*J/(4alpha²)=14 mod49`, direct Sage n3 comparison PASS.

The new explicit [universal correction lemma](c01_sage_n3_minus_n2_universal_lemma_auditable_2026-10-26.md) derives the `1/4` coefficient from the cyclotomic binomial increment and two real components, cancels the lower moment by distribution, and identifies the correction with the two C01 moments using the Hecke relation and cusp orientation. Its assumptions and independent source-to-reference computational gate are written separately. The small-prime test data and provenance are archived in [direct p5/p7 test certificate](../results/bridge_small_primes_5_7_direct_n2_n3_sage_PASS_2026-10-26.md).

**Boundary:** Two exact small-prime comparisons with genuine Sage level-3 coefficients provide strong regression evidence for the algebraic identity; they do not constitute a proof by finite testing or a full Sage level-3 computation at p=16231. The resulting p-primary Sha application still requires explicit validation of all ordinary, surjectivity, source-to-reference, and Sage precision hypotheses. Exact p-adic equality u_p=1 or full all-prime BSD remains unproved.

---

## Addendum — 2026-10-26: source-to-reference formal Manin/Shapiro audit

An independent exact-integer/rational review of the original SHA-pinned 390-representative JSON verified **390/390 cusp-divisor identities** with **2012 relation terms** (67 identity generator terms, 1945 non-generator relation terms) and determinant-one relation matrices, all over exact rational cusps without Sage/eclib. This is a review of the immutable relation data, not a new p-adic series computation. A self-contained reproducible [Python auditor](../verification/audit_c01_exact_manin_cusps_and_exceptional_cosets.py) has been committed but awaits an actual run on IONOS.

Exact matrix analysis also identified explicit high-p exceptional transport witnesses: pair ID 38 crosses an inner infinity Shapiro coset once; pair ID 67 crosses an outer infinity coset once and inner infinity cosets 66 times. In all six tested pair-ID traces (0,38,67,16234,middle,last), the integer transport factors lie in Gamma_0(389*16231). The formal matrix-duality proof of M0/M1 and the K-term sign is written in [source-to-reference formal audit](c01_shapiro_formal_duality_and_exceptional_audit_2026-10-26.md).

A new [adversarial local direct Sage n3-versus-frozen C++ oracle](../verification/independent_c01_shapiro_exceptional_sage_oracle.py) is ready but **has not yet been executed**. It evaluates six individual pair contributions by direct Sage level-3 modular symbols, entirely independently of C01/Shapiro moment contraction, and requires equality against the previously SHA-frozen full-J executable, including IDs 38 and 67 which exercise both infinity paths. Its pass would extend the pre-existing (1,0) and (2,3) direct local validations to adversarial exceptional branches. Such a sampled test does not replace the formal algebraic argument or the shared eclib table gate.

The p=16231 prime-primary Sha assertion remains subject to the combined source semantics, correct common data, and stated Sage/Kato precision assumptions. No full direct p=16231 n3 Sage series, exact p-adic u_p=1 or all-prime BSD established.
---

## Addendum — 2026-10-26: direct p=16231 exceptional Shapiro Sage/eclib oracles PASS

The user has now executed both new auditors successfully (`EXACT_STATUS=0 0` and `ADVERSARIAL_STATUS=0 0`). The independent exact-integer audit found all 390 rational cusp-divisor relations with 2012 terms correct and inspected exact Gamma0(389*16231) decompositions for six selected full-domain pairs. The separate direct Sage/eclib level-3 weighted-moment oracle then returned precisely the same six pair contributions as the previously SHA-frozen, independently executed global dual-scalar C++ evaluator:

`id 0: 2316; id 38 (one inner infinity): 6198; id 67 (one outer infinity plus 66 inner infinity): 8719; id 16234: 11725; id 131714565: 10993; id 263429129: 2316` (all modulo p=16231). Every direct Sage/C++ match printed PASS.

This supplements the universal operator-duality theorem with strong adversarial **large-prime** finite-value validations targeting previously dangerous exceptional branches. The transcript and terminal provenance are in [executed source-to-J reference audit](../results/c01_shapiro_exact_and_adversarial_high_p_sage_PASS_2026-10-26.md). It does not replace a full independent Sage n3 high-p summation.

The current chain of separately tested computation and remaining trust dependencies is summarized in [minimal p-primary Sha logical certificate](p16231_minimal_prime_primary_sha_certificate_2026-10-26.md). The conclusion is a documented computer-assisted and source/theorem-conditional statement about only the p=16231 primary Sha component, not exact p-adic u=1 or full BSD.

---

## Addendum — 2026-10-26: uniform Skinner–Urban local criterion; corrected minimal discriminant

The minimal discriminant of the specific curve `y²+y=x³+x²−2x` is **`+389`**, not `-389`: direct formula from `b2=4,b4=-4,b6=1,b8=-3` yields `Delta=389`. As `v_389(Delta)=1`, the reduction at the unique bad conductor prime is type I1 and the Tate parameter has valuation `v_389(q_E)=1`.

Consequently the extra local criterion of Sage 10.9 `p_primary_order(ell)` is **automatically satisfied for every good ordinary prime ell>=5, ell!=389, with residually surjective Galois representation**. The exact-order theorem thus applies uniformly in its hypotheses, not in the numerical vanishing conclusion. See [uniform criterion](389a1_uniform_skinner_urban_local_gate_2026-10-26.md).

At ell=16231 the full finite-input numerical certificate already gives p-adic BSD quotient valuation zero, and the conditional computer-assisted prime-primary consequence is unchanged. The uniform local gate alone supplies no bound on the bad/supersingular/other primes and no proof of all-prime Sha triviality.