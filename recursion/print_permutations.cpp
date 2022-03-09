#include <iostream>
#include <string>
#include <algorithm>
#include "solution.h"
using namespace std;

void printPermutations(string input,string output=""){
    if(input=="")
    {
        cout<<output<<endl;
        return;
    }
    for(int i=0;i<input.size();i++)
    {
        printPermutations(input.substr(1),output+input[0]);
        rotate(input.begin(),input.begin()+1,input.end());
    }
}

int main() {
    string input;
    cin >> input;
    printPermutations(input);
    return 0;
}
