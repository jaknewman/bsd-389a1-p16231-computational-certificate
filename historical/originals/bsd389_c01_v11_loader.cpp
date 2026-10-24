// BSD389 C01 V4: bounded in-memory modular accumulator, never writes pair TSV.
// Reuses the original, SHA256-pinned source without changing its C01 arithmetic.
#if !defined(BSD389_EFFECTIVE) || !defined(BSD389_SPARSE_TOUCHED)
#error "V4 requires -DBSD389_EFFECTIVE -DBSD389_SPARSE_TOUCHED"
#endif
#define main bsd389_legacy_main_not_called
#include "bsd389_transposed_J_native.cpp"
#undef main
#include <array>
#include <stdexcept>
#include <limits>

static long long v4_number(const char *s) {
    std::string x(s); std::size_t pos=0;
    const long long result=std::stoll(x,&pos);
    if(pos!=x.size()) throw std::runtime_error("malformed interval endpoint");
    return result;
}

static void v4_load_export(const std::string& file, std::vector<Rep>& reps,
                           std::vector<int>& keyrep) {
    auto root=load(file); auto& o=root.as_object();
    auto rr=o["rinf"].as_array();
    if(rr.size()!=4) throw std::runtime_error("invalid rinf");
    RINF={rr[0].as_int64(),rr[1].as_int64(),rr[2].as_int64(),rr[3].as_int64()};
    keyrep.assign(N+1,-1);
    for(auto& v:o["key_to_rep"].as_object()) {
        const int key=std::stoi(std::string(v.key()));
        if(key<0 || key>N || keyrep[key]!=-1) throw std::runtime_error("invalid key_to_rep");
        keyrep[key]=v.value().as_int64();
    }
    auto& rows=o["reps"].as_array();
    reps.clear(); reps.reserve(rows.size());
    std::array<int,NG> gen_count{};
    for(auto& v:rows) {
        auto& z=v.as_object(); auto a=z["matrix"].as_array();
        if(a.size()!=4) throw std::runtime_error("invalid rep matrix");
        Rep R{{a[0].as_int64(),a[1].as_int64(),a[2].as_int64(),a[3].as_int64()},
              (int)z["generator"].as_int64(),{}};
        if(R.gen>=0){
            if(R.gen>=NG) throw std::runtime_error("generator out of range");
            ++gen_count[R.gen];
        }
        for(auto& tv:z["relations"].as_array()) {
            auto& t=tv.as_object(); auto aa=t["A"].as_array();
            if(aa.size()!=4) throw std::runtime_error("invalid relation matrix");
            R.rel.push_back({(int)t["coeff"].as_int64(),(int)t["r"].as_int64(),
                             {aa[0].as_int64(),aa[1].as_int64(),aa[2].as_int64(),aa[3].as_int64()}});
        }
        reps.push_back(std::move(R));
    }
    if(reps.empty()) throw std::runtime_error("empty representatives");
    for(auto c:gen_count) if(c!=1) throw std::runtime_error("generator uniqueness");
    for(auto k:keyrep) if(k<0 || k>=(int)reps.size())
        throw std::runtime_error("key_to_rep range");
    for(const auto& R:reps) for(const auto& t:R.rel)
        if(t.r<0 || t.r>=(int)reps.size() || reps[t.r].gen<0)
            throw std::runtime_error("invalid relation generator");
}

