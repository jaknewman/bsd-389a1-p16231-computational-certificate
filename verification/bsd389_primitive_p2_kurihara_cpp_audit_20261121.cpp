#include <iostream>
#include <vector>
#include <numeric>
#include <string>
#include <cassert>
using namespace std;
const string COMPACT =
"222224232123221232321222312332210011221232131210022222211110"
"222242322222111220000112210221101334422332132111111111323233"
"121211220222323121333422232134222244424332233424333433333443"
"223233222010022220010222332322344333334333424332233424442222"
"431232224333121323222022112121332323111111111231233224433101"
"122012211000022111222223242222011112222220012131232122110012"
"233213222123232122321232422222";
const int N = 389;
int vec[390],invmod[389];
int modpow(int a,int k,int m){int r=1; while(k){if(k&1)r=(long long)r*a%m;a=(long long)a*a%m;k>>=1;}return r;}
void setup(){
    assert(COMPACT.size()==390);
    for(int i=0;i<390;i++)vec[i]=COMPACT[i]-'0'-2;
    invmod[0]=0;
    for(int i=1;i<389;i++){invmod[i]=modpow(i,387,389);assert((i*invmod[i])%389==1);}
}
vector<int> logs(int q,int g,int p){
    vector<int> L(q,-1);int a=1;
    for(int k=0;k<q-1;k++){assert(L[a]==-1);L[a]=k%p;a=(long long)a*g%q;}
    assert(a==1);return L;
}
int manin(int a,int n,int p){
    int pn=1,pd=0,ln=0,ld=1,u=n,v=a,s=vec[N];
    while(v){
        int k=u/v,rem=u%v;
        int x=k*ln+pn, y=k*ld+pd;
        int det=ln*y-x*ld;assert(det==1||det==-1);
        int c=(det==1?ld:y)%389;
        int d=(det==1?y:ld)%389;
        s+=det*vec[c? (d*invmod[c])%389 : 389];
        pn=ln;pd=ld;ln=x;ld=y;u=v;v=rem;
    }
    assert(ln==a&&ld==n); s%=p; if(s<0)s+=p;return s;
}
void run(int p,int q1,int q2,int g1,int g2){
    auto L1=logs(q1,g1,p);auto L2=logs(q2,g2,p);
    int n=q1*q2; long long count=0;
    int M[4]={0,0,0,0};
    for(int a=1;a<=n/2;a++){
        int x=a%q1,y=a%q2;
        if(x==0||y==0)continue;
        int v=manin(a,n,p),u=L1[x],w=L2[y];
        assert(u>=0&&w>=0);
        M[0]=(M[0]+v)%p;M[1]=(M[1]+u*v)%p;
        M[2]=(M[2]+w*v)%p;M[3]=(M[3]+u*w*v)%p;
        count++;
    }
    assert(2*count==(long long)(q1-1)*(q2-1));
    for(auto &m:M)m=2*m%p;
    cout << "BSD389_P2_PRIMITIVE_KURIHARA_COMPLETE p="<<p<<" q="<<q1<<","<<q2<<" checked="<<count
    <<" total="<<2*count<<" moments="<<M[0]<<","<<M[1]<<","<<M[2]<<","<<M[3]<<"\n";
}
int main(){setup();run(5,41,61,6,2);run(5,61,991,2,6);run(7,2423,8597,5,2);}
