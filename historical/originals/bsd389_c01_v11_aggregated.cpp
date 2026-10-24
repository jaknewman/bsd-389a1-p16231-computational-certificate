#include "bsd389_c01_v11_loader.cpp"

#include <map>
#include <tuple>

using Key = std::array<i64,4>;
using Weights = std::array<i64,2>;

static void collect_fragments(
    i64 r, i64 s, i64 w, i64 kappa,
    std::map<Key,Weights>& grouped)
{
    std::vector<i64> h,k;
    i64 hm2=0,hm1=1,km2=1,km1=0;

    while(s){
        i64 q=r/s;
        i64 hn=q*hm1+hm2;
        i64 kn=q*km1+km2;
        h.push_back(hn);
        k.push_back(kn);
        hm2=hm1;hm1=hn;
        km2=km1;km1=kn;
        std::swap(r,s);
        s-=q*r;
    }

    if(h.empty()) return;

    auto add=[&](Key B){
        auto& z=grouped[B];
        i64 signed_w=md(-w);
        z[0]=md(z[0]+signed_w);
        z[1]=md(z[1]+(i128)signed_w*kappa%P);
    };

    add({1,h[0],0,k[0]});

    for(size_t j=0;j+1<h.size();++j){
        i64 sg=(j%2)?1:-1;
        add({sg*h[j],h[j+1],sg*k[j],k[j+1]});
    }
}

static long long exceptional_E0=0;
static long long exceptional_E1=0;

static void apply_group(
    const Key& B,
    i64 W, i64 K,
    const std::vector<Rep>& reps,
    const std::vector<int>& keyrep,
    Acc& out)
{
    M fragment{B[0],B[1],B[2],B[3]};
    int gi=keyrep[key(fragment)];
    const Rep& R=reps[gi];

    M H=mm(fragment,inv1(R.g));
    int j0=qidx(H);
    if(j0==P) ++exceptional_E0;
    M ho=mm(H,inv1(ri(j0)));

    i64 a=md(ho.a),b=md(ho.b);
    i64 q=md(-a*b),r=md(a*a);

    if(R.gen>=0){
        int slot=R.gen*(P+1)+j0;
        out.add(slot,md(q*W-K),md(r*W),1);
        return;
    }

    for(const Term& t:R.rel){
        M X=mm(ri(j0),inv1(t.A));
        int j1=qidx(X);
        if(j1==P) ++exceptional_E1;
        M hi=mm(X,inv1(ri(j1)));

        i64 aa=md(hi.a),bb=md(hi.b);
        i64 qi=md(-aa*bb);
        i64 rii=md(aa*aa);

        i64 x=md((i128)t.coeff*
                 md((i128)md(q+r*qi)*W-K)%P);
        i64 y=md((i128)t.coeff*r%P*rii%P*W%P);

        int gen=reps[t.r].gen;
        int slot=gen*(P+1)+j1;
        out.add(slot,x,y,1);
    }
}

int main(int argc,char** argv){
    try{
        if(argc!=5)
            throw std::runtime_error(
                "usage: V11 EXPORT START END OUTPUT");

        long long L=v4_number(argv[2]);
        long long R=v4_number(argv[3]);

        if(L<0 || R<=L || R>(P-1)*P || R-L>512)
            throw std::runtime_error("invalid bounded interval");

        std::vector<Rep> reps;
        std::vector<int> keyrep;
        v4_load_export(argv[1],reps,keyrep);

        std::map<Key,Weights> grouped;

        for(long long id=L;id<R;++id){
            int a=1+id/P;
            int b=id%P;

            i64 ferm=md(
                (mpow(a,P-1,P2)-1)/P,P);
            i64 ia=inv(a,P);
            i64 u=md((i128)b*ia-ferm);
            i64 w=md((i128)ia*md(2*u-1));
            i64 kap=kappa_ab(a,b);

            collect_fragments(
                a+(i64)P*b,P2,w,kap,grouped);
        }

        Acc out;
        long long active=0;

        for(const auto& entry:grouped){
            i64 W=entry.second[0];
            i64 K=entry.second[1];

            if(!W && !K) continue;
            ++active;

            apply_group(
                entry.first,W,K,reps,keyrep,out);
        }

        std::sort(
            out.touched_slots.begin(),
            out.touched_slots.end());

        std::ofstream f(argv[4],
                        std::ios::binary|std::ios::trunc);
        if(!f) throw std::runtime_error("output open");

        long long rows=0;
        for(auto slot:out.touched_slots){
            i64 c0=out.c0[slot];
            i64 c1=out.c1[slot];

            if(c0 || c1){
                f<<slot<<' '<<c0<<' '<<c1<<'\n';
                ++rows;
            }
        }

        f.close();
        if(!f) throw std::runtime_error("output write");

        std::cerr<<"V11_EXCEPTION_AUDIT E0="<<exceptional_E0<<" E1="<<exceptional_E1<<"\n";
        std::cerr<<"V11_AGGREGATE_PASS"
                 <<" L="<<L
                 <<" R="<<R
                 <<" unique="<<grouped.size()
                 <<" active="<<active
                 <<" rows="<<rows<<"\n";

        return 0;
    }
    catch(const std::exception& e){
        std::cerr<<"V11_FAIL "<<e.what()<<"\n";
        return 2;
    }
}
