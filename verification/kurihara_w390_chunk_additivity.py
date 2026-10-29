#!/usr/bin/env python3
"""Chunk-wise exact signed Manin weight aggregation.
Does not claim sublinear complexity or a global p=107 certificate.
Run beside kurihara_390_weight_aggregation.py and kurihara_manin_390_fast.py.
"""
import argparse, hashlib, json, math
from sage.all import EllipticCurve, QQ
from sage.libs.eclib.newforms import ECModularSymbol
from kurihara_manin_390_fast import N,table_390,dlog,symbol_by_manin
from kurihara_390_weight_aggregation import edges,vec_390

def compute(p,q1,q2,start,stop):
    n=q1*q2; assert 1<=start<=stop<=(n-1)//2
    E=EllipticCurve(QQ,[0,1,1,-2,0]); sym=ECModularSymbol(E,sign=1)
    M=vec_390(table_390(sym,p))
    logs1,g1=dlog(q1,p);logs2,g2=dlog(q2,p)
    W=[0]*(N+1); direct=0; units=0; nonzero=0
    for a in range(start,stop+1):
        x,y=a%q1,a%q2
        if not x or not y:continue
        units+=1; wt=logs1[x]*logs2[y]%p
        if wt==0:continue
        nonzero+=1
        for idx,sg in edges(a,n):W[idx]=(W[idx]+wt*sg)%p
        direct=(direct+wt*symbol_by_manin(a,n,p,(M[:N],M[N])))%p
    contraction=sum(x*y for x,y in zip(M,W))%p
    assert contraction==direct,(contraction,direct)
    return {'p':p,'q1':q1,'q2':q2,'n':n,'start':start,'stop':stop,'units':units,
            'nonzero_weights':nonzero,'roots':[g1,g2],'contraction_unpaired':contraction,
            'sha256':hashlib.sha256(bytes(W)).hexdigest(),'W':W}

def merge(reports):
    base=reports[0];p=base['p'];q1=base['q1'];q2=base['q2']
    ordered=sorted(reports,key=lambda r:r['start'])
    assert all((r['p'],r['q1'],r['q2'],r['n'],r['roots'])==(p,q1,q2,base['n'],base['roots']) for r in ordered)
    assert all(ordered[i]['stop']+1==ordered[i+1]['start'] for i in range(len(ordered)-1)), 'noncontiguous ranges'
    W=[sum(r['W'][i] for r in ordered)%p for i in range(N+1)]
    E=EllipticCurve(QQ,[0,1,1,-2,0]);M=vec_390(table_390(ECModularSymbol(E,sign=1),p))
    value=sum(m*w for m,w in zip(M,W))%p
    assert value==sum(r['contraction_unpaired'] for r in ordered)%p
    out={'p':p,'q1':q1,'q2':q2,'start':ordered[0]['start'],'stop':ordered[-1]['stop'],
         'chunks':len(ordered),'unpaired':value,'W_sha256':hashlib.sha256(bytes(W)).hexdigest()}
    if out['stop']==(base['n']-1)//2 and out['start']==1:
        out['kind']='COMPLETE';out['delta_mod_p']=2*value%p
    else:out['kind']='PARTIAL_ONLY'
    return out,W

def cli():
    ap=argparse.ArgumentParser();ap.add_argument('--selftest',action='store_true');ap.add_argument('--merge',nargs='+');
    ap.add_argument('--p',type=int,default=107);ap.add_argument('--q1',type=int,default=369793)
    ap.add_argument('--q2',type=int,default=383917);ap.add_argument('--start',type=int,default=1)
    ap.add_argument('--stop',type=int,default=1000);ap.add_argument('--out');a=ap.parse_args()
    if a.selftest:
        for p,q1,q2,end,expected in [(5,41,61,1250,4),(7,113,673,38024,2),(107,369793,383917,1000,53)]:
            mid=end//2;one=compute(p,q1,q2,1,mid);two=compute(p,q1,q2,mid+1,end)
            report,W=merge([one,two]);whole=compute(p,q1,q2,1,end)
            assert W==whole['W'];assert report['unpaired']==whole['contraction_unpaired']
            assert (report['delta_mod_p'] if report['kind']=='COMPLETE' else report['unpaired'])==expected
            print('K107_W390_CHUNK_ADDITIVITY_PASS',p,expected,'sha256',report['W_sha256'],flush=True)
        return
    if a.merge:
        data=[json.load(open(path)) for path in a.merge];report,W=merge(data)
        print('K107_W390_MERGE',json.dumps(report,sort_keys=True),flush=True)
        if a.out:
            with open(a.out,'w') as f:json.dump({'report':report,'W':W},f)
    else:
        result=compute(a.p,a.q1,a.q2,a.start,a.stop)
        print('K107_W390_CHUNK',json.dumps({k:v for k,v in result.items() if k!='W'},sort_keys=True),flush=True)
        if a.out:
            with open(a.out,'w') as f:json.dump(result,f)
if __name__=='__main__':cli()