// Independent exact Mazur-Tate p^2 moment regression for E=389a1.
// Uses original full convergent rational numerator/denominator method,
// not Python symbol_by_manin or the optimized p599 denominator automaton.
// Build: g++ -O3 -std=c++17 -Wall -Wextra -o ~/bsd389_p599_cyclotomic_p2_independent verification/bsd389_p599_cyclotomic_p2_independent_native.cpp
// Run: ~/bsd389_p599_cyclotomic_p2_independent --table ~/bsd389_p599_manin_table.txt
// No Kurihara delta or Sha claim.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;
using u64=uint64_t;
static constexpr int LEVEL=389;
static int reduce(int64_t a,int p){int b=int(a%p);return b<0?b+p:b;}
static int modular_power(int a,int64_t e,int n){
  u64 ans=1,base=u64(a)%n;
  while(e){if(e&1)ans=ans*base%n;base=base*base%n;e>>=1;}
  return int(ans);
}
static int inv(int x,int p) {
  // Independent extended Euclid in F_389.
  int a=x,b=p,u=1,v=0;
  while(b){int q=a/b;int t=a-q*b;a=b;b=t;t=u-q*v;u=v;v=t;}
  if(a!=1)throw runtime_error("unexpected noninvertible c");
  return reduce(u,p);
}
static int symbol(int a,int n,int p,const array<int,390>&M,u64 &edges){
  // Signed full rational-convergent method; all numerators and denominators.
  int64_t pn=1,pd=0,ln=0,ld=1,x=n,y=a;
  int value=M[389],sign=-1;
  while(y) {
    int64_t q=x/y,r=x%y;x=y;y=r;
    int64_t nn=q*ln+pn,nd=q*ld+pd;
    int c=int((sign==1?ld:nd)%LEVEL);
    int d=int((sign==1?nd:ld)%LEVEL);
    int idx=c==0?389:reduce(int64_t(d)*inv(c,LEVEL),LEVEL);
    value=reduce(int64_t(value)+sign*M[idx],p);
    pn=ln;pd=ld;ln=nn;ld=nd;sign=-sign;
    ++edges;
  }
  if(x!=1 || ln!=a || ld!=n)
    throw runtime_error("invalid terminal convergent");
  return value;
}
int main(int argc,char**argv){
  try{
    string tab;
    for(int i=1;i+1<argc;i++)if(string(argv[i])=="--table")tab=argv[++i];
    if(tab.empty())throw runtime_error("required --table PATH");
    ifstream f(tab);
    if(!f)throw runtime_error("cannot read table");
    int p,q1,q2;f>>p>>q1>>q2;
    if(!f||(p!=5&&p!=7&&p!=599))throw runtime_error("invalid p");
    if(p==599 && (q1!=6912461||q2!=13963889))throw runtime_error("unexpected source table header");
    array<int,390>M{};
    for(int &v:M){f>>v;if(!f||v<0||v>=p)throw runtime_error("bad Manin value");}
    string extra;if(f>>extra)throw runtime_error("unexpected extra table data");
    const int n=p*p,half=(n-1)/2;
    array<int,3>C={0,0,0};
    array<int,599> bucket{};
    u64 edges=0,paired=0,checksum=0;
    for(int a=1;a<=half;a++){
      if(a%p==0)continue;
      int t=modular_power(a,p-1,n);
      if(t%p!=1)throw runtime_error("Fermat quotient invalid");
      int k=reduce(-((t-1)/p),p);
      if(int(u64(modular_power(a,p,n))*(1+u64(p)*k)%n)!=a)
        throw runtime_error("Teichmuller times Gamma decomposition failed");
      int v=symbol(a,n,p,M,edges);
      int b=a%p;
      bucket[b]=reduce(bucket[b]+v,p);
      bucket[p-b]=reduce(bucket[p-b]+v,p);
      C[0]=reduce(C[0]+2*v,p);
      C[1]=reduce(C[1]+2LL*v*k,p);
      C[2]=reduce(C[2]+int64_t(v)*k*(k-1),p);
      checksum=(checksum+(u64(a)*v+u64(k)*k)%1000000007ULL)%1000000007ULL;
      paired++;
    }
    if(paired!=u64(p)*(p-1)/2)throw runtime_error("wrong number of pairs");
    for(int b=1;b<p;b++){
      // For supersingular p599 with E rank two, a_p=S(0)=0.
      if(p==599&&bucket[b]!=0)throw runtime_error("p599 Hecke fibre failed");
    }
    if(p==599 && (C[0]!=0||C[1]!=0||C[2]!=543))
      throw runtime_error("p599 genuine certified moments mismatch");
    cout<<"CYCLOTOMIC_P2_INDEPENDENT_NATIVE_PASS"
        <<" p="<<p<<" pairs="<<paired<<" C0="<<C[0]<<" C1="<<C[1]
        <<" C2="<<C[2]<<" edges="<<edges<<" checksum="<<checksum<<"\n";
    cout<<"BOUNDARY: independent exact finite-level moments; not Kurihara/Selmer/Sha.\n";
  }catch(const exception&e){cerr<<"ERROR: "<<e.what()<<"\n";return 2;}
}
