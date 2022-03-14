def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate(arr, n, d):
    if not arr or d == 0:
        return

    reverse(arr, 0, n - 1)
    reverse(arr, n - d, n - 1)
    reverse(arr, 0, n - d - 1)
