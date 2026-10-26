// Independent scalar J evaluator for E=389a1 at p=16231.
// THIS IS NOT THE ORIGINAL V11 PRODUCER. No C01 sparse accumulators,
// no historical V19 output/chunks/checkpoints, no Boost or Sage API.
// It uses the independent V65 eclib Hecke table and the already separately
// audited 390-representative Manin/Shapiro relations.
//
// The reference terminal V65 dual-moment exact NTT/CRT code is reused
// solely to form the 67*16232 basis-moment lookup table. The outer
// 263,429,130-pair summation, Manin resolution, and scalar-contraction
// algorithm are new and independent of the V11/V19 producer.
//
// Compile from repo root:
//   g++ -O2 -std=c++17 -Wall -Wextra verification/independent_c01_scalar_J.cpp -o /tmp/bsd389_independent_J
//
// Input is provided via SHA-pinned standard-library-only JSON->stream
// exporter, identical input format as c01_all_shapiro_transports_noboost.
//   python verification/export_shapiro_transport_stream.py ORIGINAL.json |
//      /tmp/bsd389_independent_J TABLE.bin START END CHECKPOINT.txt
//
// For full corpus START=0 END=263429130 and checkpoint is fixed path.
// The checkpoint is atomically replaced every 1,000,000 pairs. Same
// command resumes from last saved pair if interrupted. No full result
// is claimed before the actual independent run prints FULL_PASS.

#define main bsd389_v65_unused_main
#include "../historical/v65/v65_independent_terminal_ntt.cpp"
#undef main

#include <array>
#include <cstdio>
#include <filesystem>
#include <limits>
#include <sstream>

using Wide = __int128_t;
static constexpr i64 P2=i64(P)*P;
static constexpr i64 P3=P2*P;
static constexpr i64 TOTAL=i64(P)*(P-1);
static constexpr int NR=390, RELS=2012;
static constexpr i64 STEP=1000000;

struct Mat { i64 a,b,c,d; };
struct Rel { int e, target; Mat A; };
struct Row { Mat g; int generator; std::vector<Rel> rel; };

