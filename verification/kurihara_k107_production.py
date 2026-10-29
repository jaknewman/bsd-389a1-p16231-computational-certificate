#!/usr/bin/env python3
"""Restartable audited Kurihara p=107 half-sum using native 390-Manin program.

Starts only with --run. Each chunk stores the entire W390 vector, provenance,
SHA256 and a verified dot product. Merging refuses missing or inconsistent chunks.
"""
import argparse, hashlib, json, os, re, subprocess, tempfile, time
from pathlib import Path

P,Q1,Q2=107,369793,383917
N=Q1*Q2
HALF=(N-1)//2
HDR=re.compile(r'^K107_NATIVE_CHUNK (.+)$')

def sha(b): return hashlib.sha256(b).hexdigest()
def canonical(d): return json.dumps(d,sort_keys=True,separators=(',',':')).encode()
def atomic_json(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='wb',dir=path.parent,delete=False) as f:
        f.write(canonical(data)+b'\n');temp=f.name;f.flush();os.fsync(f.fileno())
    os.replace(temp,path)

def load_table(path):
    raw=path.read_bytes(); a=raw.split()
    if len(a)!=393:raise ValueError('Expected p q1 q2 and 390 Manin values')
    p,q1,q2=map(int,a[:3]); M=list(map(int,a[3:]))
    if (p,q1,q2)!=(P,Q1,Q2) or any(not 0<=m<P for m in M):raise ValueError('Invalid Manin table')
    return sha(raw),M

def bounds(i,chunk):
    start=1+i*chunk
    return start,min(HALF,start+chunk-1)

def chunk_path(directory,i):return directory/f'chunk_{i:06d}.json'
def verify_payload(x,i,start,end,table_sha,exe_sha,M):
    if x.get('payload_sha256')!=sha(canonical({k:v for k,v in x.items() if k!='payload_sha256'})):
        raise ValueError('payload hash mismatch')
    fields=dict(index=i,start=start,end=end,p=P,q1=Q1,q2=Q2,n=N,table_sha256=table_sha,exe_sha256=exe_sha)
    for k,v in fields.items():
        if x.get(k)!=v:raise ValueError(f'chunk {i}: {k} mismatch: {x.get(k)} != {v}')
    W=x.get('W390')
    if not isinstance(W,list) or len(W)!=390 or any(type(v)!=int or not 0<=v<P for v in W):raise ValueError('invalid W390')
    if sum(m*w for m,w in zip(M,W))%P!=x.get('contraction'):raise ValueError('M.W mismatch')
    if not 0<=x['contraction']<P:raise ValueError('bad contraction')
    if x['units']>end-start+1 or x['weights']>x['units']:raise ValueError('bad counts')

def execute(executable,table,i,start,end,table_sha,exe_sha,M):
    r=subprocess.run([str(executable),'--table',str(table),'--start',str(start),'--end',str(end)],capture_output=True,text=True)
    if r.returncode:raise RuntimeError(f'Native failed on chunk {i}, exit {r.returncode}: {r.stderr}')
    lines=r.stdout.strip().splitlines()
    if len(lines)!=2 or not lines[0].startswith('K107_NATIVE_CHUNK ') or not lines[1].startswith('W390 '):
        raise ValueError(f'Unexpected native output: {r.stdout[:300]}')
    words=dict(part.split('=',1) for part in lines[0].split()[1:] if '=' in part)
    for k,v in [('p',P),('q1',Q1),('q2',Q2),('start',start),('end',end)]:
        if int(words[k])!=v:raise ValueError(f'native field mismatch {k}')
    if words.get('STATUS')!='PARTIAL_ONLY':raise ValueError('Unexpected native status')
    W=list(map(int,lines[1].split()[1:]))
    doc=dict(index=i,start=start,end=end,p=P,q1=Q1,q2=Q2,n=N,table_sha256=table_sha,exe_sha256=exe_sha,
             contraction=int(words['contraction']),units=int(words['units']),weights=int(words['weights']),edges=int(words['edges']),
             W390=W)
    doc['payload_sha256']=sha(canonical(doc))
    verify_payload(doc,i,start,end,table_sha,exe_sha,M)
    return doc

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--table',type=Path,required=True)
    ap.add_argument('--native',type=Path,required=True)
    ap.add_argument('--outdir',type=Path,required=True)
    ap.add_argument('--chunk-size',type=int,default=100_000_000)
    ap.add_argument('--max-new-chunks',type=int,default=0,help='0 means unlimited when --run; use 2 for pilot')
    ap.add_argument('--run',action='store_true',help='actually perform missing chunks; without it only audit')
    args=ap.parse_args()
    table=args.table.resolve(strict=True);native=args.native.resolve(strict=True)
    table_sha,M=load_table(table)
    exe_sha=sha(native.read_bytes())
    if args.chunk_size<1:ap.error('chunk-size must be positive')
    count=(HALF+args.chunk_size-1)//args.chunk_size
    root=args.outdir.resolve();root.mkdir(parents=True,exist_ok=True)
    config=dict(p=P,q1=Q1,q2=Q2,n=N,half=HALF,chunk_size=args.chunk_size,chunks=count,
                table_sha256=table_sha,exe_sha256=exe_sha)
    config_path=root/'config.json'
    if config_path.exists():
        if json.loads(config_path.read_text())!=config:raise ValueError('Config changed; choose a new --outdir')
    else:atomic_json(config_path,config)
    aggregate=[0]*390;residue=0;units=weights=edges=0;seen=0;new=0
    for i in range(count):
        start,end=bounds(i,args.chunk_size)
        path=chunk_path(root,i)
        if path.exists():x=json.loads(path.read_text())
        elif args.run and (not args.max_new_chunks or new<args.max_new_chunks):
            x=execute(native,table,i,start,end,table_sha,exe_sha,M)
            atomic_json(path,x);new+=1
            print(f'K107_CHUNK_PASS {i+1}/{count} {start} {end} residue={x["contraction"]}',flush=True)
        else:continue
        verify_payload(x,i,start,end,table_sha,exe_sha,M)
        seen+=1;residue=(residue+x['contraction'])%P
        units+=x['units'];weights+=x['weights'];edges+=x['edges']
        aggregate=[(a+b)%P for a,b in zip(aggregate,x['W390'])]
    if seen==count:
        if sum(m*w for m,w in zip(M,aggregate))%P!=residue:raise ValueError('final contraction mismatch')
        final=dict(**config,complete=True,chunks_verified=seen,half_contraction=residue,
                   kurihara_delta=(2*residue)%P, W390=aggregate, W390_sha256=sha(canonical(aggregate)),
                   units=units,weights=weights,edges=edges)
        atomic_json(root/'FINAL_COMPLETE.json',final)
        print('K107_GLOBAL_DELTA_COMPLETE',final['kurihara_delta'],'NONZERO',final['kurihara_delta']!=0,
              'HALF',residue,'W390_SHA256',final['W390_sha256'],flush=True)
    else:
        print('K107_INCOMPLETE_NO_CERTIFICATE',f'verified={seen}/{count}',f'new={new}',flush=True)

if __name__=='__main__':main()