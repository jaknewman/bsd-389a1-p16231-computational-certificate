// V65 independent exact terminal consumer. No producer, native-moment kernel,
// V23 or V26 source is included.  Reindexes the Hecke operators via
// P^1(F_p), then uses exact two-prime NTT+CRT for cyclic correlations.
// Compile: g++ -O3 -std=c++17 -Wall -Wextra -o v65_ntt v65_independent_terminal_ntt.cpp
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using i64=std::int64_t;
using u16=std::uint16_t;
constexpr int P=16231,N=389,NG=67,SLOTS=NG*(P+1),L=32768;
constexpr int Q1=998244353,Q2=1004535809;
static int md(i64 x,int p=P){x%=p;if(x<0)x+=p;return int(x);}
static int powm(i64 a,int n,int p){i64 z=1;for(;n;n>>=1,a=a*a%p)if(n&1)z=z*a%p;return int(z);}
static int inverse(int x,int p){if(md(x,p)==0)throw std::runtime_error("inverse zero");return powm(md(x,p),p-2,p);}
static void insist(bool yes,const std::string &m){if(!yes)throw std::runtime_error(m);}
static std::vector<std::uint8_t> bytes(const std::string&s){
  std::ifstream f(s,std::ios::binary);insist(bool(f),"missing file: "+s);
  return {std::istreambuf_iterator<char>(f),std::istreambuf_iterator<char>()};
}
static int le16(const std::vector<std::uint8_t>&b,std::size_t i){return int(b.at(i))+(int(b.at(i+1))<<8);}
static int le32(const std::vector<std::uint8_t>&b,std::size_t i){return le16(b,i)+(le16(b,i+2)<<16);}
static void ntt(std::vector<int>&a,bool invert,int mod){
  int n=int(a.size());insist((n&(n-1))==0,"bad transform length");
  for(int i=1,j=0;i<n;i++){
    int bit=n>>1;for(;j&bit;bit>>=1)j^=bit;j^=bit;
    if(i<j)std::swap(a[i],a[j]);
  }
  for(int len=2;len<=n;len<<=1){
    int wlen=powm(3,(mod-1)/len,mod);
    if(invert)wlen=inverse(wlen,mod);
    for(int i=0;i<n;i+=len){i64 w=1;
      for(int j=0;j<len/2;j++){
        int u=a[i+j],v=int(w*a[i+j+len/2]%mod);
        int x=u+v;if(x>=mod)x-=mod;
        int y=u-v;if(y<0)y+=mod;
        a[i+j]=x;a[i+j+len/2]=y;w=w*wlen%mod;
      }
    }
  }
  if(invert){int invn=inverse(n,mod);for(int &v:a)v=int(i64(v)*invn%mod);}
}
struct NTT {
  int q;std::vector<int> af;
  NTT(int mod,const std::vector<int>&a):q(mod),af(L,0){
    for(int i=0;i<P;i++)af[i]=a[i];
    ntt(af,false,q);
  }
  std::vector<int> convolve(const std::vector<int>&b) const {
    std::vector<int> arr(L,0);
    for(int i=0;i<P;i++)arr[i]=b[i];
    ntt(arr,false,q);
    for(int i=0;i<L;i++)arr[i]=int(i64(arr[i])*af[i]%q);
    ntt(arr,true,q);return arr;
  }
};
static std::vector<i64> cyclic(const std::vector<int>&b,const NTT&n1,const NTT&n2){
  auto u=n1.convolve(b),v=n2.convolve(b);
  std::vector<i64> ans(P);
  const int qinv=inverse(Q1%Q2,Q2);
  auto crt=[&](int x,int y)->i64{
    i64 t=i64(md(i64(y)-x,Q2))*qinv%Q2;
    return i64(x)+i64(Q1)*t;
  };
  const i64 bound=i64(P)*(P-1)*(P-1);
  for(int j=0;j<P;j++){
    i64 left=crt(u[j],v[j]);
    i64 right=(j+P<=2*P-2)?crt(u[j+P],v[j+P]):0;
    ans[j]=left+right;
    insist(ans[j]>=0 && ans[j]<=bound,"CRT exceeds exact convolution bound");
  }
  return ans;
}
int main(int argc,char**argv){try{
  insist(argc==4,"usage: ./v65_ntt STATE.bin TABLE.bin OUTPUT_PER_GENERATOR.tsv");
  auto state=bytes(argv[1]);auto tab=bytes(argv[2]);
  insist(state.size()==std::size_t(SLOTS)*4,"state must contain all C0 then all C1, uint16");
  insist(tab.size()==20+std::size_t(NG)*(P+2)*2,"table byte count incorrect");
  insist(std::string(tab.begin(),tab.begin()+8)=="BSD65F01","table header magic mismatch");
  insist(le32(tab,8)==P && le32(tab,12)==N && le32(tab,16)==NG,"table header dimensions mismatch");
  const int alpha_inv=inverse(128,P), invN=inverse(N,P), Ainf=-40,Binf=-1669;
  insist(alpha_inv==5199 && md(i64(Ainf)*P-Binf*N)==1,"curve/exceptional metadata mismatch");
  std::vector<int> inv(P),a(P,0);
  for(int k=1;k<P;k++)inv[k]=inverse(k,P);
  // Cyclic correlation A[x]*B[x+j] via A_rev[k]=A[-k].
  for(int k=1;k<P;k++)a[k]=md(i64(invN)*inv[P-k]);
  NTT ntt1(Q1,a),ntt2(Q2,a);
  std::ofstream out(argv[3]);insist(bool(out),"cannot write per-generator output");
  out<<"g\tJ0\tJ1\tHecke\tM1exceptional\n";
  int J0=0,J1=0;
  for(int g=0;g<NG;g++){
    std::size_t base=20+std::size_t(g)*(P+2)*2;
    int fG=le16(tab,base), fP=le16(tab,base+2);
    std::vector<int> fs(P),b(P,0);
    for(int s=0;s<P;s++){
      fs[s]=le16(tab,base+4+2*s);
      insist(fs[s]<P,"invalid modular symbol residue");
    }
    insist(fG<P && fP<P,"invalid fG/fP residue");
    i64 heckesum=fP;for(int v:fs)heckesum+=v;
    insist(md(heckesum-128*fG)==0,"Hecke self-check failed for g="+std::to_string(g));
    b[0]=fP;
    for(int y=1;y<P;y++)b[y]=fs[md(i64(invN)*inv[y])];
    auto cyc=cyclic(b,ntt1,ntt2);
    // independent direct-sum oracle for a few j; exact integer arithmetic.
    for(int j: {0,1,71,P-1}){
      i64 direct=0;
      for(int x=1;x<P;x++)direct+=i64(md(i64(invN)*inv[x]))*b[(x+j)%P];
      insist(direct==cyc[j],"cyclic correlation mismatch for g="+std::to_string(g));
    }
    int m1special=0;
    for(int t=0;t<P;t++){
      int den=md(Ainf+i64(N)*t);
      int s=den?md(i64(Binf)*inverse(den,P)):P;
      int fv=(s==P?fP:fs[s]);
      m1special=md(m1special+i64(t)*fv);
    }
    m1special=md(i64(alpha_inv)*m1special);
    int j0=0,j1=0;
    for(int i=0;i<=P;i++){
      int sel=(i==0)? fP : (i==P?fs[0]:fs[md(i64(invN)*inv[i])]);
      int m0=md(fG-i64(alpha_inv)*sel);
      int m1=(i==P)?m1special:md(i64(alpha_inv)*md(cyc[i]));
      int slot=g*(P+1)+i;
      int c0=le16(state,2*std::size_t(slot));
      int c1=le16(state,2*(std::size_t(SLOTS)+slot));
      insist(c0<P && c1<P,"non-field coefficient");
      j0=md(j0+i64(c0)*m0);j1=md(j1+i64(c1)*m1);
    }
    J0=md(J0+j0);J1=md(J1+j1);
    out<<g<<'\t'<<j0<<'\t'<<j1<<'\t'<<md(heckesum-128*fG)<<'\t'<<m1special<<'\n';out.flush();
    std::cout<<"V65_INDEPENDENT_TERMINAL_GEN "<<g<<" J0 "<<j0<<" J1 "<<j1<<std::endl;
  }
  out<<"TOTAL\t"<<J0<<'\t'<<J1<<"\t0\t0\n";out.close();
  std::cout<<"V65_INDEPENDENT_J0 "<<J0<<"\nV65_INDEPENDENT_J1 "<<J1
           <<"\nV65_INDEPENDENT_JTOTAL "<<md(J0+J1)<<std::endl;
  if(J0!=16014||J1!=4703||md(J0+J1)!=4486){
    std::cerr<<"V65_TERMINAL_INDEPENDENT_MISMATCH: do NOT conclude equivalence\n";
    return 3;
  }
  std::cout<<"V65_INDEPENDENT_TERMINAL_PASS\n";
} catch(const std::exception&e){std::cerr<<"V65_ERROR "<<e.what()<<std::endl;return 2;}}
