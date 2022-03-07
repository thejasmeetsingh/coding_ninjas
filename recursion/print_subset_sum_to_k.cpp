#include <iostream>
using namespace std;
#include "solution.h"


void printSubsetSumToK(int input[], int size, int k,string output="") {
    if(size==0)
    {
        if(k==0)
        {
            cout<<output<<endl;
            return ;
        }
        return;
    }
    printSubsetSumToK(input+1,size-1,k,output);
    printSubsetSumToK(input+1,size-1,k-input[0],output+to_string(input[0])+" ");
}

int main() {
  int input[1000],length,k;
  cin >> length;
  for(int i=0; i < length; i++)
    cin >> input[i];
  cin>>k;
  printSubsetSumToK(input, length,k);
}
