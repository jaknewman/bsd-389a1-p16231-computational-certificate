# D+ progress: two-prime Kurihara certificates for each good prime and a new exact p=107 local pair

Date: 2026-10-27. **Status: new exact arithmetic proof strategy and executable finite-field data, not yet a proof of Sha[107^infinity]=0 nor a uniform D+.** Based on independent finite-field arithmetic at p=107, and newly identified 2025 Chan-Ho Kim and January 2026 Castella–Sano Selmer/Fitting theorems.

## 1. Specialized unconditional equivalence at a fixed good prime

Let E=389a1: `y²+y=x³+x²−2x`, conductor 389, rank E(Q)=2, no torsion, Δmin=+389, Tamagawa product 1, analytic root number +1. Fix a good prime p≥5 with surjective residual image E[p] and p prime to the optimal Manin constant. Since E is the optimal quotient of squarefree conductor, Mazur's Manin constant theorem supplies the latter p-condition when p²∤N.

Define a *Kurihara auxiliary prime* q by `q ≡1 (mod p)`, `q ≠389`, and `p|#E(F_q)`, equivalently `a_q≡q+1 (mod p)`. If q1!=q2 are two such primes, put `n=q1*q2`. Let

`delta_n = sum_{a mod n, (a,n)=1} [a/n]^+ log_q1(a) log_q2(a) in Z/I_n`

using the Néron-normalized plus modular symbols and the exact residue ideals `I_q=(q-1,a_q-q-1)Z_p cap Z`, `I_n=I_q1+I_q2`. Then the **fixed-prime rank-two criterion** is:

`Sha(E/Q)[p^infinity]=0 iff there exists a pair of Kurihara primes q1,q2 with delta_(q1*q2) NOT 0 mod p`,

under the listed p and E hypotheses.

**Forward implication from witness to Sha=0 (proved from published theorems):** Let rho be the least number of distinct Kurihara primes of n for which delta_n !=0 at some p-power precision. The witness has rho≤2. Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves* (2025), Theorem 1.9 (1), gives `rho=corank_Zp Sel_{p^infinity}(E/Q)`. The 2 MW generators imply corank≥2, so rho=2. Its exact finite-quotient formula, also quoted in Castella–Sano (2026, page 3), says

`v_p(#X_BK)=M_rho-M_infty(delta)`

where `X_BK=Sel_{p^infinity}/(maximal divisible subgroup)`, and `M_r=min_{n:nu(n)=r} v_p(delta_n)`. As the witness has v_p(delta_n)=0, `M_2=0`, and monotonicity implies `M_infty=0`. Hence `#X_BK=1`. Meanwhile rho=2 makes Sha[p^infinity] finite: corank of Sel equals rank MW, so the quotient Sha cannot have a divisible p-corank. Its finite torsion is now identified with X_BK by the Kummer sequence and so must vanish. QED.

**Reverse implication (uses new January 2026 theorem B):** Assume Sha[p^infinity]=0. Then Sel_{p^infinity}=(Q_p/Z_p)^2 is fully divisible, so corank Sel=2 and `#X_BK=1`. Castella–Sano Theorem B proves for good ordinary p, or good supersingular p with squarefree N=389, that `M_infty(delta)=v_p(TamE)=0` under surjectivity and the Manin condition. In particular the δ collection does not vanish identically. Thus Kim gives rho=2; its finite quotient formula gives M_2=M_infty=0. Consequently at least one squarefree n with exactly two Kurihara factors has delta_n nonzero mod p. QED.

**Scope:** Both directions for good p>=5 satisfying the stated Galois/Manin hypotheses; p=389 multiplicative is not covered by the *reverse* use of Castella–Sano Theorem B. p=3 and p=2 are handled separately. This equivalence gives a finite witness criterion at **each** good prime, not one finite all-prime certificate and not an upper bound on the sizes of witness primes as p varies.

## 2. A completely explicit first supersingular test, p=107

