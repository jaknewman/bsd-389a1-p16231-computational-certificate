#include <boost/json.hpp>
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#ifdef BSD389_C01_PROFILE
#include <unordered_map>
#endif
#include <vector>
using i64=std::int64_t; using i128=__int128_t; namespace bj=boost::json;
static constexpr i64 N=389, P=16231, P2=P*P, NG=67, SLOTS=NG*(P+1);
static i64 md(i64 x,i64 m=P){x%=m;return x<0?x+m:x;}
static i64 inv(i64 a,i64 m){i64 t=0,nt=1,r=m,nr=md(a,m);while(nr){i64 q=r/nr;std::swap(t,nt);nt-=q*t;std::swap(r,nr);nr-=q*r;}if(r!=1)throw std::runtime_error("inverse");return md(t,m);}
static i64 mpow(i64 a,i64 e,i64 m){i64 z=1;while(e){if(e&1)z=(i128)z*a%m;a=(i128)a*a%m;e>>=1;}return z;}
struct M{ i64 a,b,c,d; };
static M RINF;
static M mm(M x,M y,i64 mod=P){return {(i64)((((i128)x.a*y.a+(i128)x.b*y.c)%mod+mod)%mod),(i64)((((i128)x.a*y.b+(i128)x.b*y.d)%mod+mod)%mod),(i64)((((i128)x.c*y.a+(i128)x.d*y.c)%mod+mod)%mod),(i64)((((i128)x.c*y.b+(i128)x.d*y.d)%mod+mod)%mod)};}
static M inv1(M x){return {x.d,-x.b,-x.c,x.a};}
struct Term{int coeff,r; M A;}; struct Rep{M g; int gen; std::vector<Term> rel;};
#ifdef BSD389_C01_PROFILE
struct C01Profile {
  std::uint64_t contrib_calls=0,path_calls=0,euclid_steps=0,fragments=0;
  std::uint64_t rep_lookups=0,relation_terms=0,coefficient_adds=0;
  std::unordered_map<std::string,std::uint64_t> exact_B,mod389_B,modP_B;
} C01P;
static std::string mkey(M x){return std::to_string(x.a)+","+std::to_string(x.b)+","+std::to_string(x.c)+","+std::to_string(x.d);}
static std::string modkey(M x,i64 m){return std::to_string(md(x.a,m))+","+std::to_string(md(x.b,m))+","+std::to_string(md(x.c,m))+","+std::to_string(md(x.d,m));}
#endif
#ifdef BSD389_SPARSE_TOUCHED
struct Acc{
  std::vector<i64> c0,c1;
  std::vector<std::uint32_t> stamp;
  std::vector<std::uint32_t> touched_slots;
  std::uint32_t epoch=1;
  Acc():c0(SLOTS),c1(SLOTS),stamp(SLOTS){}
  void reset(){
    touched_slots.clear();
    if(++epoch==0){std::fill(stamp.begin(),stamp.end(),0);epoch=1;}
  }
  void add(int s,i64 x,i64 y,i64 w){
    if(stamp[s]!=epoch){stamp[s]=epoch;c0[s]=0;c1[s]=0;touched_slots.push_back((std::uint32_t)s);}
    c0[s]=md(c0[s]+w*x);c1[s]=md(c1[s]+w*y);
  }
};
#else
struct Acc{std::vector<i64> c0,c1; Acc():c0(SLOTS),c1(SLOTS){} void add(int s,i64 x,i64 y,i64 w){c0[s]=md(c0[s]+w*x);c1[s]=md(c1[s]+w*y);}};
#endif
static int key(M x){i64 c=md(x.c,N),d=md(x.d,N);return d?int(c*inv(d,N)%N):int(N);}
static int qidx(M x){i64 c=md(x.c),d=md(x.d);return d?int((i128)c*inv(d,P)%P*inv(N,P)%P):int(P);}
static M ri(int j){return j<P?M{1,0,N*(i64)j,1}:RINF;}
#ifdef BSD389_EFFECTIVE
static i64 kappa_ab(i64 a,i64 b){
  const i64 P3=P2*P;
  i64 om=mpow(a,P2,P3);
  i64 q=md((mpow(a,P-1,P2)-1)/P,P);
  i64 t=md((i128)b*inv(a,P)-q,P);
  i64 base=(i128)om*mpow(1+P,t,P3)%P3;
  i64 diff=base-(a+P*b);
  if(diff%P2!=0) throw std::runtime_error("kappa divisibility");
  return md(diff/P2,P);
}
#endif
static void path(i64 r,i64 s,int sign,i64 w,const std::vector<Rep>& reps,const std::vector<int>& keyrep,Acc& out
#ifdef BSD389_EFFECTIVE
                 ,i64 kappa
#endif
                 ){
#ifdef BSD389_C01_PROFILE
  C01P.path_calls++;
#endif
  const i64 initial_r=r, initial_s=s;
  std::vector<i64> h,k,qv; i64 hm2=0,hm1=1,km2=1,km1=0;
  while(s){
#ifdef BSD389_C01_PROFILE
    C01P.euclid_steps++;
#endif
    i64 aa=r/s,hn=aa*hm1+hm2,kn=aa*km1+km2;qv.push_back(aa);h.push_back(hn);k.push_back(kn);hm2=hm1;hm1=hn;km2=km1;km1=kn;std::swap(r,s);s-=aa*r;}
  std::vector<M> vs; if(h.empty())return; vs.push_back({1,h[0],0,k[0]});
  for(size_t j=0;j+1<h.size();++j){i64 sg=(j%2)?1:-1;vs.push_back({sg*h[j],h[j+1],sg*k[j],k[j+1]});}
#ifdef BSD389_TRACE_VS
  std::cerr<<"TRACE_PATH r="<<initial_r<<" s="<<initial_s<<" quotients=";
  for(size_t j=0;j<qv.size();++j) std::cerr<<(j?",":"")<<qv[j];
  std::cerr<<" h="; for(size_t j=0;j<h.size();++j) std::cerr<<(j?",":"")<<h[j];
  std::cerr<<" k="; for(size_t j=0;j<k.size();++j) std::cerr<<(j?",":"")<<k[j]; std::cerr<<"\n";
  for(const M&B:vs){
    i128 det=(i128)B.a*B.d-(i128)B.b*B.c;
    std::cerr<<"TRACE_VS B="<<B.a<<","<<B.b<<","<<B.c<<","<<B.d<<" det="<<(long long)det<<"\n";
    if(det!=1) throw std::runtime_error("INVALID_SL2_FRAGMENT");
  }
#endif
  for(M B:vs){
#ifdef BSD389_C01_PROFILE
    C01P.fragments++; C01P.rep_lookups++;
    C01P.exact_B[mkey(B)]++; C01P.mod389_B[modkey(B,N)]++; C01P.modP_B[modkey(B,P)]++;
#endif
    int gi=keyrep[key(B)]; const Rep& R=reps[gi]; M g=R.g; M H=mm(B,inv1(g)); int j0=qidx(H); M ho=mm(H,inv1(ri(j0))); i64 a=md(ho.a),b=md(ho.b); i64 qo=md(-a*b
#ifdef BSD389_EFFECTIVE
    -kappa
#endif
    ),ro=md(a*a); int sg=(i64)sign*w%P;
    if(R.gen>=0){int slot=R.gen*(P+1)+j0;out.add(slot,qo,ro,sg);
#ifdef BSD389_C01_PROFILE
      C01P.coefficient_adds++;
#endif
      continue;}
    for(const Term&t:R.rel){
#ifdef BSD389_C01_PROFILE
      C01P.relation_terms++;
#endif
      M ai=inv1(t.A);M X=mm(ri(j0),ai);int j1=qidx(X);M hi=mm(X,inv1(ri(j1)));i64 aa=md(hi.a),bb=md(hi.b);i64 qi=md(-aa*bb),rii=md(aa*aa);i64 x=md((i64)t.coeff*(qo+ro*qi)),y=md((i64)t.coeff*ro*rii);int base_gen=reps[t.r].gen;if(base_gen<0)throw std::runtime_error("relation term not generator");int slot=base_gen*(P+1)+j1;out.add(slot,x,y,sg);
#ifdef BSD389_C01_PROFILE
      C01P.coefficient_adds++;
#endif
    }
  }
}
static void contrib(int a,int b,const std::vector<Rep>& reps,const std::vector<int>& keyrep,Acc& out){
#ifdef BSD389_C01_PROFILE
  C01P.contrib_calls++;
#endif
  i64 x=a+(i64)P*b; i64 ferm=((mpow(a,P-1,P2)-1)/P)%P; i64 ia=inv(a,P); i64 u=md((i128)b*ia-ferm);i64 w=md((i128)ia*md(2*u-1));path(x,P2,-1,w,reps,keyrep,out
#ifdef BSD389_EFFECTIVE
  ,kappa_ab(a,b)
#endif
  );}
