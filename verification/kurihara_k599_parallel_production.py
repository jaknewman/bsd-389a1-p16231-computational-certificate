#!/usr/bin/env python3
"""Restartable audited Kurihara p=107 half-sum using native 390-Manin program.

Starts only with --run and at most two new chunks by default; --run --full explicitly opts into all remaining work. Each chunk stores the entire W390 vector, provenance,
SHA256 and a verified dot product. Merging refuses missing or inconsistent chunks.
"""
import argparse, hashlib, json, os, re, subprocess, tempfile, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

P,Q1,Q2=599,6912461,13963889
N=Q1*Q2
HALF=(N-1)//2
PHI_HALF=(Q1-1)*(Q2-1)//2
assert HALF == 48262419060414 and PHI_HALF == 48262408622240
HDR=re.compile(r'^KURIHARA_NATIVE_CHUNK (.+)$')

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
    def m(q):return end//q-(start-1)//q
    expected_units=(end-start+1)-m(Q1)-m(Q2)+m(N)
    if x['units']!=expected_units or not 0<=x['weights']<=x['units'] or x['edges']<x['weights']:
        raise ValueError('bad unit/weight/edge counts')

def execute(executable,table,i,start,end,table_sha,exe_sha,M):
    cmd=[str(executable),'--table',str(table),'--start',str(start),'--end',str(end)]
    if end-start+1>1_000_000:cmd.append('--allow-large')
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode:raise RuntimeError(f'Native failed on chunk {i}, exit {r.returncode}: {r.stderr}')
    lines=r.stdout.strip().splitlines()
    if len(lines)!=2 or not lines[0].startswith('KURIHARA_NATIVE_CHUNK ') or not lines[1].startswith('W390 '):
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
    ap.add_argument('--chunk-size',type=int,default=1_000_000_000)
    ap.add_argument('--max-new-chunks',type=int,default=2,help='bounded number of new chunks when --run')
    ap.add_argument('--workers',type=int,default=1,help='parallel native subprocesses; plan memory ~42 MB per worker')
    ap.add_argument('--full',action='store_true',help='explicitly allow all remaining chunks, requires --run')
    ap.add_argument('--run',action='store_true',help='actually perform missing chunks; without it only audit')
    args=ap.parse_args()
    if not 1<=args.workers<=128:ap.error('workers must be 1..128')
    if not 1<=args.chunk_size<=10_000_000_000:ap.error('chunk-size outside 1..1e10')
    if not 1<=args.max_new_chunks<=1_000_000:ap.error('max-new-chunks must be positive')
    if args.full and not args.run:ap.error('--full requires --run')
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

    print('K599_PRODUCTION_CONFIG_PASS',f'total_chunks={count}',f'workers={args.workers}',
          f'chunk_size={args.chunk_size}',f'table_sha256={table_sha}',flush=True)
    if args.run:
        remaining=(i for i in range(count) if not chunk_path(root,i).exists())
        limit=count if args.full else args.max_new_chunks
        # Never submit all jobs to memory. At most 2*workers active/queued.
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            inflight={}
            for _ in range(min(limit,2*args.workers)):
                try:i=next(remaining)
                except StopIteration:break
                lo,hi=bounds(i,args.chunk_size)
                inflight[pool.submit(execute,native,table,i,lo,hi,table_sha,exe_sha,M)]=i
            new=0
            while inflight:
                future=next(as_completed(inflight))
                i=inflight.pop(future)
                record=future.result()
                atomic_json(chunk_path(root,i),record)
                new+=1
                print(f'K599_CHUNK_PASS {i+1}/{count} {record["start"]} {record["end"]} residue={record["contraction"]}',flush=True)
                if new+len(inflight)<limit:
                    try:j=next(remaining)
                    except StopIteration:continue
                    lo,hi=bounds(j,args.chunk_size)
                    inflight[pool.submit(execute,native,table,j,lo,hi,table_sha,exe_sha,M)]=j
        print('K599_NEW_CHUNKS_WRITTEN',new,flush=True)
    aggregate=[0]*390;residue=0;units=weights=edges=0;seen=0
    # A sparse audit avoids iterating billions of nonexistent tiny chunks.
    for path in sorted(root.glob('chunk_*.json')):
        try:i=int(path.stem.split('_')[1])
        except (IndexError,ValueError):raise ValueError(f'unexpected chunk file {path.name}')
        if i<0 or i>=count or path != chunk_path(root,i):raise ValueError(f'invalid chunk file name {path.name}')
        start,end=bounds(i,args.chunk_size)
        x=json.loads(path.read_text())
        verify_payload(x,i,start,end,table_sha,exe_sha,M)
        seen+=1;residue=(residue+x['contraction'])%P
        units+=x['units'];weights+=x['weights'];edges+=x['edges']
        aggregate=[(a+b)%P for a,b in zip(aggregate,x['W390'])]
    if sum(m*w for m,w in zip(M,aggregate))%P!=residue:raise ValueError('global M.W mismatch')
    if seen==count:
        if units!=PHI_HALF:raise ValueError('complete unit count mismatch')
        final=dict(**config,complete=True,chunks_verified=seen,half_contraction=residue,
                   kurihara_delta=(2*residue)%P,W390=aggregate,W390_sha256=sha(canonical(aggregate)),
                   units=units,weights=weights,edges=edges)
        atomic_json(root/'FINAL_COMPLETE.json',final)
        print('K599_GLOBAL_DELTA_COMPLETE',final['kurihara_delta'],'NONZERO',final['kurihara_delta']!=0,
              'HALF',residue,'W390_SHA256',final['W390_sha256'],flush=True)
    else:
        # Never leave an old COMPLETE artifact when checkpoints have been removed.
        (root/'FINAL_COMPLETE.json').unlink(missing_ok=True)
        print('K599_INCOMPLETE_NO_CERTIFICATE',f'verified={seen}/{count}',f'units={units}/{PHI_HALF}',
              f'partial_mod599={residue}',flush=True)

if __name__=='__main__':main()