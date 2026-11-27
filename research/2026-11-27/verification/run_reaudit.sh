#!/usr/bin/env bash
# BSD389 finite-evidence re-audit (not a proof of global BSD).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
python3 "$HERE/bsd389_standalone_p2_audit.py" --primes 5 7 11 13 17 89 --p389
c++ -O2 -std=c++17 "$HERE/bsd389_ordinary_p2_audit.cpp" -o "$TMP/ordinary"
"$TMP/ordinary" "$HERE/manin_390.txt" 5 7 11 13 17 89 | tee "$TMP/ordinary.log"
grep -F 'P 89 AP -8 N 7921 COUNT 7832 RAW_C0_C1_C2_C3 0 0 8 33 ORDINARY 1' "$TMP/ordinary.log" >/dev/null
c++ -O2 -std=c++17 "$HERE/bsd389_p389_native.cpp" -o "$TMP/cyclo389"
"$TMP/cyclo389" "$HERE/manin_390.txt"
python3 "$HERE/bsd389_p389_cyclotomic.py"
python3 "$HERE/bsd389_measure_projection_audit.py" --primes 5 7 11 13 17 89 389
# The independent Fourier/AGM audit requires NumPy; core finite checks do not.
if python3 -c 'import numpy' >/dev/null 2>&1; then
  python3 "$HERE/bsd389_independent_analytic_manin_audit.py"
else
  echo 'NUMPY_ABSENT_SKIPPING_INDEPENDENT_FOURIER_AGM_AUDIT'
fi
echo 'BSD389_REAUDIT_FINITE_MOMENTS_PASS: mathematical Selmer comparisons still require review'
