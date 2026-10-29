#!/usr/bin/env python3
"""Export exact 390-entry table from Sage/eclib for native C++ kernel."""
import argparse
from sage.all import EllipticCurve, QQ
from sage.libs.eclib.newforms import ECModularSymbol
from kurihara_manin_390_fast import table_390
A=argparse.ArgumentParser();A.add_argument('--p',type=int,default=107);A.add_argument('--q1',type=int,default=369793);A.add_argument('--q2',type=int,default=383917);A.add_argument('--out',required=True);z=A.parse_args()
E=EllipticCurve(QQ,[0,1,1,-2,0]);tab=table_390(ECModularSymbol(E,sign=1),z.p)
values=[*tab[0],tab[1]]
assert len(values)==390
with open(z.out,'w') as f:
 f.write(f'{z.p} {z.q1} {z.q2}\n')
 f.write(' '.join(map(str,values))+'\n')
print('K107_MANIN_TABLE_EXPORT_PASS',z.p,z.q1,z.q2,z.out)