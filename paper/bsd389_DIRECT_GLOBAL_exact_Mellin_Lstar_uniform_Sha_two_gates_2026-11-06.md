# DIRECT GLOBAL BSD ATTACK — E=389a1 (2026-11-06)

This is a fresh, independent-of-p workstream. Existing local certificates stay archived, unchanged. No claim of complete BSD is made.

## Two genuinely global obligations

For E: y²+y=x³+x²−2x, conductor N=389, the accepted exact modular-symbol and Arb proof establishes analytic rank 2 and L''(E,1)/2>0. The certified full Mordell–Weil group has rank 2, torsion 1, and Tamagawa product 1.

What still has to be proved:
(G) Sha(E/Q) is finite (ideally identically zero).
(A) EXACTLY L''(E,1)/2=Omega_E Reg_E #Sha(E/Q).

A proof of Sha=0 without (A) is not complete BSD. A proof of L''/2=Omega Reg without (G) does not imply Sha=0. Additional isolated p-primary Sha certificates, even infinitely many without a uniform argument, do not prove either global result.

## Exact global archimedean formula with explicit rapidly converging tail

Let f(z)=sum_(n>=1) a_n exp(2 pi i n z) be the normalized weight-2 newform of conductor 389, root number +1. Set t0=1/sqrt(389). The completed L-function is
Lambda(E,s)=(sqrt(389)/(2 pi))^s Gamma(s)L(E,s).

**Theorem 1 (exact Mellin-Fricke identity).** For any complex s,

Lambda(E,s) = sqrt(389) integral_(t0)^infty f(it) [ (t sqrt(389))^(s-1) + (t sqrt(389))^(1-s) ] dt.

Proof. Split the standard Mellin transform 389^(s/2) integral_0^infty f(it)t^(s-1)dt at t0. For the lower interval substitute t=1/(389 u). The Fricke relation at global root sign +1 is f(i/(389u))=389 u² f(iu). The two upper-half integrals combine into the claimed formula. Both are entire by exponential decay, so differentiation under the integral is justified.

Because the root number is +1 and the archived exact modular symbol proves L(E,1)=0, we have L'(E,1)=0. Twice differentiating the identity at s=1 gives

**EXACT EQUATION (AN):**
L''(E,1)/2 =
2 pi integral_(1/sqrt(389))^infty f(it) log²(t sqrt(389))dt
= 2 pi sum_(n>=1) a_n integral_(1/sqrt(389))^infty
exp(-2 pi n t) log²(t sqrt(389))dt.

No p-adic L-function, Sha assumption, or numerical extrapolation enters this exact identity. It is an explicit restatement of the underlying Mellin computation, not a new solution of BSD.

**Theorem 2 (exact global exponential truncation bound).** Let S_M be the rightmost series truncated at n<=M, c=2pi/sqrt(389)>0. Using the Hecke/Deligne estimate |a_n|<=d(n)sqrt(n)<=2n and log(t sqrt(389))<=sqrt(389)(t-t0) for t>=t0 gives

|L''(E,1)/2 - S_M|
 <= (389/pi²) sum_(n>M) exp(-c n)/n²
 <= (389/pi²) exp(-c(M+1))/[(M+1)²(1-exp(-c))].

Proof. Put t=t0+x. Integrate x² exp(-2pi n x) explicitly: 2/(2pi n)^3; multiply by |a_n|<=2n and the outer 2pi; then bound the remaining geometric series. This bound is fully rigorous. A 140-coefficient independent sanity calculation reproduces 0.759316500288426770230187605..., consistent with the **previously certified** Arb interval; it does not replace the original rigorous execution.

The exact arithmetic-analytic identity still needed for predicted Sha=1 is therefore:

**GLOBAL COMPLEX TARGET (C):**
2 pi sum_(n>=1) a_n integral_(t0)^infty
exp(-2 pi n t) log²(t sqrt(389))dt
= Omega_E [hat h(P)hat h(Q) - <P,Q>_NT²],

