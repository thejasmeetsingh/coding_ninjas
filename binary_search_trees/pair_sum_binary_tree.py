def GetArray(root, arr):
    if not root:
        return
    
    GetArray(root.left, arr)
    arr.append(root.data)
    GetArray(root.right, arr)
    
    
def pairSum(root, sum):
    if not root:
        return
    
    arr = []
    GetArray(root, arr)
    arr.sort()
    
    i, j = 0, len(arr) - 1
    
    while i < j:
        if arr[i] + arr[j] == sum:
            print(arr[i], arr[j])
            i += 1
            j -= 1
        elif arr[i] + arr[j] > sum:
            j -= 1
        elif arr[i] + arr[j] < sum:
            i += 1
