# 389a1 — exact global second-Fitting criterion, squarefree refinement, and obstruction to reusing a fixed Kurihara pair

**Date: 23 November 2026. Mathematical status: elementary theorems PROVED; an arithmetic global comparison has NOT been constructed, so no new full BSD or global Sha-finiteness claim.**

## 1. Exact p-adic algebraic Selmer decomposition, with no Sha finiteness assumption

Let E/Q be y²+y=x³+x²−2x, with Mordell–Weil group E(Q)=Z·P ⊕ Z·Q and torsion 0, as already certified. For **every prime** p set

- X_p := Sel(Q,E[p^∞])^∨, the Pontryagin dual (a finitely generated Z_p-module, because mod-p Selmer is finite);
- Y_p := Sha(E/Q)[p^∞]^∨.

Kummer and Pontryagin duality give the split short exact sequence of **Z_p modules**

    0 → Y_p → X_p → Z_p² → 0.

The splitting uses only that Z_p² is projective. Thus X_p ≅ Z_p² ⊕ Y_p, but there is no reason that Y_p=0 or even finite.

For a finitely generated module over the DVR Z_p,

    Fitt_{2,Z_p}(X_p) = Fitt_{0,Z_p}(Y_p).

If Y_p has positive free Z_p-rank, the ideal is (0). If Y_p is finite of cardinality p^e, the ideal is exactly (p^e). In particular

    Fitt_2(X_p) = (p^e)  iff  Sha(E/Q)[p^∞] is finite of order p^e,

and Fitt_2(X_p)=(0) if its p-primary component has positive corank. These are identities, not BSD assumptions. Because Y_p is finitely generated, corank zero implies Y_p finite.

## 2. One nonzero INTEGER sufficient for *global* finiteness

**Theorem 1 (uniform integral second-Fitting gate).**
Suppose there is a SINGLE nonzero integer D, constructed independently of the unknown Sha, for which a genuine arithmetic argument proves

    (D)·Z_p ⊆ Fitt_{2,Z_p}(X_p)       for EVERY prime p.

Then Sha(E/Q) is finite and its order divides |D|.

**Proof.** For each p, (D)Z_p is nonzero, so Fitt_2(X_p) is nonzero and Sha[p^∞] is finite, say of order p^{e_p}. The ideal inclusion is equivalent to e_p≤v_p(D). Thus e_p=0 whenever p∤D. Summing the finite p-primary components shows finite support and the order bound ∏_p p^{e_p}|D|. QED.

This condition is in fact EQUIVALENT to global Sha finiteness if one allows choosing D after knowing Sha: take D=#Sha. This is why **producing D and a noncircular uniform comparison is the entire hard step**. The theorem is a precise acceptance test, not an automatic consequence of Kato, Kim, local Chebotarev or an analytic near-one ratio.

## 3. A stronger squarefree conclusion, using Cassels–Tate

