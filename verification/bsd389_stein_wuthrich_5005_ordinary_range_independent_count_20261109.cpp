// Independent ordinary/supersingular PRIME RANGE audit for 389a1, no Sage.
// Reproduces the COUNT AND excluded set of Stein-Wuthrich 2013, Thm 12.3.
// NOT a second proof of the published Sha[p]=0 computation.
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main(){
 const int MAXP=48859;
 vector<char> isprime(MAXP+1,true);
 isprime[0]=isprime[1]=false;
 for(int d=2;d*d<=MAXP;++d)if(isprime[d])
  for(int k=d*d;k<=MAXP;k+=d)isprime[k]=false;
 vector<int> ordinary,supers,anomalous;
 int ap3=999;
 for(int p=3;p<MAXP;p+=2){
  if(!isprime[p]||p==389)continue;
  vector<signed char> qr(p,-1);qr[0]=0;
  for(int y=1;y<p;y++) qr[(long long)y*y%p]=1;
  int sum=0;
  for(long long x=0;x<p;x++){
   long long z=(((((4*x%p+4)*x%p-8)%p)*x+1)%p+p)%p;
   sum+=qr[z];
  }
  int ap=-sum, n=p+1-ap;
  if(p==3)ap3=ap;
  if(p>=5){
   if(ap==0)supers.push_back(p);
   else ordinary.push_back(p);
   if(n%p==0)anomalous.push_back(p);
  }
 }
 vector<int> excluded=supers;
 excluded.push_back(389); excluded.push_back(16231);
 sort(excluded.begin(),excluded.end());
 const vector<int> published={
 107,389,599,1049,2957,6661,8263,9397,9551,14633,15101,
 16231,28591,30671,30869,31799,34781,36263,45161};
 const vector<int> expected_anom={
 859,1213,1493,1951,2521,12697,26821,38747};
 if(ap3!=-2 || ordinary.size()!=5004 || supers.size()!=17
   || excluded!=published || anomalous!=expected_anom)return 1;
 cout<<"SW2013_INDEPENDENT_RANGE_COUNTS_PASS  ordinary_p_ge_5 "
     <<ordinary.size()<<" ordinary_p_ge_3 "<<ordinary.size()+1
     <<" supersingular "<<supers.size()
     <<" excluded "<<excluded.size()<<"\n";
 cout<<"SW2013_PUBLISHED_SHA_P_ZERO_COUNT 5005 (p=2 plus 5004 ordinary)\n";
 cout<<"BOUNDARY: This verifies trace/prime counts, NOT global Sha or uniformity.\n";
}
