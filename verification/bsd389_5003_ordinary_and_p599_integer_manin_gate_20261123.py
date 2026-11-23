#!/usr/bin/env python3
"""Finite-range BSD prime inventory and p599 *integer Manin* C2 audit.

This is a fresh, dependency-free standard-library implementation, using
the independently archived integer Manin vector (not the eclib p599 table).
It certifies: 5003 covered ordinary primes in the interval, p599 C2=543,
and the CONDITIONAL signed-minus scalar -C2/2=28 mod599.

It does NOT independently identify this scalar with the normalized
Pollack/BSTW analytic L_p^-(T); hence does NOT itself prove Sha[599]=0.
"""
from math import isqrt

B=48859
SUPER={107,599,1049,2957,6661,8263,9397,9551,14633,15101,
       28591,30671,30869,31799,34781,36263,45161}
BAD=389;ORDINARY_EXC=16231
P=599
N=389
MOD=P**2
MANIN_DIGITS="222224232123221232321222312332210011221232131210022222211110222242322222111220000112210221101334422332132111111111323233121211220222323121333422232134222244424332233424333433333443223233222010022220010222332322344333334333424332233424442222431232224333121323222022112121332323111111111231233224433101122012211000022111222223242222011112222220012131232122110012233213222123232122321232422222"
assert len(MANIN_DIGITS)==390
V=[int(z)-2 for z in MANIN_DIGITS]
INV=[0]+[pow(i,-1,N) for i in range(1,N)]

def prime_range():
    sieve=bytearray(b'\x01')*B
    sieve[0:2]=b'\x00\x00'
    for j in range(2,isqrt(B-1)+1):
        if sieve[j]:
            sieve[j*j:B:j]=b'\x00'*(((B-1-j*j)//j)+1)
    return {i for i in range(5,B) if sieve[i]}

def audit_range():
    s=prime_range()
    assert len(s)==5022
    assert len(SUPER)==17 and SUPER<s
    assert BAD in s and ORDINARY_EXC in s
    ordinary=s-(SUPER|{BAD,ORDINARY_EXC})
    assert len(ordinary)==5003
    assert len((s-{BAD})-ordinary)==18
    covered=ordinary|{107}
    excluded=(s-{BAD})-covered
    assert len(covered)==5004 and len(excluded)==17
    print("STEIN_WUTHRICH_2013_THEOREM_12_3_EXTERNAL_INPUT")
    print("389A1_GOOD_ORDINARY_P_GE5_UNDER_48859_SHA_ZERO",len(ordinary))
    print("PLUS_INDEPENDENT_P107_ZERO",len(covered))
    print("GOOD_EXCEPTIONS_UNDER_BOUND",*sorted(excluded))

def symbol(a):
    # Signed P1(F389) Manin continued-fraction edges from infinity to a/MOD.
    assert 0<a<MOD and a%P
    prevn,prevd,lastn,lastd=1,0,0,1
    u,v=MOD,a
    total=V[N]
    while v:
        quotient,rem=divmod(u,v)
        u,v=v,rem
        qn=quotient*lastn+prevn
        qd=quotient*lastd+prevd
        det=lastn*qd-qn*lastd
        assert det in (-1,1)
        c,d=(lastd,qd) if det==1 else (qd,lastd)
        c%=N
        d%=N
        idx=N if c==0 else (d*INV[c])%N
        total+=det*V[idx]
        prevn,prevd,lastn,lastd=lastn,lastd,qn,qd
    assert (lastn,lastd)==(a,MOD)
    return total%P

def check_c2():
    C0=C1=C2=0
    count=0
    for a in range(1,(MOD-1)//2+1):
        if a%P==0:
            continue
        weight=symbol(a)
        z=pow(a,P-1,MOD)
        assert (z-1)%P==0
        k=(-((z-1)//P))%P
        assert (pow(a,P,MOD)*(1+P*k)-a)%MOD==0
        C0=(C0+2*weight)%P
        C1=(C1+2*weight*k)%P
        C2=(C2+weight*k*(k-1))%P
        count+=1
    assert (count,C0,C1,C2)==(179101,0,0,543)
    print("P599_INDEPENDENT_390_INTEGER_MANIN_COMPLETE",count)
    print("P599_C0_C1_C2_MOD599",C0,C1,C2)
    candidate=(-C2*pow(2,-1,P))%P
    assert candidate==28
    print("P599_SIGNED_MINUS_CANDIDATE_MOD599",candidate)
    print("BOUNDARY: candidate-to-TRUE_POLLACK_SIGNED_L_MINUS_SOURCE_NORMALIZATION_NOT_AUDITED")
    print("NO_NEW_SHA599_OR_GLOBAL_BSD_THEOREM_ASSERTED")

if __name__=="__main__":
    audit_range()
    check_c2()