static i64 field(Wide x,i64 p=P){i64 v=i64(x%p);return v<0?v+p:v;}
static void ensure(bool cond, const std::string& message) {
    if(!cond)throw std::runtime_error(message);
}
static Mat matexact_inverse(const Mat& a){return {a.d,-a.b,-a.c,a.a};}
static Mat matmulmod(const Mat& a, const Mat& b) {
    return {
        field(Wide(a.a)*b.a+Wide(a.b)*b.c),
        field(Wide(a.a)*b.b+Wide(a.b)*b.d),
        field(Wide(a.c)*b.a+Wide(a.d)*b.c),
        field(Wide(a.c)*b.b+Wide(a.d)*b.d)
    };
}
static bool detone(const Mat& x){
    return Wide(x.a)*x.d-Wide(x.b)*x.c==1;
}
static i64 powmod(i64 a,i64 k,i64 mod) {
    i64 y=1;
    for(;k;k>>=1,a=i64(Wide(a)*a%mod))
        if(k&1)y=i64(Wide(y)*a%mod);
    return y;
}
static void require_tag(const char* tag) {
    std::string value;
    ensure(bool(std::cin>>value), std::string("stream missing tag ")+tag);
    ensure(value==tag, std::string("stream tag mismatch: ")+value);
}
static std::vector<Row> read_original_export(Mat& rinf) {
    require_tag("BSD389_SHAPIRO_V1");
    i64 level,p;
    int reps,gens,terms;
    ensure(bool(std::cin>>level>>p>>reps>>gens>>terms),"bad export header");
    ensure(level==N&&p==P&&reps==NR&&gens==NG&&terms==RELS,
           "bad relation export dimensions");
    require_tag("RINF");
    ensure(bool(std::cin>>rinf.a>>rinf.b>>rinf.c>>rinf.d),
           "missing infinity representative");
    ensure(detone(rinf)&&rinf.c%N==0&&field(rinf.d)==0,
           "invalid infinity representative");
    std::vector<Row> data(NR);
    int seen=0;
    for(int i=0;i<NR;++i) {
        require_tag("REP");
        int id,len;
        Row& row=data[i];
        ensure(bool(std::cin>>id>>row.g.a>>row.g.b>>row.g.c>>
                         row.g.d>>row.generator>>len),"bad representative");
        ensure(id==i&&detone(row.g)&&len>=0&&len<=RELS,
               "bad representative metadata");
        ensure(row.generator>=-1&&row.generator<NG,"bad generator label");
        for(int k=0;k<len;++k) {
            require_tag("TERM");
            int owner;
            Rel t{};
            ensure(bool(std::cin>>owner>>t.e>>t.target>>t.A.a>>
                t.A.b>>t.A.c>>t.A.d),"bad relation entry");
            ensure(owner==i&&(t.e==1||t.e==-1)&&t.target>=0&&
                   t.target<NR&&detone(t.A)&&t.A.c%N==0,
                   "malformed Gamma0(N) relation");
            row.rel.push_back(t);
            ++seen;
        }
    }
    std::string excess;
    ensure(!(std::cin>>excess),"unexpected export trailing token");
    ensure(seen==RELS,"wrong number of relations");
    for(const Row& row:data)
        for(const Rel& t:row.rel)
            ensure(data[t.target].generator>=0,
                   "relation target is not a generator");
    return data;
}
static std::vector<i64> modular_inverses(int n) {
    std::vector<i64> invs(n,0);
    invs[1]=1;
    for(int x=2;x<n;++x)
        invs[x]=field(-Wide(n/x)*invs[n%x],n);
    return invs;
}
static std::vector<Mat> shapiro_reps(const Mat& infinity) {
    std::vector<Mat> r(P+1);
    for(int j=0;j<P;++j)r[j]={1,0,i64(N)*j,1};
    r[P]=infinity;
    return r;
}
static int manin_key(const Mat& x,const std::vector<i64>& invN) {
    i64 c=field(x.c,N),d=field(x.d,N);
    return d?int(field(Wide(c)*invN[d],N)):int(N);
}
static int shapiro_key(const Mat& x,const std::vector<i64>& invP,
                       i64 inv_N_modP) {
    i64 c=field(x.c),d=field(x.d);
    return d?int(field(Wide(c)*invP[d]*inv_N_modP)):P;
}
static std::vector<int> key_map(const std::vector<Row>& rows,
                                const std::vector<i64>& invN) {
    std::vector<int> out(N+1,-1);
    std::vector<int> gen(NG,0);
    for(int i=0;i<NR;++i) {
        int k=manin_key(rows[i].g,invN);
        ensure(out[k]==-1,"duplicate projective Manin representative");
        out[k]=i;
        if(rows[i].generator>=0) ++gen[rows[i].generator];
    }
    for(int j:out) ensure(j>=0,"missing P1(Z/389) representative");
    for(int c:gen) ensure(c==1,"duplicated/missing Manin generator");
    return out;
}
struct Moments {
    std::vector<std::uint16_t> m0,m1;
};

