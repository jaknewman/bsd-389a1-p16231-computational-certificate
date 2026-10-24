#!/usr/bin/env python3
"""Offline replay of every *existing* V19 chunk into every saved checkpoint.

Checks complete interval coverage, per-chunk SHA, sorted sparse rows, exact
mod-p accumulation, every checkpoint's bytes and metadata, source fingerprints.
Does NOT independently recompute the mathematical contributions of chunks.
Run with the historical source files unchanged. No eclib/Sage calculations.
"""
from __future__ import annotations
import argparse
from array import array
from pathlib import Path
import hashlib
import json
import os
import re
import sys
import time

P=16231
NG=67
SLOTS=NG*(P+1)
STEP=512
BLOCK=65536
SEED=131072
TOTAL=P*(P-1)
ROOT=Path.home()/'bsd389-c01-v14-production'
CHUNKS=ROOT/'chunks'
CHECK=ROOT/'v19_checkpoints'
BIN=Path.home()/'bsd389-c01-v11-test/bsd389_c01_v11_aggregated'
EXPORT=Path.home()/'bsd389-portable-c01-v2/data/bsd389_tame_relation_export_p16231.json'
PROGRESS=ROOT/'v19_independent_chain_audit_progress.json'
EXPECTED_BIN='31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63'
EXPECTED_EXPORT='9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8'
EXPECTED_FINAL='5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e'
EXPECTED_DRIVER='61eef8564236babf1b669c3fdd40db5d201ebc96bb4f1f8a40a04a6b9e5df418'
EXPECTED_CXX='0d8b18696587fc3a0f497c54ebbba99f4d582e69d5a98d0da0e2a4275172b187'
AUDIT_VERSION='full-chunk-chain-v1'

def demand(ok,msg):
    if not ok: raise AssertionError(msg)

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        while True:
            b=f.read(1<<20)
            if not b: break
            h.update(b)
    return h.hexdigest()

def file_hashes():
    for name,path,digest in (
        ('EXECUTABLE',BIN,EXPECTED_BIN),('EXPORT',EXPORT,EXPECTED_EXPORT),
        ('DRIVER',ROOT/'v19_production.py',EXPECTED_DRIVER),
        ('AGGREGATOR',Path.home()/'bsd389-c01-v11-test/bsd389_c01_v11_aggregated.cpp',EXPECTED_CXX)):
        demand(path.is_file(),f'{name} missing: {path}')
        d=sha(path)
        demand(d==digest,f'{name} SHA MISMATCH: {d} != {digest}')
        print('SOURCE_MATCH',name,d,flush=True)

def chunk(c0,c1,L,R):
    stem=f'{L}_{R}.tsv'
    path=CHUNKS/stem
    sidecar=CHUNKS/(stem+'.sha256')
    demand(path.is_file(),f'MISSING_CHUNK {stem}')
    demand(sidecar.is_file(),f'MISSING_SIDECAR {stem}')
    h=hashlib.sha256()
    prev=-1
    rows=0
    with path.open('rb') as f:
        for lineno,raw in enumerate(f,1):
            h.update(raw)
            t=raw.split()
            demand(len(t)==3, f'{stem}:{lineno} columns {len(t)}')
            try: s,x,y=map(int,t)
            except ValueError as e: raise AssertionError(f'{stem}:{lineno} invalid ints') from e
            demand(prev<s<SLOTS, f'{stem}:{lineno} slot order/index {prev},{s}')
            demand(0<=x<P and 0<=y<P and (x or y),f'{stem}:{lineno} bad residue')
            c0[s]=(c0[s]+x)%P
            c1[s]=(c1[s]+y)%P
            prev=s
            rows+=1
    parts=sidecar.read_text().split()
    demand(len(parts)==2 and parts[1]==stem,f'INVALID_SIDECAR {stem}')
    demand(parts[0]==h.hexdigest(),f'CHUNK_HASH_MISMATCH {stem}')
    return rows

def state(end,c0,c1):
    meta=CHECK/f'state_{end}.json'
    binary=CHECK/f'state_{end}.bin'
    demand(meta.is_file() and binary.is_file(),f'MISSING_CHECKPOINT {end}')
    data=json.loads(meta.read_text())
    demand(data.get('end')==end and data.get('p')==P and data.get('slots')==SLOTS,
           f'CHECKPOINT_METADATA_INVALID {end}')
    demand(data.get('v11_sha256')==EXPECTED_BIN and data.get('export_sha256')==EXPECTED_EXPORT,
           f'CHECKPOINT_SOURCE_HASH_INVALID {end}')
    stored=binary.read_bytes()
    demand(len(stored)==4*SLOTS,f'CHECKPOINT_BYTES_INVALID {end}')
    digest=hashlib.sha256(stored).hexdigest()
    demand(digest==data.get('binary_sha256'),f'CHECKPOINT_HASH_INVALID {end}')
    expected=c0.tobytes()+c1.tobytes()
    demand(expected==stored,f'CHECKPOINT_STATE_MISMATCH {end}')
    if end==TOTAL: demand(digest==EXPECTED_FINAL,'FINAL_SHA_MISMATCH')
    return digest

