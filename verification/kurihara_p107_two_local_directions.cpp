// Exact finite-field audit for 389a1 at the first excluded supersingular p=107.
// g++ -O3 -std=c++17 verification/kurihara_p107_two_local_directions.cpp -o /tmp/p107 && /tmp/p107
// Proven: 107-admissible q1,q2, reduction point counts, two transverse local MW directions.
// NOT computed/proven: the global Kurihara modular-symbol number delta_{q1*q2}.
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
struct Point{ll x,y;bool infinity;};
static ll mod(ll a,ll p){a%=p;return a<0?a+p:a;}
static ll inverse(ll a,ll p){ll b=p,u=1,v=0;a=mod(a,p);while(b){ll t=a/b;a-=t*b;swap(a,b);u-=t*v;swap(u,v);}assert(a==1);return mod(u,p);}
static Point add(Point a,Point b,ll q){
  if(a.infinity)return b;if(b.infinity)return a;
  ll slope;
  if(a.x==b.x){
    if(mod(a.y+b.y+1,q)==0)return {0,0,true};
    slope=mod((3*a.x*a.x+2*a.x-2)*inverse(2*a.y+1,q),q);
  }else slope=mod((b.y-a.y)*inverse(b.x-a.x,q),q);
  ll x3=mod(slope*slope-1-a.x-b.x,q);
  ll y3=mod(-slope*(x3-a.x)-a.y-1,q);
  return {x3,y3,false};
}
static Point multiple(ll n,Point p,ll q){
  Point s={0,0,true};while(n){if(n&1)s=add(s,p,q);p=add(p,p,q);n>>=1;}return s;
}
static bool equal(Point a,Point b){return a.infinity?b.infinity:(!b.infinity&&a.x==b.x&&a.y==b.y);}
static bool is_prime(ll n){if(n<2)return false;for(ll d=2;d*d<=n;d++)if(n%d==0)return false;return true;}
static ll points(ll q){
  vector<uint8_t> quadratic(q,0);
  for(ll j=1;j<=(q-1)/2;j++)quadratic[(j*j)%q]=1;
  // y^2+y=x^3+x^2-2x has 1+chi(1+4f(x)) y's above each x.
  ll trace_sum=0;
  for(ll x=0,f=0;x<q;x++){
    ll d=(1+4*f)%q;
    if(d)trace_sum+=quadratic[d]?1:-1;
    f=(f+3*x*x+5*x)%q; // f(x+1)-f(x)=3x^2+5x
  }
  return q+1+trace_sum;
}
int main(){
  const ll p=107;const ll qs[2]={369793,383917};
  const ll Ns[2]={369792,384772};const int slope[2]={58,3};
  Point P={0,0,false},Q={1,0,false};
  for(int i=0;i<2;i++){
    ll q=qs[i];assert(is_prime(q)&&q%p==1&&q!=389);
    ll N=points(q);assert(N==Ns[i]&&N%p==0&&N%(p*p)!=0);
    Point A=multiple(N/p,P,q),B=multiple(N/p,Q,q);
    assert(!A.infinity && !B.infinity);
    assert(multiple(p,A,q).infinity && multiple(p,B,q).infinity);
    assert(equal(multiple(slope[i],A,q),B));
    cout<<"P107_AUX_PASS q="<<q<<" #E(Fq)="<<N<<" a_q="<<(q+1-N)
        <<" q_mod107="<<q%p<<" Q_div_P_mod107="<<slope[i]<<endl;
  }
  ll det=mod(slope[1]-slope[0],p);assert(det==52);
  cout<<"P107_LOCAL_DETERMINANT_PASS "<<det<<endl;
  cout<<"P107_KURIHARA_LEVEL "<<qs[0]*qs[1]
      <<" PHI "<<(qs[0]-1)*(qs[1]-1)<<endl;
  cout<<"P107_GLOBAL_KURIHARA_DELTA_NOT_COMPUTED"<<endl;
}