// Construct ALL 67*16232 basis moments from the independently
// Sage/eclib-computed V65 table, using V65's independent NTT/CRT code.
// No C01 sparse coefficients, original producer or V19 state is read.
static Moments build_basis_moments(const std::string& filename) {
    auto table=bytes(filename);
    ensure(table.size()==20+std::size_t(NG)*(P+2)*2,
           "V65 reference table size mismatch");
    ensure(std::string(table.begin(),table.begin()+8)=="BSD65F01",
           "V65 reference table magic mismatch");
    ensure(le32(table,8)==P&&le32(table,12)==N&&
           le32(table,16)==NG,"wrong V65 table dimensions");
    Moments out{std::vector<std::uint16_t>(SLOTS),
                std::vector<std::uint16_t>(SLOTS)};
    const int alpha_inv=inverse(128,P),invN=inverse(N,P);
    ensure(alpha_inv==5199,"wrong alpha_inv mod p");
    const auto inv=modular_inverses(P);
    std::vector<int> twist(P,0);
    for(int k=1;k<P;++k)
        twist[k]=md(i64(invN)*inv[P-k]);
    const NTT transform1(Q1,twist),transform2(Q2,twist);

    for(int g=0;g<NG;++g) {
        std::size_t base=20+std::size_t(g)*(P+2)*2;
        int fG=le16(table,base),fP=le16(table,base+2);
        std::vector<int> fs(P),shifted(P,0);
        ensure(fG<P&&fP<P,"V65 basis values invalid");
        i64 hecke=fP;
        for(int t=0;t<P;++t){
            fs[t]=le16(table,base+4+2*t);
            ensure(fs[t]<P,"invalid V65 beta symbol");
            hecke+=fs[t];
        }
        ensure(md(hecke-128*fG)==0,"V65 eclib Hecke check failed");
        shifted[0]=fP;
        for(int y=1;y<P;++y)
            shifted[y]=fs[md(i64(invN)*inv[y])];
        auto cyc=cyclic(shifted,transform1,transform2);

        int mspecial=0;
        for(int t=0;t<P;++t) {
            int denom=md(-40+i64(N)*t);
            int s=denom?md(-1669*inv[denom]):P;
            mspecial=md(mspecial+i64(t)*(s==P?fP:fs[s]));
        }
        mspecial=md(i64(alpha_inv)*mspecial);

        // Rigorous independent direct correlations on selected indices.
        for(int j:{0,1,71,P-1}) {
            i64 expected=0;
            for(int x=1;x<P;++x)
                expected+=i64(md(i64(invN)*inv[x]))*shifted[(x+j)%P];
            ensure(expected==cyc[j],"V65 exact-CRT correlation mismatch");
        }

        for(int j=0;j<=P;++j) {
            int sel=j==0?fP:(j==P?fs[0]:fs[md(i64(invN)*inv[j])]);
            i64 v0=md(fG-i64(alpha_inv)*sel);
            i64 v1=j==P?mspecial:md(i64(alpha_inv)*md(cyc[j]));
            std::size_t slot=std::size_t(g)*(P+1)+j;
            out.m0[slot]=std::uint16_t(v0);
            out.m1[slot]=std::uint16_t(v1);
        }
        if((g+1)%10==0||g+1==NG)
            std::cout<<"INDEPENDENT_SCALAR_BASIS_PROGRESS "<<g+1
                     <<"/"<<NG<<"\n";
    }
    std::cout<<"INDEPENDENT_SCALAR_ALL_BASIS_MOMENTS_PASS "<<SLOTS<<"\n";
    return out;
}

// Pre-evaluate the full 390 x (p+1) Manin-representative basis under
// all Shapiro cosets. This is the DUAL calculation: reduce symbolic
// moments once, rather than V11's repeated pushforward into sparse C0/C1.
static Moments build_all_manin_moments(
    const std::vector<Row>& rows,const std::vector<Mat>& rj,
    const std::vector<i64>& invP,i64 inv_N_modP,
    const Moments& basis)
{
    Moments out{std::vector<std::uint16_t>(std::size_t(NR)*(P+1)),
                std::vector<std::uint16_t>(std::size_t(NR)*(P+1))};
    unsigned long long expanded=0;
    for(int i=0;i<NR;++i) {
        const Row& rep=rows[i];
        for(int j=0;j<=P;++j) {
            std::size_t slot=std::size_t(i)*(P+1)+j;
            if(rep.generator>=0) {
                std::size_t z=std::size_t(rep.generator)*(P+1)+j;
                out.m0[slot]=basis.m0[z];
                out.m1[slot]=basis.m1[z];
            } else {
                i64 m0=0,m1=0;
                for(const Rel& rel:rep.rel) {
                    Mat X=matmulmod(rj[j],matexact_inverse(rel.A));
                    int k=shapiro_key(X,invP,inv_N_modP);
                    Mat h=matmulmod(X,matexact_inverse(rj[k]));
                    i64 q=field(-Wide(h.a)*h.b),r=field(Wide(h.a)*h.a);
                    int gen=rows[rel.target].generator;
                    std::size_t z=std::size_t(gen)*(P+1)+k;
                    i64 z0=basis.m0[z],z1=basis.m1[z];
                    m0=field(Wide(m0)+Wide(rel.e)*z0);
                    m1=field(Wide(m1)+Wide(rel.e)*
                              field(Wide(q)*z0+Wide(r)*z1));
                    ++expanded;
                }
                out.m0[slot]=std::uint16_t(m0);
                out.m1[slot]=std::uint16_t(m1);
            }
        }
    }
    ensure(expanded>0,"empty Manin coset relations");
    std::cout<<"INDEPENDENT_SCALAR_ALL_390_REP_MOMENTS_PASS"
             <<" slots="<<out.m0.size()
             <<" expanded_relation_terms="<<expanded<<"\n";
    return out;
}

