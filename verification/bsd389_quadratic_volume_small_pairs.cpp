// E389a1: independent genuine Mazur-Tate two-prime Kurihara arithmetic at p=5 and p=7.
// Finite empirical discovery: quadratic local-volume factorization on 105 + 10 + 15 pairs.
// This does NOT establish a theorem for all q or all p, or prove BSD globally.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

constexpr int N=389;
const string COMPACT="22222423212322123232122231233221001122123213121002222221111022224"
"23222221112200001122102211013344223321321111111113232331212112202"
"22323121333422232134222244424332233424333433333443223233222010022"
"22001022233232234433333433342433223342444222243123222433312132322"
"20221121213323231111111112312332244331011220122110000221112222232"
"42222011112222220012131232122110012233213222123232122321232422222";
int V[390], Inv389[389];
int mod(int64_t x,int m){int r=int(x%m);return r<0?r+m:r;}
int pw(int a,int64_t n,int m){int64_t z=1,v=mod(a,m);while(n){if(n&1)z=z*v%m;v=v*v%m;n>>=1;}return int(z);}
struct Pt{int x=0,y=0;bool inf=true;};
bool eq(Pt a,Pt b){return a.inf==b.inf&&(a.inf||(a.x==b.x&&a.y==b.y));}
Pt point_add(Pt a,Pt b,int q){
 if(a.inf)return b;
 if(b.inf)return a;
 if(a.x==b.x&&mod(a.y+b.y+1,q)==0)return {};
 int l;
 if(a.x==b.x)l=mod(int64_t(3)*a.x*a.x+2*a.x-2,q)*int64_t(pw(2*a.y+1,q-2,q))%q;
 else l=mod(b.y-a.y,q)*int64_t(pw(b.x-a.x,q-2,q))%q;
 int nu=mod(a.y-int64_t(l)*a.x,q);
 int x=mod(int64_t(l)*l-1-a.x-b.x,q);
 return {x,mod(-int64_t(l)*x-nu-1,q),false};
}
Pt mul(Pt a,int64_t n,int q){Pt s{};while(n){if(n&1)s=point_add(s,a,q);a=point_add(a,a,q);n>>=1;}return s;}
Pt rationalP(int q){return {q-1,1,false};}
Pt rationalQ(int q){return {0,q-1,false};}
int point_count(int q){int total=1;for(int x=0;x<q;++x){int d=mod(1+4LL*(int64_t(x)*x*x+int64_t(x)*x-2*x),q);total+=(d==0?1:(pw(d,(q-1)/2,q)==1?2:0));}return total;}

