# SageMath 10.9 — independent p-primary Sha bounds for E = 389a1

**Execution:** user Ubuntu Sage session, 2026-11-02.  
**Evidence:** terminal output supplied by the user in this conversation, reproduced below.  
**Scope:** independent Sage `E.sha().p_primary_bound(p)` calculation; not a Kurihara 710-chunk native replay.  
**Important:** this is a transcription of the user's terminal output, *not* a cryptographic copy or SHA256 authentication of the Ubuntu log file.

## Exact arithmetic output

```text
CURVE (0, 1, 1, -2, 0)
CONDUCTOR 389
SAGE_VERSION SageMath version 10.9, Release Date: 2026-05-04
START 5
A_P 5 -3
CERTIFIED_UPPER_EXPONENT 5 0
SHA_P_PRIMARY_ZERO_PASS 5
SECONDS 5 1.136
START 7
A_P 7 -5
CERTIFIED_UPPER_EXPONENT 7 0
SHA_P_PRIMARY_ZERO_PASS 7
SECONDS 7 0.076
START 11
A_P 11 -4
CERTIFIED_UPPER_EXPONENT 11 0
SHA_P_PRIMARY_ZERO_PASS 11
SECONDS 11 0.089
START 13
A_P 13 -3
CERTIFIED_UPPER_EXPONENT 13 0
SHA_P_PRIMARY_ZERO_PASS 13
SECONDS 13 0.087
START 107
A_P 107 0
CERTIFIED_UPPER_EXPONENT 107 0
SHA_P_PRIMARY_ZERO_PASS 107
SECONDS 107 163.86
PIPELINE_STATUS=0
```

The run also printed a non-fatal deprecation warning recommending `sage.version.version` in place of `version()`.

## Interpretation and limits

For `p_primary_bound(p)`, a certified upper exponent `e=0` bounds the order of the p-primary Tate–Shafarevich group by `p^0=1`, under the correctness and stated prerequisites of Sage's algorithm. Hence this run supplies an independent Sage-based certificate of `Sha(E/Q)[p^infinity]=0` for `p in {5,7,11,13,107}`, including the supersingular prime `p=107` (`a_107=0`).

This independent result **does not** authenticate the original p107 modular-symbol index map, native C++ loop, or p-integral Kurihara normalization. The separate frozen 710-block archive audit reconstructed `delta_107=34 mod 107` from stored block records and remains distinct.

**Next provenance task:** if desired, add the complete user-local `~/bsd389_sha_iwasawa_independent.log` as an explicitly force-added `.log` file with its SHA256, rather than claiming the markdown transcript is the bitwise original log.

## Reproduction

```sage
E = EllipticCurve('389a1')
S = E.sha()
for p in [5,7,11,13,107]:
    print(p, E.ap(p), S.p_primary_bound(p))
```
