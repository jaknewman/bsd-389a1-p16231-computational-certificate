# Independent scalar J: two pilot runs verified (2026-10-26)

User ran the standalone dual-scalar engine on IONOS with both pipelines exiting successfully.

Pilot 1, pair ID 0, (a,b)=(1,0):
- ORIGINAL_EXPORT_SHA256_PASS 9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8
- INDEPENDENT_SCALAR_ALL_BASIS_MOMENTS_PASS 1087544
- INDEPENDENT_SCALAR_ALL_390_REP_MOMENTS_PASS slots=6330480 expanded_relation_terms=31571240
- INDEPENDENT_SCALAR_TEICH_TABLE_PASS 16230
- INDEPENDENT_SCALAR_LOCAL_ORACLE_PASS id=0 J=2316
- INDEPENDENT_SCALAR_INTERVAL_PASS start=0 end=1 J_mod_p=2316
- PILOT1_STATUS=0 0 0

Pilot 2, pair ID 16234, (a,b)=(2,3), nonzero kappa=11458:
- ORIGINAL_EXPORT_SHA256_PASS 9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8
- INDEPENDENT_SCALAR_ALL_BASIS_MOMENTS_PASS 1087544
- INDEPENDENT_SCALAR_ALL_390_REP_MOMENTS_PASS slots=6330480 expanded_relation_terms=31571240
- INDEPENDENT_SCALAR_TEICH_TABLE_PASS 16230
- INDEPENDENT_SCALAR_LOCAL_ORACLE_PASS id=16234 J=11725
- INDEPENDENT_SCALAR_INTERVAL_PASS start=16234 end=16235 J_mod_p=11725
- PILOT2_STATUS=0 0 0

The engine does not read V11 producer output or V19 chunks/checkpoints. It uses the independently constructed V65 eclib moment table and original audited Manin export. Both local results match previous full-lift Sage/eclib analytic oracles.

BOUNDARY: These are two pilot pair evaluations, **not** the full 263429130-pair independent scalar calculation. J=4486 has NOT yet been independently reproduced by this engine. Do not claim full BSD or exact p-adic unit equality.
