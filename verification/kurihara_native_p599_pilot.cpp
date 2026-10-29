// 389a1: bounded Kurihara W390 native pilot, including supersingular p=599.
// Corrects the K107-native 8-bit log-table limitation: residues stored in uint16_t.
// Compile: g++ -O3 -std=c++17 -Wall -Wextra -o /tmp/k599_pilot verification/kurihara_native_p599_pilot.cpp
// Run: /tmp/k599_pilot --table /path/to/p599_manin390.txt --start 1 --end 10000
// NEVER emits a full Kurihara certificate; every interval has STATUS=PARTIAL_ONLY.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using u64=uint64_t;
static constexpr int N=389;
static int mod(int64_t x,int p){x%=p;return x<0?int(x+p):int(x);}
static u64 arg(int argc,char**argv,const string &key,u64 def){
 for(int i=1;i+1<argc;i++){if(string(argv[i])==key)return stoull(argv[i+1]);}
 return def;
}
static bool flag(int argc,char**argv,const string &key){
 for(int i=1;i<argc;i++){if(string(argv[i])==key)return true;}
 return false;
}
static int modpow(int a,int e,int q){
 u64 v=1,b=a;
 while(e){if(e&1)v=v*b%q;b=b*b%q;e>>=1;}return int(v);
}
static int generator_and_dlog(int q,int p,vector<uint16_t> &logs){
 vector<int> divisors;int k=q-1;
 for(int d=2;int64_t(d)*d<=k;d++)if(k%d==0){
   divisors.push_back(d);while(k%d==0)k/=d;
 }
 if(k>1)divisors.push_back(k);
 int g=2;
 while(g<q){bool ok=true;for(int d:divisors)if(modpow(g,(q-1)/d,q)==1){ok=false;break;}
  if(ok)break;
  g++;
 }
 if(g==q)throw runtime_error("no generator: q may not be prime");
 logs.assign(q,0);int x=1;
 for(int j=0;j<q-1;j++){logs[x]=uint16_t(j%p);x=int(u64(x)*g%q);}
 if(x!=1)throw runtime_error("generator validation failed");
 return g;
}
int main(int argc,char**argv){
 try{
  string table;
  for(int i=1;i+1<argc;i++)if(string(argv[i])=="--table")table=argv[i+1];
  if(table.empty())throw runtime_error("usage: --table FILE --start 1 --end 10000");
  ifstream f(table);if(!f)throw runtime_error("table not found");
  int p,q1,q2;f>>p>>q1>>q2;
  if(!f || p<5 || p>65535 || q1<3 || q2<3 || q1==q2 ||
      q1==N || q2==N || (q1-1)%p || (q2-1)%p || q1>2000000000 || q2>2000000000)
       throw runtime_error("invalid header; p must fit uint16_t; q_i must be valid p-admissible candidates");
  array<int,390> M{};for(int &v:M){f>>v;if(!f||v<0||v>=p)throw runtime_error("bad Manin table entry");}
  string extra;if(f>>extra)throw runtime_error("extra fields in table");
  const u64 n=u64(q1)*u64(q2),half=(n-1)/2;
  u64 start=arg(argc,argv,"--start",1),end=arg(argc,argv,"--end",10000);
  if(start<1||end<start||end>half)throw runtime_error("interval outside half-range");
  if(end-start+1>1000000 && !flag(argc,argv,"--allow-large"))
    throw runtime_error("pilot limit 1,000,000 terms; explicit --allow-large required");
  vector<uint16_t>L1,L2;
  const int g1=generator_and_dlog(q1,p,L1),g2=generator_and_dlog(q2,p,L2);
  array<int,389> inv{};
  for(int i=1;i<N;i++)for(int j=1;j<N;j++)if(i*j%N==1){inv[i]=j;break;}
  array<u64,390> W{};u64 units=0,weighted=0,edges=0;
  int residue=0; auto tic=chrono::steady_clock::now();
  int r1=int(start%q1),r2=int(start%q2);
  for(u64 a=start;a<=end;a++){
   if(r1 && r2){
    units++;
    const int wt=int(u64(L1[r1])*L2[r2]%u64(p));
    if(wt){
     weighted++;
     W[389]+=wt;int val=M[389];
     u64 pn=1,pd=0,ln=0,ld=1,x=n,y=a;
     int sign=-1;
     while(y){
      const u64 quot=x/y,r=x%y;x=y;y=r;
      const u64 nn=quot*ln+pn,nd=quot*ld+pd;
      const int c=int((sign==1?ld:nd)%N),d=int((sign==1?nd:ld)%N);
      const int idx=(c==0?389:int(int64_t(d)*inv[c]%N));
      W[idx]+=u64(sign==1?wt:p-wt);
      val+=sign*M[idx];edges++;
      pn=ln;pd=ld;ln=nn;ld=nd;sign=-sign;
     }
     if(ln!=a||ld!=n)throw runtime_error("continued fraction convergence failure");
     residue=mod(int64_t(residue)+int64_t(wt)*mod(val,p),p);
    }
   }
   if(++r1==q1)r1=0;
   if(++r2==q2)r2=0;
  }
  int contracted=0;
  for(int i=0;i<390;i++)contracted=mod(int64_t(contracted)+int64_t(W[i]%p)*M[i],p);
  if(contracted!=residue)throw runtime_error("390-dimensional contraction mismatch");
  const double sec=chrono::duration<double>(chrono::steady_clock::now()-tic).count();
  cout<<"KURIHARA_NATIVE_CHUNK p="<<p<<" q1="<<q1<<" q2="<<q2
      <<" g1="<<g1<<" g2="<<g2<<" start="<<start<<" end="<<end
      <<" contraction="<<contracted<<" units="<<units<<" weights="<<weighted
      <<" edges="<<edges<<" seconds="<<sec<<" STATUS=PARTIAL_ONLY\n";
  cout<<"W390";for(int i=0;i<390;i++)cout<<' '<<W[i]%p;cout<<'\n';
  return 0;
 }catch(const exception&e){cerr<<"ERROR: "<<e.what()<<'\n';return 2;}
}