struct Direct {
    const std::vector<Row>& reps;
    const std::vector<int>& keys;
    const std::vector<Mat>& shapiro;
    const std::vector<i64>& invP,invN;
    i64 inv_N_modP;
    const Moments& all;
    std::vector<i64> fermat,inv_a,teich,gammas;

    Direct(const std::vector<Row>& reps0,
           const std::vector<int>& keys0,
           const std::vector<Mat>& shapiro0,
           const std::vector<i64>& invP0,
           const std::vector<i64>& invN0,i64 inverseN,
           const Moments& vals)
        :reps(reps0),keys(keys0),shapiro(shapiro0),
         invP(invP0),invN(invN0),inv_N_modP(inverseN),all(vals),
         fermat(P,0),inv_a(P,0),teich(P,0),gammas(P,0)
    {
        gammas[0]=1;
        for(int u=1;u<P;++u)
            gammas[u]=i64(Wide(gammas[u-1])*(1+P)%P3);
        for(int a=1;a<P;++a) {
            inv_a[a]=invP[a];
            fermat[a]=((powmod(a,P-1,P2)-1)/P)%P;
            teich[a]=powmod(a,P2,P3);
            ensure(powmod(teich[a],P-1,P3)==1,
                   "Teichmuller root check failed");
        }
        std::cout<<"INDEPENDENT_SCALAR_TEICH_TABLE_PASS "<<P-1<<"\n";
    }
    // Directly evaluate both functional moments on one oriented SL2
    // continued-fraction fragment, without constructing a sparse C01 row.
    void fragment(const Mat& B,i64& m0,i64& m1) const {
        int i=keys[manin_key(B,invN)];
        Mat H=matmulmod(B,matexact_inverse(reps[i].g));
        int j=shapiro_key(H,invP,inv_N_modP);
        Mat h=matmulmod(H,matexact_inverse(shapiro[j]));
        i64 q=field(-Wide(h.a)*h.b),r=field(Wide(h.a)*h.a);
        std::size_t slot=std::size_t(i)*(P+1)+j;
        m0=field(Wide(m0)+all.m0[slot]);
        m1=field(Wide(m1)+Wide(q)*all.m0[slot]+
                 Wide(r)*all.m1[slot]);
    }
    int pair(i64 id) const {
        int a=int(1+id/P),b=int(id%P);
        const i64 x=a+i64(P)*b;
        i64 u=field(Wide(b)*inv_a[a]-fermat[a]);
        i64 w=field(Wide(inv_a[a])*(2*u-1));
        i64 base=i64(Wide(teich[a])*gammas[u]%P3);
        i64 diff=field(base-x,P3);
        ensure(diff%P2==0,"kappa divisibility");
        i64 kap=diff/P2;

        std::array<i64,64> h{},k{};
        i64 r=x,s=P2,hm2=0,hm1=1,km2=1,km1=0;
        int len=0;
        while(s) {
            ensure(len<64,"Euclidean path exceeds 64 steps");
            i64 q=r/s;
            i64 hn=q*hm1+hm2,kn=q*km1+km2;
            h[len]=hn;k[len]=kn;++len;
            hm2=hm1;hm1=hn;km2=km1;km1=kn;
            i64 old=s;
            s=r-q*s;r=old;
        }
        ensure(len>0 && h[len-1]*P2==k[len-1]*x,
               "continued-fraction endpoint mismatch");
        i64 m0=0,m1=0;
        fragment({1,h[0],0,k[0]},m0,m1);
        for(int j=0;j+1<len;++j) {
            i64 sg=(j%2)?1:-1;
            fragment({sg*h[j],h[j+1],sg*k[j],k[j+1]},m0,m1);
        }
        return int(field(-Wide(w)*field(Wide(m1)-Wide(kap)*m0)));
    }
};

