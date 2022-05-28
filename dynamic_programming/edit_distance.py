def editDistance(s1, s2):
    m = len(s1)
    n = len(s2)
    
    arr = [[0 for __ in range(n + 1)] for _ in range(m + 1)]
    
    for col in range(n + 1):
        arr[0][col] = col
    
    for row in range(m + 1):
        arr[row][0] = row
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[m - i] == s2[n - j]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                arr[i][j] = min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1]) + 1
    
    return arr[m][n]
