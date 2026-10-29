// Stage K107-NATIVE: exact finite chunk sums over 390 Manin edge classes.
// Compile: g++ -O3 -std=c++17 -march=native -o /tmp/k107native kurihara_k107_native.cpp
// Only emits PARTIAL chunks unless full half-range has been explicitly covered and merged.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>
using namespace std;
using u64=uint64_t;
static const int N=389;
static u64 arg(int argc,char**argv,const string&key,u64 def){for(int i=1;i+1<argc;i++)if(argv[i]==key)return stoull(argv[i+1]);return def;}
static int imod(int x,int p){x%=p;return x<0?x+p:x;}
static int gen_dlog(int q,int p,vector<unsigned char>&T){
 vector<int> primes; int x=q-1;
 for(int d=2;(int64_t)d*d<=x;d++)if(x%d==0){primes.push_back(d);while(x%d==0)x/=d;}
 if(x>1)primes.push_back(x);
 auto powmod=[&](int a,int k){int64_t v=1,b=a;while(k){if(k&1)v=v*b%q;b=b*b%q;k>>=1;}return (int)v;};
 int g=2;while(true){bool ok=true;for(int r:primes)if(powmod(g,(q-1)/r)==1){ok=false;break;}if(ok)break;g++;}
 T.assign(q,0);int v=1;for(int k=0;k<q-1;k++){T[v]=(unsigned char)(k%p);v=(int)((int64_t)v*g%q);}if(v!=1)throw runtime_error("dlog table invalid");return g;
}
int main(int argc,char**argv){
 try{
 string table=""; for(int i=1;i+1<argc;i++)if(string(argv[i])=="--table")table=argv[i+1];
 if(table.empty())throw runtime_error("usage: --table /path/to/manin_table.txt --start 1 --end 1000");
 ifstream f(table);if(!f)throw runtime_error("no table");
 int p,q1,q2;f>>p>>q1>>q2;if(!f || p<3 || q1<3 || q2<3)throw runtime_error("bad header");
 array<int,390>M{};for(auto &v:M){f>>v;if(!f||v<0||v>=p)throw runtime_error("bad table entry");}
 const u64 n=(u64)q1*q2,half=(n-1)/2;
 u64 start=arg(argc,argv,"--start",1),end=arg(argc,argv,"--end",1000);
 if(start<1||end<start||end>half)throw runtime_error("interval outside half-range");
 vector<unsigned char>L1,L2;int g1=gen_dlog(q1,p,L1),g2=gen_dlog(q2,p,L2);
 array<int,389>inv{}; for(int i=1;i<N;i++)for(int j=1;j<N;j++)if(i*j%N==1){inv[i]=j;break;}
 array<u64,390>W{};u64 units=0,weighted=0,edges=0;int partial=0;
 auto begin=chrono::steady_clock::now();
 for(u64 a=start;a<=end;a++){
   int r1=(int)(a%q1),r2=(int)(a%q2);if(r1==0||r2==0)continue;units++;
   int wt=(int)L1[r1]*(int)L2[r2]%p;if(wt==0)continue;weighted++;
   // Starting edge infinity->0, then CF edges. Store unsigned mod-p counts.
   W[389]+=wt;int val=M[389];
   u64 pn=1,pd=0,ln=0,ld=1,x=n,y=a;
   int sign=-1;
   while(y){
     u64 quot=x/y,r=x%y;x=y;y=r;
     u64 nn=quot*ln+pn,nd=quot*ld+pd;
     int c=(int)((sign==1?ld:nd)%N),d=(int)((sign==1?nd:ld)%N);
     int idx=(c==0?389:(int)((int64_t)d*inv[c]%N));
     W[idx]+=(u64)(sign==1?wt:p-wt);
     val+=sign*M[idx];edges++;
     pn=ln;pd=ld;ln=nn;ld=nd;sign=-sign;
   }
   if(ln!=a||ld!=n)throw runtime_error("CF convergence failure");
   partial=imod(partial+wt*imod(val,p),p);

 }
 auto elapsed=chrono::duration<double>(chrono::steady_clock::now()-begin).count();
 int contracted=0;for(int i=0;i<390;i++)contracted=imod(contracted+(int)(W[i]%p)*M[i],p);
 if(contracted!=partial)throw runtime_error("Manin contraction mismatch");
 cout<<"K107_NATIVE_CHUNK p="<<p<<" q1="<<q1<<" q2="<<q2<<" g1="<<g1<<" g2="<<g2
 <<" start="<<start<<" end="<<end<<" contraction="<<contracted<<" units="<<units
 <<" weights="<<weighted<<" edges="<<edges<<" seconds="<<elapsed
 <<" rate="<<((end-start+1)/max(elapsed,1e-9))<<" STATUS=PARTIAL_ONLY\n";
 cout<<"W390";for(int i=0;i<390;i++)cout<<' '<<W[i]%p;cout<<'\n';
 return 0;
 }catch(const exception&e){cerr<<"ERROR "<<e.what()<<'\n';return 2;}
}