static bj::value load(const std::string&f){std::ifstream in(f);std::string s((std::istreambuf_iterator<char>(in)),{});return bj::parse(s);}
int main(int argc,char**argv){try{auto root=load(argc>1?argv[1]:"/home/user/bsd389_tame_relation_export_p16231.json");auto& o=root.as_object();auto rr=o["rinf"].as_array();RINF={rr[0].as_int64(),rr[1].as_int64(),rr[2].as_int64(),rr[3].as_int64()};std::vector<Rep> reps;std::vector<int> keyrep(N+1);for(auto&v:o["key_to_rep"].as_object())keyrep[std::stoi(std::string(v.key()))]=v.value().as_int64();for(auto&v:o["reps"].as_array()){auto&z=v.as_object();auto ar=z["matrix"].as_array();M g{ar[0].as_int64(),ar[1].as_int64(),ar[2].as_int64(),ar[3].as_int64()};Rep R{g,(int)z["generator"].as_int64(),{}};for(auto&tv:z["relations"].as_array()){auto&t=tv.as_object();auto aa=t["A"].as_array();R.rel.push_back({(int)t["coeff"].as_int64(),(int)t["r"].as_int64(),{aa[0].as_int64(),aa[1].as_int64(),aa[2].as_int64(),aa[3].as_int64()}});}reps.push_back(R);}int n=argc>2?std::stoi(argv[2]):10000;Acc out;std::ofstream pf;if(argc>4)pf.open(argv[4]);auto t0=std::chrono::steady_clock::now();for(int k=0;k<n;k++){int a,b;if(n==100){a=1+k/10;b=k%10;}else{a=1+(k%(P-1));b=(k/(P-1))%P;}if(argc>4){Acc tmp;contrib(a,b,reps,keyrep,tmp);for(i64 i=0;i<SLOTS;i++)if(tmp.c0[i]||tmp.c1[i])pf<<a<<" "<<b<<" "<<i<<" "<<tmp.c0[i]<<" "<<tmp.c1[i]<<"\n";for(i64 i=0;i<SLOTS;i++){out.c0[i]=md(out.c0[i]+tmp.c0[i]);out.c1[i]=md(out.c1[i]+tmp.c1[i]);}}else contrib(a,b,reps,keyrep,out);}auto t1=std::chrono::steady_clock::now();double sec=std::chrono::duration<double>(t1-t0).count();size_t n0=0,n1=0;for(i64 x:out.c0)n0+=x!=0;for(i64 x:out.c1)n1+=x!=0;std::cout<<"terms="<<n<<" seconds="<<sec<<" rate="<<n/sec<<" support_C0="<<n0<<" support_C1="<<n1<<"\n";if(argc>3){std::ofstream f(argv[3]);for(i64 i=0;i<SLOTS;i++)if(out.c0[i]||out.c1[i])f<<i<<" "<<out.c0[i]<<" "<<out.c1[i]<<"\n";}}catch(std::exception&e){std::cerr<<"ERROR "<<e.what()<<"\n";return 2;}}
