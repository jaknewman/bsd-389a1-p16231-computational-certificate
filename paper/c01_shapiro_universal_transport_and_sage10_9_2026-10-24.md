# Universal C01–Shapiro transport, exact orientations, and Sage 10.9 bridge

Research audit dated 2026-10-24. Curve E = 389a1, conductor N=389,
prime p=16231, a_p=128. **Scope: source-level algebraic proof for the
archived producer algorithm; not an independent fresh execution of all
263,429,130 pair contributions.**

The original V11 production source is
`historical/originals/bsd389_c01_v11_aggregated.cpp` and included loader
`historical/originals/bsd389_c01_v11_loader.cpp` and
`historical/originals/bsd389_transposed_J_native.cpp`.
The original relation export was independently checked with exact rational
cusp divisors on all 390 representatives and 2012 relation matrices.

## Theorem 1: covariance of C01's two moments

Let m be the plus eclib modular symbol normalized by Sage's
`L_ratio` convention, and for any positive-determinant integral matrix D
write

`F(D)=m(D.infinity)-m(D.0)`.

Let `Pmat=diag(p,1)`, `beta_t=[1,t;0,p]`,
and `alpha` be the ordinary root of
`X^2-a_p*X+p` (so `alpha=a_p (mod p)`). Define modulo p:

`M0(D)=F(D)-alpha^-1 F(Pmat D)`;
`M1(D)=alpha^-1 sum_(t in Fp) t*F(beta_t D)`.

For every **integral** `h=[A,B;C,D0] in Gamma_0(Np)`, put
`q(h)=-AB mod p` and `r(h)=A^2 mod p`.
Then

`M0(h G)=M0(G)`,
`M1(h G)=q(h)*M0(G)+r(h)*M1(G)`.

**Proof.** Since `h in Gamma_0(N)`, `F(hG)=F(G)`.
Also `Pmat*h*Pmat^-1=[A,pB;C/p,D0]` lies in
`Gamma_0(N)`, hence `F(Pmat hG)=F(Pmat G)`.
This proves the first equality.

Since `C=0 (mod p)`, `A,D0` are units modulo p. For each
`t in Fp`, choose `s=(B+t D0)/A (mod p)`.
The exact matrix
`beta_t*h*beta_s^-1` is integral of determinant one and has
bottom-left entry `p*C` divisible by N; therefore it is in
`Gamma_0(N)`. Consequently `F(beta_t hG)=F(beta_s G)`.
Because `A D0=1 (mod p)`, the inverse change is
`t=A^2 s-A B (mod p)`. Thus

`M1(hG)=A^2*M1(G)-AB*alpha^-1*sum_s F(beta_s G)`.

The modular symbol Hecke eigen-relation gives

`sum_s F(beta_s G)+F(Pmat G)=a_p*F(G)`.

As `alpha^-1*a_p=1 (mod p)`, the last term equals
`M0(G) (mod p)`; the result follows. QED.

**Composition.** Writing `(q,r)` for the moment action, composing
two such transformations gives

`(q,r) o (q',r')=(q+r*q',r*r')`.

This equality holds identically in `Fp` and does not depend on
the chosen modular symbol value.

## Theorem 2: all Shapiro cosets, including infinity

The original `qidx(H)` function takes `H in Gamma_0(N)`
and sets

- if `d != 0 (mod p)`, `j=c/(N d) (mod p)`;
- if `d = 0 (mod p)`, `j=p` (the exceptional index).

For a finite j, let `r_j=[1,0;Nj,1]`. Then

`h=H*r_j^-1` is in `Gamma_0(Np)`:
its lower-left is `c-Njd=0 (mod Np)`.

For `j=p`, the original source uses

`r_inf=[-40,-1669;389,16231]`.

