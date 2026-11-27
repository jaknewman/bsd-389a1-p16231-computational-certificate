// Independent native check of the p=389 first cyclotomic Mazur--Tate layer.
// Exact Neron integral Manin symbols, no BSD or Sha assumption.
#include <bits/stdc++.h>
using namespace std;
using i64=long long;
static const int p=389, n=p*p;
int vals[p+1], inverses[p], bins[p][6];
int gcdint(int a,int b){while(b){int c=a%b;a=b;b=c;}return a;}
int powm(int b,int e,int mod){int acc=1;while(e){if(e&1)acc=(i64)acc*b%mod;b=(i64)b*b%mod;e>>=1;}return acc;}
int sym(int a,int den){
    if(gcdint(a,den)!=1)throw runtime_error("bad cusp");
    int a0=1,b0=0,a1=0,b1=1;
    int x=den,y=a,acc=vals[p];
    while(y){
        int quot=x/y,rem=x%y;
        int a2=quot*a1+a0,b2=quot*b1+b0;
        int determinant=a1*b2-a2*b1;
        if(abs(determinant)!=1)throw runtime_error("invalid path determinant");
        int c=(determinant>0?b1:b2)%p;
        int d=(determinant>0?b2:b1)%p;
        int index=c==0?p:(i64)d*inverses[c]%p;
        acc+=determinant*vals[index];
        a0=a1;b0=b1;a1=a2;b1=b2;x=y;y=rem;
    }
    if(a1!=a||b1!=den) throw runtime_error("invalid path final");
    return acc;
}
int main(int argc,char**argv){
 if(argc!=2){cerr<<"usage: independent_cyclotomic manin390.txt\n";return 2;}
 ifstream f(argv[1]);for(int i=0;i<=p;i++)if(!(f>>vals[i]))throw runtime_error("bad table");
 for(int i=1;i<p;i++)inverses[i]=powm(i,p-2,p);
 for(int i=0;i<p;i++){bins[i][0]=1;for(int k=1;k<6;k++)bins[i][k]=k>i?0:(i64)bins[i][k-1]*(i-k+1)%p*inverses[k]%p;}
 if(sym(7,p)!=-1||sym(5,p)!=-2)throw runtime_error("failed Neron normalization");
 vector<int> moments(6,0); vector<long long> rawU(p,0);
 int symbad=0,nonunit=0;
 for(int a=1;a<n;a++){
    if(a%p==0){nonunit++;continue;}
    int m=sym(a,n);
    rawU[a%p]+=m;
    int powv=powm(a,p-1,n);
    if(powv%p!=1)throw runtime_error("bad cyclotomic projection");
    int j= (p - ((powv-1)/p) %p)%p; // -((powv-1)/p) mod p, exactly
    for(int k=0;k<6;k++){
      moments[k]=(moments[k]+(i64)(m%p+p)%p*bins[j][k])%p;
    }
    if(a<n/2&&sym(n-a,n)!=m)symbad++;
 }
 int badU=0;
 for(int a=1;a<p;a++)if(rawU[a]!=sym(a,p))badU++;
 if(badU||symbad)throw runtime_error("U_p compatibility or symmetry fails");
 const int expected[]={0,0,0,321,102,102};
 for(int k=0;k<6;k++)if(moments[k]!=expected[k])throw runtime_error("unexpected Taylor coefficient");
 cout<<"CYC389_NATIVE_FULL_PASS n="<<n<<" units="<<(n-p)<<" nonunits="<<nonunit
     <<" first6=";for(int k=0;k<6;k++)cout<<(k?",":"")<<moments[k];
 cout<<" U389_ALL_388_EXACT_PASS symmetry=PASS\n";
}
