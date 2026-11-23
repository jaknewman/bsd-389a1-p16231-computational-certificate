# User's genuine Ubuntu arithmetic preflight PASS — local obstruction at 13001 for twenty real degree-25 fields

**Date:** 2026-11-23. This is a faithful transcription of the user's terminal output in ChatGPT, not a cryptographically authenticated logfile. The script checks genuine finite-field and theta-histogram facts. Its Poitou–Tate lines PRINT a theorem-level mathematical inference; they do not compute the actual global Selmer cohomology or Sha directly.

Command:
\`\`\`bash
python -u verification/bsd389_p5_all20_local_13001_relaxed_selmer_sha_nonzero_gate.py --hist /tmp/bsd389_val1_all20.txt
\`\`\`

Exact observed output:
\`\`\`text
LOCAL_TWO_INDEPENDENT_COUNTS_PASS 5351 point_count 5375 E_Fq_5torsion_count 5 finite_singular_dim 1
LOCAL_TWO_INDEPENDENT_COUNTS_PASS 13001 point_count 13075 E_Fq_5torsion_count 25 finite_singular_dim 2
LOCAL_MW_13001_CODIM_ONE_PASS E_Fq_mod5_dimension 2 rational_MW_local_image_dimension 1 Q_equals_2P True
LOCAL_MW_BOTH_PRIMES_RANK2_PASS q5351_Q_equals_minus_P True q13001_Q_equals_2P True minor_mod5 3
ALL20_ACTUAL_THETA_SHA_AND_ORDER_THREE_PASS 1a22c0ed1b4ac336a648ec0a0bf1d6121fd6224993c37e928713117cd1d4c463
POITOU_TATE_MATH_THEOREM base_Sel5_dim_2 relaxed_at_13001_dim_3 G_invariant_Sel5_K_dim_3 new_Sha_K_5_class_nonzero
IF_PRIOR_BH_AND_MW_RANK_STABILITY_ACCEPTED all20_Sha5_K_order_at_least_25 r_mod5_1_2_at_most_5^20 r_mod5_3_4_at_most_5^32
BOUNDARY_SCRIPT_CHECKS_LOCAL_ARITHMETIC_NOT_GLOBAL_SELmer
\`\`\`

## Mathematical interpretation

At the good prime 13001, the full 5-torsion dimension is 2 but the rational Mordell–Weil image dimension is 1. Assuming the previously established base Sha(Q)[5]=0, the Poitou–Tate relaxed Selmer group at this prime has dimension 3. The degree25 totally tamely ramified extensions kill its local inertia obstruction, and inflation–restriction carries the extra global Selmer direction injectively into each K_r. Previous rank-stability E(K_r)=E(Q) makes that direction genuinely Sha rather than Mordell–Weil. This is the theorem proved in:

- [A general local-defect formula](../paper/bsd389_p5_local_defect_general_Sha_lower_bound_2026-11-23.md).
- [Specific twenty-field theorem](../paper/bsd389_p5_all20_relaxed_Selmer_nonzero_Sha_theorem_2026-11-23.md).

The companion arithmetic script **has now been extended** to produce an explicit independent 5-torsion basis A=(1365,7777), D=(11168,5591) at 13001. That additional certificate was independently checked by assistant Python but has NOT yet been run in this transcribed user's log. Do not conflate the two versions.

**Scope:** genuine nonvanishing of Sha over K_r conditional on prior recorded arithmetic inputs, not global Sha(E/Q) finiteness nor full BSD.
