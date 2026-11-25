# BSD 389a1 — A rigorous rank-four obstruction to the missing primitivity implication (9 November 2026)

**NEW MATHEMATICAL RESULT:** a real, non-CM, semistable rank-four elliptic curve disproves the proposed *general* inference “full primitive Kato/Kurihara system + maximal local Kummer extensions ⇒ a nonzero two-prime Kurihara derivative”. The example works for **every sufficiently large good prime**, not just an isolated congruence. **This does not disprove a rank-two-specific comparison for 389a1, and does not establish global Sha finiteness or complex BSD.**

## 1. Published rank-four countermodel

Let

    C : y² + xy = x³ − x² − 79x + 289

have conductor N=234446=2·117223, discriminant 468892=4·117223, proven Mordell–Weil rank **4**, and no CM. Published independent generators include

    (−10,7), (−9,19), (−8,23), (0,17).

The four point equations and invariants were rechecked by standalone exact Python. The rank-four independence itself is a *published input*, not implied by checking these equations.

For all sufficiently large good primes p, Serre's open image theorem gives residual GL₂(Fp) image; p is a unit for the fixed nonzero Manin constant. Since N is squarefree, Castella–Sano (2026) Theorem B yields

    **M_infty(C,p)=v_p(Tam(C))=0**.

Thus C has a *globally primitive Kurihara system*: at least one integrally normalized coefficient at some finite auxiliary length is a p-unit.

On the other hand, rank(C(Q))=4 forces corank Sel_(p∞)(C/Q)≥4. Kim (2025), **Corollary 1.11**, proves that the existence of any nonzero Kurihara coefficient δ_n at its *actual* coefficient precision implies

    corank Sel_(p∞)(C/Q) ≤ ν(n).

Therefore **ALL length-0,1,2,3 Kurihara coefficients vanish** at their actual p-adic precision:

    **M₂(C,p)=∞, yet M∞(C,p)=0**.

This is a source-based mathematical theorem for all sufficiently large good primes p.

## 2. Kummer separation still does not repair it

Any two of the independent rational points remain linearly independent mod p for all but finitely many p. Sah's lemma, the natural GL₂ representation, and Chebotarev then supply infinitely many good nonidentity-unipotent auxiliary q,r for each large p, with **unit two-by-two local Kummer determinant** for those two points. Nonetheless

    **delta_(q·r)(C) = 0 in Zp/I_(qr)**

for **every** such pair, by Kim's corank bound. Thus the combined *generic* assertion

    local rank-two independence + global Kato primitivity
       ⇒ nonzero two-prime Kurihara

is demonstrably FALSE, even with maximal mod-p image and a squarefree conductor. Any valid theorem specialized to E389a1 must use the fact that its **ENTIRE** Mordell–Weil rank is two AND independently exclude extra global Selmer directions.

## 3. Exact two-layer remaining gate for E389a1

For E=389a1, rank E(Q)=2 and Tamagawa product=1. Under Kim's Theorem 1.1 + Castella–Sano's Theorem B at every eligible good p≥5, put rho_p=min number of factors in a nonzero δ_n (nonzero in its actual coefficient ring). Then

    rho_p = corank Sel_(p∞)(E/Q)
          = 2 + corank Sha(E/Q)[p∞].

Therefore

    **rho_p=2  iff  Sha(E/Q)[p∞] is finite.**

Once rho_p=2, Fitt₂(Sel_(p∞)^dual)=p^(M₂(p)) and M₂(p)=v_p(#Sha[p∞]) is even by Cassels–Tate. A *single* true two-prime coefficient nonzero mod p² forces M₂(p)=0, hence Sha[p∞]=0.

The exact missing all-p inputs separate into:
(A) **FINITE CORANK GATE**: prove rho_p=2 (rule out a p-divisible Sha component) for all relevant p, independently of Kummer;
(B) **FINITE SUPPORT GATE**: prove M₂(p)=0 for all sufficiently large p, and handle finitely many exceptional primes.
Neither is implied by M∞(p)=0.

The previously defined “global integer ideal” A_E=intersection_p Fitt₂(Sel_p^dual)∩Z is **canonical but nonconstructive**: A_E≠0 already *equivalent* to Sha(E) being finite. Giving it a name does not produce a nonzero integer in it. No all-prime integral matrix controlling the global strict Selmer has been constructed.

## 4. Exact reproducibility and references

See conversation files \`bsd389_new_obstruction/rank4_kurihara_obstruction_audit.py\`, \`bsd389_new_obstruction/bsd389_rank4_primitive_vs_length2_no_go_20261109.md\`, and ZIP. The code confirms four rational points, c4=3801, discriminant 468892 and squarefree conductor 234446, NOT published rank independence, open image or advanced theorems.

- [M. Rubinstein — rank 4 curves, proven rank, independent generators](https://www.math.uwaterloo.ca/~mrubinst/elliptic_curves/records/rank_4.html).
- [Castella–Sano, 2026, Theorem B](https://web.math.ucsb.edu/~castella/Kurihara.pdf).
- [Kim, 2025, Theorem 1.1, Corollary 1.11](https://arxiv.org/pdf/2505.09121).
- Serre's open-image theorem; Sah's lemma; Chebotarev.

**Verdict:** A definitive no-go for the *generic* local-Kummer + global-primitive shortcut, but the rank-two-specific global Sha and exact archimedean BSD problems remain OPEN.

## 5. Sharpened dichotomy specifically for 389a1

The root number of E389a1 is +1 and δ_1=L(E,1)/Ω=0 exactly, so the Kurihara functional equation kills odd auxiliary lengths and ρ_p≥2. If **every** two-prime coefficient vanishes in its actual integral coefficient ring, then ρ_p≥4. The Kim structure theorem gives

    corank_Zp Sha(E389a1)[p∞] = ρ_p−2 ≥2,

so Sha(E389a1)[p∞] contains an abstract divisible subgroup (Qp/Zp)^2.

On the other hand, **if any** two-prime coefficient survives at some actual finite p^h precision, then ρ_p=2 and Sha[p∞] is finite.

This is an exact source-based **finite-versus-divisible alternative** for every eligible good p, not a test that can be decided by looking only modulo p. A vanishing δ mod p can coexist with a nonzero δ mod p², as the previously audited depth-25 p=5 example shows.

The root number +1, rank two and vanishing central L-value of E389a1 are recorded by [LMFDB 389.a1](https://www.lmfdb.org/EllipticCurve/Q/389a1/).