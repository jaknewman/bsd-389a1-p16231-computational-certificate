# BSD 389a1: a *theoretical explanation* of the 481 Kurihara/Kummer zero matches (9 Nov 2026)

**New mathematical deduction from standard Poitou–Tate and two SOURCE theorems (Kim 2025; Castella–Sano 2026). Not a global BSD proof.** It explains why prior finite support coincidences are expected at primes where Sha[p] is *already known* to vanish. It does not independently make Sha vanish at untested primes.

Let E: y²+y=x³+x²−2x, conductor 389, discriminant +389, MW basis P=(-1,1), Q=(0,-1), MW rank 2 and torsion zero; all Tamagawa numbers 1.

Fix p≥5, p≠389, with full mod-p Galois image, p-unit Manin constant, **good nonanomalous** reduction p ∤ #E(F_p). Let q,r≠p,389 be distinct Kurihara admissible primes with q≡r≡1 mod p, a_q≡a_r≡2 mod p, and *v_p(#E(F_q))=v_p(#E(F_r))=1*. Then I_q=I_r=I_{qr}=pZ_p, both Frobenius actions are nonidentity unipotents and the local finite cohomology spaces are one-dimensional.

Write B_{qr} for the local finite Kummer 2×2 matrix of P,Q, and D_{qr}=det B_{qr}, well-defined up to an Fp unit. Write δ_{qr} for the minimally integrally normalized two-prime Kurihara number.

## Lemma (unconditional, even if Sha infinite)

If D_{qr}≠0 then

    Sel_{BK(qr)}(Q,E[p]) ≅ Sha(E/Q)[p],

where the left side uses **transverse local conditions** at q,r and usual finite conditions elsewhere. This is an exact global isomorphism, dependent on q,r for its explicit realization.

*Proof.* The standard p-Selmer S maps onto H¹_f(Q_q,E[p])⊕H¹_f(Q_r,E[p]) since the restriction to MW/p is B_{qr}. Poitou–Tate for the selfdual finite local structure implies that its relaxation at both q,r adds no classes: S_rel=S. A class of S_rel is already finite at q,r. It is transverse there exactly when its finite localizations both vanish, since finite∩transverse=0. Thus Sel_BK(qr)=ker(S→Fp²). The exact global Kummer sequence and uniqueness of the MW correction when B is invertible identify this kernel with Sha[p]. No use of BSD or Sha finiteness. QED.

## Theorem (pointwise support in rank two, as a deduction from Kim + Castella–Sano)

Under the specified conditions on p,q,r, and taking Kim's rigidity and Castella–Sano's proven refined Kurihara nonvanishing and integral comparison:

    δ̄_{qr} ≠ 0   <==>  [ D_{qr} ≠ 0 AND Sha(E/Q)[p]=0 ].

Here is the source-based proof roadmap, carefully separating prerequisites:

1. **Primitivity.** Castella–Sano Theorem B gives M∞(δ)=v_p(Tam_E)=0, since good p is either ordinary or supersingular with squarefree N=389. Theorem 2.1.3 relates the p-singular Kato derivative to δ_n by a p-adic **unit** times p^t, with p^t=#E(Q_p)[p∞]=1 for our nonanomalous p. Hence Kato's Kolyvagin system is primitive mod p.
2. **Core-vertex rigidity.** In Kim Theorem 3.9, at level I_n=p the mod-p derivative κ_n spans the stub module p^{λ(n)}H(n), where λ(n)=dim_Fp Sel_{0,n}. Since the Kato system is primitive, κ_n is nonzero exactly at a core vertex (λ(n)=0). The canonical relaxed Selmer module H(n) is one-dimensional there (Kim Theorem 3.7).
3. **Core vertex vs modified Bloch–Kato group.** Sel_{0,n} is the p-**strict** subgroup of the transverse Bloch–Kato Selmer Sel_{BK(n)}. If Sel_{BK(n)}=0 then certainly λ(n)=0. Conversely, if λ(n)=0, Sel_{BK(n)} injects under localization into H¹_f(Q_p,E[p]), a one-dimensional vector space by non-anomalous reduction. Kim §5.4 formula (5.8), based on Flach's self-dual Cassels–Tate pairing, gives *even dimension* for Sel_{BK(n)} over Fp; hence Sel_{BK(n)}=0.
4. **Derived Kato reciprocity.** When Sel_{BK(n)}=0, nonzero κ_n cannot be finite at p, so its p-singular image is nonzero. Conversely a nonzero p-singular image makes κ_n nonzero. Castella–Sano Theorem 2.1.3 now gives δ̄_n≠0 exactly when Sel_{BK(n)}=0.
5. **Necessity of D and Sha.** If D=0, a nonzero linear combination of P,Q has zero local finite classes at q,r, and hence gives a nonzero global class in Sel_{BK(n)}; consequently δ̄_n=0. If δ̄_n≠0, Kim Theorem 1.1 and M∞=0 force the entire p-primary Sha to vanish.
6. **Sufficiency.** If D≠0 and Sha[p]=0, the unconditional lemma makes Sel_{BK(n)}=0, so δ̄_n≠0.

**Strictly limited conclusion:** For each nonanomalous p satisfying these theorems, the equality of the *zero supports* across all qualifying q,r is a theorem PROVIDED Sha[p]=0. Thus the 481 earlier exact calculations at p=5,7,11,13,17 are explained theoretically once their independently certified p-primary Sha vanishings are used as input.

Conversely, **for any good nonanomalous p with Sha[p] nonzero**, all two-prime Kurihara numbers are 0 mod p (by Kim), but Kummer–Chebotarev still supplies pairs with D≠0. The empirical zero-support equivalence therefore cannot hold at such a prime. This makes the boundary of the theorem sharp.

## Independent local-hypothesis audit

The Python audit \`bsd389_theoreme_support_481_audit.py\` (local current-session copy) rechecked all 481 archived pairs from their JSON, verifies v_p(#E(F_q))=1 at every archived auxiliary prime, independently enumerates #E(F_p) for p=5,7,11,13,17, and verifies 481/481 matching zero statuses. Local orders of E(F_p): 9,13,16,17,24 respectively, all prime to p.

For reproducibility the full source-based mathematical note and independent Python script are provided as conversation artifacts. This GitHub file records the proof argument, not the large finite JSON inputs.

## Not solved

The theorem **does not prove Sha[p]=0 at an unknown p**: it identifies the nonvanishing of any suitably separating two-prime Kurihara number with precisely that arithmetic obstruction. It also does not establish finite support of Sha over all p, handle p-anomalous reduction or the bad prime p=389 by the present proof, nor does it establish the **complex exact leading-term identity**

    L''(E,1)/2 = Omega_E Reg(E) · #Sha(E/Q).

The already proven Mellin–Fricke series and Arakelov height identities describe each side *separately*, not their equality.

## Primary references

- Kim & Pollack, *The refined Tamagawa number conjectures for GL₂*, arXiv:2505.09121, Ths. 1.1, 3.7–3.9, §5.4 especially formula (5.8): https://arxiv.org/pdf/2505.09121 .
- Castella–Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, arXiv:2601.14504 (January 2026 preprint), Th. B and Th. 2.1.3: https://arxiv.org/pdf/2601.14504 .
- Standard Poitou–Tate for finite self-dual Selmer structures; Mazur–Rubin, *Kolyvagin Systems*, Memoirs AMS 2004.

**Verdict: new exact conditional support theorem, not uniform Sha vanishing and not a complex rank-two BSD proof.**