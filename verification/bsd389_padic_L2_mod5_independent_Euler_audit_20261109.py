#!/usr/bin/env python3
"""Pure arithmetic audit of 389a1 p=5 Euler multiplier and published digits.
The analytic T² coefficient 4 comes from SageMath documentation.
The normalized 5-adic regulator digit 1 comes from Mazur-Stein-Tate 2006.
Neither published p-adic result is recomputed by this script.
"""
def count(q):
    squares={y*y%q for y in range(q)}
    n=1
    for x in range(q):
        d=(1+4*(x*x*x+x*x-2*x))%q
        n+=1 if d==0 else 2 if d in squares else 0
    return n
R={5:1,7:6,11:4,13:9,17:4,19:3,23:17,29:9,31:1,37:28,41:20,43:40,47:25}
for p,r in R.items():
    n=count(p);a=p+1-n
    assert n%p and a%p and r%p
    eps=(1-pow(a%p,-1,p))**2%p
    assert eps
    print('GOOD_ORDINARY_NONANOMALOUS_PUBLISHED_REGULATOR_UNIT_PASS',
          p,'#E(Fp)',n,'a_p',a,'epsilon',eps,'Rmodp',r)
p=5;n=count(p);a=p+1-n
eps=(1-pow(a%p,-1,p))**2%p
L2=4; reg=R[p]
ratio=L2*pow((eps*reg)%p,-1,p)%p
assert (n,a,eps,ratio)==(9,-3,4,1)
print('P5_PADIC_TWO_SOURCE_NORMALIZATION_COMPATIBILITY_PASS',
      'L2_published',L2,'epsilon_calculated',eps,
      'R_published',reg,'ratio_mod5',ratio)
print('BOUNDARY: published digits are inputs; no independent Sha or BSD proof')
