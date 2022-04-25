def percolateUp(arr, start, end):
    childIndex = end
    
    while childIndex > 0:
        parentIndex = (childIndex-1) // 2

        if arr[parentIndex] > arr[childIndex]:
            arr[parentIndex], arr[childIndex] = arr[childIndex], arr[parentIndex]
            childIndex = parentIndex
        else:
            break

        
def percolateDown(arr, start, end):
    parentIndex = start

    while (2 * parentIndex + 1) < end:
        childIndex = 2 * parentIndex + 1

        if (childIndex + 1) < end and arr[childIndex + 1] < arr[childIndex]:
            childIndex += 1

        if arr[parentIndex] < arr[childIndex]:
            break
		
        arr[parentIndex], arr[childIndex] = arr[childIndex], arr[parentIndex]
        parentIndex = childIndex

        
def heapSort(arr):
    if not arr:
        return
    
    for i in range(1, len(arr)):
        percolateUp(arr, 0, i)

    end = len(arr)
    
    while end > 1:
        arr[0], arr[end - 1] = arr[end - 1], arr[0]
        end -= 1
        percolateDown(arr, 0, end)