static void persist(const std::string& checkpoint,i64 begin,
                    i64 stop,i64 next,i64 sum) {
    std::string tmp=checkpoint+".tmp";
    {
        std::ofstream f(tmp,std::ios::trunc);
        ensure(bool(f),"cannot write checkpoint "+tmp);
        f<<"BSD389_INDEPENDENT_SCALAR_J_V1 "
         <<begin<<" "<<stop<<" "<<next<<" "<<sum<<"\n";
        f.flush();
        ensure(bool(f),"checkpoint write failure");
    }
    std::filesystem::rename(tmp,checkpoint);
}
static std::pair<i64,i64> recover(const std::string& checkpoint,
                                  i64 begin,i64 stop){
    if(!std::filesystem::exists(checkpoint))return {begin,0};
    std::ifstream f(checkpoint);
    std::string magic,extra;
    i64 a=0,b=0,next=0,sum=0;
    ensure(bool(f>>magic>>a>>b>>next>>sum),"invalid checkpoint");
    ensure(magic=="BSD389_INDEPENDENT_SCALAR_J_V1"&&a==begin&&b==stop
           &&begin<=next&&next<=stop&&0<=sum&&sum<P,
           "checkpoint interval/values mismatch");
    ensure(!(f>>extra),"checkpoint trailing token");
    std::cout<<"INDEPENDENT_SCALAR_RESTART_PASS"
             <<" next="<<next<<" J_partial="<<sum<<"\n";
    return {next,sum};
}
int main(int argc,char** argv) {
    try {
        ensure(argc==5,
           "usage: BINARY V65_TABLE.bin START_ID END_ID CHECKPOINT.txt < pinned_original_stream");
        std::string table_path=argv[1],checkpoint=argv[4];
        auto integer=[](const std::string& s) {
            std::size_t pos=0;
            i64 v=std::stoll(s,&pos);
            ensure(pos==s.size(),"invalid interval integer");
            return v;
        };
        i64 lo=integer(argv[2]),hi=integer(argv[3]);
        ensure(0<=lo&&lo<hi&&hi<=TOTAL,"invalid global pair interval");
        Mat infinity{};
        const auto reps=read_original_export(infinity);
        const auto ip=modular_inverses(P),in=modular_inverses(N);
        const i64 invN=ip[N];
        const auto keys=key_map(reps,in);
        const auto shapiro=shapiro_reps(infinity);
        const auto basis=build_basis_moments(table_path);
        const auto all=build_all_manin_moments(reps,shapiro,ip,invN,basis);
        const Direct direct(reps,keys,shapiro,ip,in,invN,all);
        auto [start,sum]=recover(checkpoint,lo,hi);
        for(i64 id=start;id<hi;++id) {
            int v=direct.pair(id);
            if(id==0 || id==i64(P)+3) {
                int expected=id==0?2316:11725;
                ensure(v==expected,
                       "independent scalar disagrees with direct Sage local oracle");
                std::cout<<"INDEPENDENT_SCALAR_LOCAL_ORACLE_PASS"
                         <<" id="<<id<<" J="<<v<<"\n";
            }
            sum=field(Wide(sum)+v);
            i64 next=id+1;
            if(next%STEP==0||next==hi) {
                persist(checkpoint,lo,hi,next,sum);
                std::cout<<"INDEPENDENT_SCALAR_CHECKPOINT_PASS next="
                         <<next<<" sum_mod_p="<<sum
                         <<" of="<<hi<<"\n"<<std::flush;
            }
        }
        std::cout<<"INDEPENDENT_SCALAR_INTERVAL_PASS"
                 <<" start="<<lo<<" end="<<hi
                 <<" J_mod_p="<<sum<<"\n";
        if(lo==0&&hi==TOTAL){
            if(sum==4486){
                std::cout<<"INDEPENDENT_SCALAR_GLOBAL_J_4486_PASS"
                         <<" pairs="<<TOTAL<<"\n";
            }else{
                std::cerr<<"INDEPENDENT_SCALAR_GLOBAL_J_MISMATCH"
                         <<" observed="<<sum<<" expected=4486\n";
                return 3;
            }
        }
        std::cout<<"BOUNDARY: new full scalar outer sum, independent of V11"
                 <<" producer/V19 chunks, but reuses pinned V65 eclib table"
                 <<" and original independently audited Manin export.\n";
        return 0;
    }catch(const std::exception& e){
        std::cerr<<"INDEPENDENT_SCALAR_J_FAIL "<<e.what()<<"\n";
        return 2;
    }
}