When finite, Sha(E/Q) has a perfect alternating Cassels–Tate pairing, and hence its order is a perfect square (for elliptic curves with their canonical principal polarization). Consequently, under Theorem 1,

    v_p(#Sha) ≤ 2⌊v_p(D)/2⌋.

Thus the order of Sha divides the **largest square divisor**
    D_sq = ∏_p p^{2⌊v_p(D)/2⌋}.

**Corollary 2.** If the verified common integer D is squarefree, then **Sha(E/Q)=0** (not merely finite). More generally, primes occurring to exponent at most one in D are automatically excluded from Sha; only squarefull primes p with p²|D could remain.

This squarefree gain concerns an **ORDER/FITTING bound**. It is NOT valid for a merely squarefree annihilator D·Sha=0: the group (Z/p)^2 is killed by squarefree p but has order p². The distinction matters critically.

## 4. How to package a testable prime-independent comparison

A concrete, noncircular *sufficient certificate format* is:

1. Exhibit a finite rank integer matrix A∈M_m(Z) from **independently computed arithmetic objects** with det A = D≠0.
2. For every prime p, construct (and prove compatible with local Selmer conditions) a **surjective Z_p-linear comparison**
   
       coker(A:Z_p^m→Z_p^m) ↠ Y_p = Sha[p^∞]^∨.

Then Y_p is a quotient of a finite p-group of order p^{v_p(D)}, so its length is at most v_p(D); Theorem 1 applies. A subquotient relation is sufficient. One can equivalently establish directly the uniform Fitt_2 inclusion without presenting such a matrix.

**The missing arithmetic map is not in the repository.** The fixed 390-term integral modular-symbol vector has content one, and the Hecke/Brandt eigenspace has an integral primitive vector, but these facts alone do not construct a map onto Y_p for any p. A characteristic-ideal theta unit is also not an augmentation Fitt2 containment; explicit countermodels in paper/bsd389_2026_fitting_augmentation_bockstein_obstruction.md prove this.

The natural research target is a genuinely global *derived rank-two Kato/Euler-system/Selmer-complex integral comparison*, not an invented mapping from primitive Hecke data into Sha.

## 5. Rigorous obstruction: a fixed collection of auxiliary primes can NEVER cover the p-tail

If q is p-admissible in the sense used for a Kurihara derivative, it satisfies

    q≡1 (mod p).

Therefore p divides q−1. For any FIXED finite set of auxiliary primes Q, all candidate p divide the integer
    M_Q = ∏_{q∈Q}(q−1),
so no p>max_{q∈Q}(q−1) can be detected by a Kurihara computation using only primes in Q.

For the authentic two-prime p=11 witness q=397 and 991,

    gcd(397−1,991−1) = gcd(396,990) = 198 = 2·3²·11.

Therefore the ONLY prime p≥5 for which BOTH primes are p-admissible is p=11. No fixed q397,q991 norm or two-prime determinant can be recycled as an all-p Sha certificate. Varying q with p (or replacing this method by an integral derived class over Z independent of p) is mathematically unavoidable.

This conclusion is independent of the value δ_397·991=1 mod11.

## 6. Sharp audit of the earlier bounded-range integer D_low

An existing proof branch computes the squarefree integer

    D_low = ∏_{p∈E_low} p

over 18 excluded primes p<48859 (including the bad prime 389). It proves

    D_low · (⊕_{5≤p<48859} Sha[p]) = 0.

For p|D_low this is merely the universal fact p·Sha[p]=0. It does NOT prove the stronger Fitt2 inclusion (D_low)⊂Fitt2(X_p), and **cannot** be fed into the squarefree corollary.

Indeed take at any p|D_low the formally allowable paired module
    Y_p=(Z/p)^2, X_p=Z_p² ⊕ Y_p.
Then D_low annihilates Sha[p], but Fitt2(X_p)=(p²), which does not contain (p). This model respects the Cassels–Tate square-order constraint. The wrong implication is therefore formally disproved.

## 7. Clear acceptance test for the next *genuine* global theorem

To conclude BSD finiteness we must obtain either:
- a **specific nonzero D** and actual compatible arithmetic maps at ALL p giving (D)⊂Fitt2(X_p), with no Sha-finiteness hypothesis, or
- an independently proved cutoff B such that Sha[p]=0 for all p>B, plus p-primary finiteness at every remaining prime.

The first route could deliver Sha=0 immediately if D is squarefree. The second route is precisely where the existing 5004 finite-range results stop: their cutoff is a **range checked**, not a proof that the rest of the p-tail is zero.

The near-one Archimedean ratio from the project provides no Fitt2 containment, because the exact rank-two BSD leading-term equality used to turn the ratio into #Sha is itself unproved.

**Scope:** this document sharpens and audits the one-shot global proof obligation, demonstrates two exact no-go deductions, and does not pretend that the sought global comparison has been built.
