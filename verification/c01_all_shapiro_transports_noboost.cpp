// SHA-pinned stream produced by export_shapiro_transport_stream.py.
// Exhaustive independent EXACT-Z checker of 2012*16232 Manin/Shapiro
// relations. C++17 standard library only: NO Boost, NO Sage.
//
// g++ -O2 -std=c++17 -Wall -Wextra \
//     verification/c01_all_shapiro_transports_noboost.cpp \
//     -o /tmp/bsd389_shapiro_noboost
//
// python verification/export_shapiro_transport_stream.py ORIGINAL.json |
//     /tmp/bsd389_shapiro_noboost --pilot
//
// python verification/export_shapiro_transport_stream.py ORIGINAL.json |
//     /tmp/bsd389_shapiro_noboost --full

#include <algorithm>
#include <array>
#include <cstdint>
#include <exception>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

using Int = std::int64_t;
using Wide = __int128_t;
constexpr Int N=389, P=16231, Q=N*P;
constexpr int NREPS=390, NGEN=67, NTERMS=2012;

struct M { Int a,b,c,d; };
struct Term { int coeff, r; M A; };
struct Rep { M g; int gen; std::vector<Term> rel; };

[[noreturn]] static void fail(const std::string& s) {
    throw std::runtime_error(s);
}
static void demand(bool ok, const std::string& s) {
    if(!ok) fail(s);
}
static Int mod(Wide a, Int p=P) {
    Int v=Int(a%p);
    return v<0?v+p:v;
}
static Int inv(Int a, Int p) {
    Int t=0,nt=1,r=p,nr=mod(a,p);
    while(nr) {
        Int k=r/nr;
        Int tmp=t-k*nt; t=nt; nt=tmp;
        tmp=r-k*nr; r=nr; nr=tmp;
    }
    demand(r==1,"noninvertible modular denominator");
    return mod(t,p);
}
static Int checked(Wide v) {
    demand(v>=std::numeric_limits<Int>::min() &&
           v<=std::numeric_limits<Int>::max(),
           "exact matrix multiplication would overflow int64");
    return Int(v);
}
static M product(const M& x, const M& y) {
    return {
        checked(Wide(x.a)*y.a+Wide(x.b)*y.c),
        checked(Wide(x.a)*y.b+Wide(x.b)*y.d),
        checked(Wide(x.c)*y.a+Wide(x.d)*y.c),
        checked(Wide(x.c)*y.b+Wide(x.d)*y.d)
    };
}
static M product_mod(const M& x, const M& y) {
    return {
        mod(Wide(x.a)*y.a+Wide(x.b)*y.c),
        mod(Wide(x.a)*y.b+Wide(x.b)*y.d),
        mod(Wide(x.c)*y.a+Wide(x.d)*y.c),
        mod(Wide(x.c)*y.b+Wide(x.d)*y.d)
    };
}
static M inverse1(const M& x) { return {x.d,-x.b,-x.c,x.a}; }
static bool det1(const M& x) {
    return Wide(x.a)*x.d-Wide(x.b)*x.c==1;
}
static Int q(const M& h) { return mod(-Wide(mod(h.a))*mod(h.b)); }
static Int r(const M& h) { return mod(Wide(mod(h.a))*mod(h.a)); }
static int key(const M& m, const std::vector<Int>& invN) {
    Int dd=mod(m.d,N),cc=mod(m.c,N);
    return dd==0?int(N):int(mod(Wide(cc)*invN[dd],N));
}
static int qidx(const M& x, const std::vector<Int>& invP, Int inv_N_modP) {
    Int d=mod(x.d),c=mod(x.c);
    return d==0?int(P):int(mod(Wide(c)*invP[d]*inv_N_modP));
}
static std::uint64_t mix64(std::uint64_t h,std::uint64_t a) {
    return h^(a+UINT64_C(0x9e3779b97f4a7c15)+(h<<6)+(h>>2));
}
static void read_tag(const char* expected) {
    std::string token;
    demand(bool(std::cin>>token),std::string("missing stream token ")+expected);
    demand(token==expected,
           std::string("unexpected stream tag: expected ")+expected+", got "+token);
}