Its determinant is exactly one:
`(-40)*16231-(-1669)*389=1`.
Moreover for any `H=[a,b;Nk,d]` with `d=0 (mod p)`,
the lower-left entry of `H*r_inf^-1` is
`N*(p k-d)`, divisible by Np. Thus in **both** cases
`h in Gamma_0(Np)`, and Theorem 1 applies with no special
coefficient identity needed. The implementation's exceptional
branch counts are therefore tests of reachable cosets, not
exceptions to the covariance lemma.

The Manin export gives an exact cusp-divisor identity for each
non-generator representative R_i:

`[R_i.infinity]-[R_i.0]
 = sum_(e,A,R_g) e*([A^-1 R_g.infinity]-[A^-1 R_g.0])`,

where `A in Gamma_0(N)` and `R_g` is one of the 67 generators.
Left-multiplying this *exact* identity by any Shapiro coset r_j,
and reducing `r_j A^-1` to `h_i r_{j_i}` using qidx,
proves the relation-branch transport. The two moment actions
compose by `(q+r*q_i,r*r_i)`, exactly the C++ expressions.
All 390 rational cusp-divisor relations and 2012 group lifts
were independently checked from the full original JSON.

## Theorem 3: sign, cusp path and coefficient identification

For `a=1,...,p-1`, `b=0,...,p-1`, let

`x=a+p*b`,
`u=b*a^-1 - (a^(p-1)-1)/p (mod p)`,
`w=(2u-1)*a^-1 (mod p)`.

Let `omega(a)` be Teichmuller at p, `gamma=1+p` and

`kappa=(omega(a)*gamma^u - x)/p^2 (mod p)`.

The C++ uses `omega(a)=a^(p^2) (mod p^3)`.
This agrees with the unique Teichmuller lift modulo p^3.

The continued-fraction routine `collect_fragments(x,p^2,...)`
uses determinant-one matrices whose successive cusp endpoints
telescope **from infinity to x/p^2**. More explicitly, with
convergents h_j/k_j of x/p^2, its first matrix
`[1,h_0;0,k_0]` has cusps infinity and h_0/k_0.
Its j-th subsequent matrix
`[sign_j*h_j,h_(j+1);sign_j*k_j,k_(j+1)]`
has cusps h_j/k_j and h_(j+1)/k_(j+1),
where `sign_j=(-1)^(j+1)` gives determinant +1.
Thus sum of F(fragment) is `m(infinity)-m(x/p^2)`;
there is **no unexplained orientation sign**.

C++ stores two aggregated fragment weights

`W=-sum w (mod p)`,
`K=-sum w*kappa (mod p)`.

For a direct generator transport h it adds

`(C0,C1)=(q(h)*W-K,r(h)*W)`.

Contracted against the stored moments this equals

`W*M1(hD)-K*M0(hD)
 = -sum w * [M1(fragment)-kappa*M0(fragment)]`.

For a non-generator exported relation with coefficient e, the
code adds

`e*(C0,C1)=e*((q+r*q_i)*W-K,(r*r_i)*W)`.

By Theorems 1 and 2 and exact cusp-divisor linearity, the same
identity holds after a relation and on every Shapiro class
(including exceptional classes).

Finally, the C++ interval loop `id=0,...,p(p-1)-1` uses
`a=1+id//p`, `b=id%p`, a bijection onto the complete domain.
Therefore, **provided the reviewed C++ source is executed faithfully
with the exact verified export**, its terminal contraction computes

`J_ref=-sum_(a,b) w(a,b)*[M1(D_x)-kappa(a,b)*M0(D_x)] (mod p)`.

This is a universal algebraic source-level identity, **not a statistical
inference from the 57 replayed sample chunks**.

## Theorem 4: comparison with the actual SageMath 10.9 coefficient

Authoritative version-pinned upstream source:

- https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/padic_lseries.py
- https://github.com/sagemath/sage/blob/10.9/src/sage/schemes/elliptic_curves/sha_tate.py

Sage 10.9 `pAdicLseriesOrdinary.series(n,prec=3,eta=0)`
uses `gamma=1+p`, eclib `normalize='L_ratio'`,
and divides by `E.real_components()=2` for positive sign and
untwisted `D=1`.
Its `measure(y,n)` (good ordinary p) is

