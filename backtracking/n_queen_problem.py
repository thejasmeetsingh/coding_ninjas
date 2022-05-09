arr = []

def isPossiblePlace(n, row, col):
    i = row
    
    while i >= 0:
        if arr[i][col] == 1:
            return False
        i -= 1
    
    i = row
    j = col
    
    while i >= 0 and j >= 0:
        if arr[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    
    while i >= 0 and j < n:
        if arr[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def printPathsUtil(n, row):
    if row >= n:
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
        print()
        return
    
    for j in range(n):
        if isPossiblePlace(n, row, j):
            arr[row][j] = 1
            printPathsUtil(n, row + 1)
            arr[row][j] = 0


def printPaths(n):
    global arr
    arr = [[0 for __ in range(n)] for _ in range(n)]
    printPathsUtil(n, 0)


if __name__ == "__main__":
    n = int(input())
    printPaths(n)
