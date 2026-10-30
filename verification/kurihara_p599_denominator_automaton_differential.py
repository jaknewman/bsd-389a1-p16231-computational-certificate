#!/usr/bin/env python3
"""Bounded differential test: original native p599 vs denominator automaton.

Compares all 390 Manin weights, units, weighted terms, edge counts, residue,
and both primitive roots on 9 scattered intervals. Also runs an independent
Python BSGS/continued-fraction oracle for the five short intervals, using
kurihara_p599_pilot_independent_check.py in the same directory.

The real Sage-exported table is pinned by its exact SHA256. The first
two 1m block residues are also checked against archived real checkpoints.
No global Kurihara or Sha certificate is asserted.
"""
import argparse
import hashlib
import re
import subprocess
from pathlib import Path

P=599
REAL_SHA='fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8'
HALF=(6912461*13963889-1)//2
FIVE=((1,30,237),(100000,100030,153),(6912450,6912480,500),
      (13963880,13963900,4),(48262408622200,48262408622235,511))

def execute(executable, table, lo, hi):
    args=[str(executable),'--table',str(table),'--start',str(lo),'--end',str(hi)]
    if hi-lo+1>1000000:
        args.append('--allow-large')
    r=subprocess.run(args,check=True,capture_output=True,text=True)
    lines=r.stdout.strip().splitlines()
    if len(lines)!=2 or not lines[0].startswith('KURIHARA_NATIVE_CHUNK ') or not lines[1].startswith('W390 '):
        raise AssertionError(('unexpected native response',r.stdout[:500]))
    fields=dict(re.findall(r'(\w+)=(\S+)',lines[0]))
    assert fields['STATUS']=='PARTIAL_ONLY'
    assert (int(fields['p']),int(fields['q1']),int(fields['q2']))==(599,6912461,13963889)
    assert (int(fields['start']),int(fields['end']))==(lo,hi)
    weights=tuple(map(int,lines[1].split()[1:]))
    assert len(weights)==390 and all(0<=v<P for v in weights)
    return fields,weights

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--baseline',type=Path,required=True)
    ap.add_argument('--automaton',type=Path,required=True)
    ap.add_argument('--table',type=Path,required=True)
    ap.add_argument('--no-independent',action='store_true',help='skip independent BSGS checks')
    args=ap.parse_args()
    for path in (args.baseline,args.automaton,args.table):
        assert path.is_file(),path
    args.baseline=args.baseline.resolve()
    args.automaton=args.automaton.resolve()
    args.table=args.table.resolve()
    raw=args.table.read_bytes()
    assert list(map(int,raw.split()[:3]))==[599,6912461,13963889]
    table_hash=hashlib.sha256(raw).hexdigest()
    authentic=(table_hash==REAL_SHA)
    print('K599_DENOMINATOR_INPUT_SHA',table_hash,'authentic',authentic,flush=True)
    oracle=None
    if not args.no_independent:
        from kurihara_p599_pilot_independent_check import check
        oracle=check
    trials=[(a,b) for a,b,_ in FIVE]
    trials.extend(((1,1000000),(1000001,2000000),
                   (24131209530207,24131210030206),
                   (HALF-499999,HALF)))
    speeds=[]
    for lo,hi in trials:
        old,wold=execute(args.baseline,args.table,lo,hi)
        new,wnew=execute(args.automaton,args.table,lo,hi)
        assert wold==wnew,('W390 mismatch',lo,hi)
        for k in ('g1','g2','contraction','units','weights','edges'):
            assert old[k]==new[k],('field mismatch',lo,hi,k,old[k],new[k])
        if authentic:
            for a,b,expected in FIVE:
                if (lo,hi)==(a,b):
                    assert int(new['contraction'])==expected,('authentic oracle mismatch',lo,hi)
            if (lo,hi)==(1,1000000):
                assert int(new['contraction'])==456
            if (lo,hi)==(1000001,2000000):
                assert int(new['contraction'])==22
        if oracle and (lo,hi) in [(a,b) for a,b,_ in FIVE]:
            oracle(args.automaton,args.table,(lo,hi))
        if hi-lo+1>=500000:
            speed=float(old['seconds'])/max(float(new['seconds']),1e-12)
            speeds.append(speed)
            print('K599_DENOMINATOR_BOUNDED_SPEED_COMPARE',lo,hi,
                  'baseline_loop_s',old['seconds'],'automaton_loop_s',new['seconds'],
                  'speed_ratio',round(speed,3),flush=True)
        print('K599_DENOMINATOR_W390_EXACT_INTERVAL_PASS',lo,hi,
              'residue',new['contraction'],'weighted',new['weights'],
              'edges',new['edges'],flush=True)
    print('K599_DENOMINATOR_AUTOMATON_EXACT_DIFF_PASS','intervals',len(trials),
          'median_loop_speed_ratio',round(sorted(speeds)[len(speeds)//2],3),flush=True)
    print('BOUNDARY: bounded exact differential test; no full delta599 or Sha result.',flush=True)

if __name__=='__main__':main()