`mu_n(y)=alpha^-n*[m(y/p^n)-alpha^-1 m(y/p^(n-1))]`.

At n=2, each residue `x=a+p*b` has exponent u modulo p.
At n=3 its p lifts `y=x+p^2*c` have exponents
`j=u+p*v`, `v=(c-kappa)*a^-1 (mod p)`.
The Hecke distribution relation yields

`sum_c mu_3(x+p^2*c)=mu_2(x)` exactly.

Subtracting the n=2 coefficient and using
`binom(u+p*v,2)-binom(u,2)
  = p*v*(2u-1)/2 (mod p^2)` gives

`A2^(3)-A2^(2)
 = (p/4)*sum_(a,b) w*sum_c(c-kappa)*mu_3(x+p^2*c)
 (mod p^2)`.

Here `1/4` is the product of `1/2` from the quadratic
binomial coefficient and `1/2` from the 2 real components.

Using `F(beta_c D_x)=-m((x+p^2 c)/p^3)` and that
`sum_c(c-kappa)=0 (mod p)`, the Hecke relation gives

`alpha^2*sum_c(c-kappa)*mu_3(x+p^2*c)
 = -[M1(D_x)-kappa*M0(D_x)] (mod p)`.

Therefore, with no further finite-level heuristic,

**`A2^(3)-A2^(2) = p*J_ref/(4*alpha^2) (mod p^2)`.**

This is a source-level algebraic equality under the verified
Sage normalization, not an independent direct run of
`lp.series(n=3)`.

## Numerics, p-primary theorem and nonclaims

Already verified user-run archival audits support:
- `A2^(2)=1199*p (mod p^2)`: full 254+254 chunk-level
  V54/V61 audit, with exact eclib rational computation in the
  historical source and SHA-pinned outputs.
- `J_V19=16014+4703=4486 (mod p)`: independent
  terminal V23/V26/V65 contraction, with full eclib table SHA.
- `J_ref=J_V19`: source-level Theorems 1–3 plus trusted
  C01 historic production, byte-rebuild provenance, all archived
  514511 chunks/checkpoint recomposition, and 57 native byte-equal
  replay samples.
- `A2^(3)/p=(1199+4486/(4*128^2))=9534 (mod p)`.
- `B_p/p=9534 (mod p)`: independently reported Sage 10.9
  regulator result, with `v_p(Reg_p)=3`, `v_p(B_p)=1`.

Sage 10.9 `Sha.p_primary_bound` documents and implements a
**proved upper exponent** for Sha[p^infinity] in arbitrary rank
under its checked reduction/Galois hypotheses (which the 2026-10-19
installed-Sage gate reports satisfied), by taking the valuation of
`self.an_padic(p,prec=0,use_twists=True)`.
`an_padic` itself is the *conjectural p-adic BSD quotient*;
the **bound theorem**, not equality conjecture, gives the conclusion.
Since the inferred analytic quotient is a unit,
the **computer-assisted implication**, subject to the trusted
authenticated historic finite computation, is

`Sha(E/Q)[16231^infinity]=0`.

Strictly, the computed quotient is `1 (mod p)` as a first
p-adic digit, NOT an identity `u_p=1` in Q_p. The direct
expensive `E.sha().p_primary_bound(16231)` was not executed,
and this dossier does not prove all-prime Sha triviality or
full complex Birch–Swinnerton-Dyer.

### Trust boundary, precisely

The universal **mathematical transport statements** no longer
depend on sampled native outputs. They depend on verified exact
exported cusp identities, standard modular symbol Hecke relations,
and correct Sage normalization. The **numerical value** `4486`
depends on the finite authentic V19 execution and on the assumed
correctness of C++/compiler/runtime/archived data; SHA-based chain
recomposition and partial independent native replay cannot logically
guarantee all 514511 producer outputs without additional assumptions.
A source-level proof is not a formal verification of the binary.
