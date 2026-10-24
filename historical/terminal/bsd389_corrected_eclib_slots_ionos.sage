from pathlib import Path
import json, hashlib, time
p=16231; N=389; alpha_inv=5199
E=EllipticCurve('389a1')
m=E.modular_symbol(sign=+1, implementation='eclib')
def f(n,d):
    if d == 0: return ZZ(0)
    q = -m(QQ(n)/QQ(d))
    num = ZZ(q.numerator())
    den = ZZ(q.denominator())
    if den % p == 0:
        raise ArithmeticError("Denominateur non inversible modulo p")
    return num * inverse_mod(den, p) % p
data=json.load(open(str(
    Path.home() / "bsd389-portable-c01-v2" / "data" /
    "bsd389_tame_relation_export_p16231.json"
)))
bygen={int(x['generator']):x for x in data['reps']}
def D_for(slot):
    g=slot//(p+1); i=slot%(p+1)
    z=bygen[g]['matrix']; r=[[ZZ(z[0]),ZZ(z[1])],[ZZ(z[2]),ZZ(z[3])]]
    return matrix(ZZ,[[1,0],[N*i,1]])*matrix(ZZ,r)
def m0(D):
    Pm=matrix(ZZ,[[p,0],[0,1]])
    return (f(D[0,1],D[1,1])-f(D[0,0],D[1,0])-alpha_inv*(f((Pm*D)[0,1],(Pm*D)[1,1])-f((Pm*D)[0,0],(Pm*D)[1,0])))%p
def m1(D):
    z=ZZ(0); t0=time.time()
    for t in range(p):
        A=matrix(ZZ,[[D[0,0]+t*D[1,0],D[0,1]+t*D[1,1]],[p*D[1,0],p*D[1,1]]])
        z += t*(f(A[0,1],A[1,1])-f(A[0,0],A[1,0]))
        if (t+1)%2048==0: print('progress',t+1,'seconds',round(time.time()-t0,2),flush=True)
    return alpha_inv*z%p
for slot in [0,412586,811357,827589]:
    D=D_for(slot); print('slot',slot,'D',list(D), 'M0',m0(D), 'M1',m1(D),flush=True)
