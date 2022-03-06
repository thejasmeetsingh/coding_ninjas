def get_subsets(arr):
    if not arr:
        return [[]]
    
    subsets = get_subsets(arr[1:])
    results = []
    
    for subset in subsets:
        results.append(subset)

    for subset in subsets:
        results.append([arr[0]] + subset)
    
    return results


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    results = get_subsets(arr)
    
    for result in results:
        if result:
        	print(" ".join(map(str, result)))
