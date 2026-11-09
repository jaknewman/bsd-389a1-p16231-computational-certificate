# BSD 389a1 — Local p² Kurihara/Kummer distinction and exact Hasse complexity barrier

**2026-11-09.** Authenticated new exact finite-field enumeration + unconditional Hasse inequality. **Not** uniform Sha finiteness or complex BSD.

## 1. A genuine depth-25 witness that does NOT have two primitive-transvection primes

Fix E/Q: y²+y=x³+x²−2x, P=(−1,1), Q=(0,−1), p=5. The independently archived authentic depth-25 Kurihara calculation gives

    δ_(5351·13001) = 15 (mod 25).

The q’s are both 25-Kurihara-admissible, since q≡1 mod25 and a_q≡2 mod25. However an **independent entire finite-field point enumeration** now proves

| q | a_q | #E(Fq) | #E(Fq)[5] | 5-primary group | projected P,Q |
|---|---:|---:|---:|---|---|
| 5351 | −23 | 5375=125·43 | 5 | Z/125 | U,64U |
| 13001 | −73 | 13075=25·523 | 25 | (Z/5)² | U,2U |

Thus Frobenius at **13001 is identity on E[5]**, and H¹_f(Q_13001,E[25]) ≅ (Z/5)², not Z/25. The q=5351 prime has cyclic 5-primary local points and a nonidentity-unipotent mod-5 Frobenius.

**Conclusion:** a p²-Kurihara admissible prime does **not** automatically have the *primitive transvection* Frobenius and cyclic local quotient assumed in the high-depth Kummer–Chebotarev theorem. The published δ=15 mod25 result remains valid; we do NOT re-evaluate it here. It gives an authentic valuation-one witness but is not a 2-transvection numerical example.

The executed audit is shipped in the conversation artifact \`bsd389_depth2_Kummer_Kurihara_Hasse_gap_20261109.zip\` with complete SHA256 checks, using only Python standard library and exact elliptic group laws.

## 2. Exact Hasse trace-gap theorem

Let p≥5 and m≥1. If a good auxiliary prime q satisfies

    q ≡ 1 (mod p^m),    a_q(E) ≡ 2 (mod p^m),

and a_q(E)≠2 as an **ordinary integer**, then a_q=2+k p^m for k∈Z\\{0}; hence |a_q|≥p^m−2 and Hasse's bound |a_q|≤2√q proves

    **q≥ceil((p^m−2)²/4).**

For two such q,r with both traces not exactly 2, the conductor obeys

    **qr≥ceil((p^m−2)²/4)²**, asymptotically p^(4m)/16.

For m=2:

- p=17: each q≥20,593; qr≥424,071,649.
- p=107: each q≥32,758,453; qr≥1,073,116,242,953,209.
- p=599: each q≥32,184,180,601; qr≥1,035,821,480,957,784,721,201.
- p=16231: each q≥17,350,864,294,659,721; qr≥301,052,491,771,697,577,522,239,179,797,841.

The special integer-trace case a_q=2 is an **explicit exception**: the theorem does not lower-bound q in that case. Do not suppress the exception or claim a fully uniform complexity lower bound.

Thus passing from testing a mod-p unit to testing a mod-p² nonzero Kurihara coefficient weakens the **logical nonvanishing condition** (by Cassels–Tate parity), but may sharply raise the direct-sum arithmetic cost. This cannot substitute for a *global* Euler/Kolyvagin-system theorem of two-prime nonvanishing.

## 3. Exact conditional global obstruction

For a fixed good p≥5 satisfying Kim 2025 Th. 1.1 + Castella–Sano 2026 Th. B, if Sha(E/Q)[p]≠0, **every** admissible two-prime δ defined modulo p² must be zero modulo p². Otherwise its p-adic valuation ≤1 would force Sha[p∞] finite of order p^e with 0≤e≤1; Cassels–Tate's nondegenerate alternating pairing forces e even and hence zero, contradiction.

But high-depth Kummer–Chebotarev still supplies infinitely many q,r with cyclic local quotients and invertible MW determinant mod p². Therefore local Kummer separation alone **cannot** prove global δ nonvanishing without an extra global arithmetic input; this is a **conditional logical statement**, not a claim that Sha(389a1)[p] is nonzero.

**Next open mathematical gate:** construct an independent *global rank-two derived-Kato/Selmer-determinant primitive element* for all sufficiently large p, rather than lifting already-known rational points or multiplying admissible modulus depth.

**Complex rank-two BSD leading-term equality remains separately open.**

Sources: Castella–Sano arXiv:2601.14504, definitions and Ths. 2.1.3, B; Kim arXiv:2505.09121, Ths. 1.1 and 3.9; Hasse bound.