Stein–Wuthrich Theorem 12.3 excludes p=107 as the first good supersingular prime of E. The auxiliary search below is independent of the paper and of the earlier Shapiro/χ53 computation.

Take

`q1=369793`, prime, `q1=1 (mod 107)`, `#E(F_q1)=369792=107*3456`, `a_q1=2`;

`q2=383917`, prime, `q2=1 (mod 107)`, `#E(F_q2)=384772=107*3596`, `a_q2=-854`.

Both have p-valuation exactly 1 in their point counts, and also q_i-1 has p-valuation 1, so `I_q1=I_q2=I_n=(107)`. The target modular-symbol sum is therefore a single element of `F_107` with NO need for p² precision.

Let P=(0,0), Q=(1,0). Reduction of `(N_i/107)P` and `(N_i/107)Q` gives the following actual affine coordinates:

q1: `A=(254307,70688)`, `B=(11836,301059)`, with `B=58*A` in E(F_q1)[107];

q2: `A=(334889,236306)`, `B=(153546,353110)`, with `B=3*A` in E(F_q2)[107].

Thus the two local reduction directions are `lambda_q1(P,Q)=(1,58)` and `lambda_q2(P,Q)=(1,3)`, and their determinant is

`det[[1,58],[1,3]]=-55 ≡ 52 (mod 107) ≠0`.

Therefore the natural reduction map from the rank-two Mordell–Weil quotient

`E(Q)/107E(Q) -> E(F_q1)/107 E(F_q1) ⊕ E(F_q2)/107 E(F_q2)`

is an **isomorphism**, each target component having dimension one. This is a new exact finite-field certificate for p=107; its full source can be compiled and run at [verification/kurihara_p107_two_local_directions.cpp](../verification/kurihara_p107_two_local_directions.cpp). The computation independently passed point counts, primality, order, the discrete-log relations and determinant.

**NONCONCLUSION:** An isomorphism on the *Mordell–Weil* quotient is not yet an isomorphism on the full 107-Selmer group. Extra Sha[107]-classes, if any, could lie in the kernel of the two localizations. The published Kurihara–Kim global comparison requires the additional modular-symbol witness `delta_n !=0`. It has **NOT** been computed.

The target level is `n=369793*383917=141969819181`, and `phi(n)=141969065472`. Direct naïve summation of 142 billion rational symbols is not a realistic quick certificate. The next exact computational task, if pursued, must exploit the two-variable Mazur–Tate theta element and Manin-module distribution/Hecke symmetries to extract just its `X_q1 X_q2` coefficient mod 107; NO faster extraction has yet been proved or implemented here.

## 3. Consequences for constructing D+

The new Castella–Sano Theorem B shows for **every** good p>=5 satisfying its residual and Manin hypotheses (including supersingular p), that some nontrivial mod-p Kurihara witness exists with some even number rho≥2 of auxiliary prime factors. To force Sha[p^infinity]=0, we specifically need rho=2. Theorem B by itself proves neither rho=2 nor global Sha finiteness; it is logically compatible with rho=4,6,... corresponding to extra Selmer corank. This is the **rank-two gap**.

The genuinely promising uniform reformulation is: **prove that for all sufficiently large good p there is an order-two (two-auxiliary-prime) Kurihara witness with nonzero delta mod p.** That would force global vanishing outside finitely many primes, covering ordinary and supersingular alike. This statement is still open and is not implied by the pointwise existence theorem; it is another form of the uniform D+ challenge.

## Bibliography

- Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, 2025 manuscript, Theorems 1.9 and 1.11: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
- Francesc Castella and Takamichi Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, 2026-01-20, Theorems A and B: https://web.math.ucsb.edu/~castella/Kurihara.pdf
- Stein–Wuthrich (2013), Theorem 12.3, p.1788: https://wstein.org/papers/mcom2649-iwasawa-alg.pdf

**STATUS:** Exact p107 finite arithmetic and rigorous published-theorem-driven *conditional mod107 global Selmer gate*. Sha[107^infinity] NOT certified; uniform D+ NOT constructed.