int primitive_root(int q){
 int t=q-1;vector<int> primes;
 for(int d=2;d*d<=t;++d)if(t%d==0){primes.push_back(d);while(t%d==0)t/=d;}
 if(t>1)primes.push_back(t);
 for(int g=2;g<q;++g){bool ok=true;for(int d:primes)if(pw(g,(q-1)/d,q)==1){ok=false;break;}if(ok)return g;}
 assert(false);return -1;
}
vector<int> logs(int q,int p){vector<int> v(q,-1);int g=primitive_root(q),x=1;for(int i=0;i<q-1;++i){assert(v[x]==-1);v[x]=i%p;x=int(int64_t(x)*g%q);}assert(x==1);return v;}
int symbol(int a,int n,int p){
 int64_t pn=1,pd=0,ln=0,ld=1,u=n,v=a,s=V[N];
 while(v){int64_t quo=u/v,rem=u%v;u=v;v=rem;int64_t nn=quo*ln+pn,nd=quo*ld+pd;
  int det=int(ln*nd-nn*ld);assert(det==1||det==-1);
  int c=mod(det==1?ld:nd,N),d=mod(det==1?nd:ld,N);
  s+=det*V[c?mod(int64_t(d)*Inv389[c],N):N];
  pn=ln;pd=ld;ln=nn;ld=nd;
 }
 assert(ln==a&&ld==n);return mod(s,p);
}
struct Local{int q,order,first,second;vector<int> logarithms;};
Local local(int q,int p){
 assert((q-1)%p==0);
 int n=point_count(q);assert(mod(q+1-n,p)==2%p);
 assert(n%p==0);int m=n/p;assert(m%p!=0); // restrict to exactly one p in #E(F_q)
 Pt a=mul(rationalP(q),m,q),b=mul(rationalQ(q),m,q);
 assert(eq(mul(a,p,q),Pt{})&&eq(mul(b,p,q),Pt{}));
 assert(!a.inf||!b.inf);
 int rowP=a.inf?0:1,rowQ;
 if(a.inf)rowQ=1;
 else{rowQ=-1;for(int i=0;i<p;++i)if(eq(mul(a,i,q),b)){rowQ=i;break;}assert(rowQ>=0);}
 return {q,n,rowP,rowQ,logs(q,p)};
}
int kurihara(const Local& a,const Local& b,int p){
 const int n=a.q*b.q;int64_t sum=0;int coverage=0;
 for(int k=1;k<=(n-1)/2;++k){int x=a.logarithms[k%a.q],y=b.logarithms[k%b.q];if(x<0||y<0)continue;
  int w=x*y%p;if(w)sum+=int64_t(w)*symbol(k,n,p);coverage++;}
 assert(coverage==(a.q-1)*(b.q-1)/2);
 return mod(2*sum,p);
}
int determinant(Local a,Local b,int p){return mod(int64_t(a.first)*b.second-int64_t(a.second)*b.first,p);}
int main(){
 assert(COMPACT.size()==390);
 for(int i=0;i<390;++i)V[i]=COMPACT[i]-'2';
 assert(V[389]==0);
 for(int a=1;a<N;++a)Inv389[a]=pw(a,N-2,N);
 const vector<vector<int>> tests={{41,61,131,211,251,271,571,641,751,991,1031,1181,1321,1381,1811},
                                   {113,673,1429,2423,3389},
                                   {397,991,1321,3389,3433,4643}};
 for(int p:{5,7,11}){
  const auto& qs=tests[p==5?0:(p==7?1:2)];const int sz=int(qs.size());vector<Local> ls;
  for(int q:qs)ls.push_back(local(q,p));
  vector<vector<int>> delta(sz,vector<int>(sz)),det(sz,vector<int>(sz));
  int count=0,nz=0,zero=0;
  for(int i=0;i<sz;++i)for(int j=i+1;j<sz;++j){
   int d=kurihara(ls[i],ls[j],p);int m=determinant(ls[i],ls[j],p);
   delta[i][j]=delta[j][i]=d;det[i][j]=det[j][i]=m;
   assert((d!=0)==(m!=0));count++;if(d)nz++;else zero++;
   if(p==5 && ls[i].q==41 && ls[j].q==61)assert(d==4);
   if(p==7 && ls[i].q==113 && ls[j].q==673)assert(d==2);
   if(p==11 && ls[i].q==397 && ls[j].q==991)assert(d==1);
   if(p==5 && ls[i].q==131 && ls[j].q==211)assert(d==0);
   if(p==7 && ls[i].q==1429 && ls[j].q==3389)assert(d==0);
  }
  auto C=[&](int i,int j){assert(det[i][j]!=0);return mod(int64_t(delta[i][j])*pw(det[i][j],p-3,p),p);};
  assert(det[0][1]&&det[0][2]&&det[1][2]);
  int scalar=mod(int64_t(C(0,1))*C(0,2)*pw(C(1,2),p-2,p),p);assert(scalar);
  vector<int> u(sz,0);u[0]=1;
  for(int i=1;i<sz;++i){int a=det[0][i]?0:1;assert(det[a][i]);u[i]=mod(int64_t(C(a,i))*pw(scalar*u[a]%p,p-2,p),p);assert(u[i]);}
  int crosschecks=0;
  for(int i=0;i<sz;++i)for(int j=i+1;j<sz;++j){
   int predicted=mod(int64_t(scalar)*u[i]*u[j]*det[i][j]*det[i][j],p);
   assert(predicted==delta[i][j]);crosschecks++;
  }
  int cycle=0;
  for(int a=0;a<sz;++a)for(int b=a+1;b<sz;++b)for(int c=b+1;c<sz;++c)for(int d=c+1;d<sz;++d){
   if(!det[a][b]||!det[c][d]||!det[a][c]||!det[b][d]||!det[a][d]||!det[b][c])continue;
   int x=C(a,b)*C(c,d)%p,y=C(a,c)*C(b,d)%p,z=C(a,d)*C(b,c)%p;
   assert(x==y&&y==z);cycle++;
  }
  cout<<"FINITE_SAMPLE_QUADRATIC_VOLUME_FACTORISATION_PASS p="<<p
      <<" primes="<<sz<<" pairs="<<count<<" det_units="<<nz
      <<" det_zero="<<zero<<" factor_C="<<scalar<<" all_pair_checks="<<crosschecks
      <<" four_prime_checks="<<cycle<<"\n";
  cout<<"p="<<p<<" PRIMES";for(int i=0;i<sz;++i)cout<<" ("<<ls[i].q<<":"<<ls[i].first<<","<<ls[i].second<<";u="<<u[i]<<")";cout<<"\n";
 }
 cout<<"BOUNDARY: finite verified samples only; local units recovered using two-prime coefficients, NOT an independent global Sha proof\n";
}
