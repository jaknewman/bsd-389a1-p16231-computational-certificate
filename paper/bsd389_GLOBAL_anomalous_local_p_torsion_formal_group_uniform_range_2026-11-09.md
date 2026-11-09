# BSD 389a1 — A uniform formal-group local p-torsion criterion and all p<10000 audit (9 Nov 2026)

**NEW EXACT LOCAL THEOREM; NOT A PROOF OF GLOBAL Sha VANISHING OR STRONG BSD.**

Set E: y²+y=x³+x²−2x, conductor and minimal discriminant +389, and rational points A=(0,0), B=(1,0). The transformation U=36x+12, V=216y+108 produces V²=U³−3024U+46224 over every Q_p with p>=5. Write t=−U/V for the formal-group parameter at infinity.

## 1. Universal anomalous-prime lifting criterion

Let p>=7 be a good **anomalous** prime, so p|#E(F_p). Hasse's inequality yields a_p=1 and #E(F_p)=p. A mod p is a nonidentity element and therefore a generator. The reduction exact sequence, the p-adic formal-group logarithm and [p]E_1(Q_p)=E_2(Q_p) prove the exact equivalence

    E(Q_p)[p]=0  iff  w_p(A):=t([p]A)/p mod p !=0.

Proof: local p-torsion exists precisely if the reduction generator A can be corrected by a formal point to become p-torsion, which is possible iff [p]A∈[p]E_1=E_2. The latter is equivalent to t([p]A)≡0 mod p². This gives a *single necessary and sufficient* arithmetic test at all anomalous primes; it does not prove its nonvanishing for infinitely many p.

## 2. Verified complete finite range

An independently executed standard-library Python script checked all 1,225 good primes 7≤p<10,000, p≠389, by exact Legendre-sum point counting. Exactly five have p|#E(F_p). For each anomalous p, two independent modular p² group-law implementations (weighted Jacobian and homogeneous projective) obtained the same residues for the multiples [p]A and [p]B.

| p | a_p | #E(F_p) | t([p]A)/p mod p | t([p]B)/p mod p |
|---:|---:|---:|---:|---:|
| 859 | 1 | 859 | 831 | 38 |
| 1213 | 1 | 1213 | 743 | 428 |
| 1493 | 1 | 1493 | 1451 | 1074 |
| 1951 | 1 | 1951 | 927 | 1591 |
| 2521 | 1 | 2521 | 840 | 1994 |

Each residue is nonzero, so E(Q_p)[p]=0 at every anomalous prime in range. All other good primes in range are nonanomalous, hence also have E(Q_p)[p]=0. The good p=5 has #E(F_5)=9.

At the bad prime 389, c4=112, c6=−856, Δ=389, Kodaira type I_1 and c389=1. The split character is determined by −c6=856≡78 mod389, a quadratic residue; E has split multiplicative reduction. The identity component's residue group F389× has order 388, the component group order 1, and the formal kernel is 389-torsion-free. Therefore E(Q_389)[389]=0.

**EXACT FINITE-RANGE CONCLUSION:**

    E(Q_p)[p]=0 for EVERY rational prime 5≤p<10000 (1,227 primes in total).

This removes the previously overly strong 'nonanomalous' hypothesis from the p-local part of the pointwise Kurihara support theorem over this explicit finite range. It does not remove the global hypothesis Sha(E/Q)[p]=0 from that theorem, and it does not extend Castella–Sano's good-p Theorem B to bad p=389.

## 3. What remains

To finish prime-uniform Sha, a theorem controlling the actual global p-Selmer/Fitting ideal for all sufficiently large p is still required. Exact Mellin–Fricke and Faltings–Hriljac formulas separately characterize L''(E,1)/2 and Ω_E Reg(E), but do not prove their equality. Neither obstacle follows from this local computation.

**Reproducibility:** Standalone companion files in current conversation: \`bsd389_anomalous_local_torsion_audit.py\`, \`bsd389_anomalous_local_torsion_report.json\`, \`audit.log\`, and a ZIP archive with all four artifacts. Python standard library only.

**References:** Silverman, *The Arithmetic of Elliptic Curves*, formal groups and local reduction; Castella–Sano (2026), Theorem B (https://arxiv.org/pdf/2601.14504), and Kim (2025), §3–§5 (https://arxiv.org/pdf/2505.09121).