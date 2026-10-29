#!/usr/bin/env python3
"""Read-only final audit of 389a1/Kurihara p=107 production artifacts.

Does NOT replace an independent proof of correctness of the C++ Manin path
or a proof that eclib's normalization equals the Neron-period normalization.
"""
import argparse, hashlib, json, subprocess, pathlib, random
P,Q1,Q2=107,369793,383917
N=Q1*Q2
HALF=(N-1)//2

def digest(data):return hashlib.sha256(data).hexdigest()
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def check(cond,label):
    if not cond:raise AssertionError(label)

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--table',type=pathlib.Path,required=True)
    a.add_argument('--native',type=pathlib.Path,required=True)
    a.add_argument('--outdir',type=pathlib.Path,required=True)
    a.add_argument('--spot-checks',type=int,default=5,help='recompute this many representative chunks with native executable; 0 disables')
    z=a.parse_args()
    tabraw=z.table.read_bytes(); fields=tabraw.split()
    check(len(fields)==393,'TABLE_LENGTH')
    check(tuple(map(int,fields[:3]))==(P,Q1,Q2),'TABLE_HEADER')
    M=list(map(int,fields[3:]));check(len(M)==390 and all(0<=x<P for x in M),'TABLE_ENTRIES')
    exe_hash=digest(z.native.read_bytes());tab_hash=digest(tabraw)
    config=json.loads((z.outdir/'config.json').read_text())
    check(config['p']==P and config['q1']==Q1 and config['q2']==Q2 and config['n']==N,'CONFIG_PARAMS')
    check(config['half']==HALF and config['chunk_size']==100_000_000 and config['chunks']==710,'CONFIG_GRID')
    check(config['table_sha256']==tab_hash and config['exe_sha256']==exe_hash,'CONFIG_HASHES')
    A=[0]*390; total=0;units=weights=edges=0; ranges=[]
    for i in range(710):
        path=z.outdir/f'chunk_{i:06d}.json'
        x=json.loads(path.read_text())
        h=x.pop('payload_sha256')
        check(h==digest(canonical(x)),f'PAYLOAD_HASH_{i}')
        start=1+i*100_000_000;end=min(start+100_000_000-1,HALF)
        for k,v in dict(index=i,start=start,end=end,p=P,q1=Q1,q2=Q2,n=N,table_sha256=tab_hash,exe_sha256=exe_hash).items():
            check(x.get(k)==v,f'HEADER_{i}_{k}')
        W=x['W390'];check(len(W)==390 and all(type(v)==int and 0<=v<P for v in W),f'W_{i}')
        r=x['contraction'];check(r==sum(m*w for m,w in zip(M,W))%P,f'DOT_{i}')
        check(0<=x['weights']<=x['units']<=end-start+1,f'COUNTS_{i}')
        total=(total+r)%P;units+=x['units'];weights+=x['weights'];edges+=x['edges']
        A=[(u+v)%P for u,v in zip(A,W)]
        ranges.append((i,start,end,r,W))
    check(sum(m*w for m,w in zip(M,A))%P==total,'AGGREGATE_DOT')
    check(total==17 and 2*total%P==34,'EXPECTED_DELTA')
    final=json.loads((z.outdir/'FINAL_COMPLETE.json').read_text())
    for k,v in dict(complete=True,chunks_verified=710,half_contraction=17,kurihara_delta=34,
                    W390=A,W390_sha256=digest(canonical(A)),units=units,weights=weights,edges=edges).items():
        check(final.get(k)==v,f'FINAL_{k}')
    check(final['W390_sha256']=='ee3fa1f5fca6de2b04300cbcc042e00e1a19a0e060adb24d2f3b90afabc0f8d0','REFERENCE_SHA')
    print('K107_FINAL_PAYLOAD_AND_COVERAGE_PASS 710/710')
    print('K107_FINAL_DOT_AND_MERGE_PASS HALF 17 DELTA 34')
    print('K107_FINAL_W390_SHA256',digest(canonical(A)))
    print('K107_TABLE_SHA256',tab_hash)
    print('K107_EXECUTABLE_SHA256',exe_hash)
    if z.spot_checks:
        indices=[0,113,354,708,709]
        indices=(indices+random.Random(107).sample(range(710), min(710,z.spot_checks)))[:z.spot_checks]
        for i in indices:
            _,start,end,r,W=ranges[i]
            cmd=[str(z.native.resolve()),'--table',str(z.table.resolve()),'--start',str(start),'--end',str(end)]
            out=subprocess.check_output(cmd,text=True).splitlines()
            check(len(out)==2 and out[0].startswith('K107_NATIVE_CHUNK ') and out[1].startswith('W390 '),f'REPLAY_OUTPUT_{i}')
            dic=dict(w.split('=',1) for w in out[0].split()[1:] if '=' in w)
            check(int(dic['contraction'])==r and list(map(int,out[1].split()[1:]))==W,f'REPLAY_MISMATCH_{i}')
            print('K107_REPLAY_PASS',i+1,'/',710,'residue',r,flush=True)
    print('K107_REPRODUCIBLE_ARTIFACT_AUDIT_PASS')
    print('BOUNDARY: verification of Neron/eclib normalization and independent Manin algorithm remains separate')
if __name__=='__main__':main()