#!/usr/bin/env python3
"""Exact rational point/group law and formal p-adic logarithm mod p², p=5,7."""
from fractions import Fraction as F
P=(F(-1),F(1)); Q=(F(0),F(-1))
def add(A,B):
 if A is None:return B
 if B is None:return A
 x,y=A;u,v=B
 if x==u and y+v+1==0:return None
 if x!=u: slope=(v-y)/(u-x); nu=(y*u-v*x)/(u-x)
 else:
  d=2*y+1
  assert d
  slope=(3*x*x+2*x-2)/d
  nu=(-x*x*x-2*x-y)/d
 X=slope*slope-1-x-u;Y=-slope*X-nu-1
 assert Y*Y+Y==X*X*X+X*X-2*X
 return X,Y
def mul(n,T):
 U=None
 while n:
  if n&1:U=add(U,T)
  T=add(T,T);n//=2
 return U
def val(n,p):
 if not n:return 999999
 v=0
 while n%p==0:n//=p;v+=1
 return v
def grouporder(p):
 return 1+sum((y*y+y-x*x*x-x*x+2*x)%p==0 for x in range(p) for y in range(p))
for p,expected in [(5,9),(7,13)]:
 n=grouporder(p)
 assert n==expected and n%p
 C=[]
 for label,T in [('P',P),('Q',Q)]:
  A=mul(n,T)
  t= -A[0]/A[1]
  assert val(t.numerator,p)-val(t.denominator,p)>=1
  f=t/p
  assert f.denominator%p
  raw=(f.numerator*pow(f.denominator,-1,p))%p
  coord=raw*pow(n,-1,p)%p
  C.append(coord)
  print('LOCAL_LOG_MODP_PASS',p,label,'t/p',raw,'coordinate',coord)
 assert C=={5:[2,4],7:[5,3]}[p]
 print('LOCAL_KUMMER_SPANS_FINITE_P_LINE_PASS',p,C)
print('BOUNDARY: no derived Kato class or global BSD proof')
