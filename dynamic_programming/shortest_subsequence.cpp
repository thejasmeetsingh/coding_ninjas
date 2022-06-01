#include<vector>
#include<string>
#include<climits>
int solve(string s, string v) {
    int m = s.length();
    int n = v.length();
    
    vector<vector<int>> dp(m + 1, vector<int>(n + 1));
    
    for(int i = 0; i < m + 1; i++) {
     	dp[i][0] = 1;   
    }
    
    for(int j = 0; j < n + 1; j++) {
        dp[0][j] = 1001; 
    }
    
    for(int i = 1; i < m + 1; i++) {
        for(int j = 1; j < n + 1; j++) {
             char current = s[i - 1];
             auto it = v.substr(0,j).rfind(current);
             
             if(it != ULONG_MAX) {	
                 dp[i][j] = min(dp[i - 1][j], dp[i - 1][it] + 1);		
             } else {
                 dp[i][j] = 1;  
             }
        }
    }
    
    return dp[m][n];
}
