#include <bits/stdc++.h>
using namespace std;
using ll=long long;
static const int LEVEL=389;
int v[390];int inv389[389];
ll modpow(ll a,ll e,ll n){ll r=1;while(e){if(e&1)r=r*a%n; a=a*a%n;e>>=1;}return r;}
int mod(int a,int p){a%=p;return a<0?a+p:a;}
int symbol(ll a,ll n){
  if(a<=0||a>=n||gcd(a,n)!=1)throw runtime_error("bad cusp");
  ll pn=1,pd=0,ln=0,ld=1,total=v[LEVEL],x=n,y=a;
  while(y){ll q=x/y,r=x%y,nn=q*ln+pn,nd=q*ld+pd;
    ll det=ln*nd-nn*ld;
    if(llabs(det)!=1)throw runtime_error("det");
    int c=mod(det==1?ld:nd,LEVEL),d=mod(det==1?nd:ld,LEVEL);
    total+=det*v[c==0?LEVEL:int(d*inv389[c]%LEVEL)];
    pn=ln;pd=ld;ln=nn;ld=nd;x=y;y=r;
  }
  if(ln!=a||ld!=n)throw runtime_error("bad expansion");
  return total;
}
int ap(int p){ll sum=0;for(int x=0;x<p;x++){ll t=x, rhs=(t*t*t+t*t-2*t)%p;ll disc=mod(1+4*rhs,p);int chi=disc==0?0:(modpow(disc,(p-1)/2,p)==1?1:-1);sum+=chi;}return -int(sum);}
int main(int argc,char**argv){
 if(argc<3){cerr<<"usage: binary table.txt p1 [p2 ...]\n";return 2;}
 ifstream f(argv[1]); for(int&i:v){if(!(f>>i)){cerr<<"table failure\n";return 2;}}
 for(int i=1;i<389;i++)inv389[i]=(int)modpow(i,387,389);
 if(symbol(7,389)!=-1 || symbol(5,389)!=-2){cerr<<"anchor mismatch\n";return 3;}
 for(int k=2;k<argc;k++){
 int p=atoi(argv[k]);if(p<=3||p==389)continue;int an=ap(p);if(an==0){cout<<"P "<<p<<" AP "<<an<<" SUPERSINGULAR_SKIP\n"<<flush;continue;}
 ll n=1ll*p*p;int c0=0,c1=0,c2=0,c3=0;ll count=0;
 for(ll a=1;a<n;a++)if(a%p){int s=symbol(a,n);int j=int(mod(-(int)((modpow(a,p-1,n)-1)/p),p)); // j = -(a^(p-1)-1)/p mod p
   int jchoose2=int(1ll*j*(j-1)/2%p),jchoose3=int(1ll*j*(j-1)*(j-2)/6%p);
   c0=(c0+s)%p;c1=(c1+s*j)%p;c2=(c2+s*jchoose2)%p;c3=(c3+s*jchoose3)%p;count++;
 }
 cout<<"P "<<p<<" AP "<<an<<" N "<<n<<" COUNT "<<count<<" RAW_C0_C1_C2_C3 "<<mod(c0,p)<<" "<<mod(c1,p)<<" "<<mod(c2,p)<<" "<<mod(c3,p)<<" ORDINARY "<<(an%p!=0)<<"\n"<<flush;
 }
}
