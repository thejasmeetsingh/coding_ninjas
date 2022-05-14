def count_subsets(arr, _sum, k):
    global count
    
    if not arr:
        if _sum == k:
            count += 1
        return
    
    count_subsets(arr[1:], arr[0] + _sum, k)
    count_subsets(arr[1:], _sum, k)


if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        count = 0
        count_subsets(arr, 0, k)
        print(count)
