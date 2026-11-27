from itertools import permutations
cases={
 5:(4,1,3,2,1,1),
 7:(2,1,6,2,3,3),
}
for p,values in cases.items():
 edges=dict(zip(((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)),values))
 d=lambda i,j: edges[tuple(sorted((i,j)))]
 def match(t):
  a,b,c,e=t
  return (d(a,b)*d(c,e),d(a,c)*d(b,e),d(a,e)*d(b,c))
 def pf(t):
  A,B,C=match(t)
  return (A-B+C)%p
 def haf(t):
  return sum(match(t))%p
 base=(0,1,2,3)
 trans=(0,2,1,3)
 assert all(haf(t)==haf(base) for t in permutations(base))
 assert pf(trans)!=(-pf(base))%p
 print('p',p,'pf_original',pf(base),'pf_transpose23',pf(trans),'negative_expected',(-pf(base))%p,'hafnian',haf(base),'PASS')