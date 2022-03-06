#include <iostream>
#include <bits/stdc++.h>
#include "solution.h"
using namespace std;


void replacePi(char input[], int start = 0) {
    if (input[start] == '\0' || input[start + 1] == '\0') {
        return;
    }
 
    replacePi(input, start + 1);
 
    if (input[start] == 'p' && input[start + 1] == 'i') {
 
        for (int i = strlen(input); i >= start + 2; i--) {
            input[i + 2] = input[i];
        }

        input[start] = '3';
        input[start + 1] = '.';
        input[start + 2] = '1';
        input[start + 3] = '4';
    }
}

int main() {
    char input[10000];
    cin.getline(input, 10000);
    replacePi(input);
    cout << input << endl;
}
