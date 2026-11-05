// Exact arbitrary-precision 4x4 Gross norm-19 CM transition core, via ctypes.
// Only applies Sage-certified quaternionic edges. Stops on any cache miss.
#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <cstdint>
#include <sstream>
#include <string>
#include <unordered_map>
#include <algorithm>
using boost::multiprecision::cpp_int;
using Arr=std::array<cpp_int,4>;
struct Edge{int dest;cpp_int den;std::array<Arr,4> mat;};
static std::unordered_map<uint32_t,Edge> edges;
static const int p=16231,m=263445361,w=138112843,s=10816;
static const int V[33]={0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,
                       0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0};
static const uint64_t H=87809710ULL;
static struct{
  uint64_t n=0,hits=0,misses=0;
  int a=1,j=9;
  Arr z;
  std::array<int,3> mom{};
  std::array<uint64_t,33> hist{};
  cpp_int maxcoord=0;
}st;
static std::string msg,buffer;
static int pos19(const cpp_int& x){
  int r=(x%19).convert_to<int>();
  return r<0?r+19:r;
}
static uint32_t key(int j,const Arr& z){
  uint32_t out=(uint32_t)j;
  for(auto &x:z)out=out*19+(uint32_t)pos19(x);
  return out;
}
static cpp_int absq(cpp_int x){return x<0?-x:x;}
extern "C" int bsd_clear(){
  edges.clear();st={};msg.clear();return 0;
}
extern "C" int bsd_register_edge(const char* line){
  if(!line){msg="null edge";return -1;}
  std::istringstream in(line);
  int j;Arr residues;Edge edge;
  if(!(in>>j)||j<0||j>=33){msg="invalid source class";return -2;}
  for(auto &x:residues){
    if(!(in>>x)||x<0||x>=19){msg="invalid residue";return -3;}
  }
  if(!(in>>edge.dest)||edge.dest<0||edge.dest>=33||
     !(in>>edge.den)||edge.den<=0){msg="invalid destination or denominator";return -4;}
  for(auto &row:edge.mat)
    for(auto &x:row)
      if(!(in>>x)){msg="invalid matrix element";return -5;}
  uint32_t k=key(j,residues);
  if(edges.count(k)){msg="repeated edge key";return -6;}
  if(edges.size()>=12540){msg="maximum 12540 keys exceeded";return -7;}
  edges.emplace(k,std::move(edge));return 0;
}
extern "C" int bsd_set_state(const char* line){
  if(!line){msg="null state";return -1;}
  std::istringstream in(line);
  if(!(in>>st.n>>st.a>>st.j)||st.n>=H||
     st.a<=0||st.a>=m||st.j<0||st.j>=33){msg="invalid header";return -2;}
  for(auto &x:st.z)if(!(in>>x)){msg="invalid q coordinate";return -3;}
  for(auto &x:st.mom)if(!(in>>x)||x<0||x>=p){msg="invalid moment";return -4;}
  uint64_t total=0;
  for(auto &x:st.hist){if(!(in>>x)){msg="invalid class histogram";return -5;}total+=x;}
  if(total!=st.n+1){msg="histogram does not match coverage";return -6;}
  if(!(in>>st.maxcoord)){msg="invalid max coordinate";return -7;}
  st.hits=st.misses=0;return 0;
}
extern "C" int bsd_run_until(uint64_t target){
  if(target>=H){msg="target outside finite ring-class cycle";return -1;}
  if(target<st.n){msg="cannot rewind";return -2;}
  while(st.n<target){
    auto found=edges.find(key(st.j,st.z));
    if(found==edges.end())return 1;  // Python/Sage builds the absent edge.
    const Edge &e=found->second;Arr next;
    for(unsigned r=0;r<4;++r){
      cpp_int val=0;
      for(unsigned c=0;c<4;++c)val+=e.mat[r][c]*st.z[c];
      if(val%e.den!=0){msg="nonintegral exact matrix quotient";return -3;}
      next[r]=val/e.den;
    }
    st.z=std::move(next);
    st.j=e.dest;
    ++st.n;
    st.a=(int)(((uint64_t)st.a*(uint64_t)w)%(uint64_t)m);
    uint64_t i=((st.n%(uint64_t)p)*(uint64_t)s)%(uint64_t)p;
    int v=V[st.j];
    int64_t weights[3]={1,(int64_t)i,(int64_t)(i*(i-1)/2)};
    for(int a=0;a<3;++a){
      int64_t x=((int64_t)st.mom[a]+weights[a]*v)%p;
      st.mom[a]=(int)(x<0?x+p:x);
    }
    ++st.hist[st.j];
    for(auto &x:st.z)st.maxcoord=std::max(st.maxcoord,absq(x));
    ++st.hits;
  }
  return 0;
}
extern "C" const char* bsd_state_text(){
  std::ostringstream out;
  out<<st.n<<' '<<st.a<<' '<<st.j;
  for(auto &x:st.z)out<<' '<<x;
  for(auto &x:st.mom)out<<' '<<x;
  for(auto &x:st.hist)out<<' '<<x;
  out<<' '<<st.maxcoord<<' '<<st.hits<<' '<<st.misses;
  buffer=out.str();return buffer.c_str();
}
extern "C" const char* bsd_missing_key(){
  std::ostringstream out;out<<st.j;
  for(auto &x:st.z)out<<' '<<pos19(x);
  buffer=out.str();return buffer.c_str();
}
extern "C" int bsd_cache_size(){return (int)edges.size();}
extern "C" const char* bsd_error(){return msg.c_str();}
