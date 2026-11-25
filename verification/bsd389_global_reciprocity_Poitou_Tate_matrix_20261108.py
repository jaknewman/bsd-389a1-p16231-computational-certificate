#!/usr/bin/env python3
"""Exact F_p matrix identities for global Poitou-Tate formula (not Kato computation)."""
from itertools import product
CASES={5:((1,3),(1,0)),7:((1,3),(1,6))}
def inv2(A,p):
 (a,b),(c,d)=A
 det=(a*d-b*c)%p
 assert det
 u=pow(det,-1,p)
 return ((d*u%p,-b*u%p),(-c*u%p,a*u%p)),det
for p,B in CASES.items():
 Bt=((B[0][0],B[1][0]),(B[0][1],B[1][1]))
 Inv,det=inv2(Bt,p)
 assert det=={5:2,7:3}[p]
 for x,z in product(range(p),repeat=2):
  y0=(Inv[0][0]*x+Inv[0][1]*z)%p
  y1=(Inv[1][0]*x+Inv[1][1]*z)%p
  assert (Bt[0][0]*y0+Bt[0][1]*y1)%p==x
  assert (Bt[1][0]*y0+Bt[1][1]*y1)%p==z
 print('POITOU_TATE_MATRIX_ALL_RHS_PASS',p,B,'det',det,'inv_Bt',Inv,'checks',p*p)
print('BOUNDARY: finite-field matrix regression; no global Sha/Kato theorem tested')
