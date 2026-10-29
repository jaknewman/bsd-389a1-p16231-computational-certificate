#!/usr/bin/env python3
"""Pure-Python p599 Artin-Schreier/Fourier checks; not a Sha or delta certificate."""
from math import comb,lcm
def factor(n):
 f=[];d=2
 while d*d<=n:
  if n%d==0:
   f.append(d)
   while n%d==0:n//=d
  d=3 if d==2 else d+2
 if n>1:f.append(n)
 return f
def order(a,q):
 k=q-1
 for r in factor(k):
  while k%r==0 and pow(a,k//r,q)==1:k//=r
 assert pow(a,k,q)==1 and all(pow(a,k//r,q)!=1 for r in factor(k))
 return k
def disc_log_p(q,p,g):
 assert all(pow(g,(q-1)//r,q)!=1 for r in factor(q-1))
 h=pow(g,(q-1)//p,q);target=pow(p,(q-1)//p,q);x=1
 for k in range(p):
  if x==target:return k
  x=x*h%q
 raise ValueError("no p-log")
def trace_monomial(power,p,c):
 z=[0]*(p+2)
 for j in range(p):
  for k in range(power+1):
   z[power-k]=(z[power-k]+comb(power,k)*pow(j*c,k,p))%p
 for degree in range(p+1,p-1,-1):
  v=z[degree];z[degree]=0
  z[degree-p+1]=(z[degree-p+1]+v)%p
  z[degree-p]=(z[degree-p]+v*c)%p
 return z[:p]
def toy_cyclotomic(p,q):
 g=next(g for g in range(2,q) if all(pow(g,(q-1)//r,q)!=1 for r in factor(q-1)))
 logs=[0]*q;x=1
 for k in range(q-1):logs[x]=k%p;x=x*g%q
 assert x==1
 c=disc_log_p(q,p,g)
 # A^p-A-c vanishes modulo Phi_q iff all q coefficients agree.
 z=[0]*q;z[0]=-c%p
 for x in range(1,q):
  z[x*p%q]=(z[x*p%q]+logs[x])%p
  z[x]=(z[x]-logs[x])%p
 assert len(set(z))==1
def toy_fourier_crt():
 p,q1,q2=5,41,61;n=q1*q2
 def logs(q):
  g=next(g for g in range(2,q) if all(pow(g,(q-1)//r,q)!=1 for r in factor(q-1)))
  L=[0]*q;x=1
  for k in range(q-1):L[x]=k%p;x=x*g%q
  return L
 L1,L2=logs(q1),logs(q2)
 u1,u2=pow(q2,-1,q1),pow(q1,-1,q2)
 for m in (0,1,2,41,61,123,2500):
  lhs=[0]*n;rhs=[0]*n
  for a in range(1,n):
   if a%q1 and a%q2:
    j=m*a%n;lhs[j]=(lhs[j]+L1[a%q1]*L2[a%q2])%p
  for x in range(1,q1):
   for y in range(1,q2):
    j=m*(q2*u1*x+q1*u2*y)%n
    rhs[j]=(rhs[j]+L1[x]*L2[y])%p
  assert lhs==rhs,m
 print("K599_CRT_GROUP_RING_FOURIER_TOY_PASS",p,n,7)
def main():
 p=599;q1=6912461;q2=13963889
 d1,d2=order(p,q1),order(p,q2);d=lcm(d1,d2);phi=(q1-1)*(q2-1)
 assert (d1,d2,d,phi//d)==(3456230,3490972,10071454220,9584)
 assert phi%d==0 and d%p==0
 c1,c2=disc_log_p(q1,p,2),disc_log_p(q2,p,3)
 assert (c1,c2,c2*pow(c1,-1,p)%p)==(187,56,500)
 assert ((q1-1)//2)%p==((q2-1)//2)%p==0
 assert (pow(p,d//2,q1),pow(p,d//2,q2))==(1,q2-1)
 print("K599_AS_AND_FROBENIUS_PASS",d1,d2,d,"orbits",phi//d,
       "sign_orbits",phi//d//2,"logp",(c1,c2),"lambda",500,
       "trace_targets",3*(phi//d//2))
 for pp,qq in ((5,41),(5,61),(7,113),(7,673)):toy_cyclotomic(pp,qq)
 toy_fourier_crt()
 for pp,c in ((5,2),(7,1)):
  for k in range(pp+2):
   expect=[(-1 if k==pp-1 else 0)%pp]+[0]*(pp-1)
   assert trace_monomial(k,pp,c)==expect,(pp,k)
 print("K599_FORMAL_AS_AND_TRACE_TOYS_PASS")
 print("BOUNDARY: relative-trace coefficients and beta NOT computed; no delta or Sha certificate.")
if __name__=="__main__":main()
