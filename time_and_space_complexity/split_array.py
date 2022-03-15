def split(arr, i, left_sum, right_sum):
    if len(arr) == i:
        return left_sum == right_sum
    
    if arr[i] % 3 == 0:
        left_sum += arr[i]
    elif arr[i] % 5 == 0:
        right_sum += arr[i]
    else:
        return split(arr, i + 1, left_sum + arr[i], right_sum) or split(arr, i + 1, left_sum, right_sum + arr[i])
    
    return split(arr, i + 1, left_sum, right_sum)
