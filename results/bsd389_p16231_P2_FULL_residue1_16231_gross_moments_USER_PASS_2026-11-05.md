# E389a1 K=-3 p=16231: first FULL 16231-point P2 Gross i-orbit — user PASS

Date 2026-11-05. Primary provenance: user-pasted complete Ubuntu Sage terminal output, 633 lines, including sha256sum -c on the previous 512-point chunk, successful remaining 31 chunk runs and exact complete aggregation. The assistant checked all 31 ranges are consecutive from i=512 through 16230, and checked aggregation algebra against the prior i=0..511 chunk.

## Decisive actual output

```text
/home/bsdadmin/bsd389_p16231_P2_u_orbit_chunk_certificates/r1_i00000_00512.json: OK
P2_EXACT_CHUNK_PASS 1 15872 16231
P2_AGGREGATE_COVERAGE 16231 OF 16231 MISSING 0
P2_FULL_ONE_TEICH_ORBIT_MOMENTS_MODP [0, 10775, 5515]
P2_ONE_TEICH_ORBIT_THETA_DEG0_1_2_CONTRIBUTIONS_MODP [0, 460, 13755]
P2_FULL_ONE_TEICH_ORBIT_RESULT /home/bsdadmin/bsd389_p16231_P2_u_orbit_chunk_certificates/r1_FULL_ORBIT_MOMENTS.json
P2_FULL_ONE_TEICH_ORBIT_MOMENTS_PASS
BOUNDARY_OTHER_5410_TEICH_UNIT_ORBITS_NOT_SUMMED
BOUNDARY_THETA_ORDER2_AND_SHA_NOT_PROVED
ORBIT1_FINAL_STATUS=0
```

The final exact class histogram is:
```text
{0: 495, 1: 527, 2: 527, 3: 463, 4: 535, 5: 502, 6: 479, 7: 479, 8: 463, 9: 476, 10: 476, 11: 535, 12: 492, 13: 492, 14: 502, 15: 510, 16: 510, 17: 558, 18: 520, 19: 504, 20: 532, 21: 499, 22: 505, 23: 505, 24: 462, 25: 499, 26: 493, 27: 508, 28: 493, 29: 528, 30: 474, 31: 517, 32: 171}
```

## Independent checks possible from the pasted text

- The user had already certified `r1_i00000_00512.json`, SHA256 `2a12796dd1fd56351e82c2337c02d74d578ab87fa01f40c564dc37c79ad66db5`, with moment vector [16213,12726,5996]. The 31 new non-overlapping chunks start at index 512 and end at 16231. Each printed p4 Hensel, Peirce local chart, p8-index HNF independent preimage, right-ideal closure, and true Brandt equivalence computations as in the corresponding source `verification/bsd389_p16231_P2_u_orbit_chunked_moments.py`.
- Independently summing the **31 new printed moment vectors** modulo 16231 gives [18,14280,15750]. Adding the original 512-point vector gives **[0,10775,5515]** modulo 16231.
- The displayed class histogram sums to exactly 16231 points. Using the fixed certified 33-entry Brandt Hecke vector, the histogram's integer-weighted eigenfunction sum is **exactly 0**, independent of the printed moment0.
- The alpha_p^(-2) normalization 4986 gives `(-4986*[0,10775,5515]) mod16231 = [0,460,13755]`.
- The compiled per-point quaternion equivalence witnesses are available in the **user's 32 local JSON files**, not reproduced in this repository markdown. The aggregate code validates each JSON's indices, non-overlaps, parameter values and moments.

## Exact scope

The complete anticyclotomic principal-unit i-orbit for ONE Teichmuller representative a=1 has been computed. Its second moment and its normalized contribution to the n=1 theta quadratic coefficient are both nonzero modulo p; its linear contribution is also nonzero. This is NOT the full theta series, because the required **5410** distinct Teich representatives modulo the proven global mu3 symmetry have not been accumulated. Therefore `ord_T Theta_(f/K)=2`, Kato nonvanishing, Sha[p^infty] finiteness or global BSD do not follow from this one-orbit result.

Next structural direction: verify whether the exact norm-19 class is primitive in the entire cyclic ring-class group Pic(O_(p²)), and use it to obtain a globally coherent enumeration. This can be done by standalone exact CRT calculations and does not itself solve the 87,809,710-point Gross problem.