where Omega_E is the TOTAL real Neron period and the height determinant is computed in the full saturated MW basis.

This equality is precisely the strong BSD rank-two coefficient, NOT a consequence of the fast-convergent series or arbitrarily tight bounds.

William Stein, The Birch–Swinnerton-Dyer Conjecture, E389a Open Problem 2.18, specifically asks to prove that the quotient (L''/2)/(Omega_E Reg_E) is even a RATIONAL NUMBER: https://wstein.org/books/bsd/bsd.pdf . Numerical values approximately L''/2=0.759316500288, Omega=4.98042512171, regulator=0.152460177943, quotient≈1. These are evidential, not an integrality proof.

## One uniform Selmer theorem would rule out infinitely many bad primes

For each rational prime p, dual Kummer gives
X_p = Sel_(p-infinity)(E/Q)^dual = Z_p² direct-sum Sha(E/Q)[p-infinity]^dual.
Therefore I_p=Fitt_2,Zp(X_p)=Fitt_0,Zp(Sha[p-infinity]^dual).

**Theorem 3 (precise globally sufficient arithmetic statement).**
If one INDEPENDENTLY constructs a fixed nonzero integer D and proves
D Z_p is contained in I_p for EVERY p, then Sha is finite and its order divides |D|. If D is squarefree, Cassels–Tate forces odd-primary Sha to vanish. An independently proved 2-primary certificate then yields Sha=0.

Proof. Since D is nonzero in every Z_p, each I_p is nonzero so every Sha[p-infinity] is finite; Fitt0 of a finite Z_p-module is p^(v_p(#Sha_p)) Z_p, so v_p(#Sha_p)<=v_p(D). Thus no Sha appears outside the finitely many prime divisors of D, and the direct sum is finite. Finite odd-p Sha has square order, whence any exponent <=1 is 0.

**Circularity warning.** The prior exact diagonal Fitting-intersection theorem in this repository shows that merely *asserting existence* of such a nonzero D is EQUIVALENT to Sha finiteness. This becomes an independent method ONLY by constructing D from finite arithmetic data unrelated to the desired Sha conclusion AND proving a genuine prime-uniform integral comparison with the ACTUAL Selmer Fitting ideals. The known finite toric-factor norm 729 and Hecke Smith constant 2 do NOT currently possess this comparison.

The 2026 Castella–Sano unrestricted auxiliary-degree Kurihara result does not give the degree-two primitive statement needed for rank-two Sha. A collection of individually certified prime cases does not establish the uniform bound.

## Research decision (effective immediately)

STOP expanding the p16231 first-layer Galois action investigation as the primary route. Keep all its archived results as tools, and only revisit when they enter a separately justified ALL-PRIME theorem.

Global priority 1: independently construct a single integral motivic/Euler-system comparison with uniform p-Selmer support, or prove a different all-p finiteness theorem. Its precise target is Theorem 3, but it must NOT assume that theorem's conclusion.

Global priority 2: establish rationality, and ideally integrality and exact equality, of the **COMPLEX** ratio in (C) via a genuine regulator/height theorem (not p-adic approximation). The exact analytic side is given with a certified explicit tail in Theorems 1–2.

No theorem currently established in this note proves either missing arithmetic-global obligation. Full BSD for 389a1 remains unproved.

References:
- Sage official tutorial on 389a1: E.sha().bound()=(0,0), no global finiteness bound; https://doc.sagemath.org/html/en/thematic_tutorials/explicit_methods_in_number_theory/elliptic_curves.html
- William Stein, E389a Open Problem 2.18, https://wstein.org/books/bsd/bsd.pdf .
- Existing repository certified analytic-rank-2 output: results/full_BSD_exact_analytic_rank2_PASS_2026-10-19.md .
- Existing uniform Fitting noncircularity theorem: paper/bsd389_global_diagonal_Fitt_intersection_exact_criterion_2026-11-01.md .
