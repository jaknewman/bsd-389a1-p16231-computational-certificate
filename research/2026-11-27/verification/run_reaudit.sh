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
python3 "$HERE/universal_manin_exact_certificate.py" --table "$HERE/manin_390.txt"
if python3 -c 'import mpmath' >/dev/null 2>&1; then
  python3 "$HERE/bsd389_certified_interval_388.py"
else
  echo 'MPMATH_ABSENT_SKIPPING_CERTIFIED_NERON_INTERVAL_AUDIT'
fi
python3 "$HERE/bsd389_period_convention_audit.py"
# Optional longer complete sweep (~30s on the audit host).
if [ "${BSD389_FULL_297:-0}" = "1" ]; then
  python3 "$HERE/bsd389_replay_all_297.py"
fi
# Beyond the original 297-prime sweep: optional 12 good ordinary primes >2000.
if [ "${BSD389_EXTENSION_12:-0}" = "1" ]; then
  c++ -O3 -std=c++17 "$HERE/bsd389_ordinary_p2_audit_half.cpp" -o "$TMP/ordinary_extension"
  "$TMP/ordinary_extension" "$HERE/manin_390.txt" 2003 2011 2017 2027 2029 2053 2063 2081 2083 2087 2089 2099 > "$TMP/extension.log"
  diff -u "$HERE/../results/ordinary_2003_2099.log" "$TMP/extension.log"
  echo 'ORDINARY_12_PRIMES_BEYOND_1999_EXACT_MATCH_PASS'
fi
echo 'BSD389_REAUDIT_FINITE_MOMENTS_PASS: mathematical Selmer comparisons still require review'
