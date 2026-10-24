# C01 functional to Sage's level-3 quadratic coefficient (source-level derivation)

Date: 2026-10-24. Curve \`389a1\`, \`p=16231\`, \`a_p=128\`.

**Scope.** This document derives the algebraic correction formula from Sage's
ordinary \`pAdicLseriesOrdinary.series\` and \`measure\` definitions, matching the
now-archived C01 source's sign and moment conventions. It does **not** independently
execute the full V19 production or rederive the historical raw level-2 coefficient.

### Normalization

Take \`m(r)=E.modular_symbol(sign=+1,implementation='eclib',normalize='L_ratio')(r)\`.
This is both the default on the curve and the ordinary p-adic L-series default.
Sage uses \`gamma=1+p\`, Teichmüller component \`eta=0\`, and \`D=1\`.
The twist-period quotient is \`1\`; Sage's \`series\` divides by
\`E.real_components()=2\`.

For an integer determinant-one matrix D, put
\`F(D)=m(D.infinity)-m(D.0)\`. Thus for \`D_x=[1,x;0,p^2]\`
(with \`D_x.infinity=infinity\`, \`D_x.0=x/p^2\`),
\`F(D_x)=-m(x/p^2)\`. This is the orientation of the
\`collect_fragments\` continued-fraction path in the archived producer.

Let \`Pmat=diag(p,1)\`, \`beta_t=[1,t;0,p]\` and \`alpha\` the
ordinary root \`alpha^2-a_p*alpha+p=0\`; \`alpha mod p=a_p=128\`.

Define the C01 moments, modulo p,

\`M0(D)=F(D)-alpha^-1 F(Pmat D)\`,

\`M1(D)=alpha^-1 sum_(t=0)^(p-1) t F(beta_t D)\`.

They match V23 and V26's modular-symbol orientation. Their mod-p Hecke
relation is
\`alpha^-1 sum_t F(beta_t D)=M0(D) (mod p)\`,
because \`sum_t F(beta_t D)+F(Pmat D)=a_p F(D)\` and
\`a_p/alpha=1+p/alpha^2 =1 (mod p)\`.

### Level 2 and level 3 groupings

Sage at finite level n sums over Teichmüller lifts \`omega(a)\`,
\`1<=a<p\`, and powers \`gamma^j\`, \`0<=j<p^(n-1)\`;
the coefficient of \`T^2\` carries \`binom(j,2)\` and the normalizing
factor \`1/2\` for two real connected components.

At level 2 write \`x=a+p*b\`, \`0<=b<p\`; uniquely
\`x=omega(a)*gamma^u (mod p^2)\` where

\`u=b/a - ((a^(p-1)-1)/p) (mod p)\`.

At level 3 set \`j=u+p*v\`. The unique lift in each residue class is
\`y=x+p^2*c\`, \`0<=c<p\`. Define kappa by

\`omega(a)*gamma^u=x+p^2*kappa (mod p^3)\`.

Then \`v=(c-kappa)/a (mod p)\`; consequently

\`binom(u+p*v,2)-binom(u,2)
  =p*v*(2*u-1)/2 (mod p^2)\`.

Write \`w=(2*u-1)/a (mod p)\`. The finite-level measures satisfy the
exact distribution relation
\`sum_c mu_3(x+p^2*c)=mu_2(x)\`: it follows directly from Sage's
\`measure\` code, the Hecke identity and \`alpha^2-a_p*alpha+p=0\`.

Thus the difference of **raw finite-level** quadratic coefficients is

\`A2^(3)-A2^(2) = (p/4)*sum_(a,b) w*sum_c (c-kappa)*mu_3(x+p^2*c) (mod p^2)\`.

The factor \`1/4\` is exactly \`1/2\` from \`binom(j,2)\`
and \`1/2\` from the two real connected components. It must not
be inserted a second time or omitted.

### Collapse of the level-3 weighted measure to two moments

Sage's good ordinary measure is

\`mu_3(y)=alpha^-3*(m(y/p^3)-alpha^-1*m(y/p^2))\`.

For \`y=x+p^2*c\`, \`m(y/p^2)=m(x/p^2)\` by integer-translation
invariance. Because \`sum_c (c-kappa)=0 (mod p)\`, the second
term vanishes modulo p when multiplied by \`alpha^2\`.

As \`m((x+p^2*c)/p^3)=-F(beta_c D_x)\`, we obtain modulo p:

\`alpha^2*sum_c (c-kappa)*mu_3(x+p^2*c)
  =-alpha^-1 sum_c (c-kappa)*F(beta_c D_x)
  =-[M1(D_x)-kappa*M0(D_x)]\`.

Consequently, with the **independently defined**

\`J_ref = -sum_(a,b) w*[M1(D_x)-kappa*M0(D_x)] (mod p)\`,

we have the sourced algebraic identity

**\`A2^(3)-A2^(2) = p * J_ref/(4*alpha^2) (mod p^2)\`.**

The archived C01 C++ loops over every \`a,b\` pair and accumulates
\`W=-sum(w)\`, \`K=-sum(w*kappa)\`, with direct
\`(C0,C1)=(-a*b*W-K,a*a*W)\`, consistent with this \`J_ref\`
and the mod-p two-moment covariance. The original relation JSON's 390
cusp identities have been independently rechecked with exact integers.

### Numerical consequence and precise gap

From the historic terminal \`J_V19=4486 mod 16231\` and archived
raw level-2 \`A2^(2)=1199*p (mod p^2)\`, **if** the complete
historical producer and terminal contraction faithfully evaluate
\`J_ref\`, we derive

- \`(4*128^2)^-1 mod p = 9362\`;
- \`J_ref*(4*128^2)^-1 = 8335 mod p\`;
- \`A2^(3)/p = 1199+8335 = 9534 mod p\`.

Sage's reported \`_prec_bounds(3,3)=[+Infinity,2,2]\` makes the
level-3 \`T^2\` coefficient valid modulo \`p^2\`. The independently
reported p-adic regulator yields \`B_p/p=9534 mod p\`. If all those
input computations are faithful, the quotient is a p-adic unit:
\`(A2/B_p) mod p=1\`, **not** exact equality \`A2/B_p=1\`.

Sage's \`Sha.p_primary_bound\` source says the returned valuation is
a **proved upper bound** on the p-primary Sha order under its checked
hypotheses; exponent zero yields \`Sha[16231^infinity]=0\`. This
conditional substitution is not the execution of the expensive direct
\`Sha.p_primary_bound(16231)\` call.

**Open for an end-to-end certificate:** original raw level-2
calculation provenance/precision; independently reproducible full V19
producer-to-chunk chain; independent verification that all terminal
\`M0/M1\` data stem from the normalized modular symbols (V65 supplies
a substantial separately computed terminal check, but its full
\`eclib_beta_table.bin\` is an external frozen dependency). The
full all-prime Sha problem and complex BSD leading term are separate
and still open in this research dossier.

Primary code references:
- https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/padic_lseries.py
- https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/sha_tate.py