int main(int argc, char** argv) {
    try {
        demand(argc==2,"usage: CHECKER --pilot|--full < canonical.stream");
        std::string mode=argv[1];
        demand(mode=="--pilot"||mode=="--full","invalid mode");

        read_tag("BSD389_SHAPIRO_V1");
        Int n,p; int numReps,numGen,numTerms;
        demand(bool(std::cin>>n>>p>>numReps>>numGen>>numTerms),"bad header");
        demand(n==N && p==P && numReps==NREPS
               && numGen==NGEN && numTerms==NTERMS,"wrong input dimensions");
        read_tag("RINF");
        M infinity{};
        demand(bool(std::cin>>infinity.a>>infinity.b>>infinity.c>>infinity.d),
               "bad exceptional representative");
        demand(det1(infinity) && infinity.c%N==0 &&
               mod(infinity.d)==0,"exceptional representative not SL2/Gamma0(N)");

        std::vector<Rep> reps(numReps);
        int nterms=0;
        for(int i=0;i<numReps;++i) {
            read_tag("REP");
            int index,nrel;
            Rep& row=reps[i];
            demand(bool(std::cin>>index>>row.g.a>>row.g.b>>row.g.c
                        >>row.g.d>>row.gen>>nrel),"invalid rep record");
            demand(index==i && nrel>=0 && nrel<=NTERMS,
                   "bad rep index/relation count");
            demand(det1(row.g),"Manin P1 representative not in SL2(Z)");
            demand(row.gen>=-1 && row.gen<NGEN,"bad generator index");
            for(int z=0;z<nrel;++z) {
                read_tag("TERM");
                int owner; Term t{};
                demand(bool(std::cin>>owner>>t.coeff>>t.r
                            >>t.A.a>>t.A.b>>t.A.c>>t.A.d),"bad term record");
                demand(owner==i && (t.coeff==1 || t.coeff==-1) &&
                       t.r>=0 && t.r<NREPS,"bad relation coordinates");
                demand(det1(t.A) && t.A.c%N==0,"relation not in Gamma0(389)");
                row.rel.push_back(t);
                ++nterms;
            }
        }
        std::string trailing;
        demand(!(std::cin>>trailing),"unexpected tokens after relation export");
        demand(nterms==NTERMS,"not exactly 2012 input relation terms");

        std::vector<Int> invP(P,0), invN(N,0);
        for(Int a=1;a<P;++a)invP[a]=inv(a,P);
        for(Int a=1;a<N;++a)invN[a]=inv(a,N);
        const Int invNmodP=inv(N,P);
        std::vector<int> keys(N+1,-1);
        int ngen=0,nnon=0;
        for(int i=0;i<NREPS;++i) {
            int k=key(reps[i].g,invN);
            demand(k>=0 && k<=N && keys[k]==-1,"repeated projective key");
            keys[k]=i;
            if(reps[i].gen>=0)++ngen;else ++nnon;
        }
        demand(ngen==NGEN && nnon==NREPS-NGEN,"bad generator count");
        std::vector<int> labels(NGEN,0);
        for(const auto& rep:reps) {
            if(rep.gen>=0) ++labels[rep.gen];
            for(const auto& t:rep.rel)
                demand(reps[t.r].gen>=0,"relation target is not generator");
        }
        for(int count:labels)demand(count==1,"generator not unique");

        std::vector<M> shapiro(P+1);
        for(int j=0;j<P;++j)shapiro[j]={1,0,N*Int(j),1};
        shapiro[P]=infinity;

        // Explicit nontrivial Gamma0(Np) test matrix, unlike identity-only checks.
        demand(Q%2==1 && Q%3==2,"expected Q congruences failed");
        const M h0{2,1,Q,(Q+1)/2};
        const M h1{3,1,Q,(Q+1)/3};
        demand(det1(h0)&&det1(h1),"bad test matrices");
        const M composition=product(h0,h1);
        demand(mod(Wide(q(h0))+Wide(r(h0))*q(h1))==q(composition)
               &&mod(Wide(r(h0))*r(h1))==r(composition),
               "affine moment group law fails for test matrices");

        std::uint64_t checksum=UINT64_C(0x16231389facaade5);
        std::uint64_t transitions=0,inputInf=0,outputInf=0,bothInf=0;
        int max_j=mode=="--full"?int(P+1):11;
        for(int idx=0;idx<max_j;++idx) {
            const int j0=(mode=="--pilot"&&idx==10)?int(P):idx;
            const M& r0=shapiro[j0];
            demand(det1(r0),"Shapiro representative not determinant one");
            demand(qidx(r0,invP,invNmodP)==j0,"Shapiro qidx mismatch");
            for(int i=0;i<NREPS;++i) {
                for(const Term& t:reps[i].rel) {
                    // Product in Z, not mod p: must be SL2(Z) and Gamma0(Np).
                    const M X=product(r0,inverse1(t.A));
                    const int j1=qidx(X,invP,invNmodP);
                    demand(j1>=0 && j1<=P,"invalid new Shapiro class");
                    const M hi=product(X,inverse1(shapiro[j1]));
                    demand(det1(hi) && hi.c%Q==0,
                           "exact transported matrix outside Gamma0(Np)");

                    // Reproduce native C++ reduction order, independently.
                    const M native=product_mod(
                        product_mod(r0,inverse1(t.A)),
                        inverse1(shapiro[j1]));
                    demand(mod(hi.a)==native.a && mod(hi.b)==native.b &&
                           mod(hi.c)==native.c && mod(hi.d)==native.d,
                           "exact/native mod-p matrix mismatch");
                    const Int qi=q(native),ri=r(native);
                    const M composed=product_mod(h0,native);
                    demand(mod(Wide(q(h0))+Wide(r(h0))*qi)==q(composed)
                           && mod(Wide(r(h0))*ri)==r(composed),
                           "moment covariance composition mismatch");

                    checksum=mix64(checksum,std::uint64_t(j0));
                    checksum=mix64(checksum,std::uint64_t(i));
                    checksum=mix64(checksum,std::uint64_t(j1));
                    checksum=mix64(checksum,std::uint64_t(qi+P*ri));
                    ++transitions;
                    if(j0==P)++inputInf;
                    if(j1==P)++outputInf;
                    if(j0==P && j1==P)++bothInf;
                }
            }
            if(idx==9||idx==4095||idx==8191||idx==12287||idx==max_j-1)
                std::cout<<"C01_SHAPIRO_TRANSPORT_PROGRESS processed_classes="
                         <<idx+1<<" total_transitions="<<transitions<<"\n";
        }
        demand(transitions==std::uint64_t(nterms)*std::uint64_t(max_j),
               "wrong transition count");
        if(mode=="--pilot") {
            demand(inputInf==NTERMS,
                   "pilot did not actually test all exceptional input relations");
            std::cout<<"C01_ALL_COSETS_PILOT_PASS transitions="<<transitions
                     <<" exceptional_input="<<inputInf
                     <<" exceptional_output="<<outputInf
                     <<" checksum="<<checksum<<"\n";
        } else {
            demand(inputInf==NTERMS && outputInf==NTERMS,
                   "exceptional input/output cardinality mismatch");
            demand(transitions==32658784ULL,
                   "not all relation/coset transitions checked");
            std::cout<<"C01_ALL_32658784_SHAPIRO_TRANSPORTS_EXACT_PASS"
                     <<" transitions="<<transitions
                     <<" input_exceptional="<<inputInf
                     <<" output_exceptional="<<outputInf
                     <<" both_exceptional="<<bothInf
                     <<" checksum="<<checksum<<"\n";
        }
        std::cout<<"BOUNDARY: exact transported matrices and native mod-p"
                    " moment-law conformity; not a replay of all C01 pairs\n";
        return 0;
    } catch(const std::exception& e) {
        std::cerr<<"C01_SHAPIRO_STANDALONE_FAIL "<<e.what()<<"\n";
        return 2;
    }
}
