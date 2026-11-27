#include <bits/stdc++.h>
using namespace std; using u64=uint64_t; using i64=int64_t;
int v[390], inv389[389];
int main(int argc,char**argv){
 if(argc<5){cerr<<"Usage: kuri4 p table q1 q2 q3 q4 [optional q5]?\n";return 2;}
 int p=atoi(argv[1]); ifstream input(argv[2]);for(int&i:v) {if(!(input>>i)){cerr<<"missing table\n";return 2;}}
 for(int i=1;i<389;i++) for(int j=1;j<389;j++) if(i*j%389==1) {inv389[i]=j;break;}
 vector<int> qs; for(int i=3;i<argc;i++)qs.push_back(atoi(argv[i]));
 const int r=qs.size();u64 n=1;for(int q:qs)n*=q;
 vector<vector<unsigned char>> logs(r);
 for(int i=0;i<r;i++){
  int q=qs[i];logs[i].resize(q);int g=0;
  for(int k=2;k<q;k++){
   vector<unsigned char>seen(q,0);int t=1;bool primitive=true;
   for(int j=0;j<q-1;j++){if(seen[t]){primitive=false;break;}seen[t]=1;t=(i64)t*k%q;}
   if(primitive && t==1){g=k;break;}
  }
  if(!g){cerr<<"primitive root not found "<<q<<"\n";return 2;}
  int t=1;
  for(int j=0;j<q-1;j++){logs[i][t]=j%p;t=(i64)t*g%q;}
  cout<<"ROOT "<<q<<" "<<g<<"\n";
 }
 auto modSymbol=[&](u64 a)->int {
   u64 pn=1,pd=0,ln=0,ld=1,x=n,y=a;
   int acc=v[389];
   while(y){u64 quo=x/y,z=x%y,nn=quo*ln+pn,nd=quo*ld+pd;
     int det=(int)((__int128)ln*nd-(__int128)nn*ld);
     if(det!=1&&det!=-1){cerr<<"bad det\n";exit(2);}
     int c=(det==1?ld:nd)%389,d=(det==1?nd:ld)%389;
     int idx=c==0?389:((int)((i64)d*inv389[c]%389));
     acc+=det*v[idx];
     pn=ln;pd=ld;ln=nn;ld=nd;x=y;y=z;
   }
   if(ln!=a||ld!=n){cerr<<"bad convergent\n";exit(2);}
   return (acc%p+p)%p;
 };
 const bool full=(getenv("BSD389_KURIHARA_FULL")!=nullptr); u64 limit=full?(n-1):(n-1)/2,count=0;int total=0;
 auto start=chrono::steady_clock::now();
 for(u64 a=1;a<=limit;a++){
  int weight=1;
  for(int i=0;i<r;i++){
   int t=a%qs[i];if(!t){weight=0;break;}
   weight=weight*logs[i][t]%p;
   if(!weight)break;
  }
  if(weight){total=(total+weight*modSymbol(a))%p;count++;}
  if(a%10000000==0){cerr<<"SCAN "<<a<<" / "<<limit<<" secs="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n"<<flush;}
 }
 if(!full)total=(total*2)%p;
 cout<<"DELTA_R"<<r<<" "<<total<<" Q ";for(int q:qs)cout<<q<<",";cout<<" N "<<n<<" FULL "<<full<<" NONZERO_WEIGHTS_VISITED "<<count<<" SECONDS "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
}
