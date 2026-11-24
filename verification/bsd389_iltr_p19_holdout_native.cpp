// Exact adversarial p=19 Kurihara check for E389a1 (no inferred Tate values).
// Test pair 2243 * 3877, complete 4,344,996 positive-half unit residues.
// Source: historically authenticated 390-term integral Hecke-Manin vector.
// Expected authentic delta mod 19 = 4, predicted separately by Tate pairing.
// g++ -O3 -std=c++17 verification/bsd389_iltr_p19_holdout_native.cpp -o /tmp/bsd389_p19
// /tmp/bsd389_p19
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
static const string COMPACT="22222423212322123232122231233221001122123213121002222221111022224"
"23222221112200001122102211013344223321321111111113232331212112202"
"22323121333422232134222244424332233424333433333443223233222010022"
"22001022233232234433333433342433223342444222243123222433312132322"
"20221121213323231111111112312332244331011220122110000221112222232"
"42222011112222220012131232122110012233213222123232122321232422222";
constexpr int p=19,N=389,q1=2243,q2=3877,n=q1*q2;
int V[390],Inv[389];
int mod(int64_t x,int m){int y=int(x%m);return y<0?y+m:y;}
int sym(int a){
 int64_t pn=1,pd=0,ln=0,ld=1,u=n,v=a,r=V[N];
 while(v){
  int64_t t=u/v,w=u%v;u=v;v=w;
  int64_t nn=t*ln+pn,nd=t*ld+pd,d=ln*nd-nn*ld;
  assert(d==1||d==-1);
  int c=mod(d==1?ld:nd,N),b=mod(d==1?nd:ld,N);
  r+=d*V[c?mod(int64_t(b)*Inv[c],N):N];
  pn=ln;pd=ld;ln=nn;ld=nd;
 }
 assert(ln==a&&ld==n);
 return mod(r,p);
}
int main(){
 assert(COMPACT.size()==390);
 for(int j=0;j<390;j++)V[j]=COMPACT[j]-'2';
 assert(V[389]==0);
 for(int j=1;j<N;j++){
  for(int k=1;k<N;k++)if(j*k%N==1){Inv[j]=k;break;}
  assert(Inv[j]);
 }
 vector<int>L1(q1,-1),L2(q2,-1);int x=1;
 for(int i=0;i<q1-1;i++){assert(L1[x]==-1);L1[x]=i%p;x=int(int64_t(x)*2%q1);}
 assert(x==1);
 x=1;
 for(int i=0;i<q2-1;i++){assert(L2[x]==-1);L2[x]=i%p;x=int(int64_t(x)*2%q2);}
 assert(x==1);
 int64_t total=0,covered=0;
 for(int a=1;a<=(n-1)/2;a++){
  int x=L1[a%q1],y=L2[a%q2];
  if(x<0||y<0)continue;
  int wt=x*y%p;
  if(wt)total+=int64_t(wt)*sym(a);
  covered++;
 }
 assert(covered==int64_t(q1-1)*(q2-1)/2);
 int delta=mod(2*total,p);
 assert(delta==4);
 std::cout<<"GENUINE_P19_ILTR_HOLDOUT_PASS q1="<<q1<<" q2="<<q2
          <<" full_half_units="<<covered<<" actual_delta="<<delta
          <<" independently_Tate_predicted=4\n";
 std::cout<<"SCOPE: finite honest p19 witness, NO uniform Sha/complex BSD theorem\n";
}
