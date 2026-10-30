#!/usr/bin/env python3
"""Independent exact-arithmetic bounds/parameter certificate for the K107 native kernel.
Does not substitute for proof of source/binary correspondence.
"""
from math import isqrt
p,q1,q2,N=107,369793,383917,389
n=q1*q2
half=(n-1)//2
assert n==141969819181 and half==70984909590
assert q1%p==q2%p==1
assert all(q%d for q in (q1,q2) for d in range(2,isqrt(q)+1))
assert all(N%d for d in range(2,isqrt(N)+1))
assert ((q1-1)//2)%p==0 and ((q2-1)//2)%p==0
# Maximum CF length is below 64 because all partial quotients >=1
f0,f1=0,1
for i in range(2,65): f0,f1=f1,f0+f1
assert f1>n
max_w=half*65*107
assert max_w<2**64
assert 388**2<2**31 and 106**2<2**31
assert (106+64*106)*106+106<2**31
assert (107+106*106)<2**31
print('K107_STATIC_ARITHMETIC_BOUNDS_PASS',{'n':n,'half':half,'fibonacci_64':f1,'W_upper':max_w,'W_below_u64':True})
print('K107_STATIC_SCOPE_ONLY_NOT_EXECUTABLE_PROOF')
