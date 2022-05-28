def knapsack(weights, values, n, maxWeight):
    arr = [0 for i in range(maxWeight + 1)]
    
    for i in range(1, n + 1):
        for w in range(maxWeight, 0, -1):
            if weights[i - 1] <= w:
                arr[w] = max(arr[w], arr[w-weights[i - 1]] + values[i - 1])
    
    return arr[maxWeight]
