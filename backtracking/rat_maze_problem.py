def printPathsUtil(row=0, col=0):
    if row >= n or col >= n or row < 0 or col < 0:
        return

    if matrix[row][col] == 0 or arr[row][col] == 1:
        return

    if row == n - 1 and col == n - 1:
        arr[row][col] = 1
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
        print()
        arr[row][col] = 0
        return

    arr[row][col] = 1
    printPathsUtil(row - 1, col)
    printPathsUtil(row, col - 1)
    printPathsUtil(row, col + 1)
    printPathsUtil(row + 1, col)
    arr[row][col] = 0

    return


def printPaths():
    global arr
    arr = [[0 for __ in range(n)] for _ in range(n)]
    printPathsUtil()


if __name__ == "__main__":
    n = int(input())
    arr = []
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    printPaths()
