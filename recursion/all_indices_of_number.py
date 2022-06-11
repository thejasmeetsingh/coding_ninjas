import sys
sys.setrecursionlimit(10 ** 3)


def print_indexes(arr, n, k, i=0):
    if i == n:
        return
    
    if arr[i] == k:
        print(i, end=" ")
    
    print_indexes(arr, n, k, i + 1)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    
    print_indexes(arr, n, k)
    
