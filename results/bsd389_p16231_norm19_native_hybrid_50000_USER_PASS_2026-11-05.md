# Actual Ubuntu USER PASS: exact C++/Sage hybrid norm-19 Gross-point stream to n=50000

**Date:** 2026-11-05. The user ran `verification/bsd389_p16231_norm19_native_exact_stream.py --target-n 50000 --checkpoint-every 8192 --oracle-every 8192 --teich-crosscheck` under Sage (activated miniforge), with `timeout 240s`, `set -o pipefail`, resulting `NORM19_NATIVE50K_STATUS=0`.

First, conda-forge libboost-headers 1.92.0 was successfully installed, and `BOOST_HEADERS_PASS` was printed. The Python driver from commit `3ead877` automatically found `.../envs/sage/include` and `/usr/include`, and compiled the exact Boost cpp_int C++ core with a GCC Boost header warning, not an error.

Actual decisive output:

```text
BOOST_HEADERS_PASS
NORM19_NATIVE_CPP_COMPILED_PASS abccc9a5c1b855949cd6a0653535d42cd039c987091793eedccb9a6ef5eeca98
NORM19_NATIVE_BOOTSTRAP_FROM_USER_16231_PASS 24 7216
NORM19_NATIVE_REGISTER_CERTIFIED_MATRIX_EDGES 7216
NORM19_NATIVE_EXISTING_COMPLETE_TEICH_ORBIT_RECHECK_PASS [0, 10775, 5515]
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 16384 CLASS 15
NORM19_NATIVE_INDEPENDENT_GROSS_ORIENTATION_PASS 16384
NORM19_NATIVE_EXACT_CHECKPOINT_PASS 16384 MOMENTS [37, 11794, 2094] EDGES 7272 SHA256 a3a9d10e7c456f0b6428974aed77b42b068dcb22bf2796ece3216d1de3003fba
NORM19_NATIVE_COMPLETED_TEICH_ORBIT_BRIDGE_PASS 21640 I 7220 CLASS 18 VALUE 0
NORM19_NATIVE_COMPLETED_TEICH_ORBIT_BRIDGE_PASS 27050 I 9025 CLASS 4 VALUE -1
NORM19_NATIVE_COMPLETED_TEICH_ORBIT_BRIDGE_PASS 32460 I 10830 CLASS 6 VALUE -1
NORM19_NATIVE_COMPLETED_TEICH_ORBIT_BRIDGE_PASS 37870 I 12635 CLASS 9 VALUE -1
NORM19_NATIVE_COMPLETED_TEICH_ORBIT_BRIDGE_PASS 43280 I 14440 CLASS 2 VALUE 0
NORM19_NATIVE_COMPLETED_TEICH_ORBIT_BRIDGE_PASS 48690 I 14 CLASS 19 VALUE 2
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 24576 CLASS 13
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 32768 CLASS 29
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 40960 CLASS 0
NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS 49152 CLASS 13
NORM19_NATIVE_EXACT_CHECKPOINT_PASS 49152 MOMENTS [44, 15050, 1782] EDGES 11951 SHA256 2348a29ecad59bcd03e995c2201263a52532fa387c4d435938b7060313b62634
NORM19_NATIVE_EXACT_PROGRESS 49152 OF 87809709 MOMENTS [44, 15050, 1782] EDGE_KEYS 11951 NEW_EDGES 4735 EXACT_NATIVE_STEPS 32921 SECONDS 63.706
NORM19_NATIVE_EXACT_CHECKPOINT_PASS 50000 MOMENTS [57, 11013, 16042] EDGES 11967 SHA256 c30d1cd164dc20040dae1305bc4dea8dcd167f3293aa62d583ced530ced1e112
NORM19_NATIVE_EXACT_PROGRESS 50000 OF 87809709 MOMENTS [57, 11013, 16042] EDGE_KEYS 11967 NEW_EDGES 4751 EXACT_NATIVE_STEPS 33769 SECONDS 64.011
NORM19_NATIVE_EXACT_PREFIX_PASS 50001 MOMENTS [57, 11013, 16042] EDGE_KEYS 11967
BOUNDARY_FULL_87809710_CLASS_SUM_NOT_YET_COMPUTED
NORM19_NATIVE_HYBRID_DRIVER_PASS 50000 NEW_EDGES 4751 SECONDS 64.011
NORM19_NATIVE50K_STATUS=0
```

Important exact scope:
- 50001 genuine oriented quaternionic Gross states (n=0..50000) were obtained using the exact certified n=16231 prefix, Sage-verified newly encountered finite residue-19 ideal edges and native arbitrary-precision 4x4 integer-matrix transitions for cache hits.
- Of at most 12540 local keys, 11967 have now been visited/certified (95.43%); 573 potential keys remain. This is a mathematical worst-case upper bound, not a guarantee that every possible key appears.
- The 5 extra actual P2 reconstruction checks and the 6 checks against the already-completed 16231-point Teich principal-unit orbit (in addition to prior n=5410 bridge) were all PASS.
- The current **partial cyclic raw moments** are [57,11013,16042] mod16231. The overall `-3*4986` theta multiplier must not be applied as a global result unless H=87809710 points are actually included. No global theta coefficient has been determined yet; no claim about the power-series T-adic order, Sha or BSD is warranted.
- Source compiled with a Boost/ GCC header warning `-Wstringop-overread` in /usr/include; compilation succeeded and later exact anchors passed. Warnings merit care but are not evidence of a failed arithmetic check.
- The user state checkpoint SHA256 is `c30d1cd164dc20040dae1305bc4dea8dcd167f3293aa62d583ced530ced1e112`. Its edge database exists on Ubuntu at `~/bsd389_p16231_norm19_native_exact_edges.json`.
