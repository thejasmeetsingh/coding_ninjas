MAX_VALUE = 2147483647


def minCostPath(input, mRows, nCols):
    arr = [[0 for __ in range(nCols)] for _ in range(mRows)]
    row, col = mRows - 1, nCols - 1

    for i in range(mRows - 1, -1, -1):
        for j in range(nCols - 1, -1, -1):
            if i == row and j == col:
                arr[i][j] = input[i][j]
            else:
                a = arr[i][j + 1] if (j + 1) <= col else MAX_VALUE
                b = arr[i + 1][j + 1] if (i + 1) <= row and (j + 1) <= col else MAX_VALUE
                c = arr[i + 1][j] if (i + 1) <= row else MAX_VALUE
                arr[i][j] = min(a, b, c) + input[i][j]

    return arr[0][0]