#!/usr/bin/env python3
"""Compare independent Hecke/NTT terminal with all historical 67+67 blocks.

Unlike V64, no J0/J1 is assumed while building or computing the reference
moments; reference values arise from separately evaluated eclib F(beta_tG_g).
"""
from pathlib import Path
import csv,hashlib,json
P=16231
ROOT=Path.home()/'bsd389-c01-v14-production'
OUT=ROOT/'v65_independent_terminal'
STATE=ROOT/'v19_checkpoints/state_263429130.bin'
S0=ROOT/'v23_m0_progress.json'
S1=ROOT/'v26_m1_progress.json'
TABLE=OUT/'eclib_beta_table.bin'
TSV=OUT/'v65_per_generator.tsv'

def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())

def main():
    assert sha(STATE)=='5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e'
    m=load(OUT/'eclib_beta_table_manifest.json')
    assert m['table_sha256']==sha(TABLE)
    p0,p1=load(S0),load(S1)
    assert p0['next_generator']==67 and p1['next_generator']==67
    assert p0['source_sha256']==sha(STATE) and p1['source_sha256']==sha(STATE)
    assert sorted(int(x['g']) for x in p0['per_generator'])==list(range(67))
    assert sorted(int(x['g']) for x in p1['per_generator'])==list(range(67))
    c0={int(x['g']):int(x['contribution']) for x in p0['per_generator']}
    c1={int(x['g']):int(x['contribution']) for x in p1['per_generator']}
    with TSV.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    assert len(rows)==68 and rows[-1]['g']=='TOTAL'
    checked=0;j0=j1=0
    for g in range(67):
        r=rows[g]; assert int(r['g'])==g
        x=int(r['J0']);y=int(r['J1'])
        assert int(r['Hecke'])==0
        assert (x,y)==(c0[g],c1[g]), ('independent terminal mismatch',g,x,y,c0[g],c1[g])
        j0=(j0+x)%P;j1=(j1+y)%P
        checked+=1
    assert (j0,j1)==(16014,4703)
    assert (int(rows[-1]['J0']),int(rows[-1]['J1']))==(j0,j1)
    assert (j0+j1)%P==4486
    print('V65_67_GENERATORS_X_TWO_MOMENTS_INDEPENDENT_PASS',checked,flush=True)
    print('V65_INDEPENDENT_J0_J1_J',j0,j1,(j0+j1)%P,flush=True)
    cert={'status':'V65_INDEPENDENT_TERMINAL_PASS','generators':67,'checks_per_generator':2,
          'J0':j0,'J1':j1,'J':(j0+j1)%P,'state_sha256':sha(STATE),
          'reference_eclib_table_sha256':sha(TABLE),'terminal_tsv_sha256':sha(TSV),
          'v23_progress_sha256':sha(S0),'v26_progress_sha256':sha(S1),
          'scope':'independent recomputation of terminal moments, not full C01 production'}
    (OUT/'v65_terminal_certificate.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print('V65_TERMINAL_CERTIFICATE_SAVED',flush=True)
    print('BOUNDARY: does not prove all 263429130 C01 pair updates',flush=True)
if __name__=='__main__':main()
