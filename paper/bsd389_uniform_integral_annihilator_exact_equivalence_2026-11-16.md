# E389a1 — global integer annihilator, exact finiteness equivalence, and the Poitou–Tate barrier
Date: 2026-11-16. Status: proved elementary global theorem; no new Sha vanishing asserted.

## 1. Exact global-annihilator theorem

Let E/Q be an elliptic curve and Sha=Sha(E/Q). The following statements are equivalent:

(A) Sha is finite.
(B) There exists a nonzero integer C with C*Sha=0.

Proof. (A)=>(B): take C the exponent of the finite group. For (B)=>(A), the Weil–Chatelet group H^1(Q,E), hence Sha, is torsion. Write |C|=product_{p in S} p^{a_p}. Then Sha is supported on the finite set S and
Sha = direct_sum_{p in S} Sha[p^{a_p}].
For each n, the Kummer exact sequence
0 -> E(Q)/p^n E(Q) -> Sel_{p^n}(E/Q) -> Sha[p^n] -> 0
shows Sha[p^n] is finite, since Sel_{p^n} is finite by finite-descent theory. Thus Sha is finite. QED.

This is a **global** statement; knowing C_p*Sha[p^infty]=0 with an integer depending on p does not yield (B), unless the set of relevant p and their exponents are independently bounded.

In particular, an independent construction of an integer C !=0 annihilating *all* Selmer strict kernels, with no assumptions about Sha support, would already be a proof of Sha finiteness. Such a construction is mathematically possible as a proof target but is not a mere formal consequence of Poitou–Tate or Chebotarev.

## 2. Exact strict Selmer identification, and what duality says

For a fixed good p>=5, choose q1,q2 with 1-dimensional finite local Kummer spaces L_i and invertible 2x2 localization matrix on a saturated MW basis P,Q. Put S_p=Sel(E[p]/Q), M_p=E(Q)/pE(Q), K_p=ker[S_p -> L_1+L_2]. Then Kummer gives
S_p = M_p direct_sum K_p, and K_p = Sha[p]
(the isomorphism depends on q1,q2). This is valid without any Sha finiteness hypothesis.

Let S_str and S_rel change these local conditions to 0 and full H^1 respectively. Since the finite Kummer condition is self-annihilating for the local Tate pairing, global reciprocity plus surjective MW localization forces S_rel=S_p, and S_str=K_p. This is *not* K_p=0.

A formal model makes the information barrier explicit: for ANY finite-dimensional F_p-vector space K, take S=F_p^2 direct_sum K, M=F_p^2 direct_sum 0, and lambda:S->F_p^2 projection. Then lambda|M is an isomorphism, S_str=K, and the linear-algebra exact sequence of strict/ordinary/relaxed Selmer structures has no contradiction when K is nonzero. Neither density of additional Chebotarev detectors nor invertibility of lambda|M excludes K.

## 3. Two distinct uniformity targets (not interchangeable)

(1) **Finite support:** there is finite set S of rational primes such that Sha[p]=0 for p outside S. This alone does not guarantee Sha finite: at exceptional primes, p-divisible torsion with unbounded exponent is not excluded.

(2) **Finite exponent:** there is a single C !=0 annihilating all of Sha, equivalent to finite Sha by §1. To obtain (2) it suffices to combine (1) with an independent finite exponent bound on each exceptional p-primary part.

For the 389a1 project, current p-specific PASS certificates do not constitute an all-p integral annihilator. A uniform theorem proving p-unit **two-factor Kurihara** numbers at all sufficiently large eligible p would establish (1), by Kim's precise hypotheses, but would still need an exponent argument at remaining p to yield (2).

## 4. A noncircular sufficient global input: primitive Euler/Kolyvagin bound

A genuinely new arithmetic argument must furnish an independently constructed nonzero integer C and a proven divisibility
    #Sha[p^infty] | p^{v_p(C)}
for *every* p (or the equivalent statement that p^{v_p(C)} kills each p-primary Sha, with adjustment for exponents).
The first condition implies finite Sha[p^infty] for all p and triviality outside the prime divisors of C. Combined with the finite-set argument, it proves finite Sha. It is essential to prove the inequality from actual global Euler/Kolyvagin classes and all local integrality hypotheses, not from the identity C=|Sha| or from the mere MW 2x2 determinant.

Mazur–Rubin's Kolyvagin-system machinery controls dual Selmer groups *provided a suitable global system and primitivity/divisibility bounds have been constructed*. It cannot create a nonzero primitive system from formal reciprocity alone. For E/Q the ordinary Kato core Selmer rank is 1 even when MW rank is 2; one must use the correct derived/refined setup rather than silently substitute rank(MW)=2 as the Mazur–Rubin core rank. See Mazur–Rubin, Kolyvagin Systems (2004), and Mazur–Rubin, Controlling Selmer groups in the higher core rank case, J. Théor. Nombres Bordeaux 28 (2016).

## 5. Concrete next proof obligation

Find an arithmetic datum D independent of Sha, integral at every relevant p, such that a published theorem plus fully checked local hypotheses yields p^{v_p(D)}*Sha[p^infty]=0 for all p. The fixed scalar must be produced *before* invoking any hypothetical Sha finiteness. If no such global D is available, an alternative route is a uniform two-prime Kurihara unit theorem outside an explicit finite set plus certified finite exponent bounds at that set.

No such unconditional D, uniform two-prime theorem, or exact complex BSD leading-term identity is established in this note. This note proves the logical equivalence in §1 and rules out a circular shortcut through pure Chebotarev/Poitou–Tate formalism.
