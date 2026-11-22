# 389a1 — Rank-two Kurihara numbers at arbitrary p-adic depth detect the exact p-primary Sha

**22 November 2026.** Status: rigorous corollary of published theorems by Chan-Ho Kim and Castella–Sano, plus Kummer and Cassels–Tate. This is a **prime-by-prime criterion**, not an existence theorem for all primes and not full BSD.

## 1. Setup and source hypotheses

Let E/Q be `y^2+y=x^3+x^2-2x`, of conductor 389, rank 2, rational torsion zero, with product of Tamagawa numbers equal to 1. Fix a prime p>=5 of good reduction p!=389 such that `E[p]` has surjective Galois image and the optimal modular parametrization has p-unit Manin constant. (The last two assumptions must be checked or justified for each claimed range; they are not to be omitted.) Castella–Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem B, applies at p good ordinary or good supersingular when the conductor is squarefree, hence at all such good primes of E subject to these residual/Manin conditions.

For each p-admissible auxiliary q, as in the sources,

    q != p, q not dividing 389, q = 1 (mod p), a_q(E) = q+1 (mod p),
    I_q = (q-1, a_q-q-1) Z_p = p^{k_q} Z_p,
    k_q = min(v_p(q-1), v_p(a_q-q-1)) >= 1.

For n=q1*q2 with distinct admissible primes, `I_n=I_q1+I_q2=p^{k_n}Z_p`, `k_n=min(k_q1,k_q2)`. The **normalized** Kurihara symbol δ_n is defined modulo I_n; it is NOT an arbitrary p-adic number. Let

    e_n = v_p(δ_n) if δ_n != 0 in Z_p/I_n, with 0<=e_n<k_n,
    e_n = infinity if δ_n = 0 in Z_p/I_n.

This convention matches the p-adic divisibility indices in Kim's §1.5; do **not** assign valuation k_n to a zero residue. Set `d_2(p)=inf_{q1!=q2 admissible} e_{q1*q2}`.

## 2. Theorem (exact rank-two classification)

Under the above hypotheses:

    d_2(p) < infinity  <=>  Sha(E/Q)[p^infinity] is finite.

If the p-primary Sha is finite, its exact order is determined by

    v_p(#Sha(E/Q)[p^infinity]) = d_2(p).

In particular d_2 is either infinity, zero, or a positive **even integer**; d_2=1,3,5,... cannot be the global minimum.

**Proof.** Castella–Sano Theorem B proves `partial^(infinity)(δ)=v_p(Tam_E)=0` for this curve, and in particular the full Kurihara family is nonzero. Kim Theorem 1.8(1) therefore applies, giving

    ord(δ) = corank_Zp Sel_{p^infinity}(E/Q).

The Kummer exact sequence and the proven rank two show this corank equals `2 + corank_Zp Sha[p^infinity]`. Since each p-primary Sha is cofinitely generated, it is finite iff its corank is zero. By Kim's definition `ord(δ)` is the minimum number of admissible auxiliary factors among nonzero Kurihara residues. Therefore `ord(δ)=2` iff some nonzero two-prime residue exists, proving the equivalence (no degrees <2 are possible because the rank is 2).

In the finite case, Kim Theorem 1.8(2) at i=2 states

    Fitt_2(Sel_{p^infinity}(E/Q)^dual)
       = p^{partial^(2)(δ)-partial^(infinity)(δ)} Z_p
       = p^{d_2(p)} Z_p.

Dualizing Kummer gives a split Z_p-module

    Sel_{p^infinity}(E/Q)^dual ~= Z_p^2 ⊕ Sha[p^infinity]^dual.

Hence its second Fitting ideal is `p^{v_p(#Sha[p^infinity])} Z_p`, which yields the valuation identity. Cassels–Tate's perfect alternating pairing for finite Sha over Q implies its order is a square, so `d_2(p)` is even. QED.

## 3. One-witness upper bound and parity bootstrap

Suppose **one actual, correctly normalized** two-prime Kurihara residue is certified nonzero modulo I_n and has valuation `e < k_n`. Then `d_2(p) <= e`, so

    #Sha(E/Q)[p^infinity] <= p^{2 floor(e/2)}.

This also proves that p-primary Sha is finite, without *a priori* finiteness.

| Certified e of ONE nonzero two-prime residue | Conclusion for Sha[p^infinity] |
| --- | --- |
| 0 | Sha[p^infinity] = 0 |
| 1 | Sha[p^infinity] = 0 (parity improvement) |
| 2 or 3 | finite, order <= p^2 |
| 4 or 5 | finite, order <= p^4 |

In particular a properly sourced `δ_n = p*u mod p^2` with `u` a p-unit, and `I_n ⊂ p^2Z_p` (i.e. k_n>=2), is **enough to prove Sha[p^infinity]=0 even though δ_n is zero modulo p**. This does not contradict the earlier unit criterion: the theorems imply that then a *different* two-prime admissible n' with δ_n' nonzero mod p must also exist.

The distinction between the **single-witness bound** `d_2<=e` and the **exact equality** `d_2=v_p(#Sha)` is essential. A single residue e=2 does not prove that Sha has order p²; other pairs may have e=0.

## 4. Genuine versus synthetic data

Existing project anchor pairs, from authenticated earlier computations: p5 / q=(41,61), p7 / q=(113,673), p107 / q=(369793,383917). Their I_n have p-adic precision k_n=1 and reported normalized delta modulo p respectively 4,2,34. If the full modular-symbol provenance and source hypotheses are sound, e=0 certifies Sha primary zero at those p. No new p-specific user computation is claimed here.

As an *independent auxiliary-prime arithmetic check*, p5 q=(5351,10651) has `a_5351=-23`, `a_10651=2`, and `k_n=2` (verified by exact finite-field point counts); a hypothetical δ_n=5 mod25 would force Sha[5^infinity]=0 by the theorem. **That δ value is deliberately SYNTHETIC / NOT COMPUTED.** Its purpose is to exercise the novel e=1 branch without claiming a Gross or Kurihara computation.

## 5. Uniform BSD obstruction, sharply identified

At all good p satisfying the source hypotheses, global Sha finite support would follow from showing `d_2(p)=0` for all p outside a fixed finite set; global Sha finiteness would also require finiteness of the finitely many exceptional primary parts. **Neither fact is proved by this note.** Showing only that `d_2(p)<infinity` at each p establishes primewise finiteness, but permits infinitely many nontrivial components. Even proving global Sha=0 would still not establish the exact complex equality `L''(E,1)/2 = Omega_E Reg(E)`.

## References (checked directly against printed theorem pages)

- Chan-Ho Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, Theorem 1.8 and §1.4--1.5, PDF printed pages 6--7, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf .
- Francesc Castella and Takamichi Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem B (printed page 3), https://web.math.ucsb.edu/~castella/Kurihara.pdf .
- Cassels–Tate pairing, perfect alternating pairing on finite p-primary Sha for p odd (elliptic curve over Q).