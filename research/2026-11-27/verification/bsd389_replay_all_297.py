#!/usr/bin/env python3
"""Full, repeatable independent execution of all 297 ordinary p^2 sums.

Requires C++17 and standard Python3; by default recompiles the exact symmetry
reduced C++ engine and runs every ordinary good p < 2000, comparing all 297
rows to the original SHA-256-verified CSV and the complete expected log hash.
"""
import argparse
import csv
import hashlib
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
MANIFEST = HERE.parent / 'data' / 'ordinary_p2_5_to_1999.csv'
TABLE = HERE / 'manin_390.txt'
CPP = HERE / 'bsd389_ordinary_p2_audit_half.cpp'
EXPECTED_CSV_SHA = 'cd0cfbb3f9c216433eb95966c0896f0ab64eabfa38f17480e93e98f15090afe9'
EXPECTED_LOG_SHA = '2ba0dad9541b4e881b3f89c1a1d59d69979516bdad8932cd39680690bcba3759'

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def verify(log, table):
    assert sha256(MANIFEST) == EXPECTED_CSV_SHA
    assert sha256(table) == '9bce8b66c37b7f257f5a6015c08806c2b80c36d1e47356677e3819fc171e8360'
    assert sha256(log) == EXPECTED_LOG_SHA, sha256(log)
    with MANIFEST.open(newline='') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 297
    data = Path(log).read_text().strip().splitlines()
    assert len(data) == len(rows)
    for i,(line,row) in enumerate(zip(data,rows)):
        p = int(row['p'])
        expected = f"P {p} AP {row['ap']} N {row['n']} COUNT {row['count']} RAW_C0_C1_C2_C3 {row['c0']} {row['c1']} {row['c2']} {row['c3']} ORDINARY 1"
        assert line == expected, (i,p,line,expected)
        assert int(row['c0']) == int(row['c1']) == 0
        assert int(row['c2']) % p != 0
    print('FULL_297_ORDINARY_P2_REPLAY_PASS',len(rows),'RAW_C2_UNIT_COUNT',len(rows))
    print('COMPLETE_REPLAY_SHA256',sha256(log))

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--existing-log',type=Path,default=None,help='Audit a previously run complete log (skip C++ compilation)')
    args=parser.parse_args()
    if args.existing_log:
        verify(args.existing_log,TABLE)
    else:
        assert sha256(MANIFEST) == EXPECTED_CSV_SHA
        with MANIFEST.open(newline='') as f:
            primes=[int(row['p']) for row in csv.DictReader(f)]
        assert len(primes)==297
        with tempfile.TemporaryDirectory() as d:
            binary=Path(d)/'bsd389_half'
            log=Path(d)/'ordinary_all_297.log'
            subprocess.run(['c++','-std=c++17','-O3',str(CPP),'-o',str(binary)],check=True)
            with log.open('wb') as fp:
                subprocess.run([str(binary),str(TABLE),*map(str,primes)],stdout=fp,check=True)
            verify(log,TABLE)
