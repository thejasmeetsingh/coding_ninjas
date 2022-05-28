class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      m = len(text1)
      n = len(text2)
      
      arr = [[0 for __ in range(n + 1)] for _ in range(m + 1)]
      
      for i in range(1, m + 1):
        for j in range(1, n + 1):
          if text1[m - i] == text2[n - j]:
            arr[i][j] = 1 + arr[i - 1][j - 1]
          else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
      
      return arr[m][n]
