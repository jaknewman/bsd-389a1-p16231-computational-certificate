// E389a1 p=5 true p^2-depth diagonal Kurihara / Hecke low-jet test.
// All 28,488,750 plus-symmetry unit classes are evaluated in standard C++.
// The 390 integer Manin vector is independently archived (bytes SHA256
// 31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee).
// This certifies delta_{5351*10651} = 22 mod 25, not uniform all-prime Sha.
#include <iostream>
#include <vector>
#include <string>
#include <cstdint>
#include <cassert>
#include <chrono>
using namespace std;
constexpr int N=389,M=25,Q1=5351,Q2=10651;
constexpr int64_t CON=(int64_t)Q1*Q2;
const string COMPACT="22222423212322123232122231233221001122123213121002222221111022224"
"23222221112200001122102211013344223321321111111113232331212112202"
"22323121333422232134222244424332233424333433333443223233222010022"
"22001022233232234433333433342433223342444222243123222433312132322"
"20221121213323231111111112312332244331011220122110000221112222232"
"42222011112222220012131232122110012233213222123232122321232422222";
int V[390],Inv[390];
int mpow(int a,int e,int m){
    long long z=1,v=a;
    while(e){if(e&1)z=z*v%m;v=v*v%m;e>>=1;}
    return int(z);
}
int egcd(int a,int b,int &x,int &y){
    if(b==0){x=1;y=0;return a;}
    int x1,y1,d=egcd(b,a%b,x1,y1);
    x=y1;y=x1-(a/b)*y1;return d;
}
struct Pt{int x,y;bool zero;};
Pt inf(){return {0,0,true};}
bool equal(Pt A,Pt B){return A.zero==B.zero&&(A.zero||(A.x==B.x&&A.y==B.y));}
Pt sum(Pt A,Pt B,int q){
    if(A.zero)return B;
    if(B.zero)return A;
    int x=A.x,y=A.y,u=B.x,v=B.y;
    if(x==u&&(y+v+1)%q==0)return inf();
    int l,nu;
    if(x==u){
        int inv=mpow((2*y+1)%q,q-2,q);
        l=(int)((long long)(3LL*x*x+2*x-2)*inv%q);
        nu=(int)((long long)((-(long long)x*x*x-2LL*x-y)%q+q)*inv%q);
    }else{
        int inv=mpow((u-x+q)%q,q-2,q);
        l=(int)((long long)(v-y+q)*inv%q);
        nu=(int)((long long)(((long long)y*u-(long long)v*x)%q+q)*inv%q);
    }
    int X=((long long)l*l-1-x-u)%q;
    if(X<0)X+=q;
    int Y=(-(long long)l*X-nu-1)%q;
    if(Y<0)Y+=q;
    return {X,Y,false};
}
Pt mul(int n,Pt A,int q){
    Pt out=inf();
    while(n){if(n&1)out=sum(out,A,q);A=sum(A,A,q);n>>=1;}
    return out;
}
int count_points(int q){
    int n=1;
    for(int x=0;x<q;++x){
        int disc=(1+4LL*((long long)x*x*x+(long long)x*x-2*x))%q;
        if(disc<0)disc+=q;
        n+=disc==0?1:(mpow(disc,(q-1)/2,q)==1?2:0);
    }
    return n;
}
int sym(int a,int n){
    int64_t pn=1,pd=0,ln=0,ld=1;
    int u=n,v=a,res=V[N];
    while(v){
        int k=u/v,r=u%v;u=v;v=r;
        int64_t nn=(int64_t)k*ln+pn,nd=(int64_t)k*ld+pd;
        int64_t det=ln*nd-nn*ld;
        assert(det==1||det==-1);
        int64_t c=(det==1?ld:nd)%N,d=(det==1?nd:ld)%N;
        if(c<0)c+=N;
        if(d<0)d+=N;
        int idx=(c?int(d*Inv[c]%N):N);
        res+=(int)det*V[idx];
        pn=ln;pd=ld;ln=nn;ld=nd;
    }
    assert(ln==a&&ld==n);
    return (res%M+M)%M;
}
int main(){
    assert(COMPACT.size()==390);
    for(int i=0;i<390;++i)V[i]=COMPACT[i]-'2';
    assert(V[389]==0);
    for(int i=1;i<N;i++){
        int x,y;int d=egcd(i,N,x,y);
        assert(d==1);
        Inv[i]=(x%N+N)%N;
    }
    const int nq1=count_points(Q1),nq2=count_points(Q2);
    assert(nq1==5375&&nq2==10650);
    Pt P1=mul(43,{Q1-1,1,false},Q1),R1=mul(43,{0,Q1-1,false},Q1);
    assert(equal(mul(64,P1,Q1),R1));
    assert(equal(mul(125,P1,Q1),inf()));
    assert(!equal(mul(25,P1,Q1),inf()));
    Pt P2=mul(426,{Q2-1,1,false},Q2),R2=mul(426,{0,Q2-1,false},Q2);
    assert(equal(mul(2,P2,Q2),R2));
    assert(equal(mul(25,P2,Q2),inf()));
    assert(!equal(mul(5,P2,Q2),inf()));
    const int localdet=(2-14+25)%25;
    assert(localdet==13);
    cout<<"P5_MOD25_LOCAL_POINT_COUNTS "<<nq1<<" "<<nq2<<"\n";
    cout<<"P5_MOD25_TRUE_LOCAL_MW_MATRIX [[1,14],[1,2]] DET "<<localdet<<"\n";
    vector<int>L1(Q1,-1),L2(Q2,-1);
    const int g1=11,g2=7;
    {int x=1;for(int j=0;j<Q1-1;j++){
        assert(L1[x]==-1);L1[x]=j%M;x=(int)((long long)x*g1%Q1);
    }assert(x==1);}
    {int x=1;for(int j=0;j<Q2-1;j++){
        assert(L2[x]==-1);L2[x]=j%M;x=(int)((long long)x*g2%Q2);
    }assert(x==1);}
    assert((Q1-1)%M==0&&(Q2-1)%M==0);
    int64_t A[3][3]{},diagonal=0,count=0,nonzero=0;
    const int64_t half=(CON-1)/2;
    auto start=chrono::steady_clock::now();
    for(int a=1;a<=half;++a){
        int r1=a%Q1,r2=a%Q2;
        if(!r1||!r2)continue;
        int j1=L1[r1],j2=L2[r2];
        assert(j1>=0&&j2>=0);
        int v=(2*sym(a,(int)CON))%M;
        if(v)++nonzero;
        int b1[3]={1,j1,j1*(j1-1)/2};
        int b2[3]={1,j2,j2*(j2-1)/2};
        for(int i=0;i<3;++i)
          for(int j=0;j<3;++j)
            A[i][j]=(A[i][j]+(int64_t)v*b1[i]*b2[j])%M;
        int d=(j1+j2)%M;
        diagonal=(diagonal+(int64_t)v*d*(d-1)/2)%M;
        ++count;
    }
    assert(count==(int64_t)(Q1-1)*(Q2-1)/2);
    for(int i=0;i<3;++i){
        for(int j=0;j<3;++j)cout<<A[i][j]<<(j==2?'\n':' ');
    }
    cout<<"P5_MOD25_DEEP_Q1 "<<Q1<<" TRACE "<<Q1+1-nq1<<"\n";
    cout<<"P5_MOD25_DEEP_Q2 "<<Q2<<" TRACE "<<Q2+1-nq2<<"\n";
    cout<<"P5_MOD25_DEEP_COUNTS "<<count<<" nonzero_symbols "<<nonzero<<"\n";
    cout<<"P5_MOD25_DEEP_MIXED_KURIHARA "<<A[1][1]<<" diagonal "<<diagonal
        <<" pure2 "<<A[2][0]<<","<<A[0][2]<<" pure_linear "
        <<A[1][0]<<","<<A[0][1]<<" augmentation "<<A[0][0]<<"\n";
    assert(A[0][0]==0&&A[1][0]==0&&A[0][1]==0
           &&A[2][0]==0&&A[0][2]==0);
    assert(A[1][1]==22&&diagonal==22);
    cout<<"P5_MOD25_EXACT_DIAGONAL_MATCH PASS\n";
    auto seconds=chrono::duration<double>(chrono::steady_clock::now()-start).count();
    cout<<"SECONDS "<<seconds<<"\n";
}
