#!/usr/bin/env bash
# Reproducible finite-level p=5 Kurihara r=2 and r=4 counterexamples.
# Does not certify a global derived-class Bockstein contraction.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TABLE="${BSD389_TABLE:-$HERE/manin_390.txt}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
python3 "$HERE/bsd389_double_augmentation_gate.py"
python3 "$HERE/bsd389_quartic_cumulant_gate.py"
c++ -O3 -std=c++17 "$HERE/bsd389_kurihara_four_support.cpp" -o "$TMP/kuri4"
while read -r q1 q2 expected; do
  out="$("$TMP/kuri4" 5 "$TABLE" "$q1" "$q2" 2>/dev/null)"
  echo "$out" | grep -F "DELTA_R2 $expected Q $q1,$q2," >/dev/null
  echo "PAIR_PASS $q1 $q2 delta=$expected"
done <<'EOF'
41 61 4
41 131 1
41 211 2
41 251 3
61 131 2
61 211 4
61 251 1
131 211 0
131 251 1
211 251 2
EOF
for case in '41 61 131 211 2' '41 61 131 251 0'; do
  read -r q1 q2 q3 q4 expected <<< "$case"
  out="$(BSD389_KURIHARA_FULL=1 "$TMP/kuri4" 5 "$TABLE" "$q1" "$q2" "$q3" "$q4" 2>/dev/null)"
  echo "$out" | grep -F "DELTA_R4 $expected Q $q1,$q2,$q3,$q4," >/dev/null
  echo "QUARTIC_FULL_SCAN_PASS $q1 $q2 $q3 $q4 delta=$expected"
done
echo 'BSD389_QUADRATIC_EULER_AND_QUARTIC_OBSTRUCTION_REAUDIT_PASS'
