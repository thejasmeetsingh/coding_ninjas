def binary_search(arr, x):
    if not arr:
        return False
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            del arr[mid]
            return True
        
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


def get_intersection(loop_arr, search_arr):
    result = []
    for element in loop_arr:
        if binary_search(search_arr, element):
            print(element, end=" ")
            

def intersection(arr1, arr2, n, m):
    if not arr1 or not arr2:
        return
    
    arr1.sort()
    arr2.sort()
    
    get_intersection(arr1, arr2) if n < m else get_intersection(arr2, arr1)
