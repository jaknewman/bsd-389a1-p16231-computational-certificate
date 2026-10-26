# Independent scalar J verification — new full-corpus engine

Date: 2026-10-26. STATUS: IMPLEMENTED IN SOURCE, NOT YET EXECUTED ON IONOS.

## Mathematical independence

Original V11/V19 creates sparse coefficient rows C0/C1 for 263,429,130 outer pairs, then contracts with eclib modular-symbol moments. The new `verification/independent_c01_scalar_J.cpp` performs **dual scalar evaluation**: it first precomputes the 67×16232 basis moments from the separately produced V65 eclib Hecke table (using V65's exact two-prime NTT/CRT source), then precomputes moments for all 390×16232 Manin–Shapiro representatives using the original audited relations. For each pair it computes continued-fraction fragments and evaluates the scalar moments directly, without reading V11 sparse outputs, any V19 chunks, or the V19 global checkpoint.

For h in Gamma0(389p) the universal relation is M0(hD)=M0(D), M1(hD)=q(h)M0(D)+r(h)M1(D), where q(h)=-h.a*h.b and r(h)=h.a² mod p. Precompute representative moments by applying the relation's exact matrices and coefficients to the 67 basis moments. Then for each continued-fraction fragment B, reduce B to a Manin representative i and Shapiro class j, and read the precomputed representative moments; apply q(h),r(h) for the remaining h. The pair result is `-w(a,b)*(M1(D_x)-kappa(a,b)*M0(D_x)) mod p`.

**Independence boundary:** this is a genuinely new global outer-summation and dual moment computation, not a fresh computation of the eclib V65 table or an independent rederivation of the Manin relations. No global PASS should be asserted before successful execution.

## Compile, SHA pin and pilot

From the Sage-enabled shell, using the pinned eclib reference table:

```bash
cd ~/bsd-389a1-p16231-computational-certificate
git pull --ff-only
set -o pipefail
V65="$HOME/bsd389-c01-v14-production/v65_independent_terminal/eclib_beta_table.bin"
test "$(sha256sum "$V65" | cut -d' ' -f1)" = "aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c" || { echo V65_SHA_MISMATCH; exit 1; }
g++ -O2 -std=c++17 -Wall -Wextra verification/independent_c01_scalar_J.cpp -o /tmp/bsd389_independent_J
python verification/export_shapiro_transport_stream.py historical/originals/bsd389_tame_relation_export_p16231.json | /tmp/bsd389_independent_J "$V65" 0 1 "$HOME/bsd389_independent_J_pilot_1.chk" 2>&1 | tee "$HOME/bsd389_independent_J_pilot_1.log"
echo "PIPE_STATUS=${PIPESTATUS[*]}"
python verification/export_shapiro_transport_stream.py historical/originals/bsd389_tame_relation_export_p16231.json | /tmp/bsd389_independent_J "$V65" 16234 16235 "$HOME/bsd389_independent_J_pilot_2.chk" 2>&1 | tee "$HOME/bsd389_independent_J_pilot_2.log"
echo "PIPE_STATUS=${PIPESTATUS[*]}"
```

Expected independent local markers are `INDEPENDENT_SCALAR_LOCAL_ORACLE_PASS id=0 J=2316` and `INDEPENDENT_SCALAR_LOCAL_ORACLE_PASS id=16234 J=11725` (with zero exit code). These are predictions from **earlier independent local Sage/eclib tests**, not results yet reported from this new engine.

## Full restartable run (only after two pilots PASS)

```bash
python verification/export_shapiro_transport_stream.py historical/originals/bsd389_tame_relation_export_p16231.json | /tmp/bsd389_independent_J "$V65" 0 263429130 "$HOME/bsd389_independent_J_full.chk" 2>&1 | tee "$HOME/bsd389_independent_J_full.log"
echo "PIPE_STATUS=${PIPESTATUS[*]}"
```

The new engine writes an atomic text checkpoint after each million pair IDs. If interrupted, rerun the same full command (preserve same binary and inputs) and append to the log with `tee -a`. A successful independent full sum must print `INDEPENDENT_SCALAR_GLOBAL_J_4486_PASS pairs=263429130`. A mismatch exits with nonzero code and must be investigated. Source versions and data should stay pinned because the checkpoint format binds interval and sum, but not cryptographic SHA fingerprints.

This second algorithm will materially strengthen the historical production trust boundary *if actually executed and matched*. The original p-primary Sage inference still depends on the analytic source-level proof and arithmetic hypotheses; full BSD or exact p-adic u_p=1 is not thereby proved.
