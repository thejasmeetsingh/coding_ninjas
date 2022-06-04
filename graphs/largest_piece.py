def dfs_traversal(arr, visited, n, row, col):
    if (row < 0 or row >= n) or (col < 0 or col >= n):
        return 0
	
    if visited[row][col] or arr[row][col] != 1:
        return 0
    
    visited[row][col] = True
    
    return (
        dfs_traversal(arr, visited, n, row - 1, col) +
        dfs_traversal(arr, visited, n, row, col + 1) +
        dfs_traversal(arr, visited, n, row + 1, col) +
        dfs_traversal(arr, visited, n, row, col - 1)
    ) + 1

def get_count(arr, n):
    count = 0
    visited = [[False for __ in range(n)] for _ in range(n)]
    
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                count = max(count, dfs_traversal(arr, visited, n, i, j))
    
    return count
    


if __name__ == "__main__":
    N = int(input())
    arr = []
    
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    
    print(get_count(arr, N))
