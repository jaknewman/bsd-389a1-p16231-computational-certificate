#!/usr/bin/env python3
"""V65 independent terminal oracle: Sage/eclib values of F(beta_t G_g).

Does NOT import/use C01, V23 or V26 computational code. Checkpoints are
separate and can be resumed. Run with Sage's Python environment.
"""
import argparse, hashlib, json, sys, time
from array import array
from pathlib import Path
from sage.all import EllipticCurve, QQ

P, N, NG = 16231, 389, 67
REL = Path.home()/'bsd389-portable-c01-v2/data/bsd389_tame_relation_export_p16231.json'
SCALARS = Path.home()/'bsd389-portable-c01-v2/data/bsd389_tame_scalar_values_p16231.json'
ROOT = Path.home()/'bsd389-c01-v14-production/v65_independent_terminal'
SHA_REL='9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8'
SHA_VAL='7724c8d730a370e3fdc403293b9fc23f6adad632ca39b53d8439a96f18dd0c7e'

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as inp:
        for chunk in iter(lambda:inp.read(1048576),b''): h.update(chunk)
    return h.hexdigest()

def read_row(path):
    a=array('H'); a.frombytes(path.read_bytes())
    assert sys.byteorder=='little' and a.itemsize==2 and len(a)==P+2
    assert max(a)<P
    return a

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--first',type=int,default=0)
    parser.add_argument('--last',type=int,default=NG)
    args=parser.parse_args()
    assert 0<=args.first<args.last<=NG
    assert sha(REL)==SHA_REL and sha(SCALARS)==SHA_VAL
    export=json.loads(REL.read_text()); recorded=json.loads(SCALARS.read_text())['values_mod_p']
    by_g={}
    for rec in export['reps']:
        g=int(rec['generator'])
        if g>=0:
            assert g not in by_g
            by_g[g]=tuple(int(x) for x in rec['matrix'])
    assert set(by_g)==set(range(NG)) and len(recorded)==NG
    for a,b,c,d in by_g.values(): assert a*d-b*c==1
    ROOT.mkdir(exist_ok=True)
    E=EllipticCurve('389a1')
    m=E.modular_symbol(sign=+1,implementation='eclib',normalize='L_ratio')
    def cusp(top,bot):
        return QQ(0) if bot==0 else QQ(m(QQ(top)/bot))
    def reduce(q):
        num=int(q.numerator());den=int(q.denominator())
        if den%P==0: raise ArithmeticError('p in modular symbol denominator')
        return (num*pow(den,-1,P))%P
    def difference(a,b,c,d): return reduce(cusp(a,c)-cusp(b,d))
    for g in range(args.first,args.last):
        destination=ROOT/f'row_{g:02}.bin'
        if destination.exists():
            row=read_row(destination)
            assert (sum(row[2:])+row[1]-128*row[0])%P==0
            assert row[0]==int(recorded[g])%P
            a,b,c,d=by_g[g]
            for t in (0,1,101,P-1):
                assert row[2+t]==difference(a+t*c,b+t*d,P*c,P*d),('resume row altered',g,t)
            print('V65_ROW_RESUMED',g,sha(destination),flush=True)
            continue
        a,b,c,d=by_g[g]; tic=time.monotonic()
        row=array('H',[difference(a,b,c,d),difference(P*a,P*b,c,d)])
        # F(beta_t Gg): beta_t Gg = [a+t*c,b+t*d;p*c,p*d].
        for t in range(P):
            row.append(difference(a+t*c,b+t*d,P*c,P*d))
        assert len(row)==P+2 and max(row)<P
        assert row[0] == int(recorded[g])%P,(g,'F(G) eclib mismatch')
        # Independent Hecke-eigenvalue test: sum_t F(beta_t G)+F(PG)=128F(G).
        assert (sum(row[2:])+row[1]-128*row[0])%P==0,(g,'Hecke mismatch')
        buf=row.tobytes()
        assert sys.byteorder=='little'
        tmp=destination.with_suffix('.tmp');tmp.write_bytes(buf);tmp.replace(destination)
        print('V65_ECLIB_ROW_PASS',g,'SHA256',sha(destination),'SECONDS',round(time.monotonic()-tic,2),flush=True)
    if args.last==NG and args.first==0:
        for g in range(NG):
            if not (ROOT/f'row_{g:02}.bin').exists():
                raise RuntimeError('missing row '+str(g))
        combined=ROOT/'eclib_beta_table.bin'
        tmp=combined.with_suffix('.tmp')
        with tmp.open('wb') as out:
            out.write(b'BSD65F01')
            for n in (P,N,NG):out.write(n.to_bytes(4,'little'))
            for g in range(NG):out.write((ROOT/f'row_{g:02}.bin').read_bytes())
        tmp.replace(combined)
        digest=sha(combined)
        manifest={'version':'V65_REFERENCE_ECLIB_HECKE_TABLE','p':P,'N':N,'generators':NG,'table_sha256':digest,'relation_source_sha256':SHA_REL,'scalar_source_sha256':SHA_VAL,
                  'row_sha256':[sha(ROOT/f'row_{g:02}.bin') for g in range(NG)]}
        (ROOT/'eclib_beta_table_manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
        print('V65_ALL_ECLIB_HECKE_ROWS_PASS','TABLE_SHA256',digest,flush=True)

if __name__=='__main__':main()
