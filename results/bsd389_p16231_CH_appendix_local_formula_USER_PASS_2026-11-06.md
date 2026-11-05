# Authenticated Sage Ubuntu PASS — Castella--Hsieh Appendix §6 local Gross formula gate

User execution 2026-11-06:
verification/bsd389_p16231_castella_hsieh_appendix_local_formula_gate.py
with set -o pipefail, 240 second timeout. Final CH_APPENDIX_STATUS=0.

Decisive authentic output:

    CH_APPENDIX_RIGHT_ORDER_AND_EIGENFUNCTION_LENGTH_PASS
    CH_APPENDIX_BRANDT_EIGENVECTOR_PASS 2 AP -2 COLUMN True ROW True
    CH_APPENDIX_BRANDT_EIGENVECTOR_PASS 3 AP -2 COLUMN True ROW True
    CH_APPENDIX_BRANDT_EIGENVECTOR_PASS 5 AP -3 COLUMN True ROW True
    CH_APPENDIX_BRANDT_EIGENVECTOR_PASS 7 AP -5 COLUMN True ROW True
    CH_APPENDIX_P1_PRINCIPAL_UNIT_IDEAL_INVARIANCE_PASS 1
    CH_APPENDIX_P1_PRINCIPAL_UNIT_IDEAL_INVARIANCE_PASS 2
    CH_APPENDIX_P1_PRINCIPAL_UNIT_IDEAL_INVARIANCE_PASS 7
    CH_APPENDIX_P1_PRINCIPAL_UNIT_IDEAL_INVARIANCE_PASS 128
    CH_APPENDIX_CM_CUBIC_RESIDUE_ACTION_PASS 213756225 49689135
    CH_APPENDIX_P2_CM_MU3_THREE_CLASSES_PASS A 1 CLASS 9 VALUE -1
    CH_APPENDIX_P2_CM_MU3_THREE_CLASSES_PASS A 16232 CLASS 15 VALUE -1
    CH_APPENDIX_P2_CM_MU3_THREE_CLASSES_PASS A 164371339 CLASS 13 VALUE 0
    CH_APPENDIX_P2_CM_MU3_THREE_CLASSES_PASS A 138112843 CLASS 2 VALUE 0
    CH_APPENDIX_P1_DEGREES0_TO2_CANCEL_MODP_PASS
    CH_APPENDIX_P2_CYCLIC_TO_THETA_COEFFICIENT_UNIT_PASS 3739
    CH_APPENDIX_LOCAL_BRANDT_AND_MU3_FORMULA_GATE_PASS
    BOUNDARY_FINITE_LEVEL_COMPARISON_NOT_SHA_OR_BSD_PROOF
    CH_APPENDIX_STATUS=0

This independently verifies the chosen integral Brandt Hecke eigenfunction on four primes, true local n1/n2 Gross right lattice conditions, sampled P1 invariance and P2 global cubic-unit class/value symmetry, and the finite coefficient normalization. Combined with the prior full 87,809,710 point Gross cyclic sum plus final cubic unit closure, it strengthens the finite theta certificate. It does not by itself prove global adelic reciprocity orientation or exact nonvanishing and order for the infinite Iwasawa series. See the formal lemma and proof obligations in paper/bsd389_p16231_exact_Iwasawa_order2_bridge_formal_lemma_2026-11-06.md.
