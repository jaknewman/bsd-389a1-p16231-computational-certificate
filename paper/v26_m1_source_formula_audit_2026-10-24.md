# V26 global first-moment source formula audit — 2026-10-24

Scope: two original Sage sources uploaded at commit \`74c1283\`:
\`historical/terminal/bsd389_corrected_eclib_slots_ionos.sage\` and
\`historical/terminal/v26_global_m1.sage\`. This is a source-level algebraic
review, **not** a new execution of their global sums.

## Definitions and normalizations

Let \`p=16231\`, \`N=389\`, and let \`m\` be the eclib sign-plus modular
symbol used by the uploaded scripts. For the oriented divisor of a matrix
\`D=[a,b;c,d]\`, define \`F(D)=m(D infinity)-m(D 0)\`. Since the
scripts' \`f(n,d)=-m(n/d)\` and \`m(infinity)=0\`, their
\`value(D)=f(D 0)-f(D infinity)\` equals \`F(D)\` in the script's normalization.

Set \`beta_s=[1,s;0,p]\`, \`P=[p,0;0,1]\`, \`V_s=F(beta_s G)\`,
\`V_inf=F(P G)\`, and \`alpha^-1=5199 (mod p)\` (indeed
\`128*5199=1 mod 16231\`).

V26 computes \`M_1(R_j G) = alpha^-1 * sum_t t F(beta_t R_j G)\` for
\`R_j=[1,0;N*j,1]\` if \`0<=j<p\`, and for the exceptional
\`R_inf=[-40,-1669;389,p]\` if \`j=p\`. Reductions only concern the
matrix-action coefficients modulo p; the modular symbol is evaluated on
the original integral divisor matrices.

## Exact derivation of the fast formula for finite j

For \`j=0\`, \`R_0=I\`, so
\`M[0]=alpha^-1 sum_s s V_s\`, exactly as the source implements.

For \`j!=0\`, put \`u=N*j (mod p)\`. Factoring \`beta_t R_j\` on the
left by an element of \`Gamma_0(N)\` gives the projective coordinate
\`s=t/(1+u*t)\` when \`1+u*t!=0 (mod p)\`, with inverse
\`t=s/(1-u*s)\`. The missing parameter \`t=-u^-1\` contributes
\`-u^-1 V_inf\`; the missing ordinary \`s=u^-1\` is excluded. Hence

\`M[j]=alpha^-1[ sum_(s in Fp^*,s!=u^-1) (s/(1-u*s))*V_s - V_inf/u ]\`.

V26's cyclic convolution is mathematically this expression: choose
\`primitive\` generating \`Fp^*\`, write \`s=primitive^k\`, and set
\`A[k]=s V_s\`, \`Arev[k]=A[-k]\`, \`B[k]=(1-primitive^k)^-1\` except
\`B[0]=0\`. Its cyclic convolution coefficient at logarithm
\`ell=log_primitive(u)\` equals exactly
\`sum_s s V_s/(1-u*s)\` with \`u*s!=1\`. Thus the polynomial multiplication
implementation and its \`C[ell]\` index are consistent with the exact
change of variables, subject to the usual modular-symbol
\`Gamma_0(389)\` invariance.

## Exceptional coset

For \`R_inf=[a,b;c,d]=[-40,-1669;389,p]\`, reduction of
\`beta_t R_inf\` uses
\`s=(b+d*t)/(a+c*t)\` when the denominator is nonzero modulo p.
Solving yields \`t=(a*s-b)/(d-c*s)\` for \`d-c*s!=0\`.
When \`a+c*t=0\` modulo p, the branch contributes \`V_inf\`
with weight \`t_exceptional=-a/c\`.
The source's exceptional loop and single extra term implement precisely
this partition of all \`t in Fp\`.

## Audits already represented in source

1. Source checks the frozen V19 state SHA-256 and byte count and loads
   only its \`C1\` second half.
2. Its \`direct_m1()\` independently evaluates the original 16,231-summand
   definition at six points (\`g=0,1,66\` and \`j=1,p\`). **Six**
   oracle checks are not a full independent replay.
3. Its resumable \`per_generator\` list accumulates \`J1\`.
   The repository ledger reports \`J1=4703\`, but this source has
   **not been rerun in the current audit**.
4. **Crucial:** the terminal \`J0=16014\` is **hardcoded** in the V26
   source, not independently calculated there. The original C0 terminal
   contraction/replay must be retrieved and linked to the V19 state.
5. The earlier eclib slots file checks only four slots; these sample
   computations are not the complete \`M0\`/\`M1\` data.

## Unfinished arithmetic bridge

Matching the C01 V19 contraction \`J=J0+J1=4486 (mod p)\` to
the **Sage 10.9** finite-level cyclotomic \`A2^(3)-A2^(2)\`
requires (a) the actual unhardcoded terminal \`J0\` source and audit
log, (b) the V26 checkpoint and terminal log for \`J1\`, (c) a proof
that eclib \`m\` matches the \`padic_lseries\` normalizations and two
real components, and (d) the exact level-2 archive. In particular,
\`A2/B_p =1 (mod p)\` is *conditional* and does not assert exact
\`p\`-adic equality or global BSD.

Verdict: **finite/exceptional V26 moment formulas algebraically
consistent with the original source, terminal-data provenance and
Sage normalization bridge still require audit.**
