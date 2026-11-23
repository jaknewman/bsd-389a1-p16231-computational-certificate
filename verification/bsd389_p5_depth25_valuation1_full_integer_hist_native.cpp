// Full independent E389a1 p5 mod25 NONUNIT Kurihara witness 5351*13001.
// Unlike the older deep witness, delta is 15 mod25: v5=1 and delta mod5=0.
// This script emits all 25 true integer Mazur Tate theta coefficients.
// Complements the earlier mixed-jet mod25 witness by reconstructing EVERY
// integer coefficient of the actual degree24 diagonal Mazur--Tate theta.
// Output consumed by bsd389_p5_depth25_val1_Fitting_gate.py.
// Source uses the historically authenticated 390-entry Neron Manin vector.
// No all-large-p Sha/strong-BSD conclusion.
#include <iostream>
#include <string>
#include <vector>
#include <cstdint>
#include <cassert>
using namespace std;
const string compact="22222423212322123232122231233221001122123213121002222221111022224"
"23222221112200001122102211013344223321321111111113232331212112202"
"22323121333422232134222244424332233424333433333443223233222010022"
"22001022233232234433333433342433223342444222243123222433312132322"
"20221121213323231111111112312332244331011220122110000221112222232"
"42222011112222220012131232122110012233213222123232122321232422222";
constexpr int N=389,q1=5351,q2=13001,m=25,n=q1*q2;
int V[390],Inv[390];
void init(){
    assert(compact.size()==390);
    for(int i=0;i<390;i++)V[i]=compact[i]-'2';
    assert(V[N]==0);
    for(int i=1;i<N;i++){
        for(int j=1;j<N;j++)if(i*j%N==1){Inv[i]=j;break;}
        assert(Inv[i]);
    }
}
int symbol(int a){
    int64_t pn=1,pd=0,ln=0,ld=1,u=n,v=a,res=V[N];
    while(v){
        int64_t quo=u/v,rem=u%v;
        u=v;v=rem;
        int64_t nn=quo*ln+pn,nd=quo*ld+pd,det=ln*nd-nn*ld;
        assert(det==1||det==-1);
        int c=(det==1?ld:nd)%N,d=(det==1?nd:ld)%N;
        if(c<0)c+=N;
        if(d<0)d+=N;
        res+=det*V[(c?d*Inv[c]%N:N)];
        pn=ln;pd=ld;ln=nn;ld=nd;
    }
    assert(ln==a&&ld==n);
    return (int)res;
}
vector<int> logs(int q,int g){
    vector<int>L(q,-1);
    int x=1;
    for(int i=0;i<q-1;i++){
        assert(L[x]==-1);
        L[x]=i%m;
        x=(int)((int64_t)x*g%q);
    }
    assert(x==1);
    return L;
}
int main(){
    init();
    auto L1=logs(q1,11),L2=logs(q2,3);
    int64_t count=0,hist[m]={};
    for(int a=1;a<=(n-1)/2;a++){
        int x=a%q1,y=a%q2;
        if(!x||!y)continue;
        hist[(L1[x]+L2[y])%m]+=2LL*symbol(a);
        ++count;
    }
    assert(count==34775000);
    cout<<"count "<<count<<"\nhist ";
    for(auto h:hist)cout<<h<<' ';
    cout<<'\n';
}
