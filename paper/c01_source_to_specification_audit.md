# C01 → mathematical functional: source-to-specification audit

**Status:** Algebraic transport and aggregation identities derived; **not** a machine-verified end-to-end proof for the historical executable.  
**Reviewed:** 2026-10-19.  
**Scope:** elliptic curve `389a1`, `N=389`, `p=16231`, rank `2`.

## 1. Function being computed

Let `m` be the eclib-normalized plus modular symbol with `m(infinity)=0`, and set `F(D)=m(D infinity)-m(D 0)`. For `P=diag(p,1)` and `beta_t=[1,t;0,p]`, let

```text
M0(D) = F(D) - alpha^{-1} F(P D)
M1(D) = alpha^{-1} sum_{t=0}^{p-1} t F(beta_t D)
```

with `alpha` the unit root of `X²−128X+p`. The *independent mathematical definition* is

```text
x(a,b) = a+p*b,  1<=a<p, 0<=b<p
ferm(a) = (a^(p-1)-1)/p mod p
u(a,b) = b/a - ferm(a) mod p, represented 0,...,p-1
w(a,b) = (2u-1)/a mod p
omega(a) (1+p)^u == x(a,b)+p²*kappa(a,b) (mod p³)

J_ref = -sum_{a=1}^{p-1} sum_{b=0}^{p-1}
            w(a,b) [ M1(D_x) - kappa(a,b)*M0(D_x) ] mod p
```

`D_x` is the oriented modular-divisor path infinity → `x/p²`. This specification **does not** define `J_ref` using the program output.

## 2. Mathematical reduction to the coefficient of T²

Sage's ordinary p-adic L-series uses the measure

`mu_n(y)=alpha^{-n}m(y/p^n)−alpha^{-n-1}m(y/p^(n−1))`

and the `(1+T)^j` coefficient in the component `eta=0`, with `gamma=1+p`. For each `x=a+pb`, lifting to `y=x+p²c` gives

`j=u+p*v (mod p²), v=(c−kappa)/a (mod p)`.

Then

`binom(j,2)−binom(u,2) = p*w*(c−kappa)/2 (mod p²)`.

The compatibility of measures and the definitions of `M0,M1` yield

`alpha² sum_c (c−kappa)mu_3(x+p²c) = −(M1(D_x)−kappa*M0(D_x)) (mod p)`.

As `E.real_components()=2`, the exact first correction is

`A2^(3)−A2^(2) = [p/(4*alpha²)] J_ref (mod p²)`.

This uses the **Sage normalization** `normalize='L_ratio'`, `quadratic_twist=1`. See the official `pAdicLseriesOrdinary.series` / `measure` implementation.

## 3. Source-level correspondence, branch by branch

The archived terminal excerpts of `bsd389_c01_v11_aggregated.cpp` (historical SHA-256 `0d8b18696587fc3a0f497c54ebbba99f4d582e69d5a98d0da0e2a4275172b187`) contain:

1. `for(id=L; id<R; ++id)`, with `a=1+id/p`, `b=id%p`. This is a bijection from `[0,p(p−1))` to all required `(a,b)`.
2. `collect_fragments(x,p²,w,kappa)`: Euclidean continued fractions with **positive** `x∈[1,p²−1]`, hence no floor-versus-truncation ambiguity for these divisions. The oriented adjacent-cusp matrices telescope to infinity → `x/p²`. The signed weight is `W=−sum w`; the centered weight is `K=−sum w*kappa`.
3. `key(fragment)` identifies the Manin projective class modulo 389; `qidx(H)` identifies the Shapiro coset. `r_inf=[−40,−1669;389,p]` handles `d=0 (mod p)`. If `d!=0 (mod p)`, `j=c/(389*d)`. Both satisfy `H*r_j^{-1}∈Gamma_0(389p)`.
4. **Direct generator:** if `h=[A,B;C,D]∈Gamma_0(389p)`, `q=−AB` and `r=A²` modulo p, then `apply_group` adds `(C0,C1)=(q*W−K,r*W)`.
5. **Manin relation branch:** after a second transport `(qi,ri)` and relation coefficient `e`, it adds `e*((q+r*qi)*W−K, r*ri*W)`.
6. The terminal contracts `sum_{g,j} (C0[g,j]*M0[g,j] + C1[g,j]*M1[g,j])`. The `C0` contribution cannot generally be omitted.

The covariance identity follows from Hecke eigenvalue 128:

```text
M0(hD) = M0(D)
M1(hD) = -A*B*M0(D) + A²*M1(D)   (mod p).
```

It is valid for **both** finite and exceptional cosets. Composition satisfies
`(q,r)∘(qi,ri)=(q+r*qi,r*ri)`. Therefore the two branch formulas are exactly the pushforward of `-w(M1−kappa M0)` through the relations, as formal polynomials over `F_p`.

## 4. Machine arithmetic: proven bounds versus unverified preconditions

For the specified domain,
`1≤x≤p²−1=263445360`, all Euclidean numerators/denominators are bounded by `p²`. `p³=4275981654391`. The `kappa` powers use signed 128-bit products in the source excerpt. All reduced coefficient factors `q,r,W,K,qi,ri` are less than `p=16231` in absolute residue representatives. In particular,
`max(q*W+K)=263429130`, which fits signed 64-bit. The `apply_group` relation products visibly cast to `__int128` before multiplication and reduce modulo p at intermediate points.

**Preconditions to certify using full original files:**

- the historical binary really corresponds to the reviewed **complete**, correctly compiled `V11` source; V66 shows functional agreement on limited windows, but not byte-identical compilation;
- all JSON relation coefficients and generator references are valid; matrix determinant/group-membership hypotheses hold for every exported relation;
- the exact loader and sparse accumulator cannot read out-of-bounds slots, and every touched slot is written once in sorted order;
- no unreviewed numerical pathway evaluates **rational cusps after reducing their integer divisor matrices modulo p**. Reduction modulo p is legitimate for the transported *moment coefficients*, not for the underlying cusp-divisor values.

## 5. What the historical full-chain audit has accomplished

Reported terminal output on 2026-10-19:

```text
V19_FULL_CHUNK_TO_CHECKPOINT_CHAIN_PASS pairs 263429130 expected_chunks 514511 checkpoints 4019 all_rows 9759143225 final_sha256 5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e
```

This **closes the archived-chunk → checkpoint identity**. It does **not** independently evaluate every chunk from the mathematical definition.

Independent V65 verifies both terminal moment contractions on all 67 generators and independently replays the final 39,946 pairs; it likewise does **not** certify every intermediate execution instruction.

## 6. Consequence, with honest logical status

The recorded terminal invariant is `J_V19=4486` mod 16231, and the independently recorded level-2 coefficient is `A2^(2)/p=1199` mod 16231. Thus, **if** the complete historical producer realizes the mathematically defined `J_ref`, one obtains

```text
4486 * (4*128²)^(-1) = 8335 (mod 16231)
A2^(3)/p = 1199+8335 = 9534 (mod 16231)
B_p/p = 9534 (mod 16231)
valuation(A2/B_p) = 0
```

Under the now-passed arithmetic gate and the hypotheses of the proved Sage/Kato p-primary upper bound, this implies `Sha(E/Q)[16231^infinity]=0`. **That conditional implication is not a proof of full BSD or exact equality of the p-adic BSD quotient to 1.**

### Source provenance to import before external certification

See [historical manifest](../data/HISTORICAL_MANIFEST.md). Import the exact source bytes and the relevant small relation/scalar data only after SHA-256 validation. This note describes a **source-to-specification audit based on archived source excerpts**, not a byte-by-byte verification of the original binaries.
