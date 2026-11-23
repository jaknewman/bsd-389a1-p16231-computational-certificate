# 389a1 — rigorous computer-assisted proof that Sha(E/Q)[11^infinity] = 0

**Date:** 23 November 2026.
**Status:** a *prime-specific computational theorem* conditional only on the correctness of the fully executed Sage/eclib arithmetic and its period normalization; the number-theoretic deduction uses the published unconditional Theorems 1.8 and 1.10 of Chan-Ho Kim. This does **not** prove global Sha=0, all-prime finiteness, or the exact complex BSD leading coefficient.

## 1. Genuine computational witness, supplied by the user

E: y^2+y = x^3+x^2-2x; N=389; p=11.

The user ran:
\`\`\`
python -u verification/bsd389_p11_Kurihara_397_991_full_sage.py
\`\`\`
Actual terminal output included:
\`\`\`
P11_LOCAL_WEDGE_PASS [[1, 10], [1, 7]] DET 8
KIM_P5_PUBLISHED_EXAMPLE_ANCHOR_PASS 4
P11_ECLIB_SYMBOL_13_SPOTCHECK_AND_SIGN_PLUS_PASS
P11_KURIHARA_FULL_START N 393427 HALF 196713 PRIMITIVE_ROOTS (5, 6)
P11_KURIHARA_PROGRESS 50000 / 196713
P11_KURIHARA_PROGRESS 100000 / 196713
P11_KURIHARA_PROGRESS 150000 / 196713
P11_FULL_WEIGHTED_MANIN_CONTRACTION_PASS 6
P11_KURIHARA_DELTA_COMPLETE 1 NONZERO True
P11_390_TABLE_SHA256 a8f442e9bfd29e9176d43fc765c6357516b9b4956a08b60d999cdecf58a4c9cd
P11_W390_SHA256 c05dbcaffeded931355c9b5fff24d28ed351d82c2ae4259167716ef1000a7219
P11_OUTPUT /home/bsdadmin/bsd389_p11_kurihara_397_991_full.json
P11_DURATION 3.255
P11_TWO_PRIME_KIM_UNIT_GATE_PASS_SHA11_ZERO_UNDER_THEOREM_HYPOTHESES
\`\`\`

The residue 1 follows from 2*6=12=1 modulo 11, because the even Neron-normalized modular symbols and the two discrete logarithm characters obey a→N−a symmetry. The script *exhausted* all (N−1)/2=196713 half representatives, and independently contracted its complete 390-coordinate weight vector. It also checked eclib direct values at 13 denominators and recovered Kim's published 389a1,p5, n41*61 example residue 4. These are strong arithmetic checks, though both 390 and direct pathways share a continued-fraction symbol engine; the JSON is still on the user's Ubuntu machine, **not yet independently materialized or rerun elsewhere**.

**Full provenance record:** results/bsd389_p11_Kurihara_397_991_USER_SAGE_PASS_2026-11-23.md.

## 2. Exact hypotheses of Kim

Primary source: Chan-Ho Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, Theorems 1.8 and 1.10 and §1.4, [published manuscript](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf).

* **p>=5 and ordinary:** p=11, a_11(E)=−4, so E has good ordinary reduction.
* **GL_2(F11) residual surjectivity:** LMFDB lists maximal mod-ell Galois image at every ell for 389a1, including ell=11; independently, 389 is multiplicative of discriminant valuation one, giving a nontrivial transvection, and Frobenius at 2 has polynomial X²+2X+2, discriminant −4 nonsquare mod11 (irreducibility), with surjective cyclotomic determinant. See [LMFDB 389a1](https://www.lmfdb.org/EllipticCurve/Q/389a1/).
* **Manin constant a p-unit:** the optimal curve has Manin constant c_phi=1.
* **Tamagawa:** c_389=1, the sole bad factor.
* **Local p-torsion:** #E(F11)=11+1−(−4)=16, prime to11, hence E(Q_11)[11]=0 (good reduction and no 11-torsion in the 11-adic formal kernel).
* **Auxiliary p-admissibility:** q1=397, q2=991 are prime, distinct, prime to 389*11; q_i≡1 mod11. Their exact traces are a_397=24, a_991=−53, so a_qi≡q_i+1 mod11. Moreover each q_i has E(F_qi)/11 E(F_qi) dimension precisely one: #E(F397)=374=11*34 and #E(F991)=1045=11*95.

The independent local-reduction check of Mordell–Weil P=(−1,1), Q=(0,−1) reported the matrix [[1,10],[1,7]] modulo 11 and determinant 8. It proves this specific MW basis detects the two independent local directions. It is not needed as an extra hypothesis to deduce Sha[11]=0 once Kim's Selmer isomorphism and global MW rank are established; it independently corroborates their compatibility.

## 3. Proof that Sha[11^infinity] vanishes

The computed nonzero residue
\[
\widetilde\delta_{397\cdot991}\equiv1\pmod{11}
\]
is a true Kim §1.4 *two-prime* Kurihara number, in the Néron-period-integral modular-symbol normalization. Thus both \(\operatorname{ord}(\widetilde\delta)\le2\) and the corresponding mod11 minimum degree is at most two.

By Kim Theorem 1.8(1), since the full Kurihara collection is nonzero,
\[
\operatorname{corank}_{\mathbb Z_{11}}\operatorname{Sel}(\mathbb Q,E[11^\infty])
=\operatorname{ord}(\widetilde\delta)\le2.
\]
As rank E(Q)=2, Kummer injects (Q11/Z11)^2 into the 11-power Selmer, proving the reverse inequality. Hence the *full* Kurihara minimum degree is 2. The mod11 minimum degree cannot be smaller than the full minimum degree, so it also equals 2. The actual n=397*991 is therefore **minimal** as required by Kim Theorem 1.10.

Kim Theorem 1.10 gives the canonical isomorphism
\[
\operatorname{Sel}(\mathbb Q,E[11])
\xrightarrow{\sim}
(E(\mathbb Q_{397})\otimes\mathbb F_{11})\oplus
(E(\mathbb Q_{991})\otimes\mathbb F_{11}).
\]
For each q_i, good reduction q_i≠11 yields E(Q_qi)/11 ≅ E(F_qi)/11, of dimension one by the above point counts. Thus
\[
\dim_{\mathbb F_{11}}\operatorname{Sel}(\mathbb Q,E[11])=2.
\]
The global Mordell–Weil group E(Q)≈Z² with trivial rational torsion gives \(\dim E(\mathbb Q)/11E(\mathbb Q)=2\). Finally, by the exact Kummer sequence
\[
0\to E(\mathbb Q)/11E(\mathbb Q)
\to \operatorname{Sel}(\mathbb Q,E[11])
\to\Sha(E/\mathbb Q)[11]\to0,
\]
we have \(\Sha[11]=0\). A nonzero element of any 11-primary torsion group has a nonzero 11-torsion multiple, hence
\[
\boxed{\Sha(E/\mathbb Q)[11^\infty]=0.}
\]
No global finiteness assumption on Sha is used. QED subject to the authenticated computation.

**Alternative:** the same result follows from Kim Theorem 1.8(2) and the witnessed unit \(\partial^{(2)}=0\): then \(Fitt_2(X_{11})=\mathbb Z_{11}\) and the finite Selmer defect vanishes.

## 4. Status and distinct arithmetic results

The independent **p=11, K=Q(sqrt(-43))** Gross–Brandt 110/110 computation gave \([T^2]\Theta\equiv6\bmod11\), with its own archive SHA 273c9e80... ; this corroborates a different anticyclotomic rank-two structure but **is not used to prove Sha[11]=0**. It is important not to import a theta coefficient as a Selmer-module matrix.

The proof above removes exactly one prime: 11. Previous genuine unit witnesses at 5,7 and 107 are separately recorded, each with their own provenance limits. Nothing here proves that such witnesses exist for all but finitely many rational primes or that the exact complex leading coefficient equals the BSD regulator expression. These remain the two genuinely global tasks.

## References

1. C.-H. Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, [source PDF](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf), Theorems 1.8, 1.10, §1.4, and §8 Example (1).
2. [LMFDB 389a1](https://www.lmfdb.org/EllipticCurve/Q/389a1/): rank2, torsion1, Manin1, Tamagawa1, Galois images, a11=-4.
3. \`verification/bsd389_p11_Kurihara_397_991_full_sage.py\` in this repository.
