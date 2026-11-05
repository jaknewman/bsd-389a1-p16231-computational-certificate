# Genuine user PASS: E389a1 p16231 ordinary / anticyclotomic root signs

2026-11-06, Sage Ubuntu. The user ran `verification/bsd389_p16231_iwasawa_sign_and_projection_gate.py` after a git fast-forward, with `set -o pipefail`, and posted the exact output:

```text
BSD389_P16231_ORDINARY_AND_ROOT_SIGN_PASS
BSD389_K_MINUS3_389_INERT_P_SPLIT_PASS
BSD389_NPLUS_ONE_POSITIVE_THETA_INVOLUTION_SIGN_PASS
BSD389_P2_THETA_FINITE_C2_MODP 3739
BOUNDARY_REQUIRE_CHIDA_HSIEH_THETA_NORMALIZATION_IDENTIFICATION
BOUNDARY_ANALYTIC_CONSTANT_ZERO_AND_THEOREM_B_HYPOTHESES_REQUIRE_ARGUMENT
IWASAWA_BRIDGE_STATUS=0
```

The script checks E.ap(16231)=128, good ordinarity, root numbers E global +1 and local good p +1, 389 inert in K=Q(sqrt(-3)), p split, ordinary root alpha_p^(-2)=4986 modp, and -3*4986*4083=3739 modp. It does NOT check that the quaternionic Gross point chart is identical to the Castella--Hsieh appendix definition, establish exact zero of first two coefficients in Zp, or prove Sha vanishing/BSD. These are separately articulated and scoped in [paper/bsd389_p16231_ordinary_theta_iwasawa_bridge_2026-11-06.md](../paper/bsd389_p16231_ordinary_theta_iwasawa_bridge_2026-11-06.md).

The next [Appendix exact n=1 local formula test](../verification/bsd389_p16231_castella_hsieh_appendix_local_formula_gate.py) directly checks Hecke Brandt eigenvector identity, the scaled true Gross right ideals for n=1,2, P1 principal-unit invariance, and local/global cubic mu3 symmetry for several genuine P2 ideals. It is newly committed but still awaits user execution, so no PASS has been claimed for it yet.
