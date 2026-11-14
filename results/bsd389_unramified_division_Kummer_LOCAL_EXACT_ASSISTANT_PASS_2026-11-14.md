# E389a1 genuine local p-adic Kummer witnesses: assistant execution PASS

**2026-11-14.** Actually executed by assistant with Python3 exact fractions and rational elliptic-curve point arithmetic; NOT a Sage or class-group calculation. Companion verification/bsd389_unramified_division_classgroup_certificate.py is equivalent source, but not bit-identical to the locally executed artifact, whose SHA256 is:

    a276cac8bf3748250097700beb2b7ba214efbd3ff97b3b680fe26a9b673514c5

The mathematical unramified-extension claims follow separately by Sah, irreducible residual GL2, Nakayama, and Artin class field theory. The executed local data:

~~~text
BSD389_UNRAMIFIED_KUMMER_LEVEL1_EXACT_LOCAL_PASS p 5 E_Fp 9 LpP 2 LpQ 4 point -2P+1Q coordinates (-3/4,7/8) t_#E(Fp)R_mod_p2 0
BSD389_UNRAMIFIED_KUMMER_LEVEL2_EXACT_LOCAL_PASS p 5 divisibility 25 point -4P+-3Q coordinates (6832045/511392996,-315516267935/11564641211544) t_#E(Fp)R_mod_p3 0
BSD389_UNRAMIFIED_KUMMER_LEVEL1_EXACT_LOCAL_PASS p 7 E_Fp 13 LpP 5 LpQ 3 point -2P+1Q coordinates (-3/4,7/8) t_#E(Fp)R_mod_p2 0
BSD389_UNRAMIFIED_KUMMER_LEVEL2_EXACT_LOCAL_PASS p 7 divisibility 49 point -4P+-5Q coordinates (-5476046670171/4640693967529,10357242007585928617/9997108243588095083) t_#E(Fp)R_mod_p3 0
BSD389_UNRAMIFIED_KUMMER_LEVEL1_EXACT_LOCAL_PASS p 11 E_Fp 16 LpP 6 LpQ 7 point -3P+1Q coordinates (133,-1540) t_#E(Fp)R_mod_p2 0
BSD389_UNRAMIFIED_KUMMER_LEVEL1_EXACT_LOCAL_PASS p 13 E_Fp 17 LpP 6 LpQ 3 point -1P+2Q coordinates (-2,0) t_#E(Fp)R_mod_p2 0
BSD389_UNRAMIFIED_KUMMER_LEVEL1_EXACT_LOCAL_PASS p 17 E_Fp 24 LpP 10 LpQ 10 point -1P+1Q coordinates (1,-1) t_#E(Fp)R_mod_p2 0
BSD389_UNRAMIFIED_KUMMER_LEVEL1_EXACT_LOCAL_PASS p 19 E_Fp 15 LpP 15 LpQ 17 point -1P+2Q coordinates (-2,0) t_#E(Fp)R_mod_p2 0
BSD389_UNRAMIFIED_KUMMER_LEVEL1_EXACT_LOCAL_PASS p 23 E_Fp 28 LpP 6 LpQ 5 point -3P+-1Q coordinates (2869/676,154413/17576) t_#E(Fp)R_mod_p2 0
BSD389_EXACT_HIGHER_DIVISIBILITY_VALUATION_PASS 5 t([N]R) p_valuation 5 R_locally_divisible_by 625 unramified_extension_degree 390625
BSD389_EXACT_HIGHER_DIVISIBILITY_VALUATION_PASS 7 t([N]R) p_valuation 3 R_locally_divisible_by 49 unramified_extension_degree 2401
~~~

At p=5, the vector R=-4P-3Q is primitive mod5, and v5(t([9]R))=5 exactly, so it is locally divisible by 5^4 (but not 5^5). The actual Kummer extension over Q(E[5^4]) has degree 5^8=390625 and is everywhere unramified **by the proved global theorem**, not by explicit class-group computations. At p=7 the analogous explicit vector -4P-5Q has local parameter valuation 3 and yields an extension of degree 7^4=2401 over Q(E[7²]).

**Limits:** No class group itself, new Sha group, global finite-prime support or exact complex BSD leading coefficient was computed.
