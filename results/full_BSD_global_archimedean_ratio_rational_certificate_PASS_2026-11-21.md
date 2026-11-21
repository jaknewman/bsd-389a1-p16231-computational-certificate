# E389a1: first fully rigorous archimedean BSD numerical ratio — assistant run PASS

Date: 2026-11-21. Local assistant Python 3.13; **NO Sage or floating point in the new period/regulator/ratio programs**.
Pre-existing analytic input: independently user-run Sage 10.9/Arb L''(E,1)/2 rigorous ball archived in
results/full_BSD_phase1_Arb_Lstar_interval_PASS_2026-10-19.md.

Source scripts:
- verification/bsd389_real_period_exact_rational_agm_20261121.py
- verification/bsd389_canonical_regulator_exact_duplication_20261121.py
- verification/bsd389_global_archimedean_ratio_rational_interval_20261121.py

Git blob checks compared against the actual assistant-executed source files:
  period blob SHA1 = 4126ad8f05f17b7c5453b9d55aa1b33f56839287
  regulator blob SHA1 = 177444260308729f88b3928d881339cdb7b54656
  ratio blob SHA1 = 6a5891db9f255f46c20346d4f1206cb7e7dadb1d
All three match the on-branch GitHub file hashes.

Execution (full combined ratio script):

    BSD389_HEIGHT_DUPLICATION_PASS x -1 n 10 max_coordinate_bits 1038773 enclosure_12_digits ('0.686664657314', '0.686669396898')
    BSD389_HEIGHT_DUPLICATION_PASS x 0 n 10 max_coordinate_bits 494679 enclosure_12_digits ('0.326998392712', '0.327003132297')
    BSD389_HEIGHT_DUPLICATION_PASS x 4 n 10 max_coordinate_bits 2345746 enclosure_12_digits ('1.550621666675', '1.550626406259')
    BSD389_CERTIFIED_PERIOD_LOWER 4.980425121710110150642715583884604920312116360
    BSD389_CERTIFIED_PERIOD_UPPER 4.980425121710110150642715583884604920312116361
    BSD389_CERTIFIED_REGULATOR_LOWER 0.152455827790
    BSD389_CERTIFIED_REGULATOR_UPPER 0.152464449577
    BSD389_CERTIFIED_RATIO_LOWER 0.999971982756
    BSD389_CERTIFIED_RATIO_UPPER 1.000028533857
    BSD389_ARCHIMEDEAN_BSD_RATIO_CERTIFIED_NEAR_ONE_PASS
    THEOREM: If the exact strong BSD leading-term identity is true, its predicted positive integer order #Sha must be 1.
    BOUNDARY: ratio is only rigorously near one, NOT exactly one. It cannot prove the full Sha finite or the complex leading-term equality.

The separate period script also executed successfully:

    BSD389_RATIONAL_CUBIC_ROOT_ISOLATION_PASS 340 steps_per_root
    BSD389_RATIONAL_MACHIN_PI_ENCLOSURE_PASS 80 30
    BSD389_RATIONAL_AGM_ENCLOSURE_PASS 12 iterations
    BSD389_REAL_PERIOD_LOWER_55_DIGITS 4.9804251217101101506427155838846049203121163606791400801
    BSD389_REAL_PERIOD_UPPER_55_DIGITS 4.9804251217101101506427155838846049203121163606791400802
    BSD389_ARCHIMEDEAN_PERIOD_CERTIFIED_PASS

The separate regulator program with 10 exact duplications executed successfully.
Its two homogeneous Bézout identities with determinant/resulant 389 prove
  |H_NT(R)-h_x(2^10 R)/4^10| <= log(1728)/(3*4^10)
where H_NT=2*canonical point height, and the three resulting intervals
produce a regulator strictly between the stated rational endpoints.

**Status boundary**: This is an exact-rational interval computation combined with
an authentic previously user-executed certified Arb coefficient, NOT a proof
of the exact transcendental equality or global finiteness of Sha.
Mathematical proof:
  paper/bsd389_global_exact_rational_agm_period_duplication_regulator_BSD_ratio_20261121.md.
