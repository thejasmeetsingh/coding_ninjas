import sys
from sys import stdin

sys.setrecursionlimit(10 ** 6)


def dfs_traversal(arr, string, visited, str_idx, n, m, row, col):
    if str_idx == len(string):
        return True

    if (row < 0 or row >= n) or (col < 0 or col >= m):
        return False

    if visited[row][col] or arr[row][col] != string[str_idx]:
        return False

    visited[row][col] = True

    if dfs_traversal(arr, string, visited, str_idx + 1, n, m, row - 1, col - 1):
        return True

    if dfs_traversal(arr, string, visited, str_idx + 1, n, m, row - 1, col):
        return True

    if dfs_traversal(arr, string, visited, str_idx + 1, n, m, row - 1, col + 1):
        return True

    if dfs_traversal(arr, string, visited, str_idx + 1, n, m, row, col + 1):
        return True

    if dfs_traversal(arr, string, visited, str_idx + 1, n, m, row + 1, col + 1):
        return True

    if dfs_traversal(arr, string, visited, str_idx + 1, n, m, row + 1, col):
        return True

    if dfs_traversal(arr, string, visited, str_idx + 1, n, m, row + 1, col - 1):
        return True

    if dfs_traversal(arr, string, visited, str_idx + 1, n, m, row, col - 1):
        return True

    visited[row][col] = False
    return False


def solve(arr, n, m):
    string = "CODINGNINJA"
    indices = []

    for i in range(n):
        for j in range(m):
            if arr[i][j] == string[0]:
                indices.append([i, j])

    if not indices:
        return 0

    visited = [[False for __ in range(m)] for _ in range(n)]
    for row, col in indices:
        if dfs_traversal(arr, string, visited, 0, n, m, row, col):
            return 1

    return 0


def takeInput():
    # To take fast I/O
    n, m = list(map(int, stdin.readline().strip().split()))
    arr = [list(stdin.readline().strip()) for i in range(n)]
    return arr, n, m


# Main
arr, n, m = takeInput()
print(solve(arr, n, m))
