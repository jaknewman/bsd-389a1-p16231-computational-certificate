# BSD 389a1 — A genuine bounded-range integer annihilator; rigorous criterion for an ALL-p annihilator (9 Nov 2026)

**STATUS:** a new original formal reduction and exact independent finite-range enumeration, incorporating a strong PUBLISHED theorem. **No unconditional full Sha annihilator, uniform 2-prime Kurihara nonvanishing theorem, or exact complex BSD claimed.**

## I. Published theorem immediately closes >5000 Sha primes

Stein and Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013), **Theorem 12.3, p.1788**, prove for E=389a1:

    Sha(E/Q)[p] = 0

for p=2 and for **all 5005 good ordinary primes p<48859 EXCEPT p=16231**. The ordinary set includes p=3 and 5004 primes p>=5. Thus 5004 ordinary p plus p=2 are certified. As a p-primary torsion group has nonzero p-torsion if and only if it is nonzero, this also proves Sha(E)[p∞]=0 for the 5005 covered p.

The 19 primes NOT covered by their Theorem 12.3 below 48859 are:

    107,389,599,1049,2957,6661,8263,9397,9551,14633,15101,
    16231,28591,30671,30869,31799,34781,36263,45161.

These consist of **17 supersingular good primes**, the **bad** prime 389 and the **exceptional ordinary** prime 16231. Some have separate project certificates; they are exceptions to THIS published theorem, not necessarily open local computations.

Our independent complete C++ prime/trace scan (5,004 ordinary p>=5, 1 ordinary p=3, 17 supersingular, 19 exceptional matches) reproduces the exact ranges in the publication. It also finds 8 anomalous good p>=5 below 48859:
859,1213,1493,1951,2521,12697,26821,38747. For the last three a new dual projective group-law test computes nonzero t([p](0,0))/p residues 6286,5889,485 respectively, independently agreeing with t([p](1,0))/p=1214,1817,33230. These are only extra LOCAL checks.

Primary source: https://wstein.org/papers/mcom2649-iwasawa-alg.pdf.

## II. An ACTUAL bounded-range integer annihilator

Take the product of the 19 exclusions:

    D_48859 =
    67181435539744144109609850443668956733650922010230259680651383373230961639.

Then the entirely unconditional, exact statement (combining the published theorem and elementary group theory) is:

    D_48859 · ( ⊕_{prime p<48859} Sha(E/Q)[p] ) = 0.

For p not dividing D_48859, Sha[p]=0 by the published theorem. For p dividing D_48859, multiplication by p kills the group Sha[p] by definition. This is independent of the choice of p, but it **does not** annihilate higher p-power torsion at excluded primes or any p>=48859; it is NOT the requested global Sha annihilator.

## III. A full annihilator is exactly a finiteness theorem

Let X=Sha(E/Q). X is torsion, and X[n] is finite for every n (finite n-Selmer and the Kummer exact sequence).

**Proposition A:** There exists a nonzero integer D with D X=0 **if and only if** X is finite.

Proof: D X=0 implies X=X[|D|], finite. Conversely the exponent of finite X works.

**Proposition B (sufficient FULL certificate):** Suppose A∈Mat_m(Z), D=det A≠0, and for **every** prime p we construct and prove an injection

    Sha(E/Q)[p∞] ↪ coker(A:Z_p^m→Z_p^m).

Then **D Sha(E/Q)=0**. Proof: adj(A)·A=D I, so D kills all those cokernels, then all p-primary Sha; Proposition A proves global finiteness.

**Weaker prime-support certificate:** An injection Sha[p]→coker(A mod p) for every p off an explicitly finite set S would prove Sha[p]=0 for p∤D outside S. Finiteness of exceptional p-primary groups would still need independent proof.

**WHAT IS MISSING:** There is currently **no** integral comparison map from the global Sha/Selmer groups to the coker of a *single* square non-singular integer matrix A built from our Manin symbols, Faltings–Hriljac pairings, or auxiliary Kummer determinants. The 390 Manin coefficients have primitive content 1, but this does NOT prove that their content equals any global Selmer Fitting ideal; asserting so would simply assume the unproved theorem.

## IV. Fixed-conductor no-go

For any fixed two-factor conductor n=q1 q2, p-Kurihara admissibility requires p|(q1−1) and p|(q2−1). Thus p≤min(q1−1,q2−1). A **finite collection of fixed auxiliary conductors** can never certify two-prime Kurihara nonvanishing for unbounded p. The n=1 coefficient is L(E,1)/Ω=0 for this rank-two E, and odd lengths vanish by functional equation.

Any successful all-p argument must therefore either provide variable q(p),r(p) with an *additional global* nonvanishing theorem, or construct the integral Selmer-cokernel comparison in Proposition B. Castella–Sano 2026 gives **some-length** nonvanishing (Theorem B) and Kim 2025 yields **consequences** of a two-factor unit (Theorem 1.1), but neither gives a prime-uniform length-two witness.

## V. Independent obligations

The full Sha annihilator/finite-support theorem remains unproved. The exact complex identity L''(E,1)/2=Ω_E Reg(E)·#Sha remains independently unproved.

**Refs:** Stein–Wuthrich 2013 (above); Castella–Sano 2026 https://web.math.ucsb.edu/~castella/Kurihara.pdf; Kim 2025 https://arxiv.org/pdf/2505.09121; Banwait 2026 https://arxiv.org/abs/2609.08431.
