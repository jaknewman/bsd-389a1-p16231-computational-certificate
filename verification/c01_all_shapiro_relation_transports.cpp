// Independent exact-integral audit of ALL 2012*16232 relation/coset
// Shapiro transports for E=389a1, p=16231.
// Compiles against THE ARCHIVED ORIGINAL C01 loader/matrix implementation.
// No modular-symbol or 263m-pair evaluations.
//
// Compile from repository root:
// g++ -O2 -std=c++17 -DBSD389_EFFECTIVE -DBSD389_SPARSE_TOUCHED \
//   verification/c01_all_shapiro_relation_transports.cpp \
//   -o /tmp/bsd389_c01_all_shapiro_transports -lboost_json
//
// Run (pilot or full):
// /tmp/bsd389_c01_all_shapiro_transports \
//   historical/originals/bsd389_tame_relation_export_p16231.json --pilot
// /tmp/bsd389_c01_all_shapiro_transports \
//   historical/originals/bsd389_tame_relation_export_p16231.json --full
//
#include "../historical/originals/bsd389_c01_v11_loader.cpp"
#include <cstdint>
#include <limits>
#include <string>

using Wide = __int128_t;
static constexpr i64 Q = N*P;

static bool is_det_one(const M& m) {
    return ((Wide)m.a*m.d - (Wide)m.b*m.c) == 1;
}
static i64 narrow(Wide x) {
    if (x < std::numeric_limits<i64>::min()
            || x > std::numeric_limits<i64>::max()) {
        throw std::runtime_error("exact matrix overflow i64");
    }
    return (i64)x;
}
static M exactmul(const M& x, const M& y) {
    return {
        narrow((Wide)x.a*y.a+(Wide)x.b*y.c),
        narrow((Wide)x.a*y.b+(Wide)x.b*y.d),
        narrow((Wide)x.c*y.a+(Wide)x.d*y.c),
        narrow((Wide)x.c*y.b+(Wide)x.d*y.d)
    };
}
static void demand(bool ok, const std::string& msg) {
    if(!ok) throw std::runtime_error(msg);
}
static std::uint64_t mix64(std::uint64_t h, std::uint64_t a) {
    h ^= a + UINT64_C(0x9e3779b97f4a7c15) + (h<<6) + (h>>2);
    return h;
}
int main(int argc,char** argv) {
    try {
        demand(argc==3, "usage: BINARY EXPORT.json --pilot|--full");
        const std::string mode=argv[2];
        demand(mode=="--pilot"||mode=="--full","invalid mode");
        const i64 max_j=(mode=="--pilot")?10:P+1;

        std::vector<Rep> reps;
        std::vector<int> keyrep;
        v4_load_export(argv[1],reps,keyrep);
        demand(reps.size()==390,"390 Manin representatives expected");
        demand(is_det_one(RINF) && RINF.c%N==0 &&
               md(RINF.d,P)==0,"bad original exceptional representative");

        int terms=0, ngen=0, nnon=0;
        for(std::size_t i=0;i<reps.size();++i) {
            const auto& rep=reps[i];
            demand(is_det_one(rep.g),"non-SL2 representative");
            demand(key(rep.g)>=0 && keyrep[key(rep.g)]==(int)i,
                   "projective representative indexing");
            if(rep.gen>=0)++ngen; else ++nnon;
            for(const auto& t:rep.rel) {
                demand(t.coeff==1||t.coeff==-1,"unexpected relation weight");
                demand(is_det_one(t.A) && t.A.c%N==0,
                       "relation not in Gamma0(389)");
                demand(t.r>=0 && t.r<(int)reps.size() &&
                       reps[t.r].gen>=0,"relation target is not generator");
                ++terms;
            }
        }
        demand(terms==2012 && ngen==67 && nnon==323,
               "Manin relation structure mismatch");
        demand(Q%2==1 && Q%3==2,"nontrivial test matrix assumptions");
        const M h0{2,1,Q,(Q+1)/2};
        const M h1{3,1,Q,(Q+1)/3};
        demand(is_det_one(h0) && is_det_one(h1) &&
               h0.c%Q==0 && h1.c%Q==0,"test h not in Gamma0(Np)");

        // Group law for nontrivial 2x2 matrices (q,r), by exact product.
        const M group_prod=exactmul(h0,h1);
        i64 q0=md(-(Wide)md(h0.a)*md(h0.b)),r0=md((Wide)md(h0.a)*md(h0.a));
        i64 q1=md(-(Wide)md(h1.a)*md(h1.b)),r1=md((Wide)md(h1.a)*md(h1.a));
        demand(md(q0+r0*q1)==
                   md(-(Wide)md(group_prod.a)*md(group_prod.b)) &&
               md(r0*r1)==md((Wide)md(group_prod.a)*md(group_prod.a)),
               "moment affine-composition law failure");

        unsigned long long transitions=0, input_inf=0, output_inf=0;
        unsigned long long both_inf=0;
        std::uint64_t chk=UINT64_C(0x16231389facaade5);

        // Exact relation matrices: compute in Z, not just modulo p.
        for(int j0=0;j0<max_j;++j0) {
            const M rj=ri(j0);
            demand(is_det_one(rj),"bad Shapiro representative");
            demand(qidx(rj)==j0,"original qidx(ri(j)) != j");
            for(std::size_t i=0;i<reps.size();++i) {
                for(const Term& t:reps[i].rel) {
                    const M X=exactmul(rj,inv1(t.A));
                    const int j1=qidx(X);
                    demand(j1>=0 && j1<=P,"qidx not in P1(Fp)");
                    const M hi=exactmul(X,inv1(ri(j1)));
                    demand(is_det_one(hi) && hi.c%Q==0,
                           "non-Gamma0(389p) exact relation transport");

                    // The original native C01 C++ obtains hi by mod-p
                    // products before computing the 2-moment q/r.
                    const M Hreduced=mm(mm(rj,inv1(t.A)),inv1(ri(j1)));
                    demand(md(hi.a)==Hreduced.a &&
                           md(hi.b)==Hreduced.b &&
                           md(hi.c)==Hreduced.c &&
                           md(hi.d)==Hreduced.d,
                           "native mod-p vs exact-Z transport mismatch");
                    i64 aa=md(hi.a),bb=md(hi.b);
                    i64 qi=md(-(Wide)aa*bb),rii=md((Wide)aa*aa);
                    demand(qi==md(-(Wide)Hreduced.a*Hreduced.b)
                           && rii==md((Wide)Hreduced.a*Hreduced.a),
                           "moment coefficient mismatch");

                    // Test nontrivial affine group-law after h0, without
                    // overflowing exact h0*hi (reduce modulo p first).
                    const M prod_mod=mm(h0,Hreduced);
                    demand(md(q0+r0*qi)==
                               md(-(Wide)prod_mod.a*prod_mod.b) &&
                           md(r0*rii)==md((Wide)prod_mod.a*prod_mod.a),
                           "moment covariance composition mismatch");

                    chk=mix64(chk,(std::uint64_t)j0);
                    chk=mix64(chk,(std::uint64_t)i);
                    chk=mix64(chk,(std::uint64_t)j1);
                    chk=mix64(chk,(std::uint64_t)(qi+P*rii));
                    ++transitions;
                    if(j0==P)++input_inf;
                    if(j1==P)++output_inf;
                    if(j0==P && j1==P)++both_inf;
                }
            }
            if(j0==9 || j0==4095 || j0==8191 || j0==12287 || j0==P)
                std::cout<<"C01_SHAPIRO_PROGRESS classes="<<j0+1
                         <<" transitions="<<transitions<<std::endl;
        }

        demand(transitions==(unsigned long long)terms*(unsigned long long)max_j,
               "transition total discrepancy");
        if(mode=="--full") {
            demand(input_inf==2012 && output_inf==2012,
                   "P1 permutation exceptional cardinality mismatch");
            demand(transitions==32658784ULL,"all transitions not visited");
            std::cout<<"C01_ALL_32658784_SHAPIRO_TRANSPORTS_EXACT_PASS"
                     <<" transitions="<<transitions
                     <<" input_exceptional="<<input_inf
                     <<" output_exceptional="<<output_inf
                     <<" both_exceptional="<<both_inf
                     <<" checksum="<<chk<<"\n";
        } else {
            std::cout<<"C01_ALL_COSETS_PILOT_PASS"
                     <<" transitions="<<transitions
                     <<" checksum="<<chk<<"\n";
        }
        std::cout<<"BOUNDARY: exact matrices, Gamma0(Np), native mod-p"
                 <<" transport and moment group law only;"
                 <<" no modular-symbol evaluations or C01 production replay\n";
        return 0;
    } catch(const std::exception& e) {
        std::cerr<<"C01_ALL_COSETS_AUDIT_FAIL "<<e.what()<<"\n";
        return 2;
    }
}
