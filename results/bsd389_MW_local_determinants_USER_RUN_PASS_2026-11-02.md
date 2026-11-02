# Genuine Ubuntu MW two-auxiliary local determinant run — PASS for p=5,7,107 (2026-11-02)

**Provenance:** all stdout below is supplied directly by the user from their `bsdadmin@ubuntu` Sage-enabled shell, after successfully fast-forwarding GitHub `main` from `a3f1449` to `2a498dd`. The program [`verification/bsd389_MW_two_auxiliary_local_determinants.py`](../verification/bsd389_MW_two_auxiliary_local_determinants.py) uses **only Python standard-library elliptic-curve group law and exact finite-field point counts**; it neither imports Sage nor reads Kurihara modular-symbols. The output JSON is on the user's machine, **not** present in this GitHub repository.

## Actual command

```bash
python -u verification/bsd389_MW_two_auxiliary_local_determinants.py \
  --output ~/bsd389_MW_local_determinants_5_7_107.json \
  2>&1 | tee ~/bsd389_MW_local_determinants.log
```

## Verbatim user stdout

```text
MW_KURIHARA_LOCAL_P_TORSION_ZERO_PASS p 5 E_Fp_order 9
MW_KURIHARA_LOCAL_ROW_PASS p 5 q 41 a_q -3 E_Fq_order 45 cofactor 9 row (1, 3)
MW_KURIHARA_LOCAL_ROW_PASS p 5 q 61 a_q -8 E_Fq_order 70 cofactor 14 row (1, 0)
MW_KURIHARA_TWO_LOCAL_IMAGES_BASIS_PASS p 5 auxiliaries (41, 61) matrix [(1, 3), (1, 0)] det 2 inverse 3
MW_KURIHARA_LOCAL_P_TORSION_ZERO_PASS p 7 E_Fp_order 13
MW_KURIHARA_LOCAL_ROW_PASS p 7 q 113 a_q 9 E_Fq_order 105 cofactor 15 row (1, 3)
MW_KURIHARA_LOCAL_ROW_PASS p 7 q 673 a_q 2 E_Fq_order 672 cofactor 96 row (1, 6)
MW_KURIHARA_TWO_LOCAL_IMAGES_BASIS_PASS p 7 auxiliaries (113, 673) matrix [(1, 3), (1, 6)] det 3 inverse 5
MW_KURIHARA_LOCAL_P_TORSION_ZERO_PASS p 107 E_Fp_order 108
MW_KURIHARA_LOCAL_ROW_PASS p 107 q 369793 a_q 2 E_Fq_order 369792 cofactor 3456 row (1, 15)
MW_KURIHARA_LOCAL_ROW_PASS p 107 q 383917 a_q -854 E_Fq_order 384772 cofactor 3596 row (1, 53)
MW_KURIHARA_TWO_LOCAL_IMAGES_BASIS_PASS p 107 auxiliaries (369793, 383917) matrix [(1, 15), (1, 53)] det 38 inverse 31
MW_KURIHARA_LOCAL_JSON_SHA256 3d9f3b2b6f5594adbc5927794159f5425fb20cd8825ce944b52f3522d1f29e7e
MW_KURIHARA_LOCAL_REPORT /home/bsdadmin/bsd389_MW_local_determinants_5_7_107.json
BOUNDARY_LOCAL_MW_DETERMINANTS_NOT_ALL_P_SHA_OR_BSD
```

## Exactly authenticated conclusion

For **each** of p5/p7/p107, two rational MW generators `P=(-1,1)`, `Q=(0,-1)` reduce to a **basis** of the direct sum of two 1D local Kummer quotients `E(F_{q1})/p⊕E(F_{q2})/p` at the historical Kurihara auxiliaries. Determinants are `2 mod5`, `3 mod7` and `38 mod107`, respectively. The same real user run independently checks `#E(F5)=9`, `#E(F7)=13`, `#E(F107)=108`, so the local E(Qp)[p]=0 gate is satisfied by good reduction and lack of formal-group odd p torsion.

**Scope:** This proves MW localization unit at these finite p and pairs, **not** that the corresponding global Kurihara weighted numbers are nonzero. It does not establish any `Sha[p]` triviality without the independent nonzero Kurihara witness and appropriate Kim 2025 theorem hypotheses. The program **did not run with `--verify-p107-archive`**, so it did NOT authenticate the historic large p107 Kurihara archive. This can be done by a short new cross-certificate script.

**Important independent literature confirmation for p5:** Chan-Ho Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves* (2025 preprint PDF, published 2026), §8 Example (1), explicitly treats **E389.a1 and auxiliary q=(41,61)**, confirms nonzero `delta_{41·61}` modulo 5 and deduces both `Sha(E389.a1/Q)[5∞]=0` and the semilocal mod5 Selmer isomorphism to `E(Q41)/5⊕E(Q61)/5`. [Kim primary source](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf), printed p35. The present user-run explicit 2×2 MW matrix provides an **independent concrete identification** of the two MW basis images under that published Selmer isomorphism.

[Full local determinants + conditional modp Kim argument](../paper/bsd389_MW_local_two_auxiliary_determinants_and_Kim_Selmer_gate_2026-11-02.md). [Uniform local MW pair existence proof](../paper/bsd389_uniform_Chebotarev_Kummer_MW_local_two_auxiliary_wedge_2026-11-02.md). **Global all-p Sha and full BSD are still OPEN.**
