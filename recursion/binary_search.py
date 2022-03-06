def binary_search(arr, left, right, x):
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binary_search(arr, left, mid - 1, x)
    else:
        return binary_search(arr, mid + 1, right, x)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    result = binary_search(arr, 0, n - 1, x)
    print(result)