def write_progress(end,digest,done,rows):
    d={'version':AUDIT_VERSION,'end':end,'digest':digest,
       'blocks_done':done,'rows_read':rows,'bin_sha256':EXPECTED_BIN,
       'export_sha256':EXPECTED_EXPORT,'driver_sha256':EXPECTED_DRIVER}
    temp=PROGRESS.with_suffix('.json.tmp')
    with temp.open('w') as f:
        json.dump(d,f,sort_keys=True)
        f.flush();os.fsync(f.fileno())
    os.replace(temp,PROGRESS)

def resume():
    d=json.loads(PROGRESS.read_text())
    demand(d['version']==AUDIT_VERSION and d['bin_sha256']==EXPECTED_BIN
           and d['export_sha256']==EXPECTED_EXPORT and
           d['driver_sha256']==EXPECTED_DRIVER, 'AUDIT_PROGRESS_ORIGIN_MISMATCH')
    end=d['end']
    demand(SEED<=end<=TOTAL and (end-SEED)%BLOCK==0 or end==TOTAL,
           'INVALID_AUDIT_RESUME_ENDPOINT')
    source=CHECK/f'state_{end}.bin'
    raw=source.read_bytes()
    demand(len(raw)==4*SLOTS,'RESUME_STATE_BAD_SIZE')
    demand(hashlib.sha256(raw).hexdigest()==d['digest'],'RESUME_STATE_HASH_MISMATCH')
    c0=array('H');c1=array('H')
    c0.frombytes(raw[:2*SLOTS]);c1.frombytes(raw[2*SLOTS:])
    demand(len(c0)==SLOTS and len(c1)==SLOTS,'RESUME_BAD_SLOTS')
    state(end,c0,c1)
    print('V19_CHAIN_AUDIT_RESUMED',end,'blocks_done',d['blocks_done'],flush=True)
    return end,c0,c1,d['blocks_done'],d['rows_read']

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--resume',action='store_true',help='resume after own saved audit_progress')
    ap.add_argument('--max-blocks',type=int,default=None,help='preflight only; run at most this many blocks after seed')
    args=ap.parse_args()
    demand(sys.byteorder=='little','uint16 snapshot expects little endian')
    demand(array('H').itemsize==2,'uint16 required')
    demand(args.max_blocks is None or args.max_blocks>=0,'negative max blocks')
    file_hashes()
    t0=time.monotonic()
    if args.resume:
        demand(PROGRESS.is_file(),'NO_PREVIOUS_AUDIT_PROGRESS')
        end,c0,c1,blocks_done,rows=resume()
    else:
        c0=array('H',[0])*SLOTS
        c1=array('H',[0])*SLOTS
        rows=0
        for L in range(0,SEED,STEP):
            rows+=chunk(c0,c1,L,L+STEP)
        end=SEED
        digest=state(end,c0,c1)
        blocks_done=0
        write_progress(end,digest,blocks_done,rows)
        print('V19_CHAIN_SEED_256_CHUNKS_PASS',end,'rows',rows,flush=True)
    local_blocks=0
    while end<TOTAL and (args.max_blocks is None or local_blocks<args.max_blocks):
        nxt=min(end+BLOCK,TOTAL)
        for L in range(end,nxt,STEP):
            rows+=chunk(c0,c1,L,min(L+STEP,nxt))
        digest=state(nxt,c0,c1)
        blocks_done+=1;local_blocks+=1
        end=nxt
        write_progress(end,digest,blocks_done,rows)
        if blocks_done%16==0 or end==TOTAL or (args.max_blocks and local_blocks==args.max_blocks):
            print('V19_CHAIN_BLOCK_PASS',blocks_done,'end',end,'rows',rows,
                  'elapsed_s',round(time.monotonic()-t0,1),flush=True)
    if end==TOTAL:
        demand(blocks_done==4018,'UNEXPECTED_NUMBER_OF_BLOCKS')
        print('V19_FULL_CHUNK_TO_CHECKPOINT_CHAIN_PASS',
              'pairs',TOTAL,'expected_chunks',514511,'checkpoints',4019,
              'all_rows',rows,'final_sha256',digest,flush=True)
        print('LIMIT: chunk contents authenticated against sidecars;'
              ' independent mathematical re-evaluation of every chunk NOT performed.',flush=True)
    else:
        print('V19_AUDIT_PARTIAL','end',end,'blocks_done',blocks_done,
              'next_use=--resume',flush=True)

if __name__=='__main__':
    try: main()
    except (OSError,ValueError,AssertionError,KeyError,IndexError) as e:
        print('V19_CHAIN_AUDIT_FAIL',repr(e),file=sys.stderr,flush=True)
        sys.exit(2)
